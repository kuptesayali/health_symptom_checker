# AI-based Health Symptom Checker — Day 1 Starter

This project is **educational** and **not a medical diagnosis tool**. Always seek professional care for health concerns.

## Files today
- `data/symptom_dataset.csv` — small curated mapping: symptoms -> possible conditions.
- `data/symptom_canonical_list.csv` — the allowed/canonical symptom keywords.
- `data/symptom_synonyms.csv` — common variants mapped to canonical tokens.
- `requirements.txt` — Python libraries to install for Days 2–3.

## Suggested project structure
```text
your-folder/
├─ data/
│  ├─ symptom_dataset.csv
│  ├─ symptom_canonical_list.csv
│  └─ symptom_synonyms.csv
├─ src/
│  └─ __init__.py
├─ requirements.txt
└─ README.md
```

## Quick start (Windows / macOS / Linux)
1. Ensure Python 3.9+ is installed.
2. Open Terminal (Command Prompt/PowerShell on Windows).
3. `cd` into your project folder.
4. Create and activate a virtual environment:
   - Windows (PowerShell): `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
   - Windows (CMD): `python -m venv .venv` then `.venv\Scripts\activate.bat`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

## Dataset fields
- `condition_id`: stable identifier
- `condition_name`: human-readable label
- `symptoms`: **semicolon-separated** canonical symptom tokens
- `severity_flag`: one of `info | monitor | urgent | emergency`
- `advice`: short general guidance
- `when_to_see_doctor`: red flags / escalation

## Notes
- Keep inputs as general **symptoms**, not diagnoses.
- This dataset is intentionally small for a 3-day build; you can expand later.
