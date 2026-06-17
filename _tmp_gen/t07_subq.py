# -*- coding: utf-8 -*-
import pickle, sys
sys.path.insert(0, "/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen")
from helpers import S, M, TF

ALL_SINGLE = []
ALL_MULTIPLE = []
ALL_TF = []

ALL_SINGLE += [
S("Qu'est-ce qu'une sous-requete en SQL ?", "Une requete SELECT imbriquee a l'interieur d'une autre requete", "Une requete executee sur un sous-ensemble de colonnes uniquement", "Une vue materialisee automatique", "Un index secondaire"),
S("Quelle requete utilise une sous-requete dans la clause WHERE pour trouver les produits plus chers que la moyenne ?", "SELECT * FROM produits WHERE prix > (SELECT AVG(prix) FROM produits);", "SELECT * FROM produits WHERE prix > AVG(prix);", "SELECT * FROM produits HAVING prix > AVG(prix);", "SELECT * FROM produits WHERE prix > ALL(prix);"),
S("Quel operateur teste si une sous-requete retourne au moins une ligne ?", "EXISTS", "IN", "ANY", "ALL"),
S("Quelle requete trouve les clients ayant passe au moins une commande, via une sous-requete avec IN ?", "SELECT * FROM clients WHERE id IN (SELECT client_id FROM commandes);", "SELECT * FROM clients WHERE id = (SELECT client_id FROM commandes);", "SELECT * FROM clients WHERE id EXISTS commandes;", "SELECT * FROM clients JOIN (SELECT client_id) ON commandes;"),
S("Qu'appelle-t-on une sous-requete utilisee directement dans la clause FROM ?", "Une table derivee (subquery in FROM)", "Une vue permanente", "Un index", "Une procedure stockee"),
S("Quelle est la principale contrainte d'une sous-requete utilisee dans la clause FROM ?", "Elle doit obligatoirement recevoir un alias", "Elle ne peut contenir aucune clause WHERE", "Elle doit retourner une seule ligne", "Elle ne peut pas contenir de jointure"),
S("Quelle requete utilise une sous-requete correlee pour comparer chaque employe a la moyenne de son propre departement ?", "SELECT * FROM employes e WHERE salaire > (SELECT AVG(salaire) FROM employes WHERE departement = e.departement);", "SELECT * FROM employes WHERE salaire > (SELECT AVG(salaire) FROM employes);", "SELECT * FROM employes GROUP BY departement HAVING salaire > AVG(salaire);", "SELECT * FROM employes e JOIN employes ON salaire > AVG(salaire);"),
S("Une sous-requete placee directement dans la liste SELECT doit en general retourner combien de valeurs ?", "Une seule valeur (scalaire)", "Plusieurs lignes obligatoirement", "Une table entiere", "Aucune valeur"),
S("Quel operateur permet de comparer une valeur a TOUTES les valeurs retournees par une sous-requete ?", "ALL", "ANY", "SOME", "EXISTS"),
S("Quelle est la difference entre l'operateur ANY et l'operateur ALL utilises avec une sous-requete ?", "ANY est vrai si la condition est vraie pour au moins une valeur, ALL exige qu'elle soit vraie pour toutes", "ANY et ALL sont rigoureusement equivalents", "ALL ne fonctionne qu'avec des sous-requetes vides", "ANY ne peut etre utilise qu'avec EXISTS"),
S("Que retourne NOT EXISTS (sous-requete) si la sous-requete ne renvoie aucune ligne ?", "TRUE (vrai)", "FALSE (faux)", "NULL", "Une erreur de syntaxe"),
]
ALL_MULTIPLE += [
M("Parmi les emplacements suivants, lesquels peuvent contenir une sous-requete en SQL ?",
  ["La clause WHERE", "La clause FROM", "La liste de colonnes du SELECT"],
  "Le nom de la table cible d'un DROP TABLE", "Le nom d'une colonne dans CREATE TABLE"),
M("Quelles affirmations sur les sous-requetes correlees sont vraies ?",
  ["Elles font reference a une colonne de la requete externe", "Elles sont generalement reevaluees pour chaque ligne de la requete externe"],
  "Elles ne peuvent jamais utiliser de fonction d'agregation", "Elles remplacent obligatoirement toute jointure"),
]
ALL_TF += [
TF("Une sous-requete peut etre placee dans la clause WHERE d'une requete principale.", True),
TF("EXISTS retourne vrai si la sous-requete associee renvoie au moins une ligne, quel que soit son contenu.", True),
TF("Une sous-requete utilisee dans la clause FROM doit obligatoirement porter un alias dans la plupart des SGBD.", True),
TF("Une sous-requete correlee ne fait jamais reference aux colonnes de la requete externe.", False),
TF("L'operateur IN avec une sous-requete permet de tester l'appartenance a un ensemble de valeurs retournees.", True),
]

print("t07:", len(ALL_SINGLE), len(ALL_MULTIPLE), len(ALL_TF))
with open("/sessions/clever-dreamy-fermi/mnt/quiz-live/_tmp_gen/bank_t07.pkl", "wb") as f:
    pickle.dump((ALL_SINGLE, ALL_MULTIPLE, ALL_TF), f)
