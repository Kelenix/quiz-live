#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generateur de la banque de quiz Python pour Quiz Live."""
import json, os

QUIZZES = []

def Sx(stmt, options, correct_index, t=20):
    return {"statement": stmt, "type": "single", "time_limit": t,
            "answers": [{"text": a, "is_correct": (i == correct_index)} for i, a in enumerate(options)]}

def S(stmt, options, t=20):
    # premiere option = correcte
    return Sx(stmt, options, 0, t)

def M(stmt, options, correct_set, t=27):
    return {"statement": stmt, "type": "multiple", "time_limit": t,
            "answers": [{"text": a, "is_correct": (i in correct_set)} for i, a in enumerate(options)]}

def T(stmt, correct_true, t=13):
    return {"statement": stmt, "type": "truefalse", "time_limit": t,
            "answers": [{"text": "Vrai", "is_correct": correct_true},
                        {"text": "Faux", "is_correct": not correct_true}]}

def quiz(title, desc, questions):
    assert len(questions) == 6, (title, len(questions))
    types = {q["type"] for q in questions}
    assert {"single", "multiple", "truefalse"} <= types, (title, types)
    QUIZZES.append({"title": title, "description": desc, "questions": questions})

import quiz_data_a, quiz_data_b, quiz_data_c, quiz_data_d, quiz_data_e
for mod in (quiz_data_a, quiz_data_b, quiz_data_c, quiz_data_d, quiz_data_e):
    mod.build(quiz, S, Sx, M, T)

out = {"category": "Python", "quizzes": QUIZZES}
here = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(here, "..", "python.json")
with open(target, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("quizzes:", len(QUIZZES))
stmts = [q["statement"].strip().lower() for z in QUIZZES for q in z["questions"]]
print("questions:", len(stmts), "uniques:", len(set(stmts)))
# Detecte doublons
from collections import Counter
dup = [k for k, v in Counter(stmts).items() if v > 1]
if dup:
    print("DOUBLONS:", len(dup))
    for d in dup[:20]:
        print("  ", d[:80])
titles = [z["title"].strip().lower() for z in QUIZZES]
tdup = [k for k, v in Counter(titles).items() if v > 1]
print("titres uniques:", len(set(titles)), "doublons titres:", tdup[:10])
