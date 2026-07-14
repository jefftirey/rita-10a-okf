---
type: Scenario
title: "I live in Brunswick - do I file a RITA 10A?"
description: The wrong-agency trick question - Brunswick self-administers its income tax and is not a RITA member, so RITA forms do nothing for Brunswick-side taxes.
resource: https://www.brunswick.oh.us/income-tax/
tags: [scenario, boundaries, brunswick, self-administered]
timestamp: 2026-07-14T00:00:00Z
tax_years: [2023, 2024, 2025, 2026]
source: "City of Brunswick + RITA member list, retrieved 2026-07-14"
---

# "I live in Brunswick — do I file a RITA 10A?"

**No — Brunswick is not a RITA member.** It runs its own Income Tax Department
(2.0% rate; residents credited up to 1.0% for workplace tax paid, per the city's site). It
appears in neither RITA's nor CCA's member lists. This surprises people because Brunswick sits
among RITA suburbs (neighboring Medina *is* RITA).

What that means in practice:

- **Brunswick residence taxes** (returns, credits, residence-side refunds) go through
  **Brunswick's own tax department** on Brunswick's forms — brunswick.oh.us/income-tax.
- **Workplace-side claims still follow the workplace city's administrator.** A Brunswick
  resident whose employer withheld to a RITA member city (say
  [Strongsville](../municipalities/strongsville/index.md)) for days actually worked at home *does*
  file RITA's [Form 10A](../procedures/form-10a-wfh-refund.md) — against Strongsville, as a
  non-RITA resident. RITA's instructions note a RITA return may be created for non-RITA
  residents reporting work performed in RITA municipalities.
- The refund's residence-side consequence (reduced credit) then plays out on the **Brunswick**
  return, under Brunswick's credit rules — outside RITA entirely.

**The general rule an agent should extract:** *the form follows the municipality whose tax is
being refunded, not the person's home.* Check every municipality in the fact pattern against
[RITA vs. CCA vs. self-administered](../concepts/rita-vs-cca-vs-self-administered.md) before
naming a form. Same trap applies to Parma, Lakewood, and Fairlawn residents.

# Citations

- City of Brunswick Income Tax Department (2.0% rate, 1.0% credit): https://www.brunswick.oh.us/income-tax/ (retrieved 2026-07-14)
- RITA member municipalities (Brunswick absent): https://www.ritaohio.com/municipalities (retrieved 2026-07-14)
- CCA member lists (Brunswick absent): https://www.ccaohio.gov/member-municipalities (retrieved 2026-07-14)
- Form 10A instructions, TY2025 (non-RITA residents): https://cdn.ritaohio.com/Media/703124/2025%20Form%2010A%20FINAL%20Instructions.pdf (retrieved 2026-07-14)
