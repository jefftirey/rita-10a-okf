# Eval set — rita-10a-okf quality gate

20 questions with gold answers and expected citations, written 2026-07-14 against the verified
fact base. Not part of the OKF bundle — this is QA tooling. An agent given only the bundle
(starting at `rita-10a-okf/index.md`) should produce answers consistent with the gold answers,
with citations, without loading the whole bundle.

Scoring per question: **correct** (matches gold, cited), **partial** (right substance, missing
citation or year-qualifier), **wrong** (contradicts gold or answers a closed year as open).
Trick questions (marked ⚠) test whether the bundle prevents confident wrong answers.

| # | Question | Gold answer | Expected node(s) |
|---|---|---|---|
| 1 | What are Medina's 2026 tax rate and credit terms? | 1.250% rate, 25.000% credit factor, 0.750% credit limit (RITA Tax Rates Table 2026) | municipalities/medina/rates-and-credits.md |
| 2 | I live in Medina, worked hybrid in 2024 with all withholding to my Solon office. What form and claim reason apply, and what's the filing deadline? | Form 10A, claim reason 2 (Days Worked From Home); deadline 3 years from the 2024 return due date ≈ April 15, 2028 (ORC 718.19(B)(1)); paper/mail only; residence return will be amended | scenarios/wfh-2024…, procedures/form-10a-wfh-refund.md, concepts/open-claim-windows.md |
| 3 | ⚠ Can I still file a 2021 work-from-home refund claim in July 2026? | No — the 3-year window closed ~April 2025. (HB 110 did allow 2021 refunds; too late now.) | concepts/open-claim-windows.md, scenarios/wfh-2020-2021-closed-years.md |
| 4 | ⚠ Can I get my 2020 WFH withholding back? | No — HB 197 §29 was upheld in Schaad v. Alder (2024-Ohio-525) and the window closed in 2024 anyway. (Morsy: different result for an out-of-state resident, historical.) | law/schaad-v-alder.md, scenarios/wfh-2020-2021-closed-years.md |
| 5 | ⚠ I live in Brunswick — do I file a RITA Form 10A for my Brunswick taxes? | No — Brunswick is not a RITA member; it self-administers (its own tax dept). RITA forms apply only to RITA-member cities. | scenarios/brunswick-resident-wrong-agency.md, concepts/rita-vs-cca-vs-self-administered.md |
| 6 | ⚠ My employer withheld Cleveland tax; I worked from home in a RITA suburb. Does RITA refund the Cleveland withholding? | No — Cleveland is administered by CCA; the workplace-side claim goes through CCA. The residence side runs through RITA. | scenarios/cleveland-office-cca-boundary.md |
| 7 | Can I e-file Form 10A? Where does it go? | No — paper/mail only ("cannot be emailed or electronically filed… Do not fax"); mail to RITA, PO Box 95422, Cleveland, OH 44101-0033 | procedures/form-10a-overview.md |
| 8 | Does my employer have to sign my Form 10A? | No — current forms require an unsigned "Employer Representative Contact" (needed for claim reasons 2–7 and 9); RITA may call to verify | procedures/employer-certification.md |
| 9 | My 16-year-old had city tax withheld from a 2024 summer job. Recoverable? | Yes — from TY2024 all municipalities exempt under-18 income; Form 10A claim reason 1 with W-2 + proof of birthdate; pre-2024 varied by city | scenarios/under-18-summer-job.md |
| 10 | I live in Hinckley Township — do I owe residence municipal income tax? | No — Ohio townships don't levy income tax (JEDD/JEDZ districts are the exception; working inside one can be taxed) | concepts/townships-and-unincorporated.md |
| 11 | What is the statute of limitations for a refund and where does it come from? | 3 years after the return (incl. valid extension) was due or paid, whichever is later — ORC 718.19(B)(1) | concepts/statute-of-limitations.md, law/orc-718.md |
| 12 | What is the 20-day rule? | ORC 718.011: no employer withholding for a municipality where the employee worked ≤20 days that year, with principal-place-of-work / presumed-worksite / residence exceptions | concepts/twenty-day-occasional-entrant.md |
| 13 | Is there a minimum refund amount? | Yes — amounts of $10 or less are not refunded (ORC 718.19(A): overpayments over $10) | procedures/form-10a-overview.md |
| 14 | How long does RITA take to process a 10A, and how do I check status? | 90 days from a complete request; status via MyAccount "View History" or 800-860-7482 | procedures/form-10a-overview.md |
| 15 | If my workplace refund is granted, what happens to my residence-city return? | RITA amends it to disallow the credit taken on refunded amounts; per RITA you'll likely owe some of it to your residence community | procedures/amended-returns.md |
| 16 | Compare Euclid's and Westlake's 2026 tax rates. | Euclid 2.850% (100%/2.850% credit); Westlake 1.500% (100%/1.500% credit) | municipalities/euclid/…, municipalities/westlake/… |
| 17 | What's the Bainbridge-Solon JEDD's 2026 rate? | 2.000% (0% credit factor/limit) — it's a special district, not a municipality | municipalities/jedd-jedz-districts.md |
| 18 | Which tax years can still be claimed as of July 2026? | 2023, 2024, 2025 open; 2022 only with a valid extension (until ~Oct 2026); 2020–2021 closed; 2026 not yet claimable | concepts/open-claim-windows.md |
| 19 | ⚠ Can I get municipal tax back on my stock options? | No — RITA's FAQ: stock options (and severance) are not refundable; they remain taxable to the employment municipality | procedures/form-10a-overview.md |
| 20 | Give me the direct link to the actual Form 10A PDF for tax year 2024. | https://cdn.ritaohio.com/Media/703143/Form10A%202024v2.pdf (or via the forms index page) | procedures/official-documents.md |

## Traversal expectation

A correct run answers each question by walking indexes and loading only relevant nodes —
typically 3–6 files, never the whole bundle. Agents should also honor the two load-first nodes
(not-tax-advice, open-claim-windows) per the root index instruction.
