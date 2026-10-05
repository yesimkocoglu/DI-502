# Project Executive Summary

This section briefly summarizes the entire project charter, highlighting the significant points of interest to the reader. It includes all of the information required for approval by the key stakeholders. The summary should also include some background information on the project that:

- includes the reason(s) for creating the project (e.g., a business problem or opportunity, a legal requirement, etc.); and,
- the budget, duration and timeline of the project.

While filling in this page, focus on end-users: the people who use the system. Everything from objectives, project scope and the desired features should cater to end-users, not to developers (yourselves).

Write objectives as **outcomes for the people who use the system**, not as work your team will do. Write "By the end of Sprint 4, residents find their next collection day in under 1 minute, compared with about 5 minutes on the current city website" (illustrative numbers), not "Build a RAG chatbot".

In ISO/IEC 5338 terms, this page belongs to the Inception stage [1]. It covers the 6.4.1 Business or mission analysis process and the 6.4.2 Stakeholder needs and requirements definition process [1]. You do not need to write ISO process names or numbers in your charter.

Numbers in examples are illustrative only. Outside sources are cited by number, for example [1]; full references are at the end.

## How to fill in each part

| Part | What it means | When it applies | Question it answers |
|---|---|---|---|
| **Background** | The reason the project exists: a business problem, an opportunity or a legal requirement | Always; it opens the page | Why is this project needed? |
| **Budget, duration and timeline** | The fixed budget, the length of the project and its start and end dates | Always | How much, how long, and from when to when? |
| **Stakeholders** | The key stakeholders who will benefit from the project results, each labelled with its role (see possible roles from ISO 5339) | Always | Who gains from the result, and in which role? |
| **Project vision** | The future state the project creates for its end-users, in one or two sentences; see 2.1 | Once per charter; revise it with the charter | What will be different for end-users when the project is done? |
| **Objectives** | The project's business objectives: an overhead view of what the project aims for, written by the SMART method | Every row of the objectives table | What outcome do we commit to, for whom, by when? |
| **Success criteria** | Concrete, measurable criteria that confirm whether an objective has been met, written in plain language | Every objective, without exception | How will we know the objective is met, and who decides? |
| **Business outcomes** | Results expected at the end of the project | Every objective; expected at the end of the project | What measurable change do the stakeholders get? |
| **Scope definition** | A high-level description of the features and functions of the product, service or result | Written once here. This page is the project proposal, and later scope must not grow beyond it | What will the product do for its users? |

## Background, budget, duration and timeline

1. The background states why the project exists: a business problem, an opportunity or a legal requirement.
2. The budget line states the fixed budget: $100 of Google Cloud credits per project.
3. The duration states the number of sprints, and the timeline states the project's start and end dates.
4. Sprint-by-sprint dates go on the Release Plan page; cost items go on the Cost & Funding page.

## 1. Stakeholders

Identify the key stakeholders who will benefit from the project results. Label each one with its role (see possible roles from ISO 5339 below).

### Possible roles from ISO 5339

ISO/IEC 5339 defines two groups of stakeholders. It also sorts them into "make", "use" and "impact" perspectives [2].

**AI stakeholders**

| Role | Perspective | Who it is (paraphrased) |
|---|---|---|
| **AI producer** | Make | Designs, develops, tests and deploys products or services that use AI systems. Involved in all stages, from inception to retirement. |
| **AI developer** | Make | Builds the AI product or service for the AI producer: model and system design, implementation, verification and validation. Can be an employee, contractor or partner. |
| **Data provider** | Make | Collects and/or prepares the data for the AI model. |
| **AI application provider** | Shares part of the make perspective | Provides the AI system's capabilities as a product or service to internal or external customers. Mainly involved at deployment. |
| **AI partner** | (not assigned to a perspective) | Provides services to the AI producer and AI application provider within a business relationship. |
| **AI customer** | Use | Uses the AI product or service directly, or provides it to AI users. Has a business relationship with the AI application provider. |
| **AI user** | Use | Uses the AI product or service. Needs no business relationship, so a user need not be a customer. |

**Other stakeholders**

