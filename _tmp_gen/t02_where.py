# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle clause permet de filtrer les lignes retournees par une requete SELECT ?", "WHERE", "FILTER", "HAVING", "GROUP BY"),
S("Quelle requete retourne les clients dont l'age est superieur a 18 ?", "SELECT * FROM clients WHERE age > 18;", "SELECT * FROM clients FILTER age > 18;", "SELECT * FROM clients HAVING age > 18;", "SELECT * FROM clients IF age > 18;"),
S("Quel operateur logique combine deux conditions qui doivent etre vraies simultanement ?", "AND", "OR", "NOT", "XOR"),
S("Quel operateur logique exige qu'au moins une des deux conditions soit vraie ?", "OR", "AND", "NOT", "BETWEEN"),
S("Que fait l'operateur NOT dans une clause WHERE ?", "Il inverse le resultat logique de la condition", "Il combine deux conditions", "Il trie les resultats", "Il regroupe les lignes"),
S("Quelle condition selectionne les produits dont le prix est compris entre 10 et 50 inclus ?", "WHERE prix BETWEEN 10 AND 50", "WHERE prix IN (10, 50)", "WHERE prix = 10 AND prix = 50", "WHERE prix < 10 OR prix > 50"),
S("Quel operateur teste l'appartenance d'une valeur a un ensemble de valeurs donnees ?", "IN", "BETWEEN", "LIKE", "EXISTS"),
S("Quelle requete selectionne les clients dont le pays est 'France' ou 'Belgique' ?", "SELECT * FROM clients WHERE pays IN ('France', 'Belgique');", "SELECT * FROM clients WHERE pays = 'France' AND pays = 'Belgique';", "SELECT * FROM clients WHERE pays BETWEEN 'France' AND 'Belgique';", "SELECT * FROM clients WHERE pays LIKE 'France, Belgique';"),
S("Quel operateur de comparaison signifie 'different de' en SQL standard ?", "<>", "!", "=!", "NOT="),
S("Que renvoie la condition WHERE statut <> 'archive' ?", "Les lignes dont le statut n'est pas 'archive'", "Les lignes dont le statut est 'archive'", "Toutes les lignes sans exception", "Une erreur de syntaxe"),
S("Quelle clause filtre les lignes APRES qu'elles aient ete regroupees par GROUP BY ?", "HAVING", "WHERE", "FILTER", "ORDER BY"),
S("Pourquoi ne peut-on pas utiliser une fonction d'agregation comme COUNT() directement dans une clause WHERE ?", "Parce que WHERE filtre les lignes individuelles avant tout regroupement", "Parce que COUNT() n'existe pas en SQL", "Parce que WHERE n'accepte que des chaines de caracteres", "Parce que COUNT() ne retourne jamais de nombre"),
S("Quelle requete selectionne les commandes passees entre le 1er et le 31 janvier 2024 inclus ?", "SELECT * FROM commandes WHERE date_commande BETWEEN '2024-01-01' AND '2024-01-31';", "SELECT * FROM commandes WHERE date_commande IN ('2024-01-01', '2024-01-31');", "SELECT * FROM commandes WHERE date_commande LIKE '2024-01';", "SELECT * FROM commandes WHERE date_commande = '2024-01';"),
S("Quel est le resultat de la condition WHERE 1 = 1 appliquee a une table non vide ?", "Toutes les lignes de la table sont retournees", "Aucune ligne n'est retournee", "Une erreur de syntaxe est levee", "Seule la premiere ligne est retournee"),
]
ALL_MULTIPLE += [
M("Parmi les operateurs suivants, lesquels sont des operateurs de comparaison valides en SQL ?",
  ["=", "<>", ">="], "AND", "LIKE"),
M("Quelles requetes filtrent correctement les clients ages de 25 a 40 ans inclus ?",
  ["SELECT * FROM clients WHERE age BETWEEN 25 AND 40;", "SELECT * FROM clients WHERE age >= 25 AND age <= 40;"],
  "SELECT * FROM clients WHERE age IN (25, 40);", "SELECT * FROM clients WHERE age = 25 OR age = 40 ONLY;"),
M("Quelles affirmations sur la clause WHERE sont vraies ?",
  ["Elle s'execute avant le regroupement GROUP BY", "Elle peut combiner plusieurs conditions avec AND et OR"],
  "Elle peut utiliser directement une fonction d'agregation comme SUM()", "Elle s'execute toujours apres ORDER BY"),
]
ALL_TF += [
TF("L'operateur AND retourne vrai uniquement si les deux conditions qu'il relie sont vraies.", True),
TF("La clause WHERE peut filtrer sur le resultat d'une fonction d'agregation comme COUNT().", False),
TF("L'operateur BETWEEN 10 AND 50 inclut les valeurs 10 et 50 dans le resultat.", True),
TF("L'operateur IN permet de tester si une valeur appartient a une liste de valeurs.", True),
TF("La clause HAVING est utilisee pour filtrer des lignes individuelles avant tout regroupement.", False),
]

print("t02:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t02.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
