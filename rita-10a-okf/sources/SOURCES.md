---
type: Reference
title: Research source log
description: Every source consulted with retrieval dates - current filing documents and law, plus the historical record cited by the law and history nodes.
tags: [sources, provenance]
timestamp: 2026-07-14T00:00:00Z
---

# SOURCES — research log

Every source consulted in building this bundle, with retrieval dates. Organized by what it's
for: **current** sources back the live filing guidance (open tax years); **historical** sources
back the law and history nodes that explain the 2020–2021 pandemic rules and why those years can
no longer be claimed — they are kept because those nodes cite them, not because the years are
claimable. All retrieved **2026-07-14** unless noted.

Retrieval notes:
- `legislature.ohio.gov` and `lsc.ohio.gov` fail TLS verification in some fetchers; plain `curl`
  works. `search-prod.lis.state.oh.us/api/v2/.../pdf/` is a reliable direct route to enrolled bills.
- RITA serves media from both `www.ritaohio.com/Media/...` and `cdn.ritaohio.com/Media/...`.
- RITA's Tax Rates Table has **no static downloadable file** — the page renders client-side from
  a JSON endpoint that rejects non-browser requests; scraping requires a real browser session.
- RITA's direct PDF URLs churn (an older 2024 form URL is already dead); prefer starting from
  the forms index page.

## Current — filing documents and live rules (open tax years 2023–2025)

| Source | URL |
|---|---|
| Forms & instructions index (canonical, all years) | https://www.ritaohio.com/individuals/home/formdownloads |
| Form 10A, TY2025 | https://www.ritaohio.com/Media/703127/Form10A%202025%20FINAL.pdf |
| Form 10A instructions, TY2025 | https://cdn.ritaohio.com/Media/703124/2025%20Form%2010A%20FINAL%20Instructions.pdf |
| Form 10A, TY2024 (v2) | https://cdn.ritaohio.com/Media/703143/Form10A%202024v2.pdf |
| Form 10A instructions, TY2024 | https://cdn.ritaohio.com/Media/703154/10A%20Updated%20instructions.pdf |
| Form 10A, TY2023 (v2) | https://cdn.ritaohio.com/Media/703144/Form10A%202023v2.pdf |
| RITA Income Tax Rules & Regulations (eff. 2016, amended 2025-01-01; §9 refunds, §12 limitations) | https://cdn.ritaohio.com/Media/702857/RREGS_EFF%20JAN%201%202016_revised%20012225_061616.pdf |
| RITA Refunds page (90-day processing, $10 minimum, 3-year SOL) | https://www.ritaohio.com/Individuals/Home/Refunds |
| RITA Refunds FAQ | https://www.ritaohio.com/Individuals/Faqs?category=I&subcategory=Refunds |
| RITA Tax Rates Table (year tabs 2020–2026) | https://www.ritaohio.com/TaxRatesTable |
| RITA member municipality list (+ per-member profile pages at `/Municipalities/Home/MemberPage?id=<code>`) | https://www.ritaohio.com/municipalities |

## Current — the law (permanent framework)

| Source | URL |
|---|---|
| ORC 718.011 — occasional entrant / 20-day rule (eff. 2015-03-23) | https://codes.ohio.gov/ohio-revised-code/section-718.011 |
| ORC 718.03 — employer withholding (eff. 2016-09-14) | https://codes.ohio.gov/ohio-revised-code/section-718.03 |
| ORC 718.12 — limitations, interest (eff. 2025-09-30) | https://codes.ohio.gov/ohio-revised-code/section-718.12 |
| ORC 718.19 — refunds, 3-year window (eff. 2025-09-30) | https://codes.ohio.gov/ohio-revised-code/section-718.19 |

## Current — agency boundaries and municipal verification

