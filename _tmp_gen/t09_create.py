# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle instruction permet de creer une nouvelle table dans une base de donnees ?", "CREATE TABLE", "NEW TABLE", "ADD TABLE", "MAKE TABLE"),
S("Quel type de donnee est adapte pour stocker un entier en SQL ?", "INTEGER", "VARCHAR", "BOOLEAN", "TEXT"),
S("Quel type de donnee convient pour stocker une chaine de caracteres de longueur variable avec une limite maximale ?", "VARCHAR(n)", "INTEGER", "DATE", "BOOLEAN"),
S("Quel type de donnee est utilise pour stocker une date sans information d'heure ?", "DATE", "TIME", "VARCHAR", "INTEGER"),
S("Quel type de donnee convient pour stocker un nombre decimal avec une precision exacte, comme un montant financier ?", "DECIMAL ou NUMERIC", "INTEGER", "BOOLEAN", "TEXT"),
S("Quel type de donnee stocke uniquement les valeurs vrai ou faux ?", "BOOLEAN", "VARCHAR", "INTEGER", "DATE"),
S("Quelle instruction cree une table clients avec un identifiant entier et un nom en texte ?", "CREATE TABLE clients (id INTEGER, nom VARCHAR(100));", "CREATE clients (id INTEGER, nom VARCHAR(100));", "TABLE clients (id INTEGER, nom VARCHAR(100));", "NEW TABLE clients id INTEGER, nom VARCHAR(100);"),
S("Quelle instruction supprime entierement une table de la base de donnees, structure incluse ?", "DROP TABLE", "DELETE TABLE", "REMOVE TABLE", "TRUNCATE TABLE"),
S("Quelle est la difference entre TRUNCATE TABLE et DELETE FROM sans WHERE ?", "TRUNCATE est generalement plus rapide et reinitialise certains compteurs internes", "TRUNCATE supprime la table elle-meme alors que DELETE non", "DELETE est toujours plus rapide que TRUNCATE", "Il n'existe aucune difference entre les deux"),
S("Quel type de donnee convient pour stocker un texte long sans limite de taille fixe, comme un commentaire ?", "TEXT", "INTEGER", "BOOLEAN", "DATE"),
S("Quelle instruction permet de modifier la structure d'une table existante, par exemple ajouter une colonne ?", "ALTER TABLE", "MODIFY TABLE", "UPDATE TABLE", "CHANGE TABLE"),
S("Quelle instruction ajoute une colonne email a la table clients ?", "ALTER TABLE clients ADD COLUMN email VARCHAR(255);", "ALTER TABLE clients NEW COLUMN email VARCHAR(255);", "UPDATE clients ADD COLUMN email VARCHAR(255);", "ALTER clients ADD email VARCHAR(255);"),
S("Quelle instruction supprime une colonne age de la table clients ?", "ALTER TABLE clients DROP COLUMN age;", "ALTER TABLE clients REMOVE COLUMN age;", "ALTER TABLE clients DELETE COLUMN age;", "DROP COLUMN age FROM clients;"),
]
ALL_MULTIPLE += [
M("Parmi les types suivants, lesquels sont des types de donnees couramment disponibles en SQL ?",
  ["INTEGER", "VARCHAR", "DATE"], "TABLE", "SELECT"),
M("Quelles operations peuvent etre realisees avec ALTER TABLE ?",
  ["Ajouter une colonne", "Supprimer une colonne", "Renommer une colonne selon le SGBD"],
  "Supprimer toutes les lignes de la table", "Inserer une nouvelle ligne de donnees"),
]
ALL_TF += [
TF("DROP TABLE supprime a la fois les donnees et la structure (definition) de la table.", True),
TF("ALTER TABLE permet d'ajouter ou de supprimer des colonnes sur une table existante.", True),
TF("VARCHAR(n) permet de stocker des chaines de caracteres jusqu'a une longueur maximale de n caracteres.", True),
TF("TRUNCATE TABLE et DROP TABLE produisent exactement le meme resultat sur la structure de la table.", False),
TF("Le type BOOLEAN ne peut stocker que deux valeurs possibles : vrai ou faux (hors NULL).", True),
]

print("t09:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t09.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
