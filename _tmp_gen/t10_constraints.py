# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Quelle contrainte garantit qu'une colonne identifie de maniere unique chaque ligne d'une table ?", "PRIMARY KEY", "UNIQUE", "NOT NULL", "DEFAULT"),
S("Quelle contrainte etablit un lien entre une colonne d'une table et la cle primaire d'une autre table ?", "FOREIGN KEY", "PRIMARY KEY", "CHECK", "UNIQUE"),
S("Quelle contrainte interdit toute valeur nulle dans une colonne ?", "NOT NULL", "UNIQUE", "CHECK", "PRIMARY KEY"),
S("Quelle contrainte garantit qu'aucune valeur ne se repete dans une colonne, sans en faire la cle primaire ?", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY", "NOT NULL"),
S("Quelle contrainte permet de definir une regle de validation personnalisee, comme age >= 18 ?", "CHECK", "UNIQUE", "DEFAULT", "FOREIGN KEY"),
S("Quelle contrainte attribue automatiquement une valeur a une colonne si aucune n'est fournie a l'insertion ?", "DEFAULT", "CHECK", "UNIQUE", "NOT NULL"),
S("Une table peut-elle avoir plusieurs colonnes UNIQUE en plus de sa cle primaire ?", "Oui, plusieurs contraintes UNIQUE peuvent coexister sur des colonnes differentes", "Non, une seule contrainte UNIQUE est autorisee par table", "Non, UNIQUE et PRIMARY KEY sont mutuellement exclusifs", "Oui, mais uniquement sur la cle primaire elle-meme"),
S("Que se passe-t-il si on tente d'inserer une valeur dupliquee dans une colonne contrainte par PRIMARY KEY ?", "Une erreur de violation de contrainte est levee", "La nouvelle ligne remplace silencieusement l'ancienne", "La valeur est automatiquement modifiee pour etre unique", "Aucune erreur, les deux lignes coexistent"),
S("Quelle instruction definit une cle etrangere reliant commandes.client_id a clients.id ?", "FOREIGN KEY (client_id) REFERENCES clients(id)", "FOREIGN KEY (client_id) LINKS clients(id)", "REFERENCES clients(id) AS client_id", "PRIMARY KEY (client_id) REFERENCES clients(id)"),
S("Une cle primaire peut-elle accepter la valeur NULL ?", "Non, une cle primaire est implicitement NOT NULL", "Oui, NULL est toujours autorise une fois", "Oui, sans aucune restriction", "Cela depend uniquement du type de donnee choisi"),
S("Qu'est-ce qu'une cle primaire composite ?", "Une cle primaire formee de plusieurs colonnes combinees", "Une cle primaire qui change automatiquement de valeur", "Une cle etrangere dupliquee", "Un index secondaire sur une seule colonne"),
S("Quelle contrainte empeche de supprimer un client tant qu'il a des commandes liees, par defaut dans de nombreux SGBD ?", "FOREIGN KEY (sans action explicite de cascade)", "UNIQUE", "CHECK", "DEFAULT"),
]
ALL_MULTIPLE += [
M("Parmi les contraintes suivantes, lesquelles assurent une forme d'unicite des valeurs dans une colonne ?",
  ["PRIMARY KEY", "UNIQUE"], "NOT NULL", "DEFAULT"),
M("Quelles affirmations sur la contrainte FOREIGN KEY sont correctes ?",
  ["Elle garantit l'integrite referentielle entre deux tables", "Elle reference generalement la cle primaire d'une autre table"],
  "Elle interdit toute valeur NULL dans la colonne", "Elle remplace obligatoirement la cle primaire de la table"),
M("Quelles contraintes peuvent etre appliquees a une seule colonne lors de sa definition dans CREATE TABLE ?",
  ["NOT NULL", "UNIQUE", "CHECK"], "GROUP BY", "ORDER BY"),
]
ALL_TF += [
TF("Une cle primaire (PRIMARY KEY) interdit implicitement les valeurs NULL.", True),
TF("Une table peut avoir plusieurs cles primaires distinctes.", False),
TF("La contrainte CHECK permet de valider qu'une valeur respecte une condition logique avant insertion.", True),
TF("La contrainte FOREIGN KEY garantit qu'une valeur existe dans la table referencee.", True),
TF("DEFAULT et NOT NULL sont des synonymes strictement interchangeables.", False),
]

print("t10:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t10.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