| Source | URL |
|---|---|
| City of Cleveland Division of Taxation (CCA administers Cleveland) | https://www.clevelandohio.gov/city-hall/departments/finance/divisions/taxation |
| CCA — Cleveland member page (2.50% / 100% / 2.50%) | https://www.ccaohio.gov/member-municipalities/cleveland |
| CCA member lists | https://www.ccaohio.gov/member-municipalities |
| City of Brunswick Income Tax (self-administered, 2.0%) | https://www.brunswick.oh.us/income-tax/ |
| City of Parma Taxation (self-administered, 2.5%) | https://cityofparma-oh.gov/211/Taxation |
| City of Lakewood Municipal Income Tax (self-administered, 1.5%) | https://lakewoodoh.gov/municipal-income-tax/ |
| City of Fairlawn Tax Dept (self-administered, 2%) | https://www.cityoffairlawn.com/58/Tax |
| Ohio Township Association, "Townships 101" (no township income tax) | https://www.ohiotownships.org/townships101 |
| OSU Extension, JEDD factsheet (ORC 715.70–715.72) | https://ohioline.osu.edu/factsheet/cdfs-1560 |
| Ohio Dept. of Taxation "The Finder" (JEDD/JEDZ lookup) | https://thefinder.tax.ohio.gov/jedtax/jed_default.aspx |

## Historical record — cited by the law and history nodes (closed years 2020–2021)

Kept because `law/hb-197-2020.md`, `law/hb-110-2021.md`, `law/schaad-v-alder.md`,
`procedures/employer-certification.md`, and the "why you can't claim 2020–21" scenario cite them.

| Source | URL |
|---|---|
| Am. Sub. HB 197 (133rd GA), enrolled — §29 at pp. 340–341 | https://search-prod.lis.state.oh.us/api/v2/general_assembly_133/legislation/hb197/06_EN/pdf/ |
| Am. Sub. HB 110 (134th GA), enrolled — §§610.115/610.116, 757.40 | https://search-prod.lis.state.oh.us/api/v2/general_assembly_134/legislation/hb110/07_EN/pdf/ |
| LSC Final Bill Analysis, HB 110 (tax portion), pp. 446–448 | https://www.lsc.ohio.gov/assets/legislation/134/hb110/en/files/hb110-tax-bill-analysis-as-enrolled-134th-general-assembly.pdf |
| Schaad v. Alder, 2024-Ohio-525, slip opinion (decided 2024-02-14) | https://www.supremecourt.ohio.gov/rod/docs/pdf/0/2024/2024-ohio-525.pdf |
| Court News Ohio summary of Schaad | https://www.courtnewsohio.gov/cases/2024/SCO/0214/220316.asp |
| Buckeye Institute case page — Schaad v. Alder | https://www.buckeyeinstitute.org/issues/detail/schaad-v-alder |
| Buckeye Institute case page — Morsy v. Dumas (out-of-state exception) | https://www.buckeyeinstitute.org/issues/detail/morsy-v-dumas |
| Buckeye Institute case page — Curcio v. Hufford (mooted by Schaad) | https://www.buckeyeinstitute.org/issues/detail/curcio-v-hufford |
| Form 10A, TY2020 v2 (the signed employer certification, COVID checkbox) | https://cdn.ritaohio.com/Media/701508/Form10A%202020v2.pdf |
| RITA 2020 10A COVID insert (litigation suspension notice) | https://cdn.ritaohio.com/Media/701264/2020%2010A%20insert%20FINAL.pdf |
| McDonald Hopkins (Jan 2022) — HB 110 mechanics; 20-day rule back 2022-01-01 | https://mcdonaldhopkins.com/Insights/January-2022/Remote-work-impact-Ohio-municipal-income-tax |
| Ryan LLC (Fall 2024) — post-Schaad analysis, in-state vs out-of-state | https://ryan.com/about-ryan/articles/2024/remote-workers-facing-local-tax-issues/ |
| KJK (Dec 2021) — corroborates 2022 return to ordinary rules | https://kjk.com/2021/12/23/ohio-employers-facing-additional-municipal-income-tax-wage-withholding-requirements/ |
