#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generateur corrige de la banque de quiz CSS pour Quiz Live."""
import json, os, sys
from collections import Counter

QUIZZES = []

def Sx(stmt, options, correct_index, t=20):
    return {"statement": stmt, "type": "single", "time_limit": t,
            "answers": [{"text": a, "is_correct": (i == correct_index)} for i, a in enumerate(options)]}

def S(stmt, options, t=20):
    return Sx(stmt, options, 0, t)

def M(stmt, corrects, correct_set, wrongs, t=30):
    # corrects: list of correct answer texts; wrongs: list of wrong answer texts.
    # correct_set kept for call-site compatibility but ignored (corrects are always all-correct).
    answers = [{"text": c, "is_correct": True} for c in corrects] + \
              [{"text": w, "is_correct": False} for w in wrongs]
    return {"statement": stmt, "type": "multiple", "time_limit": t, "answers": answers}

def T(stmt, correct_true, t=15):
    return {"statement": stmt, "type": "truefalse", "time_limit": t,
            "answers": [{"text": "Vrai", "is_correct": correct_true},
                        {"text": "Faux", "is_correct": not correct_true}]}

def quiz(title, desc, questions):
    assert len(questions) == 6, (title, len(questions))
    types = {q["type"] for q in questions}
    assert {"single", "multiple", "truefalse"} <= types, (title, types)
    QUIZZES.append({"title": title, "description": desc, "questions": questions})

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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

# --- Fix the single pre-existing invalid "multiple" question (only 1 correct answer) ---
fixed = False
for z in QUIZZES:
    if z["title"] == "Sélecteur universel et groupement":
        for q in z["questions"]:
            if q["type"] == "multiple" and q["statement"].startswith("Quels sélecteurs ciblent strictement TOUS"):
                q["answers"] = [
                    {"text": "Il cible tous les éléments du document, sans exception", "is_correct": True},
                    {"text": "Il est souvent utilisé pour réinitialiser des styles par défaut (ex: box-sizing)", "is_correct": True},
                    {"text": "Il a une spécificité plus élevée que les sélecteurs de classe", "is_correct": False},
                    {"text": "Il ne peut cibler que les éléments de niveau racine du document", "is_correct": False},
                ]
                q["statement"] = "Quelles affirmations sur le sélecteur universel `*` sont correctes ?"
                fixed = True
assert fixed, "Le correctif du sélecteur universel n'a pas été appliqué"

# --- Fix "Combinateurs de sélecteurs" : le combinateur descendant " " (espace) était
# représenté par une chaîne vide après trim(), ce qui est rejeté par le validateur. ---
fixed2 = False
for z in QUIZZES:
    if z["title"] == "Combinateurs de sélecteurs":
        for q in z["questions"]:
            if q["type"] == "single" and q["statement"].startswith("Quel combinateur sélectionne uniquement les enfants directs"):
                for a in q["answers"]:
                    if a["text"].strip() == "":
                        a["text"] = "(espace)"
                fixed2 = True
            if q["type"] == "multiple" and q["statement"].startswith("Quels combinateurs permettent de cibler des éléments frères"):
                for a in q["answers"]:
                    if a["text"].strip() == "":
                        a["text"] = "(espace)"
                fixed2 = True
assert fixed2, "Le correctif des combinateurs n'a pas été appliqué"

# --- 6 quizzes supplémentaires pour dépasser confortablement les 100 ---
quiz(
    "Pseudo-classes de formulaire",
    "Cibler les états des champs de formulaire avec les pseudo-classes CSS.",
    [
        S("Quelle pseudo-classe cible une case à cocher ou un bouton radio sélectionné ?",
          [":checked", ":selected", ":active", ":focus"]),
        S("Quelle pseudo-classe cible un champ de formulaire désactivé ?",
          [":disabled", ":readonly", ":inactive", ":locked"]),
        S("Quelle pseudo-classe cible un champ dont la valeur ne respecte pas sa validation (ex: type=email) ?",
          [":invalid", ":error", ":wrong", ":bad-input"]),
        M("Lesquelles de ces pseudo-classes concernent l'état de validation ou d'obligation d'un champ ?",
          [":required", ":valid"], {0, 1}, [":hover", ":nth-child(2)"]),
        T("La pseudo-classe `:checked` peut s'appliquer à une `<option>` sélectionnée dans un `<select>`.", True),
        T("`:disabled` et `:read-only` désignent exactement le même état d'un champ de formulaire.", False),
    ],
)

quiz(
    "aspect-ratio et ratio d'affichage",
    "Contrôler le rapport largeur/hauteur d'un élément avec la propriété aspect-ratio.",
    [
        S("Quelle propriété CSS moderne permet de fixer directement un ratio largeur/hauteur sur un élément ?",
          ["aspect-ratio", "ratio", "box-ratio", "scale-ratio"]),
        S("Quelle valeur de aspect-ratio donne un format carré ?",
          ["1 / 1", "16 / 9", "4 / 3", "0 / 0"]),
        S("Avant l'arrivée de aspect-ratio, quelle technique CSS était couramment utilisée pour forcer un ratio (ex: via padding) ?",
          ["Le hack du padding-top en pourcentage", "La propriété z-index", "Le float: ratio", "La propriété content-ratio"]),
        M("Pour quels éléments la propriété aspect-ratio est-elle particulièrement utile ?",
          ["Les images dont la taille réelle n'est pas encore connue au chargement", "Les conteneurs de vidéos responsives"], {0, 1},
          ["Les éléments de type inline sans dimension", "Les balises meta du document"]),
        T("`aspect-ratio: 16 / 9;` appliqué à une image avec object-fit: cover évite la déformation tout en respectant le ratio.", True),
        T("La propriété aspect-ratio ignore totalement les valeurs explicites de width ou height si elles sont définies.", False),
    ],
)

