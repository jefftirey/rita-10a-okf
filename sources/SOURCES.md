# SOURCES — rita-okf Phase 0 research log

All sources retrieved **2026-07-14** unless noted. Files in `sources/raw/` are local copies of
public-law documents and RITA agency publications kept for reference (do not republish RITA
documents in the bundle; cite and link instead).

Practical retrieval notes:
- `legislature.ohio.gov` and `lsc.ohio.gov` fail TLS verification in some fetchers; plain `curl` works.
  `search-prod.lis.state.oh.us/api/v2/.../pdf/` is a reliable direct route to enrolled bill PDFs.
- RITA serves media from both `www.ritaohio.com/Media/...` and `cdn.ritaohio.com/Media/...` (cdn 302s to www).
- RITA's Tax Rates Table has **no static downloadable file** — the page renders client-side from
  `https://www.ritaohio.com/TaxRatesTable/Home/GetTaxRatesByYear?TaxYear=<year>&FilterString=`
  (JSON endpoint rejects non-browser requests; the EXPORT button builds `RITA_TaxRatesTable_<year>.csv`
  in JavaScript). Phase 4 scraping needs a real browser session.

## 1. RITA forms — Form 10A and instructions

| Source | URL | Local copy | Notes |
|---|---|---|---|
| Form 10A, TY2025 (current) | https://www.ritaohio.com/Media/703127/Form10A%202025%20FINAL.pdf | raw/rita-form-10a-2025.pdf | 3-page fillable refund application; 10 claim reasons |
| Form 10A instructions, TY2025 | https://cdn.ritaohio.com/Media/703124/2025%20Form%2010A%20FINAL%20Instructions.pdf | raw/rita-form-10a-instructions-2025.pdf | "General Guidelines for Form 10A"; SOL example; mail-only filing |
| Form 10A, TY2024 (v2) | https://cdn.ritaohio.com/Media/703143/Form10A%202024v2.pdf | raw/rita-form-10a-2024v2.pdf | Same layout/wording as 2025. Older URL `Media/702551/Form10A 2024.pdf` is dead (404) |
| Form 10A instructions, TY2024 | https://cdn.ritaohio.com/Media/703154/10A%20Updated%20instructions.pdf | raw/rita-form-10a-instructions-2024.pdf | |
| Form 10A, TY2023 (v2) | https://cdn.ritaohio.com/Media/703144/Form10A%202023v2.pdf | — | Verified live (200, PDF); content not extracted |
| Form 10A instructions, TY2023 | https://cdn.ritaohio.com/Media/703164/10A%20Updated%20instructions.pdf | — | Found linked; not fetched |
| Form 10A, TY2020 (v2) | https://cdn.ritaohio.com/Media/701508/Form10A%202020v2.pdf | raw/rita-form-10a-2020v2.pdf | 4-page COVID-era version with **signed** employer certification |
| 2020 10A COVID insert | https://cdn.ritaohio.com/Media/701264/2020%2010A%20insert%20FINAL.pdf | raw/rita-2020-10a-covid-insert.pdf | COVID refund suspension notice; cites Buckeye Institute v. Columbus City Auditor, Franklin C.P. No. 20-CV-004301 |
| 10A info sheet, 2021 | https://cdn.ritaohio.com/Media/703142/10A%20info%202021.pdf | raw/rita-10a-info-2021.pdf | SOL notice: 2021 deadline 04/18/2022 → refund request by 04/18/2025 |
| 10A info sheets, 2022 / 2019 / 2018 | https://cdn.ritaohio.com/Media/703188/10A%20info%202022.pdf ; https://www.ritaohio.com/Media/702561/10A%20info.pdf ; https://www.ritaohio.com/Media/702562/10A%20info.pdf | — | Linked from forms page; content not extracted |
| Forms & instructions index | https://www.ritaohio.com/individuals/home/formdownloads | — | Canonical index of current + prior-year individual forms |
| Special 10A — Rittman | https://www.ritaohio.com/Media/702127/Special%2010A%20RTMN.pdf | — | Municipality-specific special 10A; existence noted, not verified |

## 2. RITA agency pages and Rules & Regulations

