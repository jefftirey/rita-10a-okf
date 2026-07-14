#!/usr/bin/env python3
"""Generate per-city sub-bundles under municipalities/.

Each municipality is its own mini-bundle: a directory with an index.md and
three concept nodes (profile, rates-and-credits, refunds). Data below was
verified against RITA's Tax Rates Table (2026 tab) on 2026-07-14. To scale
past the starter set, extend CITIES (or replace it with a scrape of RITA's
rates endpoint — note the endpoint requires a real browser session).

Run from the repo root:  python3 scripts/gen_municipalities.py
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "municipalities"
VERIFIED = "2026-07-14"
TIMESTAMP = "2026-07-14T00:00:00Z"

# slug, name, RITA code, rate %, credit factor %, credit limit %, county, credit kind
CITIES = [
    ("medina", "Medina", 487, 1.25, 25, 0.75, "Medina County", "partial"),
    ("brecksville", "Brecksville", 130, 2.00, 100, 2.00, "Cuyahoga County", "full"),
    ("strongsville", "Strongsville", 780, 2.00, 75, 2.00, "Cuyahoga County", "partial"),
    ("north-royalton", "North Royalton", 570, 2.00, 100, 1.25, "Cuyahoga County", "capped"),
    ("broadview-heights", "Broadview Heights", 140, 2.00, 75, 2.00, "Cuyahoga County", "partial"),
    ("hudson", "Hudson", 378, 2.00, 100, 2.00, "Summit County", "full"),
    ("solon", "Solon", 760, 2.00, 100, 2.00, "Cuyahoga County", "full"),
    ("westlake", "Westlake", 840, 1.50, 100, 1.50, "Cuyahoga County", "full"),
    ("cleveland-heights", "Cleveland Heights", 210, 2.25, 50, 1.00, "Cuyahoga County", "partial"),
    ("shaker-heights", "Shaker Heights", 750, 2.25, 50, 1.00, "Cuyahoga County", "partial"),
    ("euclid", "Euclid", 280, 2.85, 100, 2.85, "Cuyahoga County", "full"),
    ("berea", "Berea", 100, 2.00, 100, 1.50, "Cuyahoga County", "capped"),
]

CREDIT_NOTES = {
    "full": (
        "a **full-credit city**: residents get 100% credit for workplace tax up to a {limit}% "
        "rate, so residence tax on wages already taxed at or above that rate elsewhere is "
        "generally fully offset. A workplace refund therefore largely shifts liability back to "
        "{name} rather than netting savings (rate differences aside)."
    ),
    "capped": (
        "a **capped-credit city**: the 100% credit factor applies only to workplace tax up to a "
        "{limit}% rate — below {name}'s own {rate}% — so residents working in higher-rate cities "
        "owe {name} the remainder. A workplace refund produces partial real savings; run the math."
    ),
    "partial": (
        "a **partial-credit city**: only {factor}% of workplace tax is credited (counted up to a "
        "{limit}% rate), so residents largely pay both cities on the same wages. A legitimate "
        "workplace refund here is mostly real net savings — the profile where WFH claims matter most."
    ),
}

INDEX = """# {name}, Ohio — city bundle

RITA member, code {code}, {county}. Rates verified {verified}.

- [{name} profile]({slug}/profile.md) - Who administers {name}'s income tax, its RITA code, and the authoritative links.
- [Rates and credits (2026)]({slug}/rates-and-credits.md) - {rate}% rate; {factor}% credit factor up to a {limit}% credit limit, and what that means for residents.
- [Claiming refunds in {name}]({slug}/refunds.md) - How Form 10A applies to {name} withholding and to {name} residents.
"""
# Written as municipalities/<slug>/index.md — links above are rewritten to be
# relative to that directory at write time.

PROFILE = """---
type: Municipality
title: {name}, Ohio — profile
description: RITA member municipality (code {code}) in {county} - income tax filed, withheld, and refunded through RITA.
resource: https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code}
tags: [municipality, rita-member, {countytag}]
timestamp: {timestamp}
tax_years: [2026]
source: "RITA Tax Rates Table + municipality profile, retrieved {verified}"
---

# {name}, Ohio — profile

{name} ({county}) is a **RITA member municipality**, RITA code **{code}**. Its municipal income
tax is administered by RITA: returns, withholding, and refund claims — including
[Form 10A](../../procedures/form-10a-overview.md) — all go through RITA, not a city tax office.

Authoritative documents for {name} live on its RITA profile page (the `resource` link above):
the municipality's **tax ordinances**, **special requirements**, and its
**"Recent Tax and Credit History"** table. Current numbers: [Rates and credits](rates-and-credits.md).
Refund mechanics: [Claiming refunds in {name}](refunds.md).

# Citations

- {name} RITA profile page: https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code} (retrieved {verified})
- RITA member municipality list: https://www.ritaohio.com/municipalities (retrieved {verified})
"""

RATES = """---
type: Rates
title: {name} rates and credits (2026)
description: {rate}% municipal income tax; credit factor {factor}% up to a {limit}% credit limit - verified against RITA's 2026 Tax Rates Table on {verified}.
resource: https://www.ritaohio.com/TaxRatesTable
tags: [rates, credit, {countytag}]
timestamp: {timestamp}
tax_years: [2026]
source: "RITA Tax Rates Table (2026 tab), retrieved {verified}"
---

# {name} rates and credits (2026)

