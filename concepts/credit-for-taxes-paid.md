---
type: Concept
title: Credit for taxes paid to another municipality
description: How the credit factor and credit limit work, and why the same WFH refund nets real money in Medina but roughly zero in Brecksville.
tags: [concept, credit, rates]
timestamp: 2026-07-14T00:00:00Z
resource: https://www.ritaohio.com/TaxRatesTable
tax_years: [2026]
source: "RITA Tax Rates Table (2026 tab), retrieved 2026-07-14"
---

# Credit for taxes paid to another municipality

Most residence municipalities give a credit for income tax paid to a workplace city. RITA's
Tax Rates Table publishes two numbers per member that control it:

- **Credit factor** ("Tax Credit") — the percentage of workplace tax that is credited.
- **Credit limit** ("Credit Rate") — the ceiling tax rate up to which the credit applies.

As commonly computed, the credit is `credit factor × workplace tax paid`, counting workplace tax
only up to `credit limit × wages`. **Verify the exact computation for a specific case against
RITA's Form 37 instructions or the municipality's ordinance** (linked from each RITA member's
profile page) — ordinances control and wording varies.

## Why this decides whether a WFH refund is worth anything

A [Form 10A refund](../procedures/form-10a-wfh-refund.md) of workplace tax reduces the residence
credit at the same time (see [Residence vs. workplace tax](residence-vs-workplace-tax.md)). So:

- **Full-credit residence city** (factor 100%, limit ≥ the rates involved — e.g.
  [Brecksville](../municipalities/brecksville.md), [Solon](../municipalities/solon.md),
  [Hudson](../municipalities/hudson.md)): the resident was already paying ~0 residence tax on
  those wages. A workplace refund is largely offset by new residence tax — the money mostly
  *moves between cities*, with the net depending on the rate difference.
- **Partial-credit residence city** (e.g. [Medina](../municipalities/medina.md) 25% factor /
  0.75% limit, [Shaker Heights](../municipalities/shaker-heights.md) and
  [Cleveland Heights](../municipalities/cleveland-heights.md) 50% / 1.00%): the resident was
  paying *both* cities nearly in full. Refunding the workplace tax is real net savings.
- **Rate differences matter too**: a [Westlake](../municipalities/westlake.md) resident (1.5%)
  withheld to a 2.85% city like [Euclid](../municipalities/euclid.md) saves the rate gap even
  with full credit.

A consuming agent must therefore never answer "is the refund worth filing?" without both
municipalities' rate, credit factor, and credit limit for the tax year in question — the
per-municipality nodes in [municipalities/](../municipalities/index.md) carry 2026 values, and
each node's `resource` link has the year-by-year history.

# Citations

- RITA Tax Rates Table (rates, credit factors, credit limits by year, 2020–2026): https://www.ritaohio.com/TaxRatesTable (retrieved 2026-07-14)
- RITA Refunds FAQ (refund may be owed to residence community): https://www.ritaohio.com/Individuals/Faqs?category=I&subcategory=Refunds (retrieved 2026-07-14)
