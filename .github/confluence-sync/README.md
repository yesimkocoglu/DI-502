# Markdown → Confluence sync

When you push a change to a `.md` file on `main`, the workflow `.github/workflows/confluence-sync.yml` uploads that page to your Confluence Cloud space.

## One-time setup

1. **Copy `.github/` into the root of the repository**, next to the top-level `README.md`. If the Markdown sits in a subfolder of the repo, set the variable `DOCS_DIR` (step 4) to that folder.
2. **Create an API token** for the Atlassian account that will own the pages: go to <https://id.atlassian.com/manage-profile/security/api-tokens> and choose **Create API token** (the classic kind, not "with scopes"). That account needs permission to add pages in the space.
3. **Add two secrets.** In the repo, go to *Settings → Secrets and variables → Actions → Secrets*:
   | Secret | Value |
   |---|---|
   | `CONFLUENCE_EMAIL` | the account's e-mail address |
   | `CONFLUENCE_API_TOKEN` | the token from step 2 |
4. **Add the variables.** Same screen, on the *Variables* tab:
   | Variable | Value | Required |
   |---|---|---|
   | `CONFLUENCE_BASE_URL` | `https://<your-site>.atlassian.net` | yes |
   | `CONFLUENCE_SPACE_KEY` | the key of the existing space (shown in the space URL: `/wiki/spaces/<KEY>/…`) | yes |
   | `CONFLUENCE_PARENT_ID` | id of the page that the top-level `README.md` becomes (the number in the page's URL). If you leave it out, the space homepage is used, and its current content and title are replaced. | no |
   | `DOCS_DIR` | folder that holds the Markdown. Defaults to the repo root. | no |
   | `CONFLUENCE_IGNORE` | comma-separated globs to skip, e.g. `drafts/*,notes.md` | no |
5. **Do a test run.** Go to *Actions → Sync Markdown to Confluence → Run workflow* and tick **Dry run**. The log lists every page it would create and where it would go. Then run it again without the tick to upload everything.

After that, each push to `main` uploads only the Markdown files the push changed. Running the workflow by hand always re-uploads every page. The workflow is set to `main`; if your branch is called `master`, change `branches:` in the workflow.

## How files become pages

| In git | In Confluence |
|---|---|
| `02-team-members.md` | a page, titled by the file's first `# Heading` ("Team Members") |
| `04-project-canvas/README.md` | the parent page "Project Canvas" |
| other files in `04-project-canvas/` | its child pages |
| a folder without a `README.md` | a parent page that just lists its children |
| `README.md` at the top | the root page: it replaces the content and title of the `CONFLUENCE_PARENT_ID` page, or of the space homepage |
| a link such as `[Risks](11-risks.md)` | a Confluence link to the page "Risks" |

To add a page, add a `.md` file. To give a page children, make it a folder: put the page's content in the folder's `README.md` and the children next to it.

- **Pages are matched by title.** If a page with that title already exists in the space, it gets a new version and is moved under the right parent. If not, a new page is created. Titles must be unique, and the sync stops with an error if two files share a heading.
- **Nothing is ever deleted.** If you delete a file, its page stays. If you change a file's `#` heading, the next sync creates a new page and leaves the old one. To move the old page's children across, run the workflow by hand, then delete the old page yourself.
- **Git always wins.** Edits made directly in Confluence are overwritten the next time that file changes in git. Students should copy these pages rather than edit them.
- **What converts:** headings, lists, tables (including `<br>` inside cells), bold/italic, code and links. **Images are not uploaded.**

## Preview locally

```bash
pip install -r .github/confluence-sync/requirements.txt
python .github/confluence-sync/sync.py --all --dry-run --out preview/
```

This writes the converted page bodies (Confluence storage format) to `preview/` and contacts nothing.
