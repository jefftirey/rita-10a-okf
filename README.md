# RITA Form 10A — a knowledge bundle for your AI

If you live or work in Northeast Ohio, chances are a chunk of your paycheck goes to municipal
income tax through **RITA** (the Regional Income Tax Agency). If you work from home some or all
of the time — or your employer withholds for a city you don't actually work in — you may be owed
a refund, claimed on **Form 10A**. Most people never file it.

This repository is a knowledge bundle about exactly that: RITA municipal income tax, who owes
what to which city, and how Form 10A refunds work — **written to be read by your AI assistant,
not by you**.

## How to use it

Point your AI (Claude, ChatGPT, or any assistant that can read files or URLs) at this repository
and ask your question in plain English:

> "I live in Medina and worked from home 3 days a week in 2024 while my employer withheld
> Cleveland-area city tax. Am I owed anything?"

Your assistant starts at **[rita-10a-okf/index.md](rita-10a-okf/index.md)**, walks to the relevant pages, and briefs you — with citations to
the actual law, RITA's own publications, and your municipality's real rates. You confirm anything
that matters with RITA or a tax preparer.

## What's in here

- Plain-language explanations of how Ohio municipal income tax works (residence vs. workplace,
  credits, the 20-day rule, why townships are different).
- The Form 10A refund procedures, step by step, including the work-from-home scenario — plus a
  [one-stop links page](procedures/official-documents.md) to the actual forms, rules, and statutes.
- A sub-bundle per municipality — all **413 RITA member cities and villages**, each with its
  own directory: profile, published tax rate and credit, and city-specific refund mechanics,
  generated from RITA's own rates data (plus a table of the 64 JEDD/JEDZ special districts).
- The law behind it (Ohio Revised Code Chapter 718, the 2020–2021 pandemic rules, and the
  court decisions that settled them).
- Worked example scenarios.

This bundle is a **filing aide, not a substitute for the documents**: it explains, then links
you to the actual form PDFs, the actual statutes, and the actual agency pages.

**Every factual claim is cited.** The full research log — every source URL and the date it was
retrieved — is in [rita-10a-okf/sources/SOURCES.md](rita-10a-okf/sources/SOURCES.md).

## Repository layout

- **[`rita-10a-okf/`](rita-10a-okf/)** — the knowledge bundle itself. This is what you point
  your AI at. Everything inside is OKF: markdown nodes with YAML frontmatter, per-directory
  indexes, a change log, and the source log.
- `scripts/` — maintenance tooling (not part of the bundle): fetches RITA's published rates
  data and regenerates the municipality sub-bundles and directory indexes.

## Format

The bundle uses the [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf):
a plain directory of markdown files with YAML frontmatter and per-directory indexes, designed so
AI agents can navigate knowledge the way you'd browse a well-organized binder. No special tooling
required — it's just files.

## Not tax advice

This bundle briefs; it does not advise. Nothing here is tax, legal, or financial advice. Tax
rules are year-specific and change; every page states which tax years it applies to and when its
facts were last verified. Confirm anything you plan to act on with RITA
([ritaohio.com](https://www.ritaohio.com), 800-860-7482) or a qualified tax preparer.

## About this project

This repository is a real-world example of **sharing knowledge in a form built for AI**.
It uses the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
because OKF is appealingly simple: plain markdown files with a small YAML header, organized by
folders and indexes — no database, no embeddings, no special tooling. An assistant reads an
index, follows links to just the pages it needs, and cites its sources, the same way a careful
person would use a well-organized binder. Knowledge published this way is inspectable,
correctable, and versioned — it's just files in git.

The point is effort spent once so you don't have to repeat it: the statutes have been located
and quoted, the court decision cited, RITA's forms collected, and all 477 rate-table entries
pulled from RITA's own data and spot-verified against primary sources — with every source URL
and retrieval date logged. Your AI starts from that finished work instead of re-searching the
open web and hoping.

Built by **[Jeff Tirey](https://github.com/jefftirey)**, a Northeast Ohio local. Jeff builds
AI systems for real-world businesses at
**[thalatta.ai](https://thalatta.ai/?utm_source=github&utm_medium=readme&utm_campaign=rita-10a-okf)**.

Corrections and contributions welcome — open an issue.
