# src/matcher.py

# Simple dictionary of conditions and their symptoms
conditions = {
    "flu": ["fever", "cough", "body ache", "fatigue"],
    "common cold": ["sneezing", "runny nose", "cough", "sore throat"],
    "covid-19": ["fever", "cough", "loss of taste", "loss of smell", "fatigue"],
    "migraine": ["headache", "nausea", "sensitivity to light"],
    "allergy": ["sneezing", "itchy eyes", "runny nose"],
}

def get_matches(user_input, top_k=3):
    """
    Compare user input symptoms with known conditions
    and return top matches.
    """
    input_symptoms = user_input.lower().split()
    scores = []

    for condition, symptoms in conditions.items():
        score = sum(1 for word in input_symptoms if word in symptoms)
        if score > 0:
            scores.append((condition, score))

    # Sort by score (descending)
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]
