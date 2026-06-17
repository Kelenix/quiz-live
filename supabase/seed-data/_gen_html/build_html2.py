import json
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import quiz_data_html_1
import quiz_data_html_2
import quiz_data_html_3
import quiz_data_html_4
import quiz_data_html_5
import quiz_data_html_6
import quiz_data_html_7
import quiz_data_html_8
import quiz_data_html_9b

MODULES = [
    quiz_data_html_1,
    quiz_data_html_2,
    quiz_data_html_3,
    quiz_data_html_4,
    quiz_data_html_5,
    quiz_data_html_6,
    quiz_data_html_7,
    quiz_data_html_8,
    quiz_data_html_9b,
]

def normalize(s):
    return re.sub(r"\s+", " ", str(s).strip().lower())

def main():
    all_quizzes = []
    for mod in MODULES:
        qs = mod.get_quizzes()
        print(f"{mod.__name__}: {len(qs)} quiz")
        all_quizzes.extend(qs)

    errors = []

    if len(all_quizzes) < 100:
        errors.append(f"Il faut au moins 100 quiz, trouvé {len(all_quizzes)}.")

    seen_titles = {}
    seen_statements = {}

    for qi, quiz in enumerate(all_quizzes):
        title = quiz.get("title", "")
        if not title.strip():
            errors.append(f"quiz[{qi}]: titre manquant")
        else:
            nt = normalize(title)
            if nt in seen_titles:
                errors.append(f"quiz[{qi}] '{title}': titre dupliqué (déjà utilisé par quiz[{seen_titles[nt]}])")
            else:
                seen_titles[nt] = qi

        questions = quiz.get("questions", [])
        if len(questions) != 8:
            errors.append(f"quiz[{qi}] '{title}': doit avoir exactement 8 questions, trouvé {len(questions)}")
            continue

        types_present = set()
        for qqi, q in enumerate(questions):
            stmt = q.get("statement", "")
            if not stmt.strip():
                errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: énoncé manquant")
                continue
            norm = normalize(stmt)
            if norm in seen_statements:
                errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: énoncé dupliqué (déjà utilisé par {seen_statements[norm]})")
            else:
                seen_statements[norm] = f"quiz[{qi}] '{title}' > question[{qqi}]"

            qtype = q.get("type")
            if qtype not in ("single", "multiple", "truefalse"):
                errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: type invalide '{qtype}'")
                continue
            types_present.add(qtype)

            answers = q.get("answers", [])
            if len(answers) < 2:
                errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: il faut au moins 2 réponses")
                continue
            for a in answers:
                if not a.get("text", "").strip():
                    errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: au moins une réponse a un texte vide")

            correct = [a for a in answers if a.get("is_correct") is True]

            if qtype == "truefalse":
                texts = [a["text"].strip() for a in answers]
                if len(answers) != 2 or "Vrai" not in texts or "Faux" not in texts:
                    errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: vrai/faux doit avoir exactement Vrai/Faux")
                if len(correct) != 1:
                    errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: vrai/faux doit avoir 1 bonne réponse")
            elif qtype == "single":
                if len(correct) != 1:
                    errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: single doit avoir exactement 1 bonne réponse (trouvé {len(correct)})")
            elif qtype == "multiple":
                if len(answers) < 3:
                    errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: multiple doit avoir au moins 3 réponses")
                if len(correct) < 2:
                    errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: multiple doit avoir au moins 2 bonnes réponses")
                if len(correct) >= len(answers):
                    errors.append(f"quiz[{qi}] '{title}' > question[{qqi}]: multiple doit avoir au moins 1 mauvaise réponse")

        for needed in ("single", "multiple", "truefalse"):
            if needed not in types_present:
                errors.append(f"quiz[{qi}] '{title}': aucune question de type '{needed}'")

    if errors:
        print(f"\n{len(errors)} erreur(s) trouvée(s) :")
        for e in errors[:100]:
            print(" - " + e)
        sys.exit(1)

    output = {"category": "HTML", "quizzes": all_quizzes}

    out_path = r"C:\PROJECT PERSO\quiz-live\supabase\seed-data\html.json"
    if not os.path.exists(r"C:\PROJECT PERSO"):
        out_path = "/sessions/clever-dreamy-fermi/mnt/quiz-live/supabase/seed-data/html.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    total_questions = sum(len(q["questions"]) for q in all_quizzes)
    print(f"\nOK build: {len(all_quizzes)} quiz, {total_questions} questions, {len(seen_statements)} énoncés uniques.")
    print(f"Fichier écrit : {out_path}")

if __name__ == "__main__":
    main()
