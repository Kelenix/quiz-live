# -*- coding: utf-8 -*-
import json, pickle

def S(statement, correct, wrongs, time_limit=20):
    answers = [{"text": correct, "is_correct": True}] + [{"text": w, "is_correct": False} for w in wrongs]
    return {"statement": statement, "type": "single", "time_limit": time_limit, "answers": answers}

def M(statement, corrects, wrongs, time_limit=30):
    answers = [{"text": c, "is_correct": True} for c in corrects] + [{"text": w, "is_correct": False} for w in wrongs]
    return {"statement": statement, "type": "multiple", "time_limit": time_limit, "answers": answers}

def TF(statement, is_true, time_limit=15):
    answers = [{"text": "Vrai", "is_correct": is_true}, {"text": "Faux", "is_correct": not is_true}]
    return {"statement": statement, "type": "truefalse", "time_limit": time_limit, "answers": answers}

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

# ===================== THEME 1 : SELECT de base et alias =====================
ALL_SINGLE += [
S("Quelle clause SQL permet de selectionner des colonnes dans une table ?", "SELECT", ["FETCH", "GET", "PULL"]),
S("Quel mot-cle permet de recuperer toutes les colonnes d'une table ?", "*", ["ALL", "ANY", "FULL"]),
S("Quelle instruction affiche toutes les colonnes de la table clients ?", "SELECT * FROM clients;", ["SHOW * FROM clients;", "GET * FROM clients;", "FETCH * FROM clients;"]),
S("Dans SELECT nom AS n FROM clients;, que represente AS n ?", "Un alias pour la colonne nom", ["Une nouvelle table", "Une condition de filtre", "Un type de donnee"]),
S("Quelle syntaxe permet de donner un alias a une table dans une requete SELECT ?", "SELECT * FROM clients AS c;", ["SELECT * FROM clients ALIAS c;", "SELECT * FROM clients RENAME c;", "SELECT * FROM clients LIKE c;"]),
S("Quel mot-cle SQL permet d'eliminer les doublons dans un resultat ?", "DISTINCT", ["UNIQUE", "ONLY", "SINGLE"]),
S("Que retourne SELECT DISTINCT ville FROM clients; ?", "La liste des villes sans doublons", "Toutes les lignes de la table clients", "Le nombre de villes differentes", "La premiere ville trouvee"),
S("Quelle requete selectionne uniquement les colonnes nom et prenom de la table employes ?", "SELECT nom, prenom FROM employes;", "SELECT nom AND prenom FROM employes;", "SELECT nom + prenom FROM employes;", "SELECT (nom, prenom) FROM employes;"),
S("Est-il recommande de terminer une instruction SQL par un point-virgule dans la plupart des SGBD ?", "Oui, c'est la convention standard recommandee", "Non, c'est interdit", "Seulement pour SELECT", "Seulement pour les sous-requetes"),
S("Quel est le role d'un alias de colonne defini avec AS dans le resultat affiche ?", "Renommer la colonne dans le resultat retourne", "Modifier la valeur stockee en base", "Supprimer la colonne d'origine", "Creer un index sur la colonne"),
S("Que fait la requete SELECT prix * 1.2 AS prix_ttc FROM produits; ?", "Elle calcule un prix TTC a partir du prix HT", "Elle modifie le prix stocke en base", "Elle cree une nouvelle colonne permanente", "Elle filtre les produits dont le prix depasse 1.2"),
S("Le mot-cle AS est-il obligatoire pour definir un alias en SQL standard ?", "Non, il est optionnel dans la plupart des SGBD", "Oui, toujours obligatoire", "Seulement pour les alias de table", "Seulement pour les alias de colonne"),
]
ALL_MULTIPLE += [
M("Parmi les elements suivants, lesquels peuvent suivre directement le mot-cle SELECT ?",
  ["Le caractere *", "Le nom d'une colonne", "Une expression calculee comme prix * 2"],
  ["Le mot-cle FROM seul", "Le mot-cle WHERE seul"]),
M("Quelles affirmations sur les alias en SQL sont correctes ?",
  ["Un alias de colonne change le nom affiche dans le resultat", "Un alias de table peut etre utilise pour raccourcir les references aux colonnes"],
  ["Un alias modifie le nom reel de la colonne en base", "Un alias est obligatoire pour toute colonne selectionnee"]),
M("Parmi ces requetes, lesquelles utilisent correctement DISTINCT ?",
  ["SELECT DISTINCT pays FROM clients;", "SELECT DISTINCT nom, prenom FROM clients;"],
  ["SELECT nom, DISTINCT prenom FROM clients;", "DISTINCT SELECT * FROM clients;"]),
]
ALL_TF += [
TF("La requete SELECT * FROM table; retourne toutes les colonnes et toutes les lignes de la table.", True),
TF("L'instruction SELECT permet de modifier les donnees d'une table.", False),
TF("Un alias defini avec AS modifie definitivement le nom de la colonne dans la base de donnees.", False),
TF("DISTINCT s'applique a l'ensemble des colonnes selectionnees dans la liste, pas a une seule colonne isolee.", True),
TF("Il est possible d'utiliser un alias de table pour prefixer les noms de colonnes dans une requete.", True),
]

print("Theme1:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank1.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