| Source | URL | Local copy | Notes |
|---|---|---|---|
| RITA Income Tax Rules & Regulations (eff. 1/1/2016, amended 1/1/2025) | https://cdn.ritaohio.com/Media/702857/RREGS_EFF%20JAN%201%202016_revised%20012225_061616.pdf | raw/rita-rules-and-regulations-eff2016-amended2025.pdf | 66-page RITA-wide model document; §9 refunds, §12 limitations; municipal ordinance supersedes on conflict |
| Individuals — Refunds page | https://www.ritaohio.com/Individuals/Home/Refunds | — | 90-day processing; $10 minimum; 3-year SOL; TY2020 WFH suspension language |
| Individual FAQs — Refunds | https://www.ritaohio.com/Individuals/Faqs?category=I&subcategory=Refunds | — | 10 Q&As; WFH FAQ at `&questionID=10`; TY2020 shows "SUSPENDED" in MyAccount |

## 3. RITA municipalities and rates

| Source | URL | Notes |
|---|---|---|
| RITA Tax Rates Table | https://www.ritaohio.com/TaxRatesTable | Per-year tabs 2020–2026; columns: Municipality, Code, Tax Rate, Credit Factor (Tax Credit), Credit Rate (Credit Limit) |
| RITA Municipalities list | https://www.ritaohio.com/municipalities | Alphabetical member list + JEDD/JEDZ/ENTPZ section; links to per-member profile pages |
| Per-municipality profile pattern | https://www.ritaohio.com/Municipalities/Home/MemberPage?id=<code> | Verified id=487 → Medina; page has ordinances, special requirements, "Recent Tax and Credit History" |
| City of Brunswick Income Tax | https://www.brunswick.oh.us/income-tax/ | Brunswick is **not** RITA — self-administered; 2.0% rate, credit up to 1.0% |
| City of Fairlawn Tax Dept | https://www.cityoffairlawn.com/58/Tax (FAQ: https://www.cityoffairlawn.com/FAQ.aspx?QID=59) | Not RITA, not CCA; own tax dept; 2% rate |
| City of Lakewood Municipal Income Tax | https://lakewoodoh.gov/municipal-income-tax/ | Not RITA; own division; 1.5% rate; appears on CCA "Special Members" list |
| City of Parma Taxation | https://cityofparma-oh.gov/211/Taxation | Not RITA, not CCA; own tax dept; 2.5% rate, 100% credit up to 2% |
| Cleveland Division of Taxation (CCA) | https://www.clevelandohio.gov/city-hall/departments/finance/divisions/taxation | Confirms CCA collects Cleveland's municipal income tax |
| CCA member page — Cleveland | https://www.ccaohio.gov/member-municipalities/cleveland | Cleveland 2.50% rate, 100% credit, 2.50% credit limit (eff. 1/1/2017) |
| CCA member municipalities | https://www.ccaohio.gov/member-municipalities | Regular / JEDD-JEDZ / Special member lists |
| Ohio Township Association, "Townships 101" | https://www.ohiotownships.org/townships101 | "Townships do not levy income or sales taxes" |
| OSU Extension, JEDD factsheet | https://ohioline.osu.edu/factsheet/cdfs-1560 | JEDD income tax under ORC 715.70–715.72 — the township exception |
| Ohio Dept of Taxation "The Finder" — JEDD/JEDZ | https://thefinder.tax.ohio.gov/jedtax/jed_default.aspx (rates CSV: https://thefinder.tax.ohio.gov/jedtax/Docs/JEDTaxRates.csv) | JEDD rate lookup; CSV noted, not downloaded |

## 4. Ohio Revised Code (codes.ohio.gov)

| Section | URL | Notes |
|---|---|---|
| ORC 718.011 — Occasional entrant exemption (20-day rule) | https://codes.ohio.gov/ohio-revised-code/section-718.011 | Eff. 3/23/2015 (HB 5, 130th GA); defines "principal place of work" at (A)(7) |
| ORC 718.03 — Withholding qualifying wages | https://codes.ohio.gov/ohio-revised-code/section-718.03 | Eff. 9/14/2016 (SB 172, 131st GA); withholding tied to where wages are earned |
| ORC 718.12 — Limitations | https://codes.ohio.gov/ohio-revised-code/section-718.12 | Eff. 9/30/2025 (HB 96, 136th GA); (C) cross-references 718.19 for refunds; (D) interest on overpayments |
| ORC 718.19 — Requests for refunds | https://codes.ohio.gov/ohio-revised-code/section-718.19 | Eff. 9/30/2025 (HB 96, 136th GA); **the** refund SOL: 3 years after return (incl. valid extension) was due or paid, whichever is later; >$10 threshold |

## 5. Session law — HB 197 (2020) and HB 110 (2021)

