#!/usr/bin/env python3
"""Generate the municipalities/ tree of the bundle from RITA's own rates data.

Input:  scripts/data/rita-rates-<year>.psv  (produced by scripts/fetch_rates.py,
        which parses the same endpoint RITA's Tax Rates Table page uses).
Output: rita-10a-okf/municipalities/<slug>/ sub-bundles — one per municipality,
        each with index.md, profile.md, rates-and-credits.md, refunds.md —
        plus municipalities/jedd-jedz-districts.md (special districts in one
        table) and municipalities/index.md.

The generated nodes present RITA's published numbers and link to the
authoritative pages; they do not interpret or compute credits.

Run from the repo root:  python3 scripts/gen_municipalities.py [year]
"""

import re
import shutil
import sys
from pathlib import Path

YEAR = sys.argv[1] if len(sys.argv) > 1 else "2026"
REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "scripts" / "data" / f"rita-rates-{YEAR}.psv"
OUT = REPO / "rita-10a-okf" / "municipalities"

DISTRICT_RE = re.compile(r"jedd|jedz|entpz|annexation", re.IGNORECASE)


def slugify(name: str) -> str:
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", name.lower())).strip("-")


def load():
    retrieved = None
    rows = []
    for line in DATA.read_text(encoding="utf-8").splitlines():
        if line.startswith("# Retrieved:"):
            retrieved = line.split(":", 1)[1].strip()
        if not line or line.startswith("#"):
            continue
        name, code, rate, factor, limit = line.split("|")
        rows.append(dict(name=name, code=code, rate=rate, factor=factor, limit=limit))
    if retrieved is None:
        raise SystemExit("no Retrieved: line in data file")
    return retrieved, rows


INDEX = """# {name}, Ohio — city bundle

RITA member, code {code}. Rates from RITA's {year} Tax Rates Table, retrieved {retrieved}.

- [{name} profile](profile.md) - Who administers {name}'s income tax, its RITA code, and the authoritative links.
- [Rates and credits ({year})](rates-and-credits.md) - {rate} tax rate; {factor} credit factor; {limit} credit limit, as published by RITA.
- [Claiming refunds in {name}](refunds.md) - How Form 10A applies to {name} withholding and to {name} residents.
"""

PROFILE = """---
type: Municipality
title: {name}, Ohio — profile
description: RITA member municipality (code {code}) - income tax filed, withheld, and refunded through RITA.
resource: https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code}
tags: [municipality, rita-member]
timestamp: {retrieved}T00:00:00Z
tax_years: [{year}]
source: "RITA Tax Rates Table (tax year {year}), retrieved {retrieved}"
---

# {name}, Ohio — profile

{name} is a **RITA member municipality**, RITA code **{code}**. Its municipal income tax is
administered by RITA: returns, withholding, and refund claims — including
[Form 10A](../../procedures/form-10a-overview.md) — go through RITA, not a city tax office.

Authoritative documents for {name} are on its RITA profile page (the `resource` link above):
the municipality's **tax ordinances**, any **special notes/requirements**, and its
**"Recent Tax and Credit History"**. Current published numbers:
[Rates and credits](rates-and-credits.md). Refund mechanics:
[Claiming refunds in {name}](refunds.md).

# Citations

- {name} RITA profile page: https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code} (retrieved {retrieved})
- RITA member municipality list: https://www.ritaohio.com/municipalities (retrieved {retrieved})
"""

RATES = """---
type: Rates
title: {name} rates and credits ({year})
description: As published by RITA for tax year {year} - {rate} tax rate, {factor} credit factor, {limit} credit limit.
resource: https://www.ritaohio.com/TaxRatesTable
tags: [rates, credit]
timestamp: {retrieved}T00:00:00Z
tax_years: [{year}]
source: "RITA Tax Rates Table (tax year {year}), retrieved {retrieved}"
---

# {name} rates and credits ({year})

As published in RITA's Tax Rates Table for tax year {year} (retrieved {retrieved}):

| Fact | Value |
|---|---|
| Municipal income tax rate | {rate} |
| Credit factor (tax credit) | {factor} |
| Credit rate (credit limit) | {limit} |

**These are tax year {year} values.** For a refund claim, use the claim year's values — the
[RITA Tax Rates Table](https://www.ritaohio.com/TaxRatesTable) has year tabs back to 2020, and
{name}'s [RITA profile page](https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code})
shows its rate and credit history with effective dates.

How the credit factor and credit limit combine is defined by {name}'s own ordinance (on the
profile page) and applied through RITA's Form 37 and its instructions — see
[Credit for taxes paid](../../concepts/credit-for-taxes-paid.md). This bundle does not compute
credits.

# Citations

- RITA Tax Rates Table, {year} tab: https://www.ritaohio.com/TaxRatesTable (retrieved {retrieved})
- {name} RITA profile: https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code} (retrieved {retrieved})
"""