| Role | Perspective | Who it is (paraphrased) |
|---|---|---|
| **Community** | Impact | People affected by the application beyond its customers and users, such as consumers, families or neighbours. |
| **Regulators / policy makers** | Impact | Regulators have authority over AI use where the application is deployed. Policy makers set the legal requirements for that use. |

Your own team usually holds the make roles. Describe team roles on the Project Organization page, not here.

### Rules

1. Every stakeholder row names one role (see possible roles from ISO 5339).
2. Every stakeholder row states what that stakeholder gains from the project result, or, for an impact-perspective role such as a regulator, what its interest in the project is.
3. At least one row is an AI user (an end-user). If a different party buys or commissions the system, list it as the AI customer in its own row.
4. One row holds one role. The party who buys the system (AI customer), the party who uses it (AI user) and the party who runs it (AI application provider) are different roles, even when one organization holds two of them [2].
5. The list covers more than one stakeholder type, because narrow stakeholder views can introduce bias [1].
6. If the application affects a community beyond its users, consider listing that community [2].
7. If two stakeholders want conflicting things, the conflict is written down.

### Stakeholder test

Ask these three questions of every row:

1. **Which single 5339 role is this?** If you need two roles, split the row (rule 4).
2. **What do they gain, in one sentence?** If you cannot say it, they may not be a key stakeholder (rule 2).
3. **Does anyone else want the opposite?** If yes, write the conflict below the table (rule 7).

Each right-hand entry fixes only the named defect. 
| Not this | This |
|---|---|
| "Company / application provider: the company that buys the assistant and analyses usage trends." **Defect:** two 5339 roles merged in one row (rule 4). | Row 1: "City waste department, **AI customer**: buys the assistant for its residents." Row 2: "City IT unit, **AI application provider**: runs the assistant and reviews usage trends." |
| "Students: secondary end-user target audience; gain a learning tool." **Defect:** informal group name with no 5339 role (rule 1). | "Students, **AI user**: secondary end-user target audience; gain a learning tool." |

## 2. Project Vision and Objectives

This section describes the project vision and the project objectives, and links each objective to related measurable business outcomes. Measurement criteria must also be provided to confirm that an objective has been reached.

Keep in mind that objectives defined here should be an overhead view. Each objective should have concrete, measurable success criteria to confirm whether the objective has been met. Business outcomes are results expected at the end of the project. Add rows as required.

### 2.1 Project vision

The vision states, in one or two sentences, the future state the project creates for its end-users. The project uses RAG as its basic solution; this is a constraint set by the Project Review Committee, so the vision does not need to argue for it or mention it.

**Questions to ask before you write**
- Which problem should be solved?
- Which value or advantage will be created?
- Who is impacted by the project result?
- Are there conflicts between multiple stakeholders?

**Elements of a vision statement**

| # | Element | What to write |
|---|---|---|
| 1 | Problem or opportunity | The need that triggered the project [1]. |
| 2 | Who benefits, named specifically | The end-users from section 1, named as specific groups. |
| 3 | The change for them, not the artefact | The future state end-users experience, not the system you build. |
| 4 | No implementation detail | No model names, techniques or tools. |
| 5 | No metrics or thresholds | Measurable targets go in the success criteria (2.3). |
| 6 | Short and plain | One or two sentences that a stakeholder can repeat. |
| 7 | Traceable to the objectives | Each objective reads as a step toward the vision. The vision makes no claim the objectives cannot support. |

Check also whether AI-specific risks could block the vision: privacy limits on reusing personal data, data accessibility or data quality [1]. If one could, record it on the Risks page.

Do not confuse the vision with the strategic objective. The vision describes the future for end-users, with no numbers or dates. The strategic objective is row 1 of the objectives table: the broadest objective, written by SMART, with a date and measurable success criteria. Write both.

| Not this | This |
|---|---|
| "Provide an assistant that lets users explore and compare topics; the information will be data-driven, grounded and accurate." **Defect:** describes the artefact, not the change for end-users (element 3). | "Users settle a question about [topic] in one place, without searching several sites; the information will be data-driven, grounded and accurate." |
| "By combining retrieval-augmented generation with fine-tuned domain language models, the assistant will bridge real-time events and formal records." **Defect:** implementation detail (element 4). | "The assistant will bridge real-time events and formal records." |