| Fact | Value |
|---|---|
| Municipal income tax rate | {rate}% |
| Credit factor (tax credit) | {factor}% |
| Credit rate (credit limit) | {limit}% |

**These are tax year 2026 values**, verified {verified}. For a refund claim, use the claim
year's values: the [RITA Tax Rates Table](https://www.ritaohio.com/TaxRatesTable) has year tabs
back to 2020, and the "Recent Tax and Credit History" on {name}'s
[RITA profile page](https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code}) shows
effective dates.

For residents, {name} is {credit_note} How the factor and limit combine is explained in
[Credit for taxes paid](../../concepts/credit-for-taxes-paid.md); confirm exact computation
against {name}'s ordinance (on the profile page) or RITA's Form 37 instructions.

# Citations

- RITA Tax Rates Table, 2026 tab: https://www.ritaohio.com/TaxRatesTable (retrieved {verified})
- {name} RITA profile (ordinances, rate history): https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code} (retrieved {verified})
"""

REFUNDS = """---
type: Procedure
title: Claiming refunds in {name}
description: How Form 10A applies to {name} (code {code}) - claims against {name} withholding for non-residents, and the residence-side effect for {name} residents.
resource: https://www.ritaohio.com/individuals/home/formdownloads
tags: [procedure, form-10a, {countytag}]
timestamp: {timestamp}
tax_years: [2023, 2024, 2025]
source: "RITA Form 10A + Rules & Regulations §9(F) + 2026 rates, retrieved {verified}"
---

# Claiming refunds in {name}

Because {name} is a RITA member, refunds of {name} tax use RITA's
[Form 10A](../../procedures/form-10a-overview.md) (municipality code **{code}** on the form).
Check [open claim windows](../../concepts/open-claim-windows.md) first — as of mid-2026 that
means tax years 2023–2025.

**If you worked in {name} but don't live there** — e.g. your employer withheld {name}'s {rate}%
while you actually worked from home other days — the
[work-from-home procedure](../../procedures/form-10a-wfh-refund.md) applies (claim reason 2;
days-out refunds are for non-residents of the withholding city, per RITA Rules & Regulations
§9(F)). Each misallocated dollar of wages returns {rate}% of itself.

**If you live in {name}** and claim a refund from some *other* workplace city, expect the
residence-side effect: RITA amends the {name} return to remove the credit taken on refunded
amounts ([amended returns](../../procedures/amended-returns.md)). What that costs depends on
{name}'s credit — see [Rates and credits](rates-and-credits.md) — so quote net numbers, not the
gross refund.

Documents: current and prior-year Form 10A at
[ritaohio.com/individuals/home/formdownloads](https://www.ritaohio.com/individuals/home/formdownloads);
{name}-specific ordinances and any special notes on the
[profile page](https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code}).

# Citations

- Form 10A and instructions (all years): https://www.ritaohio.com/individuals/home/formdownloads (retrieved {verified})
- RITA Rules & Regulations §9(F): https://cdn.ritaohio.com/Media/702857/RREGS_EFF%20JAN%201%202016_revised%20012225_061616.pdf (retrieved {verified})
- RITA Tax Rates Table: https://www.ritaohio.com/TaxRatesTable (retrieved {verified})
"""

TOP_INDEX_HEADER = """# Municipalities

Each municipality is its own sub-bundle: a directory with an index and nodes for the city's
profile, current rates/credits, and refund mechanics. Twelve verified starter cities below
(rates verified {verified}); RITA has ~350 members total — any city not listed here can be
checked against the [RITA member list](https://www.ritaohio.com/municipalities) and
[Tax Rates Table](https://www.ritaohio.com/TaxRatesTable). Cleveland is **not** here: it is
administered by CCA, not RITA — see
[RITA vs. CCA vs. self-administered](../concepts/rita-vs-cca-vs-self-administered.md).

"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    top_entries = []
    for slug, name, code, rate, factor, limit, county, kind in CITIES:
        fmt = dict(
            slug=slug, name=name, code=code, county=county,
            countytag=county.lower().replace(" ", "-"),
            rate=f"{rate:g}", factor=f"{factor:g}", limit=f"{limit:g}",
            verified=VERIFIED, timestamp=TIMESTAMP,
        )
        fmt["credit_note"] = CREDIT_NOTES[kind].format(**fmt)
        d = OUT / slug
        d.mkdir(exist_ok=True)
        (d / "index.md").write_text(
            INDEX.format(**fmt).replace(f"]({slug}/", "]("), encoding="utf-8")
        (d / "profile.md").write_text(PROFILE.format(**fmt), encoding="utf-8")
        (d / "rates-and-credits.md").write_text(RATES.format(**fmt), encoding="utf-8")
        (d / "refunds.md").write_text(REFUNDS.format(**fmt), encoding="utf-8")
        top_entries.append(
            f"- [{name}, Ohio]({slug}/index.md) - RITA code {code}, {county}; "
            f"{fmt['rate']}% rate, {fmt['factor']}% credit factor up to {fmt['limit']}%."
        )
        print(f"wrote {slug}/ (4 files)")
    top = TOP_INDEX_HEADER.format(verified=VERIFIED) + "\n".join(top_entries) + "\n"
    (OUT / "index.md").write_text(top, encoding="utf-8")
    print("wrote municipalities/index.md")


if __name__ == "__main__":
    main()