quiz(
    "Les compteurs CSS (counter-reset / counter-increment)",
    "Générer une numérotation automatique avec les compteurs CSS et content.",
    [
        S("Quelle propriété initialise un compteur CSS à une valeur de départ ?",
          ["counter-reset", "counter-increment", "counter-set", "counter-init"]),
        S("Quelle propriété augmente la valeur d'un compteur CSS à chaque occurrence d'un sélecteur ?",
          ["counter-increment", "counter-reset", "counter-add", "counter-step"]),
        S("Quelle fonction permet d'afficher la valeur d'un compteur via la propriété content ?",
          ["counter()", "value()", "count()", "increment()"]),
        M("Quelles affirmations sur les compteurs CSS sont correctes ?",
          ["Ils permettent de numéroter automatiquement des titres ou des éléments de liste", "Ils sont souvent utilisés avec les pseudo-éléments ::before ou ::after"], {0, 1},
          ["Ils nécessitent obligatoirement JavaScript pour fonctionner", "Ils ne peuvent compter que jusqu'à 10"]),
        T("Un compteur CSS peut être imbriqué pour produire une numérotation hiérarchique comme 1.1, 1.2, 2.1.", True),
        T("La fonction counter() ne peut être utilisée qu'à l'intérieur de la propriété color.", False),
    ],
)

quiz(
    "outline et accessibilité du focus",
    "Comprendre le rôle de outline dans la visibilité du focus clavier.",
    [
        S("Quelle propriété CSS dessine un contour autour d'un élément sans affecter la mise en page (pas de prise d'espace) ?",
          ["outline", "border", "box-shadow uniquement", "margin"]),
        S("Quelle pseudo-classe cible spécifiquement un élément ayant le focus via la navigation au clavier (et non la souris) ?",
          [":focus-visible", ":hover", ":target", ":active"]),
        S("Pourquoi est-il déconseillé de simplement écrire `*:focus { outline: none; }` sans alternative ?",
          ["Cela supprime un indicateur essentiel pour les utilisateurs naviguant au clavier", "Cela ralentit le rendu de la page", "Cela invalide le CSS", "Cela désactive complètement les formulaires"]),
        M("Lesquelles de ces affirmations sur outline sont correctes ?",
          ["outline ne modifie pas les dimensions de la boîte de l'élément", "outline peut être stylé avec outline-color, outline-style et outline-width"], {0, 1},
          ["outline respecte toujours les angles arrondis de border-radius par défaut sur tous les navigateurs", "outline remplace obligatoirement border"]),
        T("`:focus-visible` permet d'afficher un contour de focus uniquement quand cela est pertinent, par exemple lors d'une navigation au clavier.", True),
        T("Supprimer totalement l'indicateur de focus visuel sans alternative est une bonne pratique d'accessibilité recommandée.", False),
    ],
)

quiz(
    "scroll-snap et défilement contrôlé",
    "Créer des zones de défilement avec accroche grâce à scroll-snap.",
    [
        S("Quelle propriété, posée sur le conteneur défilant, active le comportement d'accroche au défilement ?",
          ["scroll-snap-type", "scroll-behavior", "overflow-snap", "scroll-anchor"]),
        S("Quelle propriété, posée sur les enfants d'un conteneur scroll-snap, définit leur point d'accroche ?",
          ["scroll-snap-align", "scroll-snap-stop", "snap-align", "scroll-point"]),
        S("Quelle propriété permet d'obtenir un défilement fluide et animé plutôt qu'un saut instantané lors d'un scroll programmatique ?",
          ["scroll-behavior: smooth", "scroll-snap-type: smooth", "transition: scroll", "animation: scroll"]),
        M("Quelles valeurs sont valides pour l'axe de scroll-snap-type ?",
          ["x", "y", "both"], {0, 1, 2}, ["diagonal"]),
        T("scroll-snap-type permet de créer un carrousel d'images qui s'accroche à chaque image lors du défilement, sans JavaScript.", True),
        T("scroll-snap-align doit obligatoirement être défini sur le conteneur parent plutôt que sur les éléments enfants.", False),
    ],
)

quiz(
    "writing-mode et direction du texte",
    "Adapter la mise en page CSS pour des directions d'écriture différentes.",
    [
        S("Quelle propriété CSS permet de faire défiler le texte verticalement au lieu d'horizontalement ?",
          ["writing-mode", "text-direction", "flow-direction", "vertical-align"]),
        S("Quelle valeur de writing-mode affiche le texte de haut en bas avec des lignes progressant de droite à gauche ?",
          ["vertical-rl", "horizontal-tb", "vertical-lr", "sideways-lr"]),
        S("Quelle propriété CSS définit le sens de lecture global (gauche-à-droite ou droite-à-gauche) d'un document ?",
          ["direction", "writing-mode", "unicode-bidi seul", "text-align"]),
        M("Quelles propriétés CSS sont liées à l'internationalisation de la mise en page (texte vertical, RTL, etc.) ?",
          ["writing-mode", "direction"], {0, 1}, ["z-index", "box-shadow"]),
        T("La valeur `direction: rtl;` est couramment utilisée pour mettre en page des contenus en arabe ou en hébreu.", True),
        T("writing-mode n'a aucun effet sur la disposition du texte et ne sert qu'à des fins décoratives.", False),
    ],
)

if len(QUIZZES) < 100:
    raise SystemExit(f"Pas assez de quiz: {len(QUIZZES)}")

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
