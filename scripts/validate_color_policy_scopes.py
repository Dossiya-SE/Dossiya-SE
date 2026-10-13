"""Contract check for the complete 18-repository scoped account design inventory."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "data/COLOR_POLICY_SCOPES_V1.json").read_text())
records = manifest["repositories"]
assert manifest["schema_version"] == "1.0.0"
assert len(records) == 18
assert len({r["repo"] for r in records}) == 18
assert all(r["repo"].startswith("Dossiya-SE/") for r in records)
assert all(r["scientific_canvas"] == "#FFFFFF" and r["scientific_panel"] == "#FFFFFF" for r in records)
assert all(r["unreviewed_visuals"] == "NOT_CERTIFIED" for r in records)
exceptions = [r for r in records if "exception" in r]
assert {r["repo"].split("/", 1)[1] for r in exceptions} == {
    "MSE-thesis", "Dossiya-SE-mscfe-quantitative-finance-lab"
}
colors = {r["exception"]["color"] for r in exceptions}
assert colors == {"#FFC627", "#F58E0B"}
assert all(len(r["exception"]["role"]) > 25 and r["exception"]["source"] for r in exceptions)
palette = json.loads((ROOT / "data/visual-palette.json").read_text())
assert palette["accent_contract"]["primary"]["hex"] == "#87CEFA"
assert palette["accent_contract"]["strong"]["hex"] == "#00BFFF"
print("PASS: 18 scopes, 2 explicit exceptions, frozen sky-blue contract and NOT_CERTIFIED visual status")
