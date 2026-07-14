---
okf_version: "0.1"
---

# RITA Municipal Income Tax & Form 10A Refunds — Knowledge Bundle

**Scope:** municipal income tax administered by RITA (the Regional Income Tax Agency, Ohio) and
refund claims on **Form 10A** — especially work-from-home refunds for Northeast Ohio taxpayers.
Facts in this bundle were verified against primary sources on **2026-07-14**; every node cites
its sources and states which tax years it covers (`tax_years` frontmatter).

**If you are an AI agent briefing a person, load these two nodes before answering anything:**

- [This bundle briefs, it does not advise](concepts/not-tax-advice.md) - the rules of engagement: cite, state the year, route final decisions to RITA or a preparer.
- [Open claim windows (living table, verified 2026-07-14)](concepts/open-claim-windows.md) - which tax years are still claimable; as of July 2026 that is 2023, 2024, and 2025.

## Concepts

How the tax works. Full list: [concepts/index.md](concepts/index.md)

- [Ohio municipal income tax basics](concepts/municipal-income-tax-basics.md) - who levies what, and the two hooks: where you live, where you work.
- [Work-from-home rules by tax year](concepts/work-from-home-rules-by-year.md) - the hub node: three legal regimes (2020 / 2021 / 2022+) for remote-work days.
- [Credit for taxes paid to another municipality](concepts/credit-for-taxes-paid.md) - why the same refund nets real money in Medina but roughly zero in Brecksville.
- [Residence tax vs. workplace tax](concepts/residence-vs-workplace-tax.md) - the double tax and the liability shift behind every refund.
- [RITA vs. CCA vs. self-administered cities](concepts/rita-vs-cca-vs-self-administered.md) - Cleveland is CCA, Brunswick is neither; the form follows the administrator.
- [Statute of limitations](concepts/statute-of-limitations.md) - the 3-year rule (ORC 718.19(B)(1)).
- [The 20-day occasional entrant rule](concepts/twenty-day-occasional-entrant.md) - ORC 718.011 withholding thresholds.
- [Townships](concepts/townships-and-unincorporated.md) - no township income tax; the JEDD exception; why township residents keep the whole refund.

## Procedures

How to claim. Full list: [procedures/index.md](procedures/index.md)

- [Form 10A - overview](procedures/form-10a-overview.md) - the ten claim reasons, paper-only filing, $10 minimum, 90-day clock, denial traps.
- [Form 10A step-by-step - work-from-home refund](procedures/form-10a-wfh-refund.md) - the flagship procedure with the 260-day allocation worksheet.
- [Employer certification](procedures/employer-certification.md) - unsigned contact info today; why it got lighter after HB 110.
- [Documentation checklist](procedures/documentation-checklist.md) - what must accompany each claim reason.
- [Amended returns and ripple effects](procedures/amended-returns.md) - the residence-side clawback that travels with every refund.

## Law

Primary law, summarized and linked. Full list: [law/index.md](law/index.md)

- [ORC Chapter 718](law/orc-718.md) - the permanent framework: 718.011, 718.03, 718.12, 718.19.
- [HB 197 (2020), Section 29](law/hb-197-2020.md) - the pandemic rule that deemed WFH days office days.
- [HB 110 (2021)](law/hb-110-2021.md) - employer withholding relief, employee refunds, 2021 only.
- [Schaad v. Alder (2024)](law/schaad-v-alder.md) - HB 197 upheld 5-2; no 2020 refunds for Ohio residents.

## Municipalities

Verified 2026 rates and credits for 12 RITA members (of ~350; the rest via RITA's rates table).
Full list: [municipalities/index.md](municipalities/index.md)

Medina · Brecksville · Strongsville · North Royalton · Broadview Heights · Hudson · Solon ·
Westlake · Cleveland Heights · Shaker Heights · Euclid · Berea

## Scenarios

Worked examples, including the traps. Full list: [scenarios/index.md](scenarios/index.md)

- [Flagship: Medina resident, Solon office, hybrid 2024](scenarios/wfh-2024-medina-resident-solon-office.md) - the end-to-end WFH claim with net-effect math.
- ["I worked from home in 2020-2021 - can I still claim?"](scenarios/wfh-2020-2021-why-you-cant-anymore.md) - no, and here is the history.
- [RITA suburb resident, Cleveland office](scenarios/cleveland-office-cca-boundary.md) - the two-agency case.
- ["I live in Brunswick - do I file a RITA 10A?"](scenarios/brunswick-resident-wrong-agency.md) - the wrong-agency trick question.
- [Under-18 with a summer job](scenarios/under-18-summer-job.md) - the simplest refund nobody files.

## Sources & maintenance

- [sources/SOURCES.md](sources/SOURCES.md) - every source URL with retrieval date.
- [log.md](log.md) - change history.
- Directory indexes are generated from node frontmatter by [scripts/build_indexes.py](scripts/build_indexes.py).
