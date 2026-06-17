#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generateur de la banque de quiz CSS pour Quiz Live."""
import json, os
from collections import Counter

QUIZZES = []

def Sx(stmt, options, correct_index, t=20):
    return {"statement": stmt, "type": "single", "time_limit": t,
            "answers": [{"text": a, "is_correct": (i == correct_index)} for i, a in enumerate(options)]}

def S(stmt, options, t=20):
    return Sx(stmt, options, 0, t)

def M(stmt, options, correct_set, t=30):
    return {"statement": stmt, "type": "multiple", "time_limit": t,
            "answers": [{"text": a, "is_correct": (i in correct_set)} for i, a in enumerate(options)]}

def T(stmt, correct_true, t=15):
    return {"statement": stmt, "type": "truefalse", "time_limit": t,
            "answers": [{"text": "Vrai", "is_correct": correct_true},
                        {"text": "Faux", "is_correct": not correct_true}]}

def quiz(title, desc, questions):
    assert len(questions) == 6, (title, len(questions))
    types = {q["type"] for q in questions}
    assert {"single", "multiple", "truefalse"} <= types, (title, types)
    QUIZZES.append({"title": title, "description": desc, "questions": questions})

import quiz_data_css_1
import quiz_data_css_2
import quiz_data_css_3
import quiz_data_css_4
import quiz_data_css_5
import quiz_data_css_6
import quiz_data_css_7
import quiz_data_css_8
import quiz_data_css_9
import quiz_data_css_10

for mod in (quiz_data_css_1, quiz_data_css_2, quiz_data_css_3, quiz_data_css_4, quiz_data_css_5,
            quiz_data_css_6, quiz_data_css_7, quiz_data_css_8, quiz_data_css_9, quiz_data_css_10):
    mod.build(quiz, S, Sx, M, T)

out = {"category": "CSS", "quizzes": QUIZZES}
here = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(here, "..", "css.json")
with open(target, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("quizzes:", len(QUIZZES))
stmts = [q["statement"].strip().lower() for z in QUIZZES for q in z["questions"]]
print("questions:", len(stmts), "uniques:", len(set(stmts)))
dup = [k for k, v in Counter(stmts).items() if v > 1]
if dup:
    print("DOUBLONS:", len(dup))
    for d in dup[:30]:
        print("  ", d[:90])
titles = [z["title"].strip().lower() for z in QUIZZES]
tdup = [k for k, v in Counter(titles).items() if v > 1]
print("titres uniques:", len(set(titles)), "doublons titres:", tdup[:10])