| Source | URL | Local copy | Notes |
|---|---|---|---|
| Am. Sub. HB 197, 133rd GA, enrolled | https://search-prod.lis.state.oh.us/api/v2/general_assembly_133/legislation/hb197/06_EN/pdf/ | raw/hb197-133ga-enrolled.pdf | Section 29 at pp. 340–341 (bill page: https://www.legislature.ohio.gov/legislation/133/hb197) |
| Am. Sub. HB 110, 134th GA, enrolled | https://search-prod.lis.state.oh.us/api/v2/general_assembly_134/legislation/hb110/07_EN/pdf/ | raw/hb110-134ga-enrolled.pdf | §§610.115/610.116 (~pp. 2369–2370), §757.40 (~pp. 2427–2428) (bill page: https://www.legislature.ohio.gov/legislation/134/hb110) |
| LSC Final Bill Analysis, HB 110 (tax portion) | https://www.lsc.ohio.gov/assets/legislation/134/hb110/en/files/hb110-tax-bill-analysis-as-enrolled-134th-general-assembly.pdf | raw/lsc-hb110-tax-analysis-as-enrolled.pdf | "Municipal income taxation during the COVID-19 pandemic," pp. 446–448; HB 197 §29 expiry date (7/18/2021) at p. 446 fn. 133 |

## 6. Litigation

| Source | URL | Local copy | Notes |
|---|---|---|---|
| Schaad v. Alder, 2024-Ohio-525 (slip opinion) | https://www.supremecourt.ohio.gov/rod/docs/pdf/0/2024/2024-ohio-525.pdf | raw/schaad-v-alder-2024-ohio-525.pdf | 176 Ohio St.3d 158; decided 2/14/2024; 5-2; HB 197 §29 upheld |
| Court News Ohio summary of Schaad | https://www.courtnewsohio.gov/cases/2024/SCO/0214/220316.asp | — | Court's own news arm; vote lineup, majority/dissent summaries |
| Buckeye Institute — Schaad case page | https://www.buckeyeinstitute.org/issues/detail/schaad-v-alder | — | Litigation timeline 2/9/2021 → 2/14/2024; no post-decision entries |
| Buckeye Institute — Morsy v. Dumas | https://www.buckeyeinstitute.org/issues/detail/morsy-v-dumas | — | PA resident vs. Cleveland; won refund + interest; Cleveland abandoned appeal Apr 2024 |
| Buckeye Institute — Curcio v. Hufford | https://www.buckeyeinstitute.org/issues/detail/curcio-v-hufford | — | Toledo/Oregon; mooted by Schaad |
| Buckeye Institute — Morsy win release | https://www.buckeyeinstitute.org/research/detail/the-buckeye-institute-wins-big-municipal-income-tax-case-cleveland-refunds-taxes-illegally-taken-from-buckeyes-client-during-pandemic | — | Full refund + interest + court costs |

## 7. Secondary / practitioner sources

| Source | URL | Notes |
|---|---|---|
| McDonald Hopkins (Jan 2022), remote work & Ohio muni tax | https://mcdonaldhopkins.com/Insights/January-2022/Remote-work-impact-Ohio-municipal-income-tax | HB 110 mechanics; 20-day rule reinstated 1/1/2022 |
| Ryan LLC (Fall 2024), "Remote Workers Still Facing Local Tax Issues" | https://ryan.com/about-ryan/articles/2024/remote-workers-facing-local-tax-issues/ | Post-Schaad analysis; in-state vs out-of-state distinction |
| KJK (Dec 2021), Ohio employer withholding alert | https://kjk.com/2021/12/23/ohio-employers-facing-additional-municipal-income-tax-wage-withholding-requirements/ | Corroborates 2022 return to ordinary rules |
| Squire Patton Boggs (Jul 2021) HB 110 alert | (page now 404s; title confirmed via search) | Employer withholding rule extended + 2021 employee refunds |
| OSCPA Municipal Tax Withholding & Refund Q&A (rev. 12/1/2021) | https://ohiocpa.com/docs/default-source/tax_resources/muni_tax_withholding_2021_faq_document.pdf | Fetch blocked (403); URL confirmed via search |
| Crain's Cleveland — Cleveland drops Morsy appeal; 2021 refund fallout | https://www.crainscleveland.com/law/city-cleveland-pulls-out-covid-income-tax-refund-lawsuit ; https://www.crainscleveland.com/government/clevelands-remote-tax-fiscal-fallout-not-so-dire | Paywalled — headlines only. A search snippet attributes "more than $15 million to more than 5,000 remote workers" (Cleveland, TY2021) to Crain's — **unconfirmed** |
| Fox 8 Cleveland, 2021 WFH refund how-to | https://fox8.com/news/worked-from-home-in-2021-how-to-seek-a-local-income-tax-refund/ | Fetch blocked (403); found via search |
