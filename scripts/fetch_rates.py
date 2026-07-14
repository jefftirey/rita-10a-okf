#!/usr/bin/env python3
"""Fetch RITA's Tax Rates Table and write it as pipe-separated data.

Source endpoint (the same AJAX call RITA's own page makes):
  https://www.ritaohio.com/TaxRatesTable/Home/GetTaxRatesByYear?TaxYear=<year>&FilterString=ALL

The response is a flat JSON array: 5 header strings followed by repeating
groups of 5 cells [link-html, code, rate, credit factor, credit limit].
The municipality name is taken from the link's title attribute; markup
(<strong>, footnote asterisks) is stripped from the value cells.

Run from the repo root:  python3 scripts/fetch_rates.py [year]
Writes scripts/data/rita-rates-<year>.psv
"""

import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

YEAR = sys.argv[1] if len(sys.argv) > 1 else "2026"
URL = (
    "https://www.ritaohio.com/TaxRatesTable/Home/GetTaxRatesByYear"
    f"?TaxYear={YEAR}&FilterString=ALL"
)
OUT = Path(__file__).resolve().parent / "data" / f"rita-rates-{YEAR}.psv"


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).replace("*", "").strip()


def main() -> None:
    req = urllib.request.Request(
        URL,
        headers={
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (rita-10a-okf bundle builder)",
            "Referer": "https://www.ritaohio.com/TaxRatesTable",
        },
    )
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)

    rows = []
    for i in range(5, len(data) - 4, 5):
        m = re.search(r'title="([^"]+)"', data[i])
        if not m:
            continue
        name = m.group(1).strip()
        code, rate, factor, limit = (strip_html(data[i + j]) for j in range(1, 5))
        rows.append("|".join([name, code, rate, factor, limit]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = (
        f"# RITA Tax Rates Table, tax year {YEAR}\n"
        f"# Source: {URL}\n"
        f"# Retrieved: {datetime.date.today().isoformat()}\n"
        "# Columns: Municipality|Code|Tax Rate|Credit Factor (Tax Credit)|Credit Rate (Credit Limit)\n"
    )
    OUT.write_text(header + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(rows)} entries)")


if __name__ == "__main__":
    main()
