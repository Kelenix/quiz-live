#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembleur final de la banque de quiz Python pour Quiz Live.
Importe quiz_data_a + b2 + c2 + d2 + e2 (versions corrigees), construit la liste finale,
verifie la coherence et ecrit supabase/seed-data/python.json
"""
import json
import os
import sys
from collections import Counter

QUIZZES = []


def Sx(stmt, options, correct_index, t=20):
    return {
        "statement": stmt,
        "type": "single",
        "time_limit": t,
        "answers": [{"text": a, "is_correct": (i == correct_index)} for i, a in enumerate(options)],
    }


def S(stmt, options, t=20):
    return Sx(stmt, options, 0, t)


def M(stmt, options, correct_set, t=27):
    return {
        "statement": stmt,
        "type": "multiple",
        "time_limit": t,
        "answers": [{"text": a, "is_correct": (i in correct_set)} for i, a in enumerate(options)],
    }


def T(stmt, correct_true, t=13):
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
    assert len(questions) == 6, (title, len(questions))
    types = {q["type"] for q in questions}
    assert {"single", "multiple", "truefalse"} <= types, (title, types)
    QUIZZES.append({"title": title, "description": desc, "questions": questions})


here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)

import quiz_data_a
import quiz_data_b2
import quiz_data_c2
import quiz_data_d2
import quiz_data_e2

MODULES = (quiz_data_a, quiz_data_b2, quiz_data_c2, quiz_data_d2, quiz_data_e2)
for mod in MODULES:
    mod.build(quiz, S, Sx, M, T)

errors = []

if len(QUIZZES) < 100:
    errors.append(f"Il faut au moins 100 quiz, trouve {len(QUIZZES)}.")


def norm(s):
    return " ".join(str(s).strip().lower().split())


titles_seen = {}
for qi, z in enumerate(QUIZZES):
    nt = norm(z["title"])
    if not z["title"].strip():
        errors.append(f"quiz[{qi}]: titre manquant")
    elif nt in titles_seen:
        errors.append(f"quiz[{qi}] '{z['title']}': titre duplique (deja vu quiz[{titles_seen[nt]}])")
    else:
        titles_seen[nt] = qi

stmts_seen = {}
for qi, z in enumerate(QUIZZES):
    qs = z["questions"]
    if len(qs) != 6:
        errors.append(f"quiz[{qi}] '{z['title']}': {len(qs)} questions (attendu 6)")
    types_present = set()
    for qqi, q in enumerate(qs):
        label = f"quiz[{qi}] '{z['title']}' > question[{qqi}]"
        if not q.get("statement", "").strip():
            errors.append(f"{label}: enonce manquant")
            continue
        ns = norm(q["statement"])
        if ns in stmts_seen:
            errors.append(f"{label}: enonce duplique (deja vu {stmts_seen[ns]})")
        else:
            stmts_seen[ns] = label
        types_present.add(q["type"])
        answers = q.get("answers", [])
        if len(answers) < 2:
            errors.append(f"{label}: il faut au moins 2 reponses")
        if any(not str(a.get("text", "")).strip() for a in answers):
            errors.append(f"{label}: reponse avec texte vide")
        correct = [a for a in answers if a.get("is_correct") is True]
        if q["type"] == "single":
            if len(correct) != 1:
                errors.append(f"{label}: single doit avoir exactement 1 bonne reponse (trouve {len(correct)})")
        elif q["type"] == "multiple":
            if len(answers) < 3:
                errors.append(f"{label}: multiple doit avoir au moins 3 reponses")
            if len(correct) < 2:
                errors.append(f"{label}: multiple doit avoir au moins 2 bonnes reponses")
            if len(correct) >= len(answers):
                errors.append(f"{label}: multiple doit avoir au moins 1 mauvaise reponse")
        elif q["type"] == "truefalse":
            texts = [str(a.get("text", "")).strip() for a in answers]
            if len(answers) != 2 or "Vrai" not in texts or "Faux" not in texts:
                errors.append(f"{label}: truefalse doit avoir exactement les reponses 'Vrai' et 'Faux'")
            if len(correct) != 1:
                errors.append(f"{label}: truefalse doit avoir exactement 1 bonne reponse")
        else:
            errors.append(f"{label}: type invalide '{q['type']}'")
    for req in ("single", "multiple", "truefalse"):
        if req not in types_present:
            errors.append(f"quiz[{qi}] '{z['title']}': aucune question de type '{req}'")

if errors:
    print(f"{len(errors)} erreur(s) de coherence trouvee(s) :")
    for e in errors[:80]:
        print(" - " + e)
    if len(errors) > 80:
        print(f"  ... et {len(errors) - 80} de plus.")
    sys.exit(1)

out = {"category": "Python", "quizzes": QUIZZES}
target = os.path.join(here, "..", "python.json")
with open(target, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

all_stmts = [q["statement"].strip().lower() for z in QUIZZES for q in z["questions"]]
print("OK - aucune erreur de coherence detectee.")
print("quizzes:", len(QUIZZES))
print("questions:", len(all_stmts), "uniques:", len(set(all_stmts)))
print("fichier ecrit:", os.path.abspath(target))