### 2.2 Objectives

The objectives on this page are business objectives. Write each one by the SMART method: Specific, Measurable, Achievable, Realistic and Time-bound. An objective that fails any one of the five tests is not yet SMART [3].

| Letter | Meaning | Test |
|---|---|---|
| **S**pecific | Says who, what, where, when and why, so that a second reader knows what success looks like [3] | Give it to a classmate. If they must ask what counts as success, it is not specific [3] |
| **M**easurable | Has a quantitative or verifiable indicator. An experience becomes measurable through a proxy such as a rating or survey score [3] | Can you name the number or check that decides it? |
| **A**chievable | Within reach of your team's resources, skills and constraints. Achievable does not mean easy [3] | What must you do, get or change to make it possible? [3] |
| **R**ealistic | The target does not overclaim; "100% correct answers on all questions" is unrealistic | Would a reviewer believe this target for your domain and time frame? |
| **T**ime-bound | Has a deadline, or milestones at set intervals [3] | Is there a date or sprint? |

**Strategic objective and Phase-1 objective.** Row 1 is a broad, outcome-focused strategic objective. A narrower MVP objective follows as the Phase-1 objective. Both have measurable success criteria. A broad objective can stay ambitious while its success criteria stay precise [3].

**Rules for objectives**

1. The objective is an outcome, not an activity: "reduce time-to-answer", not "build a RAG system".
2. The objective has a date or sprint.
3. The objective names its target users and domain.
4. The objective names no model, tool or architecture. RAG is a given constraint, not an objective.
5. The objective serves end-users, not developers.
6. The objective contains no unmeasured adjectives or buzzwords such as "fast", "intuitive" or "real time".
7. One sentence holds one goal [3].
8. No target is unrealistic, such as "100% correct answers".
9. The objective is not a milestone. "Deploy MVP and conduct demo" is a milestone.
10. The objective is not a constraint. "The system will not store any PII" reads like a constraint.
11. Across all rows, the objectives cover quality, performance/cost, adoption/UX, and safety/compliance. Model performance is not always the target.
12. Every objective has matching content in the rest of the charter. For example, a user-satisfaction target needs a milestone and a deliverable for the survey result.

### 2.3 Success criteria

1. Each criterion is a measurable result, not an action. "The system will run on the provided cloud" is not a success criterion.
2. Each criterion has a date or sprint.
3. Each criterion names its measurement method and its acceptance owner [3].
4. Each criterion uses a plain-language measure that a stakeholder understands without technical background, such as the share of answers judged correct or the time needed to find something. It uses no convoluted metric such as Recall@k or RAG-triad scores.
5. Each criterion maps to one or more specific metrics. Technical metrics are defined in the experiment cards and model card; user-facing ones, such as survey scores, are defined in the criterion itself. The Risks page uses these metrics as triggers.
6. The team sets each target level for its own project and states where the level comes from.
7. A criterion that claims an improvement compares against the **baseline**. Here, the baseline is the default state: what users do or get today without the project. It is not a model baseline. Example: today, people find it hard to find restaurants that suit them (default state); with the app, they get more personalized recommendations. To turn this into a criterion, measure both states, for example the share of users who find a restaurant they like within 5 minutes, before and with the app (illustrative).

### 2.4 Business outcomes

1. Each business outcome is a result expected at the end of the project.
2. Each business outcome is measurable.
3. Each business outcome uses no adjectives in place of numbers.
4. Each business outcome is a change for users or stakeholders. An approval is not a business outcome.
5. Each business outcome is not an activity of the team.

### Objective test

Ask these five questions of every row:

1. **Would your team do this as work?** If yes, it is an activity and belongs under Major Activities.
2. **Could a classmate tell, without asking you, whether it was met?**
3. **How does it move toward the vision, in one sentence?**
4. **Who accepts it, and by which method?**
5. **Where does it appear in Milestones and Deliverables?**

