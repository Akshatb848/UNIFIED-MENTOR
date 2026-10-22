"""Repository integrity checks for the notebook projects.

These are lightweight, stdlib-only checks (no ML stack needed):
- every notebook is valid nbformat-4 JSON and every code cell parses as Python;
- the notebooks reported as executed in the README actually contain outputs;
- the bundled datasets have the shapes and values the READMEs cite.
"""

import ast
import csv
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted(ROOT.glob("*/*.ipynb"))
EXECUTED = {
    "Cybersecurity_Web_Threats_Colab.ipynb",
    "CSAT_Text_Enhanced_EDA_Tuning.ipynb",
    "Blood_Donation_ProdReady_Final.ipynb",
    "TCS_Stock_Project (2).ipynb",
}


def _source(cell: dict) -> str:
    src = cell["source"]
    return "".join(src) if isinstance(src, list) else src


def _strip_magics(code: str) -> str:
    # IPython magics / shell escapes are not Python syntax.
    return "\n".join(
        "pass" if line.lstrip().startswith(("%", "!")) else line for line in code.splitlines()
    )


def test_all_projects_have_a_notebook_and_readme():
    for project in (
        "tcs-stock-data",
        "csat-text-classification",
        "personalised-healthcare-recommendation",
        "Cybersecurity-Web-Threat-Detection",
    ):
        folder = ROOT / project
        assert (folder / "README.md").is_file()
        assert list(folder.glob("*.ipynb"))


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_is_valid_and_code_parses(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    assert nb["nbformat"] == 4
    for i, cell in enumerate(c for c in nb["cells"] if c["cell_type"] == "code"):
        try:
            ast.parse(_strip_magics(_source(cell)))
        except SyntaxError as exc:  # pragma: no cover - failure path
            pytest.fail(f"{path.name}: code cell {i} does not parse: {exc}")


@pytest.mark.parametrize("name", sorted(EXECUTED))
def test_reported_notebooks_contain_outputs(name):
    (path,) = [p for p in NOTEBOOKS if p.name == name]
    nb = json.loads(path.read_text(encoding="utf-8"))
    outputs = [o for c in nb["cells"] if c["cell_type"] == "code" for o in c.get("outputs", [])]
    assert outputs, f"{name} has no saved outputs"


def test_blood_dataset_matches_readme():
    rows = list(csv.DictReader((ROOT / "personalised-healthcare-recommendation/blood.csv").open()))
    assert len(rows) == 748
    assert list(rows[0]) == ["Recency", "Frequency", "Monetary", "Time", "Class"]
    assert {r["Class"] for r in rows} == {"0", "1"}


def test_web_threat_anomaly_count_matches_readme():
    path = ROOT / "Cybersecurity-Web-Threat-Detection/processed_web_threats.csv"
    rows = list(csv.DictReader(path.open()))
    assert len(rows) == 282
    # README: Isolation Forest flagged 15 / 282 sessions; all rows share one label.
    assert sum(int(r["iso_anomaly"]) for r in rows) == 15
    assert {r["detection_types"] for r in rows} == {"waf_rule"}
