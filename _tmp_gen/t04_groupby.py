# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle clause permet de regrouper des lignes partageant une meme valeur de colonne ?", "GROUP BY", "ORDER BY", "WHERE", "PARTITION BY"),
S("Quelle requete compte le nombre de clients par pays ?", "SELECT pays, COUNT(*) FROM clients GROUP BY pays;", "SELECT pays, COUNT(*) FROM clients ORDER BY pays;", "SELECT pays, COUNT(*) FROM clients WHERE pays;", "SELECT COUNT(pays) FROM clients;"),
S("Quelle clause permet de filtrer les groupes resultant d'un GROUP BY selon une condition sur une agregation ?", "HAVING", "WHERE", "FILTER", "GROUP FILTER"),
S("Quelle requete affiche les pays ayant plus de 10 clients ?", "SELECT pays, COUNT(*) FROM clients GROUP BY pays HAVING COUNT(*) > 10;", "SELECT pays, COUNT(*) FROM clients WHERE COUNT(*) > 10 GROUP BY pays;", "SELECT pays, COUNT(*) FROM clients GROUP BY pays WHERE COUNT(*) > 10;", "SELECT pays FROM clients HAVING COUNT(*) > 10;"),
S("Dans une requete avec GROUP BY, quelles colonnes peuvent figurer dans le SELECT sans etre agregees ?", "Uniquement celles listees dans le GROUP BY", "Toutes les colonnes de la table", "Aucune colonne non agregee n'est autorisee", "Seulement la colonne triee avec ORDER BY"),
S("Quelle est la difference essentielle entre WHERE et HAVING ?", "WHERE filtre les lignes avant regroupement, HAVING filtre les groupes apres regroupement", "WHERE et HAVING sont strictement identiques", "HAVING s'applique uniquement aux jointures", "WHERE s'applique uniquement aux sous-requetes"),
S("Quelle requete calcule le total des ventes par produit ?", "SELECT produit_id, SUM(montant) FROM ventes GROUP BY produit_id;", "SELECT produit_id, SUM(montant) FROM ventes;", "SELECT SUM(montant) FROM ventes GROUP BY montant;", "SELECT produit_id, montant FROM ventes GROUP BY SUM(montant);"),
S("Que se passe-t-il si on utilise une colonne non agregee dans le SELECT sans la mettre dans GROUP BY (en mode strict) ?", "Une erreur est levee car la colonne n'est ni agregee ni groupee", "La premiere valeur rencontree est utilisee sans erreur", "La colonne est ignoree silencieusement", "Le moteur la regroupe automatiquement"),
S("Quelle requete affiche les categories de produits ayant une moyenne de prix superieure a 50 ?", "SELECT categorie, AVG(prix) FROM produits GROUP BY categorie HAVING AVG(prix) > 50;", "SELECT categorie, AVG(prix) FROM produits WHERE AVG(prix) > 50 GROUP BY categorie;", "SELECT categorie FROM produits HAVING prix > 50;", "SELECT categorie, AVG(prix) FROM produits GROUP BY categorie WHERE AVG(prix) > 50;"),
S("Peut-on utiliser plusieurs colonnes dans une clause GROUP BY ?", "Oui, en les separant par des virgules pour creer des groupes plus fins", "Non, une seule colonne est autorisee", "Oui mais seulement avec DISTINCT", "Non, il faut utiliser plusieurs requetes UNION"),
]
ALL_MULTIPLE += [
M("Parmi ces affirmations sur GROUP BY, lesquelles sont correctes ?",
  ["GROUP BY regroupe les lignes ayant la meme valeur sur la ou les colonnes specifiees", "GROUP BY est souvent utilise avec des fonctions d'agregation comme COUNT ou SUM"],
  "GROUP BY trie automatiquement les resultats par ordre alphabetique", "GROUP BY remplace toujours la clause WHERE"),
M("Quelles requetes sont syntaxiquement et logiquement correctes pour filtrer des groupes ?",
  ["SELECT client_id, COUNT(*) FROM commandes GROUP BY client_id HAVING COUNT(*) > 5;", "SELECT categorie, SUM(stock) FROM produits GROUP BY categorie HAVING SUM(stock) < 100;"],
  "SELECT client_id, COUNT(*) FROM commandes HAVING COUNT(*) > 5;", "SELECT categorie, SUM(stock) FROM produits WHERE SUM(stock) < 100;"),
]
ALL_TF += [
TF("HAVING permet de filtrer sur le resultat d'une fonction d'agregation, contrairement a WHERE.", True),
TF("GROUP BY doit obligatoirement etre utilise avec au moins une fonction d'agregation dans le SELECT.", False),
TF("On peut regrouper des donnees sur plusieurs colonnes simultanement avec GROUP BY col1, col2.", True),
TF("La clause HAVING s'execute avant la clause WHERE dans l'ordre logique d'execution d'une requete.", False),
TF("Dans une requete avec GROUP BY, chaque colonne non agregee du SELECT doit normalement apparaitre dans GROUP BY.", True),
]

print("t04:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t04.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