| Not this | This |
|---|---|
| Business outcome: "Building an assistant that answers users' questions using RAG." **Defect:** activity, not outcome (2.4 rule 5). | Business outcome: "Residents answer their own collection questions instead of calling the helpline." |
| Objective: "The system will provide scalability under limited academic resources." **Defect:** serves the developers, not end-users (2.2 rule 5). | Objective: "Residents can still use the assistant on collection-day mornings, when demand peaks." |
| Objective: "Provide an intuitive, responsive and trustworthy entry point for residents." **Defect:** adjectives instead of numbers (2.2 rule 6). | Objective: "Provide an entry point where residents get an answer within 3 seconds and rate it helpful in at least 80% of cases." |
| Success criterion: "Qualitative feedback collected from at least 2 stakeholder groups." **Defect:** an action, not a measurable result (2.3 rule 1). | Success criterion: "At least 70% of pilot residents rate the answers as clear in the feedback survey." |
| Success criterion: "At least 70% accuracy." **Defect:** no date and no measurement method (2.3 rules 2–3). | Success criterion: "By the end of Sprint 4, at least 70% accuracy, judged by the department's reviewer on a fixed set of 100 test questions." |
| Success criterion: "Faithfulness ≥ 0.75, relevance ≥ 0.80, grounding ≥ 0.80." **Defect:** convoluted metric names (2.3 rule 4). | Success criterion: "At least 75% of answers are supported by the sources they cite." |
| Business outcome: "Residents receive accurate, timely information from several sources without switching platforms." **Defect:** not measurable (2.4 rule 2). | Business outcome: "Residents use one source instead of three; average lookup time falls from about 5 minutes (default state, measured in Sprint 1) to under 1 minute." |
| Objective: "Deploy MVP and conduct demo." Business outcome: "Academic validation and project approval." **Defect:** a milestone, and an approval instead of an outcome (2.2 rule 9; 2.4 rule 4). | Objective: "By [date], validate problem–solution fit with an MVP assistant that delivers sourced, accurate answers and measurable time savings for [target users]". |

### If you are stuck

Use one of these patterns:

- **Template sentence:** "(By [date]), [verb] [outcome] for [target users] in [scope] to achieve [business value]."
- **Strategic plus Phase-1:** one broad objective for the whole project, then one narrower MVP objective; both with measurable success criteria.
- **From–to:** state today's value and the target, for example "raise X from 78% to 85% by [date]" [3]. Today's value is the default state.
- **Proxy measure:** make an experience measurable through a rating or survey score [3].
- **One row per family:** write one objective each for quality, performance/cost, adoption/UX and safety/compliance.

## 3. Project Scope

### 3.1. Scope Definition

Provide a high-level description of the features and functions that characterize the product, service or result to be delivered by the project. This page is the project proposal: do not grow the scope beyond it later.

Project scope sets the boundaries of a project: what is included and what is excluded [4]. Start from the goals, because every scope item should serve one [4]. A clear scope helps you spot scope creep, meaning features that were never part of the plan [4].

**Rules**

1. Each feature is described by what the user can do with it.
2. Each feature serves at least one objective.
3. No feature description names models, retrieval techniques, frameworks or architecture. The System Architecture Diagram page covers those.
4. No feature description uses unmeasured adjectives such as "simple", "easy to use" or "real time".
5. Excluded work is not described here. Mark it Out of Scope under Major Activities. Clear exclusions keep the team on the agreed objectives [4].

**Scope test** [4]**:** for each feature, name the objective row it serves. If you cannot, the feature is scope creep: drop it, or mark it Out of Scope under Major Activities.

Each right-hand entry fixes only the named defect, so it may still need other fixes.

| Not this | This |
|---|---|
| "The retriever uses vector similarity search to match queries to the most relevant text segments." **Defect:** implementation detail (rule 3). | "Residents ask a question in their own words and get the matching rule from the official collection guide." |
| "A simple, easy-to-use interface that gives responses in real time." **Defect:** unmeasured adjectives (rule 4). | "An interface where residents type a question and see the answer within 3 seconds." |

## What does not belong in this section

