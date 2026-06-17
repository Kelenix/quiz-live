# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quel type de jointure retourne uniquement les lignes ayant une correspondance dans les deux tables ?", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "CROSS JOIN"),
S("Quel type de jointure retourne toutes les lignes de la table de gauche, meme sans correspondance a droite ?", "LEFT JOIN", "INNER JOIN", "RIGHT JOIN", "CROSS JOIN"),
S("Quel type de jointure retourne toutes les lignes de la table de droite, meme sans correspondance a gauche ?", "RIGHT JOIN", "LEFT JOIN", "INNER JOIN", "CROSS JOIN"),
S("Quel type de jointure retourne toutes les lignes des deux tables, qu'il y ait correspondance ou non ?", "FULL JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN"),
S("Quel type de jointure produit le produit cartesien de deux tables (toutes les combinaisons possibles) ?", "CROSS JOIN", "INNER JOIN", "LEFT JOIN", "NATURAL JOIN"),
S("Quel mot-cle precise la condition de correspondance entre deux tables jointes ?", "ON", "WHERE", "WITH", "USING ONLY"),
S("Qu'est-ce qu'une auto-jointure (self join) ?", "Une jointure d'une table avec elle-meme via deux alias differents", "Une jointure automatique creee par le SGBD", "Une jointure qui ne necessite pas de condition ON", "Un index applique automatiquement"),
S("Quelle requete relie les commandes a leurs clients via la cle client_id ?", "SELECT * FROM commandes INNER JOIN clients ON commandes.client_id = clients.id;", "SELECT * FROM commandes INNER JOIN clients WHERE commandes.client_id = clients.id;", "SELECT * FROM commandes, clients;", "SELECT * FROM commandes JOIN clients USING client_id;"),
S("Avec un LEFT JOIN, que contiennent les colonnes de la table de droite pour les lignes sans correspondance ?", "NULL", "0", "Une chaine vide", "La derniere valeur rencontree"),
S("Dans une auto-jointure sur la table employes pour trouver le manager de chaque employe, pourquoi utilise-t-on deux alias ?", "Pour distinguer les deux roles de la meme table (employe et manager) dans la requete", "Parce que SQL l'exige pour toute jointure", "Pour creer deux tables physiques distinctes", "Parce qu'un alias unique provoquerait une erreur de syntaxe"),
S("Quelle est la consequence d'oublier la condition ON dans un INNER JOIN explicite ?", "Une erreur de syntaxe ou un comportement proche d'un produit cartesien selon le SGBD", "Le SGBD devine automatiquement la bonne condition", "La requete s'execute comme un LEFT JOIN", "Aucune ligne n'est retournee dans tous les cas"),
S("Combien de lignes produit un CROSS JOIN entre une table de 4 lignes et une table de 5 lignes ?", "20", "9", "4", "5"),
S("Quelle jointure choisir pour lister tous les clients, y compris ceux n'ayant jamais passe de commande ?", "LEFT JOIN de clients vers commandes", "INNER JOIN entre clients et commandes", "RIGHT JOIN entre commandes et clients sans alias", "CROSS JOIN entre clients et commandes"),
S("Quel est l'equivalent d'un RIGHT JOIN entre A et B en inversant l'ordre des tables ?", "Un LEFT JOIN entre B et A", "Un INNER JOIN entre A et B", "Un CROSS JOIN entre B et A", "Il n'existe pas d'equivalent possible"),
]
ALL_MULTIPLE += [
M("Parmi les types de jointures suivants, lesquels existent en SQL standard ?",
  ["INNER JOIN", "LEFT JOIN", "FULL JOIN"], "MIDDLE JOIN", "PARTIAL JOIN"),
M("Quelles affirmations sur LEFT JOIN sont correctes ?",
  ["Il conserve toutes les lignes de la table de gauche", "Les colonnes de la table de droite sont a NULL si aucune correspondance n'existe"],
  "Il exclut systematiquement les lignes sans correspondance", "Il est strictement identique a un INNER JOIN"),
M("Quelles utilisations sont typiques d'une auto-jointure (self join) ?",
  ["Trouver les employes et leur manager dans une meme table employes", "Comparer des lignes d'une meme table entre elles, comme des paires de produits"],
  "Joindre deux tables totalement independantes sans aucun lien logique", "Toujours remplacer un GROUP BY"),
]
ALL_TF += [
TF("Un INNER JOIN ne retourne que les lignes presentes dans les deux tables selon la condition de jointure.", True),
TF("Un CROSS JOIN necessite obligatoirement une clause ON pour s'executer.", False),
TF("Avec un FULL JOIN, les lignes sans correspondance d'un cote ont des valeurs NULL pour les colonnes de l'autre table.", True),
TF("Un LEFT JOIN et un RIGHT JOIN produisent toujours exactement le meme resultat quel que soit l'ordre des tables.", False),
TF("Une auto-jointure permet de comparer les lignes d'une table avec d'autres lignes de cette meme table.", True),
TF("CROSS JOIN combine chaque ligne de la premiere table avec chaque ligne de la seconde, sans condition de correspondance.", True),
]

print("t05:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t05.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
