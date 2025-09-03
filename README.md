# AI-based Health Symptom Checker

> ⚠️ This project is **educational** and **not a medical diagnosis tool**. Always seek professional care for health concerns.

## Project Overview

This Python Flask app helps users check possible health conditions based on symptoms. Enter one or multiple symptoms, and it returns top matched conditions using a curated dataset.

---

## Project Structure

```text
health_symptom_checker/
├─ data/
│  ├─ symptom_dataset.csv
│  ├─ symptom_canonical_list.csv
│  └─ symptom_synonyms.csv
├─ src/
│  └─ __init__.py
│  └─ matcher.py
├─ templates/
│  ├─ index.html
│  └─ results.html
├─ app.py
├─ requirements.txt
└─ README.md