| Item | Where it belongs |
|---|---|
| Sprint-by-sprint start and end dates | Release Plan |
| Cost items and source of funding | Cost & Funding |
| Milestones, such as "deploy MVP and conduct demo" | Milestones |
| Deliverables and their approving stakeholders | Deliverables |
| RAG as the solution approach | Assumptions & Constraints, as a constraint set by the Project Review Committee |
| Other constraint-like statements: no PII, licensing, English only, input boundaries | Assumptions & Constraints |
| Activities, and features you will not deliver | Major Activities, marked In Scope or Out of Scope |
| Team members' roles and responsibilities | Project Organization |
| The risk that an objective is not met | Risks |
| Model names, architecture, retrieval design | System Architecture Diagram |
| Specific metrics behind each success criterion, such as Recall@k or RAG-triad scores | Experiment cards and model card |
| Product backlog | Not on this page |

## Fill-in tables

### Background

> Why does this project exist? State the business problem, opportunity or legal requirement.

**Budget:** $100 of Google Cloud credits (fixed, per project).
**Duration:** [number] sprints.
**Timeline:** [start date] to [end date].

### 1. Stakeholders

| # | Stakeholder | Role (see possible roles from ISO 5339) | Perspective (make / use / impact) | Relationship to project | Benefit from project |
|---|---|---|---|---|---|
| 1 |   |   |   |   |   |
| 2 |   |   |   |   |   |
| 3 |   |   |   |   |   |

Conflicts between stakeholders (if any):

### 2. Project Vision

> One or two sentences.

### 2. Objectives

In each Success Criteria cell, write for every criterion: the plain-language target with where the level comes from, the measurement method, the acceptance owner, the date or sprint, and the specific metric(s) it maps to.

| # | Objectives | Success Criteria | Business Outcomes |
|---|---|---|---|
| 1 (strategic) |   |   |   |
| 2 (Phase-1 MVP) |   |   |   |
| 3 |   |   |   |

### 3.1. Scope Definition

> High-level description of the product.

| # | Feature | What the user can do with it | Objective(s) it serves |
|---|---|---|---|
| 1 |   |   |   |

## Example (illustrative only)

Every name, number, date and target below is invented. None is a real project fact.

**Background.** City residents find waste-collection rules in three places: a PDF calendar, the city website and a telephone helpline. Residents miss collections, and the helpline receives many repeated questions.

**Budget:** $100 of Google Cloud credits (fixed, per project). **Duration:** 4 sprints. **Timeline:** 1 October to 15 January.

**1. Stakeholders**

| # | Stakeholder | Role (ISO 5339) | Perspective | Relationship to project | Benefit from project |
|---|---|---|---|---|---|
| 1 | City residents | AI user | Use | Ask questions about sorting and collection days | Correct answers in one place |
| 2 | City waste department | AI customer | Use | Commissions the assistant for residents | Fewer repeated helpline calls |
| 3 | City IT unit | AI application provider | Make (shared) | Runs the assistant after deployment | Sees which questions residents ask most |
| 4 | Collection contractor | Data provider | Make | Supplies the collection schedules | Fewer missed-collection complaints |
| 5 | Neighbours of missed bins | Community | Impact | Affected when bins are left out | Cleaner streets |

Conflicts: the department wants fewer helpline calls, but residents without internet access still need the helpline. The helpline stays (see Out of Scope under Major Activities).

**2. Project Vision.** Every resident can find out, in one place and in their own words, what goes in which bin and when it is collected, so fewer collections are missed.

**Objectives**

