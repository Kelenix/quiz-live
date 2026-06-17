# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle clause permet de trier les resultats d'une requete SELECT ?", "ORDER BY", "SORT BY", "GROUP BY", "ARRANGE BY"),
S("Quel mot-cle precise un tri par ordre decroissant dans ORDER BY ?", "DESC", "DOWN", "REVERSE", "MAX"),
S("Quel est l'ordre de tri par defaut si aucun mot-cle n'est precise apres ORDER BY ?", "ASC (croissant)", "DESC (decroissant)", "Aleatoire", "Aucun tri n'est applique"),
S("Quelle requete trie les produits du plus chere au moins cher ?", "SELECT * FROM produits ORDER BY prix DESC;", "SELECT * FROM produits ORDER BY prix ASC;", "SELECT * FROM produits SORT prix DESC;", "SELECT * FROM produits GROUP BY prix DESC;"),
S("Peut-on trier les resultats sur plusieurs colonnes a la fois avec ORDER BY ?", "Oui, en les separant par des virgules", "Non, une seule colonne est autorisee", "Oui, mais uniquement avec UNION", "Non, il faut utiliser GROUP BY"),
S("Dans ORDER BY nom ASC, ville DESC, quel est l'ordre de priorite du tri ?", "D'abord par nom croissant, puis par ville decroissante en cas d'egalite", "D'abord par ville, puis par nom", "Les deux colonnes sont triees simultanement sans priorite", "Seule la colonne ville est utilisee pour le tri"),
S("Quelle clause permet de limiter le nombre de lignes retournees par une requete ?", "LIMIT", "TOP", "MAX", "RESTRICT"),
S("A quoi sert la clause OFFSET combinee a LIMIT ?", "A ignorer un certain nombre de lignes avant de commencer a retourner les resultats", "A trier les resultats par ordre alphabetique", "A compter le nombre total de lignes", "A dupliquer les resultats"),
S("Quelle requete retourne les 10 premiers clients par ordre alphabetique de nom ?", "SELECT * FROM clients ORDER BY nom ASC LIMIT 10;", "SELECT TOP 10 * FROM clients;", "SELECT * FROM clients LIMIT 10 ORDER BY nom;", "SELECT * FROM clients WHERE LIMIT = 10;"),
S("Quelle requete permet d'afficher la deuxieme page de 20 resultats (lignes 21 a 40) triees par identifiant ?", "SELECT * FROM produits ORDER BY id LIMIT 20 OFFSET 20;", "SELECT * FROM produits ORDER BY id LIMIT 20 OFFSET 0;", "SELECT * FROM produits ORDER BY id PAGE 2;", "SELECT * FROM produits ORDER BY id LIMIT 40 OFFSET 40;"),
S("On peut trier sur une colonne qui n'apparait pas dans la liste du SELECT, est-ce vrai en SQL standard ?", "Oui, ORDER BY peut reference une colonne de la table source non selectionnee", "Non, c'est toujours interdit", "Seulement avec GROUP BY", "Seulement si DISTINCT est utilise"),
]
ALL_MULTIPLE += [
M("Parmi ces requetes, lesquelles trient correctement les employes par salaire decroissant ?",
  ["SELECT * FROM employes ORDER BY salaire DESC;", "SELECT * FROM employes ORDER BY salaire DESC, nom ASC;"],
  "SELECT * FROM employes SORT BY salaire DESC;", "SELECT * FROM employes GROUP BY salaire DESC;"),
M("Quelles affirmations sur LIMIT et OFFSET sont correctes pour la pagination ?",
  ["LIMIT restreint le nombre de lignes retournees", "OFFSET indique combien de lignes ignorer avant de retourner les resultats"],
  "LIMIT doit obligatoirement etre utilise avec GROUP BY", "OFFSET trie automatiquement les resultats"),
]
ALL_TF += [
TF("Par defaut, ORDER BY trie les resultats en ordre croissant (ASC).", True),
TF("ORDER BY ne peut trier que sur une seule colonne a la fois.", False),
TF("LIMIT 5 OFFSET 10 retourne les lignes 11 a 15 selon l'ordre du tri applique.", True),
TF("La clause LIMIT doit obligatoirement etre placee avant ORDER BY dans une requete SELECT.", False),
TF("ORDER BY peut s'appliquer sur le resultat d'une expression calculee, comme prix * quantite.", True),
]

print("t03:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t03.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
