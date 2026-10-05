#!/usr/bin/env python3
"""Publish the Markdown pages in this repository to a Confluence Cloud space.

How the repository maps onto Confluence
---------------------------------------
* Every ``.md`` file is one Confluence page. Its title is the file's first
  ``# Heading`` (falling back to the file name).
* A folder is a parent page. Its content is the folder's ``README.md``, and
  the other files and folders inside it are its children. A folder without a
  ``README.md`` becomes a page that just lists its children.
* The ``README.md`` at the top of the docs directory is the root page: it
  updates the page CONFLUENCE_PARENT_ID, or the space homepage when that is not
  set, and every top-level page goes under it.
* Pages are matched by title inside the space: an existing page with the same
  title is updated (and moved under the right parent); otherwise a new page is
  created. Nothing is ever deleted.
* Relative links between Markdown files become Confluence page links.

Usage
-----
    python sync.py --all                 # every page
    python sync.py --since <git-sha>     # only files changed since that commit
    python sync.py --all --dry-run --out preview/   # no network; writes XHTML

Environment
-----------
    CONFLUENCE_BASE_URL    https://<site>.atlassian.net
    CONFLUENCE_SPACE_KEY   key of the existing space, e.g. DI502
    CONFLUENCE_EMAIL       Atlassian account e-mail
    CONFLUENCE_API_TOKEN   API token for that account
    CONFLUENCE_PARENT_ID   optional: page id to put top-level pages under
    DOCS_DIR               optional: folder holding the Markdown (default ".")
    CONFLUENCE_IGNORE      optional: comma-separated globs to skip
"""
from __future__ import annotations

import argparse
import fnmatch
import html
import os
import re
import subprocess
import sys
import time
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

import markdown
import requests
from lxml import etree
from lxml import html as lhtml

ZERO_SHA = "0" * 40
ROOT = PurePosixPath(".")
H1 = re.compile(r"^#[ \t]+(.+?)[ \t#]*$", re.MULTILINE)
VOID = {"br", "hr", "img", "col"}


def log(msg: str) -> None:
    print(msg, flush=True)


# --------------------------------------------------------------------------- repository model
class Docs:
    def __init__(self, root: Path, ignore: list[str]):
        self.root = root.resolve()
        self.nodes: dict[PurePosixPath, Path | None] = {}
        self.skipped: dict[str, str] = {}
        files = sorted(
            p for p in self.root.rglob("*.md")
            if not any(part.startswith(".") or part == "node_modules"
                       for part in p.relative_to(self.root).parts)
        )
        for f in files:
            rel = f.relative_to(self.root).as_posix()
            if any(fnmatch.fnmatch(rel, g) for g in ignore):
                self.skipped[rel] = "matches CONFLUENCE_IGNORE"
                continue
            self.nodes[self.node_of(rel)] = f
        # folders without their own file still need a page
        for node in list(self.nodes):
            for anc in self.ancestors(node):
                self.nodes.setdefault(anc, None)
        self._titles: dict[PurePosixPath, str] = {}

    @staticmethod
    def node_of(rel: str) -> PurePosixPath:
        """A README.md stands for its folder; any other file stands for itself."""
        p = PurePosixPath(rel)
        return p.parent if p.name == "README.md" else p

    @staticmethod
    def ancestors(node: PurePosixPath) -> list[PurePosixPath]:
        """Ancestors from the top down, excluding the root and the node itself."""
        return [a for a in reversed(node.parents) if a != ROOT]

    def title(self, node: PurePosixPath) -> str:
        if node not in self._titles:
            src = self.nodes.get(node)
            m = H1.search(src.read_text(encoding="utf-8")) if src else None
            if m:
                t = m.group(1).strip()
            else:
                name = node.name.removesuffix(".md") or "Home"
                t = re.sub(r"^\d+[-_ ]+", "", name).replace("-", " ").replace("_", " ")
                t = t[:1].upper() + t[1:]
            self._titles[node] = t
        return self._titles[node]

    def resolve_link(self, src: Path, href: str) -> PurePosixPath | None:
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or not parts.path.lower().endswith(".md"):
            return None
        target = (src.parent / unquote(parts.path)).resolve()
        try:
            rel = target.relative_to(self.root).as_posix()
        except ValueError:
            return None
        node = self.node_of(rel)
        return node if node in self.nodes else None

    def check_titles(self) -> None:
        seen: dict[str, PurePosixPath] = {}
        for node in sorted(self.nodes):
            t = self.title(node)
            if t in seen:
                sys.exit(f"ERROR: '{seen[t]}' and '{node}' both have the title '{t}'. "
                         "Confluence needs unique page titles in a space; rename one heading.")
            seen[t] = node


