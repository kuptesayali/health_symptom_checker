import pandas as pd

# Load datasets
dataset = pd.read_csv("data/symptom_dataset.csv")
canonical = pd.read_csv("data/symptom_canonical_list.csv")
synonyms = pd.read_csv("data/symptom_synonyms.csv")

# Build synonym dictionary
synonym_map = dict(zip(synonyms["symptom_synonym"], synonyms["canonical_symptom"]))



def normalize_symptom(symptom: str) -> str:
    """Convert user input into canonical symptom token"""
    s = symptom.strip().lower()
    return synonym_map.get(s, s)  # map to canonical if synonym exists


def match_symptoms(user_inputs: list[str]) -> list[dict]:
    """Match user symptoms to possible conditions"""
    normalized = [normalize_symptom(s) for s in user_inputs]

    results = []
    for _, row in dataset.iterrows():
        condition_symptoms = row["symptoms"].split(";")
        overlap = set(normalized) & set(condition_symptoms)
        if overlap:
            results.append({
                "condition": row["condition_name"],
                "severity": row["severity_flag"],
                "advice": row["advice"],
                "doctor": row["when_to_see_doctor"],
                "matched": list(overlap)
            })
    return results