REFUNDS = """---
type: Procedure
title: Claiming refunds in {name}
description: How Form 10A applies to {name} (RITA code {code}) - workplace-side claims by non-residents and the residence-side effect for {name} residents.
resource: https://www.ritaohio.com/individuals/home/formdownloads
tags: [procedure, form-10a]
timestamp: {retrieved}T00:00:00Z
tax_years: [2023, 2024, 2025]
source: "RITA Form 10A + Rules & Regulations §9(F), retrieved {retrieved}"
---

# Claiming refunds in {name}

{name} is a RITA member, so refunds of {name} tax use RITA's
[Form 10A](../../procedures/form-10a-overview.md) (municipality code **{code}**). Check
[open claim windows](../../concepts/open-claim-windows.md) first.

**Workplace side** — if {name} tax was withheld for days not actually worked in {name} (for
example, days worked from home elsewhere), the
[work-from-home procedure](../../procedures/form-10a-wfh-refund.md) applies. RITA's Rules &
Regulations §9(F) state that days-out refunds from a workplace municipality are available to
non-residents of it.

**Residence side** — for a {name} resident claiming a refund from another city, RITA's
instructions state residence returns "will be amended to disallow any residence tax credit
taken for amounts refunded" — see [Amended returns](../../procedures/amended-returns.md) and
{name}'s published [rates and credits](rates-and-credits.md).

The forms themselves: [Official documents](../../procedures/official-documents.md);
{name}-specific ordinances and special notes: the
[profile page](https://www.ritaohio.com/Municipalities/Home/MemberPage?id={code}).

# Citations

- Form 10A and instructions (all years): https://www.ritaohio.com/individuals/home/formdownloads (retrieved {retrieved})
- RITA Rules & Regulations §9(F): https://cdn.ritaohio.com/Media/702857/RREGS_EFF%20JAN%201%202016_revised%20012225_061616.pdf (retrieved {retrieved})
"""

DISTRICTS_HEADER = """---
type: Rates
title: JEDD, JEDZ, and other special districts ({year})
description: RITA-administered special taxing districts - joint economic development districts and zones - with their published {year} rates, in one table.
resource: https://www.ritaohio.com/TaxRatesTable
tags: [rates, jedd, jedz, special-districts]
timestamp: {retrieved}T00:00:00Z
tax_years: [{year}]
source: "RITA Tax Rates Table (tax year {year}), retrieved {retrieved}"
---

# JEDD, JEDZ, and other special districts ({year})

These RITA-administered entries are special taxing districts, not municipalities — mostly Joint
Economic Development Districts/Zones created under ORC 715.70–715.72 (see
[Townships](../concepts/townships-and-unincorporated.md)). Each name links pattern
`https://www.ritaohio.com/Municipalities/Home/MemberPage?id=<code>` for its profile. Rates as
published for tax year {year}, retrieved {retrieved}.

| District | Code | Tax rate | Credit factor | Credit limit |
|---|---|---|---|---|
"""

TOP_INDEX = """# Municipalities

One sub-bundle per RITA member municipality — each is a directory with an index and nodes for
the city's profile, published rates/credits, and refund mechanics. Data: RITA's Tax Rates Table
for tax year {year} (retrieved {retrieved}), parsed by script; regenerate with
`scripts/fetch_rates.py` + `scripts/gen_municipalities.py`.

Special districts (JEDD/JEDZ) are listed separately in
[JEDD, JEDZ, and other special districts](jedd-jedz-districts.md).

**Cleveland is not here**: it is administered by CCA, not RITA — see
[RITA vs. CCA vs. self-administered](../concepts/rita-vs-cca-vs-self-administered.md).

"""


def main() -> None:
    retrieved, rows = load()
    munis = [r for r in rows if not DISTRICT_RE.search(r["name"])]
    districts = [r for r in rows if DISTRICT_RE.search(r["name"])]

    slugs = {}
    for r in munis:
        slug = slugify(r["name"])
        if slug in slugs:
            raise SystemExit(f"slug collision: {slug} ({slugs[slug]} vs {r['name']})")
        slugs[slug] = r["name"]
        r["slug"] = slug

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    entries = []
    for r in sorted(munis, key=lambda x: x["slug"]):
        fmt = dict(year=YEAR, retrieved=retrieved, **r)
        d = OUT / r["slug"]
        d.mkdir()
        (d / "index.md").write_text(INDEX.format(**fmt), encoding="utf-8")
        (d / "profile.md").write_text(PROFILE.format(**fmt), encoding="utf-8")
        (d / "rates-and-credits.md").write_text(RATES.format(**fmt), encoding="utf-8")
        (d / "refunds.md").write_text(REFUNDS.format(**fmt), encoding="utf-8")
        entries.append(
            f"- [{r['name']}]({r['slug']}/index.md) - RITA code {r['code']}; "
            f"{r['rate']} rate, {r['factor']} credit factor, {r['limit']} credit limit."
        )

    dist_rows = "".join(
        f"| {r['name']} | {r['code']} | {r['rate']} | {r['factor']} | {r['limit']} |\n"
        for r in sorted(districts, key=lambda x: x["name"].lower())
    )
    (OUT / "jedd-jedz-districts.md").write_text(
        DISTRICTS_HEADER.format(year=YEAR, retrieved=retrieved) + dist_rows,
        encoding="utf-8",
    )

    (OUT / "index.md").write_text(
        TOP_INDEX.format(year=YEAR, retrieved=retrieved) + "\n".join(entries) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(munis)} municipality sub-bundles, {len(districts)} districts, index")


if __name__ == "__main__":
    main()