# --------------------------------------------------------------------------- Markdown -> storage format
def to_storage(docs: Docs, node: PurePosixPath) -> str:
    src = docs.nodes[node]
    if src is None:  # folder with no content file: show its children
        return '<ac:structured-macro ac:name="children" ac:schema-version="2" />'

    text = src.read_text(encoding="utf-8")
    text = H1.sub("", text, count=1)  # the H1 becomes the page title
    body = markdown.markdown(text, extensions=["tables", "sane_lists", "fenced_code"],
                             output_format="xhtml")
    if not body.strip():
        return ""

    tree = lhtml.fragment_fromstring(body, create_parent="div")

    # Confluence expects header rows inside <tbody>
    for thead in tree.iter("thead"):
        table = thead.getparent()
        tbody = table.find("tbody")
        if tbody is None:
            tbody = etree.SubElement(table, "tbody")
        for i, row in enumerate(list(thead)):
            tbody.insert(i, row)
        table.remove(thead)

    # relative .md links -> Confluence page links (swapped in after serialising)
    links: dict[str, str] = {}
    for a in list(tree.iter("a")):
        node_t = docs.resolve_link(src, a.get("href", ""))
        if node_t is None:
            continue
        token = f"@@CFLINK{len(links)}@@"
        label = a.text_content().replace("]]>", "]] >")
        links[token] = (
            f'<ac:link><ri:page ri:content-title="{html.escape(docs.title(node_t), quote=True)}" />'
            f"<ac:plain-text-link-body><![CDATA[{label}]]></ac:plain-text-link-body></ac:link>")
        parent, prev = a.getparent(), a.getprevious()
        filler = token + (a.tail or "")
        if prev is not None:
            prev.tail = (prev.tail or "") + filler
        else:
            parent.text = (parent.text or "") + filler
        parent.remove(a)

    # keep empty cells as <td></td> rather than <td/>
    for el in tree.iter():
        if isinstance(el.tag, str) and el.tag not in VOID and el.text is None and len(el) == 0:
            el.text = ""

    xml = etree.tostring(tree, method="xml", encoding="unicode")
    xml = re.sub(r"^<div>|</div>$", "", xml)
    for token, value in links.items():
        xml = xml.replace(token, value)
    return xml


# --------------------------------------------------------------------------- Confluence Cloud client
class Confluence:
    def __init__(self, base_url: str, email: str, token: str, space_key: str):
        self.site = re.sub(r"/wiki/?$", "", base_url.rstrip("/"))
        self.api = f"{self.site}/wiki/api/v2"
        self.s = requests.Session()
        self.s.auth = (email, token)
        self.s.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
        space = self._req("GET", f"{self.api}/spaces", params={"keys": space_key})["results"]
        if not space:
            sys.exit(f"ERROR: space '{space_key}' not found, or this account cannot see it.")
        self.space_id = space[0]["id"]
        self.homepage_id = space[0].get("homepageId")

    def _req(self, method: str, url: str, **kw):
        for attempt in range(6):
            r = self.s.request(method, url, timeout=60, **kw)
            if r.status_code == 429 or r.status_code >= 500:
                wait = int(r.headers.get("Retry-After", 2 ** attempt))
                log(f"  … {r.status_code} from Confluence, retrying in {wait}s")
                time.sleep(wait)
                continue
            if not r.ok:
                raise RuntimeError(f"{method} {url} -> {r.status_code}: {r.text[:800]}")
            return r.json() if r.content else {}
        raise RuntimeError(f"{method} {url} kept failing; giving up")

    def get(self, page_id: str) -> dict:
        return self._req("GET", f"{self.api}/pages/{page_id}")

    def find(self, title: str) -> dict | None:
        res = self._req("GET", f"{self.api}/pages",
                        params={"space-id": self.space_id, "title": title, "status": "current"})
        return next((p for p in res.get("results", []) if p["title"] == title), None)

    def create(self, title: str, parent_id: str, body: str) -> dict:
        return self._req("POST", f"{self.api}/pages", json={
            "spaceId": self.space_id, "status": "current", "title": title, "parentId": parent_id,
            "body": {"representation": "storage", "value": body}})

    def update(self, page: dict, title: str, parent_id: str | None, body: str, message: str) -> dict:
        payload = {
            "id": page["id"], "status": "current", "title": title,
            "body": {"representation": "storage", "value": body},
            "version": {"number": page["version"]["number"] + 1, "message": message}}
        if parent_id:
            payload["parentId"] = parent_id
        res = self._req("PUT", f"{self.api}/pages/{page['id']}", json=payload)
        if parent_id and str(res.get("parentId")) != str(parent_id):
            self._req("PUT", f"{self.site}/wiki/rest/api/content/{page['id']}/move/append/{parent_id}")
        return res


