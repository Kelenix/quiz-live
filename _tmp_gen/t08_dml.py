# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle instruction permet d'ajouter une nouvelle ligne dans une table ?", "INSERT INTO", "ADD ROW", "CREATE ROW", "APPEND"),
S("Quelle syntaxe insere correctement un nouveau client nomme 'Dupont' age de 30 ans ?", "INSERT INTO clients (nom, age) VALUES ('Dupont', 30);", "INSERT clients (nom, age) = ('Dupont', 30);", "INSERT INTO clients SET nom='Dupont', age=30 VALUES;", "ADD INTO clients (nom, age) VALUES ('Dupont', 30);"),
S("Quelle instruction permet de modifier des donnees existantes dans une table ?", "UPDATE", "MODIFY", "ALTER", "CHANGE"),
S("Quelle requete met a jour le prix du produit dont l'id est 5 ?", "UPDATE produits SET prix = 19.99 WHERE id = 5;", "UPDATE produits prix = 19.99 WHERE id = 5;", "SET produits.prix = 19.99 WHERE id = 5;", "MODIFY produits SET prix = 19.99 WHERE id = 5;"),
S("Que se passe-t-il si on execute un UPDATE sans clause WHERE ?", "Toutes les lignes de la table sont modifiees", "Aucune ligne n'est modifiee par securite", "Seule la premiere ligne est modifiee", "Une erreur de syntaxe est levee systematiquement"),
S("Quelle instruction permet de supprimer des lignes d'une table ?", "DELETE FROM", "REMOVE FROM", "DROP FROM", "ERASE FROM"),
S("Quelle requete supprime uniquement les clients inactifs depuis plus de 2 ans ?", "DELETE FROM clients WHERE derniere_activite < '2024-01-01';", "DELETE clients WHERE derniere_activite < '2024-01-01';", "REMOVE FROM clients WHERE derniere_activite < '2024-01-01';", "DROP FROM clients WHERE derniere_activite < '2024-01-01';"),
S("Quelle est la consequence d'un DELETE FROM table; sans clause WHERE ?", "Toutes les lignes de la table sont supprimees, mais la structure de la table reste", "La table entiere, y compris sa structure, est supprimee", "Seule la derniere ligne inseree est supprimee", "Rien ne se passe sans confirmation explicite"),
S("Quelle instruction insere plusieurs lignes en une seule requete ?", "INSERT INTO table (col1, col2) VALUES (1, 'a'), (2, 'b');", "INSERT INTO table (col1, col2) VALUES (1, 'a') AND (2, 'b');", "INSERT MULTIPLE INTO table VALUES (1, 'a'), (2, 'b');", "INSERT INTO table VALUES (1, 'a') OR (2, 'b');"),
S("Quelle requete UPDATE augmente de 10% le prix de tous les produits de la categorie 'Electronique' ?", "UPDATE produits SET prix = prix * 1.1 WHERE categorie = 'Electronique';", "UPDATE produits SET prix += 10 WHERE categorie = 'Electronique';", "UPDATE produits prix = prix * 1.1 WHERE categorie = 'Electronique';", "SET produits prix = prix * 1.1 WHERE categorie = 'Electronique';"),
S("Quelle commande SQL est generalement plus rapide pour vider entierement une table mais n'est pas du DML pur ?", "TRUNCATE TABLE", "DELETE FROM", "DROP COLUMN", "CLEAR TABLE"),
]
ALL_MULTIPLE += [
M("Parmi les instructions suivantes, lesquelles font partie du langage de manipulation de donnees (DML) ?",
  ["INSERT", "UPDATE", "DELETE"], "CREATE TABLE", "DROP TABLE"),
M("Quelles affirmations sur DELETE FROM sont correctes ?",
  ["Sans clause WHERE, DELETE supprime toutes les lignes de la table", "DELETE conserve la structure de la table apres suppression des donnees"],
  "DELETE supprime toujours la table elle-meme", "DELETE necessite obligatoirement une clause WHERE pour s'executer"),
M("Quelles requetes UPDATE sont syntaxiquement valides ?",
  ["UPDATE clients SET email = 'nouveau@mail.com' WHERE id = 1;", "UPDATE produits SET stock = stock - 1 WHERE id = 3;"],
  "UPDATE clients email = 'nouveau@mail.com' WHERE id = 1;", "SET clients email = 'nouveau@mail.com';"),
]
ALL_TF += [
TF("L'instruction UPDATE sans clause WHERE modifie toutes les lignes de la table cible.", True),
TF("DELETE FROM table; sans WHERE supprime la table elle-meme de la base de donnees.", False),
TF("INSERT INTO permet d'inserer plusieurs lignes en une seule instruction en separant les groupes de valeurs par des virgules.", True),
TF("UPDATE et DELETE font partie du langage de definition de donnees (DDL).", False),
TF("Il est possible de mettre a jour une colonne en se basant sur sa propre valeur actuelle, par exemple SET stock = stock - 1.", True),
]

print("t08:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t08.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
