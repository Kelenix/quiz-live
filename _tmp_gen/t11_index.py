# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("A quoi sert principalement un index dans une base de donnees ?", "Acceler la recherche de donnees dans une table", "Stocker des donnees redondantes pour la securite", "Empecher toute modification de la table", "Compresser les donnees stockees"),
S("Quelle instruction cree un index sur la colonne email de la table clients ?", "CREATE INDEX idx_email ON clients (email);", "ADD INDEX idx_email ON clients (email);", "CREATE INDEX ON clients.email;", "INDEX clients (email);"),
S("Un index est-il automatiquement cree sur une colonne definie comme PRIMARY KEY dans la plupart des SGBD ?", "Oui, un index est generalement cree automatiquement", "Non, jamais", "Seulement si on le precise avec INDEX KEY", "Seulement pour les cles composites"),
S("Quel est l'inconvenient principal d'ajouter trop d'index sur une table ?", "Cela ralentit les operations d'ecriture (INSERT, UPDATE, DELETE)", "Cela rend les SELECT plus lents", "Cela empeche toute jointure", "Cela supprime automatiquement les contraintes existantes"),
S("Quelle structure de donnees est tres souvent utilisee en interne pour implementer un index ?", "Un arbre B (B-tree)", "Une liste chainee simple", "Une pile (stack)", "Un tableau non trie"),
S("Un index accelere-t-il les recherches realisees avec une clause WHERE sur la colonne indexee ?", "Oui, generalement de maniere significative", "Non, un index n'a aucun effet sur WHERE", "Seulement pour les requetes UPDATE", "Seulement si la table est vide"),
S("Quelle instruction supprime un index nomme idx_email ?", "DROP INDEX idx_email;", "DELETE INDEX idx_email;", "REMOVE INDEX idx_email;", "ALTER INDEX idx_email DROP;"),
S("Un index UNIQUE garantit-il l'unicite des valeurs de la colonne indexee ?", "Oui, en plus d'accelerer les recherches", "Non, un index n'a jamais d'effet sur l'unicite", "Seulement pour les cles primaires", "Seulement pour les colonnes de type texte"),
]
ALL_MULTIPLE += [
M("Parmi les affirmations suivantes sur les index, lesquelles sont correctes ?",
  ["Un index accelere generalement les lectures filtrees sur la colonne indexee", "Trop d'index peut ralentir les ecritures (INSERT, UPDATE, DELETE)"],
  "Un index supprime automatiquement les doublons de la table", "Un index est obligatoire pour executer une requete SELECT"),
M("Quelles colonnes sont de bonnes candidates pour etre indexees dans une table volumineuse ?",
  ["Une colonne souvent utilisee dans une clause WHERE", "Une colonne souvent utilisee comme cle de jointure"],
  "Une colonne booleenne avec seulement deux valeurs possibles et peu selective", "Une colonne jamais utilisee dans les requetes"),
]
ALL_TF += [
TF("Un index permet generalement d'accelerer les recherches, mais peut ralentir les insertions.", True),
TF("Creer un index modifie le resultat logique d'une requete SELECT.", False),
TF("Une cle primaire beneficie generalement d'un index automatiquement cree par le SGBD.", True),
TF("Un index UNIQUE empeche l'insertion de deux lignes ayant la meme valeur dans la colonne indexee.", True),
]

print("t11:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t11.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
