---
okf_version: "0.1"
---

# RITA Municipal Income Tax & Form 10A Refunds — Knowledge Bundle

**Scope:** municipal income tax administered by RITA (the Regional Income Tax Agency, Ohio) and
refund claims on **Form 10A**. Facts were verified against primary sources on **2026-07-14**;
every node cites its sources and states which tax years it covers (`tax_years` frontmatter).
This bundle briefs and links to the authoritative documents; it does not advise or compute.

**If you are an AI agent briefing a person, load these two nodes before answering anything:**

- [This bundle briefs, it does not advise](concepts/not-tax-advice.md) - the rules of engagement: cite, state the year, route final decisions to RITA or a preparer.
- [Open claim windows (living table, verified 2026-07-14)](concepts/open-claim-windows.md) - which tax years are still claimable; as of July 2026 that is 2023, 2024, and 2025.

## Concepts

How the tax works. Full list: [concepts/index.md](concepts/index.md)

- [Ohio municipal income tax basics](concepts/municipal-income-tax-basics.md) - who levies what, and the two hooks: where you live, where you work.
- [Work-from-home rules by tax year](concepts/work-from-home-rules-by-year.md) - the hub node: three legal regimes (2020 / 2021 / 2022+) for remote-work days.
- [Credit for taxes paid to another municipality](concepts/credit-for-taxes-paid.md) - the credit factor and credit limit, where to find them per city and year, and which documents define the computation.
- [Residence tax vs. workplace tax](concepts/residence-vs-workplace-tax.md) - the two overlapping taxes on the same paycheck.
- [RITA vs. CCA vs. self-administered cities](concepts/rita-vs-cca-vs-self-administered.md) - Cleveland is CCA, Brunswick is neither; the form follows the administrator.
- [Statute of limitations](concepts/statute-of-limitations.md) - the 3-year rule (ORC 718.19(B)(1)).
- [The 20-day occasional entrant rule](concepts/twenty-day-occasional-entrant.md) - ORC 718.011 withholding thresholds.
- [Townships](concepts/townships-and-unincorporated.md) - no township income tax; the JEDD exception.

## Procedures

How to claim. Full list: [procedures/index.md](procedures/index.md)

- [Official documents and where to find them](procedures/official-documents.md) - direct links to the actual forms, rules, rates table, statutes, and opinion. Hand people the real documents.
- [Form 10A - overview](procedures/form-10a-overview.md) - the ten claim reasons, paper-only filing, $10 minimum, 90-day clock, denial traps.
- [Form 10A step-by-step - work-from-home refund](procedures/form-10a-wfh-refund.md) - the claim-reason-2 procedure with the 260-day allocation worksheet.
- [Employer certification](procedures/employer-certification.md) - the current unsigned contact section and its history.
- [Documentation checklist](procedures/documentation-checklist.md) - what must accompany each claim reason.
- [Amended returns and ripple effects](procedures/amended-returns.md) - what RITA's instructions say happens to the residence return after a refund.

## Law

Links to the primary law, with key language quoted verbatim — no interpretation.
Full list: [law/index.md](law/index.md)

- [ORC Chapter 718](law/orc-718.md) - the permanent framework: 718.011, 718.03, 718.12, 718.19.
- [HB 197 (2020), Section 29](law/hb-197-2020.md) - the pandemic-era withholding provision, quoted in full.
- [HB 110 (2021)](law/hb-110-2021.md) - the 2021 provisions on withholding and employee refunds.
- [Schaad v. Alder, 2024-Ohio-525](law/schaad-v-alder.md) - the Ohio Supreme Court's decision, syllabus quoted.

## Municipalities

One sub-bundle per RITA member municipality — **413 cities and villages**, generated from
RITA's own Tax Rates Table (tax year 2026, retrieved 2026-07-14), each with profile, published
rates/credits, and refund mechanics. Special districts (JEDD/JEDZ) are listed separately.
Browse the full catalog: [municipalities/index.md](municipalities/index.md) — or **jump
straight to a city** without loading the catalog: `municipalities/<slug>/index.md`, where
`<slug>` is the name lowercased with non-alphanumerics replaced by hyphens
(`north-royalton`, `st-louisville`, `mt-healthy`). If a slug misses, fall back to the catalog.

Examples: [Medina](municipalities/medina/index.md) ·
[Brecksville](municipalities/brecksville/index.md) ·
[Strongsville](municipalities/strongsville/index.md) ·
[Euclid](municipalities/euclid/index.md) ·
[Shaker Heights](municipalities/shaker-heights/index.md) ·
[JEDD/JEDZ districts](municipalities/jedd-jedz-districts.md)

## Scenarios

Fact patterns mapped to the applicable rules and documents. Full list: [scenarios/index.md](scenarios/index.md)

- [Hybrid worker, 2024 - Medina resident, Solon office](scenarios/wfh-2024-medina-resident-solon-office.md) - which rules, forms, and documents apply to the common WFH case.
- [Work-from-home in 2020 or 2021 - the closed years](scenarios/wfh-2020-2021-closed-years.md) - what the record shows about the pandemic years.
- [RITA suburb resident, Cleveland office](scenarios/cleveland-office-cca-boundary.md) - the two-agency case.
- [Brunswick resident - a self-administered city](scenarios/brunswick-resident-wrong-agency.md) - when the city is in neither agency.
- [Under-18 with a summer job](scenarios/under-18-summer-job.md) - the age exemption claim.

## Sources & maintenance

- [sources/SOURCES.md](sources/SOURCES.md) - every source URL with retrieval date, split into current filing documents and the historical record behind the law nodes.
- [log.md](log.md) - change history.
- Generated content: directory indexes and the municipality sub-bundles are built by scripts in
  the repository's `scripts/` directory (outside this bundle) from RITA's published data.
