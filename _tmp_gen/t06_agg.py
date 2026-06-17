# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle fonction d'agregation compte le nombre de lignes d'un resultat ?", "COUNT", "SUM", "TOTAL", "NUMBER"),
S("Quelle fonction d'agregation calcule la somme des valeurs d'une colonne numerique ?", "SUM", "COUNT", "AVG", "ADD"),
S("Quelle fonction d'agregation calcule la moyenne des valeurs d'une colonne ?", "AVG", "MEAN", "SUM", "MEDIAN"),
S("Quelle fonction retourne la plus petite valeur d'une colonne ?", "MIN", "LOW", "SMALLEST", "FIRST"),
S("Quelle fonction retourne la plus grande valeur d'une colonne ?", "MAX", "HIGH", "LARGEST", "LAST"),
S("Que retourne COUNT(*) sur une table de 500 lignes sans filtre ?", "500", "0", "Le nombre de colonnes", "1"),
S("Quelle est la difference entre COUNT(*) et COUNT(colonne) ?", "COUNT(colonne) ignore les valeurs NULL de cette colonne, COUNT(*) compte toutes les lignes", "Il n'y a aucune difference entre les deux", "COUNT(*) ignore les NULL et COUNT(colonne) non", "COUNT(colonne) compte uniquement les doublons"),
S("Quelle requete calcule le chiffre d'affaires total de la table ventes ?", "SELECT SUM(montant) FROM ventes;", "SELECT COUNT(montant) FROM ventes;", "SELECT AVG(montant) FROM ventes;", "SELECT montant FROM ventes GROUP BY SUM;"),
S("Les fonctions d'agregation comme SUM ou AVG prennent-elles en compte les valeurs NULL dans leur calcul ?", "Non, elles ignorent generalement les valeurs NULL", "Oui, elles considerent NULL comme 0", "Oui, elles provoquent une erreur en presence de NULL", "Cela depend uniquement de ORDER BY"),
S("Quelle requete trouve le salaire maximum par departement ?", "SELECT departement, MAX(salaire) FROM employes GROUP BY departement;", "SELECT MAX(departement, salaire) FROM employes;", "SELECT departement, salaire FROM employes ORDER BY salaire DESC LIMIT 1;", "SELECT MAX(salaire) FROM employes ORDER BY departement;"),
S("Quelle fonction d'agregation peut s'appliquer aussi bien sur des colonnes numeriques que sur COUNT(*) ?", "COUNT", "AVG", "SUM", "MIN"),
S("Quel est le resultat de SELECT COUNT(*) FROM table_vide; si la table ne contient aucune ligne ?", "0", "NULL", "Une erreur", "1"),
S("Quel est le resultat de SELECT AVG(colonne) FROM table; si toutes les valeurs de la colonne sont NULL ?", "NULL", "0", "Une erreur de division par zero", "La valeur la plus frequente"),
]
ALL_MULTIPLE += [
M("Parmi les fonctions suivantes, lesquelles sont des fonctions d'agregation SQL standard ?",
  ["COUNT", "SUM", "AVG", "MAX"], "CONCAT", "UPPER"),
M("Quelles affirmations sur COUNT(*) et COUNT(colonne) sont correctes ?",
  ["COUNT(*) compte toutes les lignes, y compris celles avec des valeurs NULL dans certaines colonnes", "COUNT(colonne) exclut les lignes ou cette colonne specifique est NULL"],
  "COUNT(*) et COUNT(colonne) donnent toujours exactement le meme resultat", "COUNT ne peut jamais etre utilise avec GROUP BY"),
M("Quelles requetes sont valides pour obtenir des statistiques agregees par groupe ?",
  ["SELECT categorie, COUNT(*), AVG(prix) FROM produits GROUP BY categorie;", "SELECT departement, SUM(salaire) FROM employes GROUP BY departement;"],
  "SELECT categorie, COUNT(*) FROM produits;", "SELECT AVG(prix) FROM produits GROUP BY AVG(prix);"),
]
ALL_TF += [
TF("La fonction SUM() ignore les valeurs NULL lors du calcul de la somme.", True),
TF("COUNT(colonne) compte toutes les lignes de la table, y compris celles ou colonne vaut NULL.", False),
TF("MIN() et MAX() peuvent s'appliquer a des colonnes de type texte, pas seulement numeriques.", True),
TF("Les fonctions d'agregation peuvent etre utilisees sans aucune clause GROUP BY pour obtenir un resultat global sur toute la table.", True),
TF("AVG(colonne) renvoie toujours 0 lorsque toutes les valeurs de la colonne sont NULL.", False),
]

print("t06:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t06.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
