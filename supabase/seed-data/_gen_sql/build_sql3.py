import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import quiz_data_sql_1b as m1
import quiz_data_sql_2 as m2
import quiz_data_sql_3 as m3
import quiz_data_sql_4 as m4
import quiz_data_sql_5 as m5
import quiz_data_sql_6 as m6
import quiz_data_sql_7 as m7
import quiz_data_sql_8 as m8
import quiz_data_sql_9 as m9

MODULES = [m1, m2, m3, m4, m5, m6, m7, m8, m9]

all_quizzes = []
for mod in MODULES:
    all_quizzes.extend(mod.QUIZZES)

errors = []

if len(all_quizzes) < 100:
    errors.append(f"Il faut au moins 100 quiz, trouvé {len(all_quizzes)}.")

def normalize(s):
    return re.sub(r"\s+", " ", str(s).strip().lower())

seen_titles = {}
seen_statements = {}

for qi, quiz in enumerate(all_quizzes):
    title = quiz.get("title", "")
    qlabel = f"quiz[{qi}] \"{title}\""

    if not title or not title.strip():
        errors.append(f"{qlabel}: titre manquant")
    else:
        nt = normalize(title)
        if nt in seen_titles:
            errors.append(f"{qlabel}: titre dupliqué (déjà utilisé par quiz[{seen_titles[nt]}])")
        else:
            seen_titles[nt] = qi

    questions = quiz.get("questions", [])
    if len(questions) != 6:
        errors.append(f"{qlabel}: doit avoir exactement 6 questions, trouvé {len(questions)}")
        continue

    types_present = set()
    for qqi, q in enumerate(questions):
        label = f"{qlabel} > question[{qqi}]"
        statement = q.get("statement", "")
        if not statement or not statement.strip():
            errors.append(f"{label}: énoncé manquant")
            continue
        norm = normalize(statement)
        if norm in seen_statements:
            errors.append(f"{label}: énoncé dupliqué (déjà utilisé par {seen_statements[norm]})")
        else:
            seen_statements[norm] = label

        qtype = q.get("type")
        if qtype not in ("single", "multiple", "truefalse"):
            errors.append(f"{label}: type invalide \"{qtype}\"")
            continue
        types_present.add(qtype)

        answers = q.get("answers", [])
        if not isinstance(answers, list) or len(answers) < 2:
            errors.append(f"{label}: il faut au moins 2 réponses")
            continue
        if any(not a.get("text") or not str(a.get("text")).strip() for a in answers):
            errors.append(f"{label}: au moins une réponse a un texte vide")

        correct = [a for a in answers if a.get("is_correct") is True]

        if qtype == "truefalse":
            texts = [str(a.get("text")).strip() for a in answers]
            if len(answers) != 2 or "Vrai" not in texts or "Faux" not in texts:
                errors.append(f"{label}: vrai/faux doit avoir exactement les réponses \"Vrai\" et \"Faux\"")
            if len(correct) != 1:
                errors.append(f"{label}: vrai/faux doit avoir exactement 1 bonne réponse")
        elif qtype == "single":
            if len(correct) != 1:
                errors.append(f"{label}: QCM unique doit avoir exactement 1 bonne réponse (trouvé {len(correct)})")
        elif qtype == "multiple":
            if len(answers) < 3:
                errors.append(f"{label}: QCM multiple doit avoir au moins 3 réponses")
            if len(correct) < 2:
                errors.append(f"{label}: QCM multiple doit avoir au moins 2 bonnes réponses (trouvé {len(correct)})")
            if len(correct) >= len(answers):
                errors.append(f"{label}: QCM multiple doit avoir au moins 1 mauvaise réponse")

    for needed in ("single", "multiple", "truefalse"):
        if needed not in types_present:
            errors.append(f"{qlabel}: aucune question de type \"{needed}\" (diversité des types exigée)")

if errors:
    print(f"{len(errors)} erreur(s) trouvée(s) :")
    for e in errors[:80]:
        print(" - " + e)
    if len(errors) > 80:
        print(f"  ... et {len(errors) - 80} de plus.")
    sys.exit(1)

output = {"category": "SQL", "quizzes": all_quizzes}

out_path = "/sessions/clever-dreamy-fermi/mnt/quiz-live/supabase/seed-data/sql.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"OK (local) : {len(all_quizzes)} quiz, {len(seen_statements)} questions uniques écrites dans {out_path}")
