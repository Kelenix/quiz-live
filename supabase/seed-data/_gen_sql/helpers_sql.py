def Sx(stmt, options, correct_index, t=20):
    answers = [{"text": o, "is_correct": (i == correct_index)} for i, o in enumerate(options)]
    return {"statement": stmt, "type": "single", "time_limit": t, "answers": answers}

def S(stmt, options, t=20):
    return Sx(stmt, options, 0, t)

def M(stmt, corrects, wrongs, t=30):
    answers = [{"text": c, "is_correct": True} for c in corrects] + [{"text": w, "is_correct": False} for w in wrongs]
    return {"statement": stmt, "type": "multiple", "time_limit": t, "answers": answers}

def T(stmt, correct_true, t=15):
    return {
        "statement": stmt,
        "type": "truefalse",
        "time_limit": t,
        "answers": [
            {"text": "Vrai", "is_correct": correct_true},
            {"text": "Faux", "is_correct": not correct_true},
        ],
    }

def quiz(title, desc, questions):
    if len(questions) != 6:
        raise ValueError(f"Quiz '{title}' doit avoir exactement 6 questions, trouvé {len(questions)}")
    types = {q["type"] for q in questions}
    for needed in ("single", "multiple", "truefalse"):
        if needed not in types:
            raise ValueError(f"Quiz '{title}' manque le type '{needed}'")
    return {"title": title, "description": desc, "questions": questions}