# --------------------------------------------------------------------------- sync
def changed_nodes(docs: Docs, since: str | None) -> list[PurePosixPath] | None:
    """Nodes whose file changed since `since`; None means 'sync everything'."""
    if not since or since == ZERO_SHA:
        log("No previous commit to compare with: syncing every page.")
        return None
    top = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                       cwd=docs.root, text=True).strip())
    if subprocess.run(["git", "cat-file", "-e", f"{since}^{{commit}}"], cwd=top,
                      capture_output=True).returncode != 0:
        log(f"Commit {since[:12]} is not in the history (force push?): syncing every page.")
        return None
    out = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=AMR", since, "HEAD", "--", "*.md"],
        cwd=top, text=True)
    nodes = []
    for line in filter(None, out.splitlines()):
        path = (top / line).resolve()
        try:
            rel = path.relative_to(docs.root).as_posix()
        except ValueError:
            continue
        if rel in docs.skipped:
            log(f"skip {rel}: {docs.skipped[rel]}")
            continue
        node = docs.node_of(rel)
        if docs.nodes.get(node) is not None and docs.nodes[node].resolve() == path:
            nodes.append(node)
    return nodes


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--all", action="store_true", help="sync every page")
    mode.add_argument("--since", metavar="SHA", help="sync files changed since this commit")
    ap.add_argument("--dry-run", action="store_true", help="convert only; do not call Confluence")
    ap.add_argument("--out", type=Path, help="with --dry-run: write the converted XHTML here")
    args = ap.parse_args()

    docs = Docs(Path(os.environ.get("DOCS_DIR") or "."),
                [g.strip() for g in os.environ.get("CONFLUENCE_IGNORE", "").split(",") if g.strip()])
    for rel, why in docs.skipped.items():
        log(f"skip {rel}: {why}")
    docs.check_titles()

    targets = None if args.all else changed_nodes(docs, args.since)
    if targets is None:
        targets = [n for n in docs.nodes if docs.nodes[n] is not None]
    targets = sorted(set(targets), key=lambda n: (n != ROOT, n.as_posix()))
    if not targets:
        log("No Markdown pages changed. Nothing to do.")
        return

    # parents first, so every page has somewhere to go
    order: list[PurePosixPath] = []
    for node in targets:
        for n in docs.ancestors(node) + [node]:
            if n not in order:
                order.append(n)
    update = set(targets)

    if args.dry_run:
        for n in order:
            action = "create/update" if n in update else "ensure exists"
            if n == ROOT:
                action, parent = "update root", "(CONFLUENCE_PARENT_ID or space homepage)"
            else:
                parent = n.parent if n.parent != ROOT else "(root page)"
            log(f"[dry-run] {action:13} '{docs.title(n)}'  <- {docs.nodes[n] and docs.nodes[n].relative_to(docs.root)}  parent: {parent}")
            if args.out and n in update:
                dest = args.out / docs.nodes[n].relative_to(docs.root).with_suffix(".xhtml")
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(to_storage(docs, n), encoding="utf-8")
        return

    need = ["CONFLUENCE_BASE_URL", "CONFLUENCE_SPACE_KEY", "CONFLUENCE_EMAIL", "CONFLUENCE_API_TOKEN"]
    missing = [v for v in need if not os.environ.get(v)]
    if missing:
        sys.exit("ERROR: missing settings: " + ", ".join(missing))

    cf = Confluence(os.environ["CONFLUENCE_BASE_URL"], os.environ["CONFLUENCE_EMAIL"],
                    os.environ["CONFLUENCE_API_TOKEN"], os.environ["CONFLUENCE_SPACE_KEY"])
    root_id = os.environ.get("CONFLUENCE_PARENT_ID") or cf.homepage_id
    if not root_id:
        sys.exit("ERROR: the space has no homepage; set CONFLUENCE_PARENT_ID.")
    sha = os.environ.get("GITHUB_SHA", "")[:7]
    message = f"Synced from git {sha}".strip()

    ids: dict[PurePosixPath, str] = {ROOT: str(root_id)}
    failures = 0
    for n in order:
        title, parent_id = docs.title(n), ids[n.parent]
        try:
            if n == ROOT:  # top-level README.md -> the root page itself
                cf.update(cf.get(ids[ROOT]), title, None, to_storage(docs, n), message)
                log(f"updated  '{title}' (root page)")
                continue
            page = cf.find(title)
            if page and str(page["id"]) == ids[ROOT]:
                raise RuntimeError(f"'{title}' is the title of the root page; rename this heading")
            if page and n not in update:
                ids[n] = page["id"]
                continue
            body = to_storage(docs, n)
            if page:
                cf.update(page, title, parent_id, body, message)
                ids[n] = page["id"]
                log(f"updated  '{title}'")
            else:
                ids[n] = cf.create(title, parent_id, body)["id"]
                log(f"created  '{title}'")
        except RuntimeError as e:
            failures += 1
            log(f"FAILED   '{title}': {e}")
            if n not in ids:  # its children cannot be placed either
                ids[n] = parent_id
    if failures:
        sys.exit(f"{failures} page(s) failed; see the log above.")
    log(f"Done: {len(update)} page(s) synced.")


if __name__ == "__main__":
    main()
