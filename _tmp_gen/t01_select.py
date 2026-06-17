# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle clause SQL permet de selectionner des colonnes dans une table ?", "SELECT", "FETCH", "GET", "PULL"),
S("Quel symbole permet de recuperer toutes les colonnes d'une table dans un SELECT ?", "*", "ALL", "ANY", "FULL"),
S("Quelle instruction affiche toutes les colonnes de la table clients ?", "SELECT * FROM clients;", "SHOW * FROM clients;", "GET * FROM clients;", "FETCH * FROM clients;"),
S("Dans SELECT nom AS n FROM clients;, que represente AS n ?", "Un alias pour la colonne nom", "Une nouvelle table", "Une condition de filtre", "Un type de donnee"),
S("Quelle syntaxe donne un alias a une table dans une requete SELECT ?", "SELECT * FROM clients AS c;", "SELECT * FROM clients ALIAS c;", "SELECT * FROM clients RENAME c;", "SELECT * FROM clients LIKE c;"),
S("Quel mot-cle SQL permet d'eliminer les doublons dans un resultat ?", "DISTINCT", "UNIQUE", "ONLY", "SINGLE"),
S("Que retourne la requete SELECT DISTINCT ville FROM clients; ?", "La liste des villes sans doublons", "Toutes les lignes de la table clients", "Le nombre de villes differentes", "La premiere ville trouvee"),
S("Quelle requete selectionne uniquement les colonnes nom et prenom de la table employes ?", "SELECT nom, prenom FROM employes;", "SELECT nom AND prenom FROM employes;", "SELECT nom + prenom FROM employes;", "SELECT (nom, prenom) FROM employes;"),
S("Quel est le role d'un alias de colonne defini avec AS dans le resultat affiche ?", "Renommer la colonne dans le resultat retourne", "Modifier la valeur stockee en base", "Supprimer la colonne d'origine", "Creer un index sur la colonne"),
S("Que calcule la requete SELECT prix * 1.2 AS prix_ttc FROM produits; ?", "Un prix TTC a partir du prix HT, sans modifier la base", "Le prix stocke en base est ecrase", "Une nouvelle colonne permanente est creee", "Les produits dont le prix depasse 1.2 sont filtres"),
S("Le mot-cle AS est-il obligatoire pour definir un alias en SQL standard ?", "Non, il est optionnel dans la plupart des SGBD", "Oui, toujours obligatoire", "Seulement pour les alias de table", "Seulement pour les alias de colonne"),
S("Quelle requete renomme la colonne resultat d'un calcul de remise en pourcent_remise ?", "SELECT remise * 100 AS pourcent_remise FROM ventes;", "SELECT remise * 100 = pourcent_remise FROM ventes;", "SELECT remise * 100 RENAME pourcent_remise FROM ventes;", "SELECT remise * 100 INTO pourcent_remise FROM ventes;"),
]
ALL_MULTIPLE += [
M("Parmi les elements suivants, lesquels peuvent suivre directement le mot-cle SELECT ?",
  ["Le caractere *", "Le nom d'une colonne", "Une expression calculee comme prix * 2"],
  "Le mot-cle FROM seul", "Le mot-cle WHERE seul"),
M("Quelles affirmations sur les alias en SQL sont correctes ?",
  ["Un alias de colonne change le nom affiche dans le resultat", "Un alias de table peut etre utilise pour raccourcir les references aux colonnes"],
  "Un alias modifie le nom reel de la colonne en base", "Un alias est obligatoire pour toute colonne selectionnee"),
M("Parmi ces requetes, lesquelles utilisent correctement DISTINCT ?",
  ["SELECT DISTINCT pays FROM clients;", "SELECT DISTINCT nom, prenom FROM clients;"],
  "SELECT nom, DISTINCT prenom FROM clients;", "DISTINCT SELECT * FROM clients;"),
]
ALL_TF += [
TF("La requete SELECT * FROM table; retourne toutes les colonnes et toutes les lignes de la table.", True),
TF("L'instruction SELECT permet de modifier les donnees d'une table.", False),
TF("Un alias defini avec AS modifie definitivement le nom de la colonne dans la base de donnees.", False),
TF("DISTINCT s'applique a l'ensemble des colonnes listees dans le SELECT, pas a une seule colonne isolee parmi plusieurs.", True),
TF("Il est possible d'utiliser un alias de table pour prefixer les noms de colonnes dans une requete.", True),
]

print("t01:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t01.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