| # | Objectives | Success Criteria | Business Outcomes |
|---|---|---|---|
| 1 (strategic) | By the end of Sprint 4, reduce the time residents need to answer a waste-collection question, compared with the current website and helpline. | Median time to answer a test question falls from 5 minutes (default state, measured on the current website in Sprint 1) to under 1 minute. Method: timed usability test with 10 residents. Owner: Product Owner. End of Sprint 4. Maps to: task completion time in the usability test, supported by end-to-end response time and answer correctness. | During the pilot, residents in the test group make 20% fewer helpline calls about collection days than before the pilot. |
| 2 (Phase-1 MVP) | By the end of Sprint 3, validate that an MVP assistant gives correct, source-backed answers to common collection questions for residents. | At least 80% of answers judged correct on a fixed set of 100 test questions; at least 90% of answers link to the official source page (levels set from the team's own research). Method: review by the department. Owner: department reviewer. End of Sprint 3. Maps to: answer correctness, retrieval quality and citation metrics in the experiment cards. | Residents need no second source for 9 of 10 questions, measured in the pilot survey. |
| 3 | By the end of Sprint 4, residents in the pilot prefer the assistant to the current website for collection questions. | At least 70% of 20 pilot residents say they would use it again. Method: post-test survey. Owner: Product Owner. End of Sprint 4. Maps to: survey score. | At least half of pilot residents report using the assistant as their first source for collection questions in the follow-up survey. |
| 4 | By the end of Sprint 4, residents are not misled when they ask questions the assistant cannot answer. | The assistant declines and points to the helpline in at least 95% of 30 out-of-domain test questions. Method: scripted test set reviewed by the department. Owner: department reviewer. End of Sprint 4. Maps to: refusal rate on out-of-domain questions. | No pilot resident reports wrong advice. |

Objectives 1–4 cover performance, quality, adoption/UX and safety in turn.

**3.1. Scope Definition.** A question-answering assistant for the city's waste-collection rules, used by residents through a web page.

| # | Feature | What the user can do with it | Objective(s) it serves |
|---|---|---|---|
| 1 | Plain-language questions | Ask about sorting or collection in their own words and get an answer | 1, 2 |
| 2 | Source link | Open the official page each answer comes from | 2 |
| 3 | Collection day by street | Enter a street name and see the next collection day | 1 |
| 4 | Out-of-domain handling | Get a pointer to the helpline when the assistant cannot answer | 4 |

## Checklist before submitting

**Whole page**
- [ ] The background gives the reason for the project, the budget ($100 of Google Cloud credits), the number of sprints, and the start and end dates
- [ ] Nowhere on the page names a model, tool or technique, or uses an unmeasured adjective

**Stakeholders**
- [ ] Each row has one ISO 5339 role and says what the stakeholder gains (or its interest, for impact roles)
- [ ] At least one row is an AI user, and any conflict between stakeholders is written down

**Vision**
- [ ] One or two sentences describe the change for end-users, with no metrics

**Objectives**
- [ ] Row 1 is the strategic objective, and row 2 is the Phase-1 MVP objective
- [ ] Each objective passes all five SMART tests, is an outcome for end-users, and is not a milestone or a constraint
- [ ] Each objective is a step toward the vision and has a matching milestone and deliverable
- [ ] Together, the objectives cover quality, performance/cost, adoption/UX and safety/compliance

**Success criteria and business outcomes**
- [ ] Each success criterion is a measurable result in plain language, with a date or sprint, a method, an owner, the metric it maps to, and where its target level comes from
- [ ] Each improvement claim compares against the default state
- [ ] Each business outcome is a measurable change for users or stakeholders, not an approval or an activity

**Scope**
- [ ] Each feature says what the user can do and which objective it serves

## References

[1] ISO/IEC JTC 1/SC 42, *ISO/IEC 5338:2023 Information technology — Artificial intelligence — AI system life cycle processes*, 1st ed. Geneva, Switzerland: International Organization for Standardization and International Electrotechnical Commission, Dec. 2023. UK implementation: BS ISO/IEC 5338:2023, London, UK: BSI Standards Limited, 2024.

[2] ISO/IEC JTC 1/SC 42, *ISO/IEC 5339:2024 Information technology — Artificial intelligence — Guidance for AI applications*, 1st ed. Geneva, Switzerland: International Organization for Standardization and International Electrotechnical Commission, Jan. 2024. UK implementation: BS ISO/IEC 5339:2024, London, UK: BSI Standards Limited, 2024.

[3] Swiss Education Group, "What Are SMART Goals? Components, Examples, and Benefits," HIM Business School, n.d. [Online]. Available: https://www.him-business-school.com/en/news/smart-goals/ (accessed Oct. 1, 2026).

[4] F. Grace, "How to define and create a project scope in 5 simple steps," Atlassian, n.d. [Online]. Available: https://www.atlassian.com/work-management/project-management/project-scope (accessed Oct. 1, 2026).
