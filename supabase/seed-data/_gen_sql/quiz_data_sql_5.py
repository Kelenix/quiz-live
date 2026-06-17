from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "Procédures stockées : notions de base",
        "Comprendre l'utilité des procédures stockées dans une base de données.",
        [
            S(
                "Qu'est-ce qu'une procédure stockée ?",
                [
                    "Un ensemble d'instructions SQL nommé et stocké dans la base, exécutable à la demande",
                    "Une table temporaire créée automatiquement",
                    "Un type d'index particulier",
                    "Une vue contenant uniquement des agrégations",
                ],
            ),
            Sx(
                "Quel est un avantage typique des procédures stockées ?",
                [
                    "Centraliser une logique métier réutilisable côté base de données",
                    "Remplacer totalement le besoin de tables",
                    "Empêcher toute connexion d'application à la base",
                    "Garantir automatiquement l'absence de bugs",
                ],
                0,
            ),
            S(
                "Quelle instruction permet généralement d'exécuter une procédure stockée nommée maj_stock ?",
                ["CALL maj_stock();", "RUN maj_stock;", "EXECUTE FROM maj_stock;", "START maj_stock();"],
            ),
            M(
                "Quelles affirmations sur les procédures stockées sont correctes ?",
                [
                    "Elles peuvent accepter des paramètres en entrée",
                    "Elles peuvent contenir plusieurs instructions SQL combinées",
                ],
                ["Elles ne peuvent jamais contenir de logique conditionnelle", "Elles remplacent obligatoirement toutes les requêtes SELECT de l'application"],
            ),
            T("Une procédure stockée peut être appelée plusieurs fois avec des paramètres différents.", True),
            T("Une procédure stockée ne peut contenir qu'une seule instruction SQL au maximum.", False),
        ],
    ),
    quiz(
        "Triggers : notions de base",
        "Déclencher des actions automatiques en réaction à des événements sur une table.",
        [
            S(
                "Qu'est-ce qu'un trigger (déclencheur) en base de données ?",
                [
                    "Une action automatique exécutée en réponse à un événement comme INSERT, UPDATE ou DELETE",
                    "Une colonne calculée automatiquement",
                    "Un type d'index spécial pour les dates",
                    "Une procédure exécutée uniquement manuellement",
                ],
            ),
            Sx(
                "Quel moment d'exécution un trigger BEFORE INSERT permet-il de cibler ?",
                [
                    "Avant que la ligne ne soit effectivement insérée dans la table",
                    "Après que la transaction entière soit validée par COMMIT",
                    "Uniquement lors de la suppression de la table",
                    "Seulement une fois par jour, à heure fixe",
                ],
                0,
            ),
            S(
                "Quel cas d'usage est typique pour un trigger ?",
                [
                    "Mettre à jour automatiquement un historique de modifications (audit)",
                    "Remplacer entièrement les clés étrangères",
                    "Créer de nouvelles bases de données",
                    "Indexer automatiquement toutes les colonnes",
                ],
            ),
            M(
                "Quelles affirmations sur les triggers sont vraies ?",
                [
                    "Un trigger peut se déclencher avant (BEFORE) ou après (AFTER) un événement",
                    "Un trigger est associé à une table et à un type d'événement précis",
                ],
                ["Un trigger doit être appelé manuellement par l'utilisateur", "Un trigger ne peut jamais réagir à un UPDATE"],
            ),
            T("Un trigger peut potentiellement déclencher en cascade d'autres modifications de données.", True),
            T("Les triggers doivent obligatoirement être exécutés manuellement après chaque requête.", False),
        ],
    ),
    quiz(
        "Révision : SELECT, WHERE et ORDER BY combinés",
        "Consolider les bases du filtrage et du tri en SQL.",
        [
            S(
                "Quelle requête retourne les noms des clients de plus de 30 ans triés par âge décroissant ?",
                [
                    "SELECT nom FROM clients WHERE age > 30 ORDER BY age DESC;",
                    "SELECT nom FROM clients ORDER BY age DESC WHERE age > 30;",
                    "SELECT nom WHERE age > 30 FROM clients ORDER BY age;",
                    "SELECT nom FROM clients WHERE age > 30 SORT age DESC;",
                ],
            ),
            Sx(
                "Quelle clause permet de combiner plusieurs conditions de filtre avec une logique 'et' ?",
                ["AND", "OR", "PLUS", "WITH"],
                0,
            ),
            S(
                "Quelle requête sélectionne les produits dont le prix est entre 20 et 100, triés par nom ?",
                [
                    "SELECT * FROM produits WHERE prix BETWEEN 20 AND 100 ORDER BY nom;",
                    "SELECT * FROM produits WHERE prix BETWEEN 20, 100 SORT nom;",
                    "SELECT * FROM produits ORDER BY nom WHERE prix BETWEEN 20 AND 100;",
                    "SELECT * FROM produits BETWEEN prix 20 AND 100 ORDER BY nom;",
                ],
            ),
            M(
                "Quelles requêtes combinent correctement WHERE et ORDER BY ?",
                [
                    "SELECT * FROM clients WHERE ville = 'Lyon' ORDER BY nom;",
                    "SELECT * FROM produits WHERE prix > 10 ORDER BY prix DESC;",
                ],
                ["SELECT * FROM clients ORDER BY nom WHERE ville = 'Lyon';", "SELECT * FROM produits ORDER prix WHERE > 10;"],
            ),
            T("L'opérateur OR permet de filtrer des lignes satisfaisant au moins une des conditions données.", True),
            T("La clause WHERE ne peut contenir qu'une seule condition au maximum.", False),
        ],
    ),
    quiz(
        "Révision : agrégation et GROUP BY avancés",
        "Approfondir les requêtes d'agrégation avec plusieurs colonnes.",
        [
            S(
                "Quelle requête calcule le nombre de commandes et le montant total par client ?",
                [
                    "SELECT client_id, COUNT(*), SUM(montant) FROM commandes GROUP BY client_id;",
                    "SELECT client_id, COUNT(*), SUM(montant) FROM commandes ORDER BY client_id;",
                    "SELECT COUNT(*), SUM(montant) FROM commandes GROUP client_id;",
                    "SELECT client_id FROM commandes GROUP BY COUNT(*), SUM(montant);",
                ],
            ),
            Sx(
                "Quelle requête trouve les clients ayant passé plus de 3 commandes ET dépensé plus de 500 en tout ?",
                [
                    "SELECT client_id FROM commandes GROUP BY client_id HAVING COUNT(*) > 3 AND SUM(montant) > 500;",
                    "SELECT client_id FROM commandes WHERE COUNT(*) > 3 AND SUM(montant) > 500;",
                    "SELECT client_id FROM commandes GROUP BY client_id WHERE COUNT(*) > 3;",
                    "SELECT client_id FROM commandes HAVING COUNT(*) > 3 GROUP BY client_id AND SUM(montant) > 500;",
                ],
                0,
            ),
            S(
                "Quelle requête regroupe les ventes par année et par mois ?",
                [
                    "SELECT EXTRACT(YEAR FROM date_vente), EXTRACT(MONTH FROM date_vente), SUM(montant) FROM ventes GROUP BY 1, 2;",
                    "SELECT SUM(montant) FROM ventes GROUP BY date_vente;",
                    "SELECT date_vente, SUM(montant) FROM ventes ORDER BY YEAR, MONTH;",
                    "SELECT SUM(montant) FROM ventes WHERE GROUP BY YEAR, MONTH;",
                ],
            ),
            M(
                "Quelles affirmations sur le GROUP BY multi-colonnes sont vraies ?",
                [
                    "Chaque combinaison unique des colonnes groupées forme un groupe distinct",
                    "On peut utiliser plusieurs fonctions d'agrégation différentes dans le même SELECT",
                ],
                ["GROUP BY ne peut s'appliquer qu'à une seule colonne par requête", "HAVING ne peut jamais combiner plusieurs conditions"],
            ),
            T("On peut utiliser HAVING avec plusieurs conditions combinées par AND ou OR.", True),
            T("GROUP BY sur plusieurs colonnes ne peut produire qu'un seul groupe au final.", False),
        ],
    ),
    quiz(
        "Révision : jointures et valeurs manquantes",
        "Combiner LEFT JOIN et la gestion des NULL pour des analyses fines.",
        [
            S(
                "Quelle requête trouve les clients n'ayant jamais passé de commande ?",
                [
                    "SELECT c.* FROM clients c LEFT JOIN commandes co ON c.id = co.client_id WHERE co.id IS NULL;",
                    "SELECT c.* FROM clients c INNER JOIN commandes co ON c.id = co.client_id WHERE co.id IS NULL;",
                    "SELECT c.* FROM clients c WHERE c.id NOT EXISTS commandes;",
                    "SELECT c.* FROM clients c RIGHT JOIN commandes co WHERE co.id IS NULL;",
                ],
            ),
            Sx(
                "Pourquoi utilise-t-on LEFT JOIN plutôt que INNER JOIN pour trouver les clients sans commande ?",
                [
                    "Parce que LEFT JOIN conserve les clients même sans correspondance, ce qui permet de filtrer ensuite sur NULL",
                    "Parce que INNER JOIN est plus rapide dans ce cas précis",
                    "Parce que LEFT JOIN trie automatiquement les résultats",
                    "Il n'y a aucune raison, les deux jointures donnent le même résultat ici",
                ],
                0,
            ),
            S(
                "Quelle requête combine LEFT JOIN et COALESCE pour afficher 0 si un client n'a aucune commande ?",
                [
                    "SELECT c.nom, COALESCE(COUNT(co.id), 0) FROM clients c LEFT JOIN commandes co ON c.id = co.client_id GROUP BY c.nom;",
                    "SELECT c.nom, COUNT(co.id) FROM clients c INNER JOIN commandes co GROUP BY c.nom;",
                    "SELECT c.nom, COALESCE(co.id, 0) FROM clients c;",
                    "SELECT c.nom FROM clients c WHERE COUNT(co.id) = 0;",
                ],
            ),
            M(
                "Quelles affirmations sur LEFT JOIN et NULL sont correctes ?",
                [
                    "Après un LEFT JOIN, les colonnes de la table de droite sans correspondance valent NULL",
                    "IS NULL est l'opérateur correct pour tester une valeur NULL, pas '= NULL'",
                ],
                ["LEFT JOIN supprime automatiquement les lignes sans correspondance", "NULL est équivalent à 0 dans toutes les comparaisons"],
            ),
            T("COUNT(co.id) ignore les lignes où co.id est NULL après un LEFT JOIN sans correspondance.", True),
            T("Un LEFT JOIN transforme automatiquement les valeurs NULL en chaînes vides.", False),
        ],
    ),
    quiz(
        "Révision : sous-requêtes et opérateurs de comparaison",
        "Utiliser ANY, ALL et des sous-requêtes scalaires.",
        [
            S(
                "Quelle requête trouve les produits plus chers que TOUS les produits de la catégorie 'Basique' ?",
                [
                    "SELECT * FROM produits WHERE prix > ALL (SELECT prix FROM produits WHERE categorie = 'Basique');",
                    "SELECT * FROM produits WHERE prix > ANY (SELECT prix FROM produits WHERE categorie = 'Basique');",
                    "SELECT * FROM produits WHERE prix > (SELECT categorie FROM produits);",
                    "SELECT * FROM produits WHERE prix = ALL categorie;",
                ],
            ),
            Sx(
                "Que signifie `prix > ANY (sous-requête)` ?",
                [
                    "Le prix est supérieur à au moins une des valeurs retournées par la sous-requête",
                    "Le prix est supérieur à toutes les valeurs retournées par la sous-requête",
                    "Le prix doit être identique à une des valeurs de la sous-requête",
                    "ANY n'a aucun effet particulier sur la comparaison",
                ],
                0,
            ),
            S(
                "Quelle requête utilise une sous-requête scalaire (qui retourne une seule valeur) dans le SELECT ?",
                [
                    "SELECT nom, (SELECT AVG(prix) FROM produits) AS prix_moyen_global FROM produits;",
                    "SELECT nom, AVG(prix) FROM produits GROUP BY nom;",
                    "SELECT nom FROM produits WHERE prix IN (SELECT prix);",
                    "SELECT nom, ALL(prix) FROM produits;",
                ],
            ),
            M(
                "Quelles affirmations sur ANY et ALL sont vraies ?",
                [
                    "ALL exige que la condition soit vraie pour toutes les valeurs de la sous-requête",
                    "ANY exige que la condition soit vraie pour au moins une valeur de la sous-requête",
                ],
                ["ANY et ALL sont rigoureusement identiques dans tous les cas", "ALL ne peut être utilisé qu'avec des chaînes de texte"],
            ),
            T("Une sous-requête scalaire doit retourner exactement une seule valeur (une ligne, une colonne).", True),
            T("ALL et ANY ne peuvent jamais être combinés avec les opérateurs de comparaison comme > ou <.", False),
        ],
    ),
    quiz(
        "Révision : INSERT, UPDATE, DELETE avec sous-requêtes",
        "Combiner les instructions de modification de données avec des sous-requêtes.",
        [
            S(
                "Quelle requête supprime les commandes des clients inactifs (table clients, colonne statut) ?",
                [
                    "DELETE FROM commandes WHERE client_id IN (SELECT id FROM clients WHERE statut = 'inactif');",
                    "DELETE FROM commandes WHERE client_id = (SELECT statut FROM clients);",
                    "DELETE commandes, clients WHERE statut = 'inactif';",
                    "DELETE FROM commandes WHERE statut = 'inactif';",
                ],
            ),
            Sx(
                "Quelle requête met à jour le statut des clients ayant dépensé plus de 1000 en commandes cumulées ?",
                [
                    "UPDATE clients SET statut = 'VIP' WHERE id IN (SELECT client_id FROM commandes GROUP BY client_id HAVING SUM(montant) > 1000);",
                    "UPDATE clients SET statut = 'VIP' WHERE SUM(montant) > 1000;",
                    "UPDATE clients SET statut = 'VIP' HAVING SUM(montant) > 1000;",
                    "UPDATE clients SET statut = 'VIP' GROUP BY client_id HAVING SUM(montant) > 1000;",
                ],
                0,
            ),
            S(
                "Quelle requête insère dans archives_clients tous les clients inactifs depuis plus de 2 ans ?",
                [
                    "INSERT INTO archives_clients SELECT * FROM clients WHERE derniere_activite < '2024-01-01';",
                    "INSERT archives_clients VALUES (SELECT * FROM clients);",
                    "INSERT INTO archives_clients (clients) WHERE derniere_activite < '2024-01-01';",
                    "COPY clients TO archives_clients WHERE derniere_activite < '2024-01-01';",
                ],
            ),
            M(
                "Quelles affirmations sur les sous-requêtes dans INSERT/UPDATE/DELETE sont correctes ?",
                [
                    "Une sous-requête peut être utilisée dans la clause WHERE d'un UPDATE ou DELETE",
                    "INSERT INTO ... SELECT permet d'insérer le résultat d'une requête",
                ],
                ["Les sous-requêtes sont interdites dans les instructions DELETE", "UPDATE ne peut jamais utiliser IN avec une sous-requête"],
            ),
            T("Utiliser une sous-requête dans un DELETE permet de cibler précisément les lignes à supprimer selon une condition complexe.", True),
            T("Une sous-requête utilisée dans une clause WHERE d'un UPDATE doit obligatoirement modifier la table cible elle-même sans jamais en référencer une autre.", False),
        ],
    ),
    quiz(
        "Révision : contraintes et intégrité des données",
        "Synthèse sur les contraintes garantissant la qualité des données.",
        [
            S(
                "Quelle contrainte empêche l'insertion d'un client_id inexistant dans la table commandes ?",
                ["FOREIGN KEY", "UNIQUE", "DEFAULT", "CHECK uniquement"],
            ),
            Sx(
                "Quelle combinaison de contraintes est typique pour une colonne email dans une table utilisateurs ?",
                [
                    "NOT NULL et UNIQUE",
                    "DEFAULT et CHECK uniquement",
                    "PRIMARY KEY et FOREIGN KEY combinées obligatoirement",
                    "Aucune contrainte n'est jamais nécessaire pour un email",
                ],
                0,
            ),
            S(
                "Quelle contrainte garantit qu'une colonne quantite ne contient jamais de valeur négative ?",
                ["CHECK (quantite >= 0)", "UNIQUE (quantite)", "DEFAULT (quantite >= 0)", "FOREIGN KEY (quantite)"],
            ),
            M(
                "Quelles affirmations sur les contraintes d'intégrité sont vraies ?",
                [
                    "Les contraintes permettent de rejeter automatiquement des données invalides à l'insertion",
                    "Une même colonne peut combiner plusieurs contraintes (ex: NOT NULL et UNIQUE)",
                ],
                ["Les contraintes ralentissent obligatoirement toutes les lectures sans exception", "Une contrainte CHECK ne peut jamais comparer deux colonnes entre elles"],
            ),
            T("Les contraintes d'intégrité aident à garantir la cohérence des données stockées dans la base.", True),
            T("Une contrainte FOREIGN KEY interdit toute valeur NULL dans la colonne concernée, sans exception possible.", False),
        ],
    ),
    quiz(
        "Synthèse : DISTINCT, alias et expressions calculées",
        "Combiner plusieurs notions de base dans une même requête de synthèse.",
        [
            S(
                "Quelle requête affiche les catégories distinctes avec le nombre de produits par catégorie ?",
                [
                    "SELECT categorie, COUNT(*) FROM produits GROUP BY categorie;",
                    "SELECT DISTINCT categorie, COUNT(*) FROM produits;",
                    "SELECT categorie, COUNT(DISTINCT *) FROM produits;",
                    "SELECT categorie FROM produits DISTINCT GROUP BY categorie;",
                ],
            ),
            Sx(
                "Que fait `COUNT(DISTINCT client_id)` dans une requête sur la table commandes ?",
                [
                    "Compte le nombre de clients distincts ayant passé au moins une commande",
                    "Compte le nombre total de commandes sans exception",
                    "Compte uniquement les clients ayant passé plus d'une commande",
                    "Retourne la liste des client_id distincts, pas un nombre",
                ],
                0,
            ),
            S(
                "Quelle requête calcule le prix TTC et lui donne un alias clair ?",
                [
                    "SELECT nom, prix * 1.2 AS prix_ttc FROM produits;",
                    "SELECT nom, prix * 1.2 prix_ttc = FROM produits;",
                    "SELECT nom, (prix * 1.2) NAME prix_ttc FROM produits;",
                    "SELECT nom, prix_ttc AS prix * 1.2 FROM produits;",
                ],
            ),
            M(
                "Quelles affirmations sur DISTINCT combiné à COUNT sont vraies ?",
                [
                    "COUNT(DISTINCT colonne) élimine les doublons avant de compter",
                    "On peut combiner COUNT(DISTINCT colonne) avec GROUP BY",
                ],
                ["COUNT(DISTINCT colonne) compte toujours le même nombre que COUNT(colonne)", "DISTINCT ne peut jamais être utilisé à l'intérieur d'une fonction d'agrégation"],
            ),
            T("Un alias défini avec AS rend une requête plus lisible, notamment pour des colonnes calculées.", True),
            T("COUNT(DISTINCT colonne) et COUNT(colonne) retournent systématiquement le même résultat.", False),
        ],
    ),
    quiz(
        "Synthèse : CASE WHEN et catégorisation de données",
        "Construire des rapports avec des catégories calculées via CASE.",
        [
            S(
                "Quelle requête classe les commandes en 'Petite', 'Moyenne' ou 'Grande' selon leur montant ?",
                [
                    "SELECT id, CASE WHEN montant < 50 THEN 'Petite' WHEN montant < 200 THEN 'Moyenne' ELSE 'Grande' END FROM commandes;",
                    "SELECT id, IF montant < 50 'Petite' ELSEIF montant < 200 'Moyenne' FROM commandes;",
                    "SELECT id, CASE montant < 50 'Petite' < 200 'Moyenne' FROM commandes;",
                    "SELECT id, CATEGORY(montant) FROM commandes;",
                ],
            ),
            Sx(
                "Peut-on utiliser CASE WHEN à l'intérieur d'une fonction d'agrégation comme SUM() ?",
                [
                    "Oui, c'est une technique courante pour des totaux conditionnels",
                    "Non, CASE WHEN est interdit dans toute fonction d'agrégation",
                    "Non, cela génère systématiquement une erreur de syntaxe",
                    "Oui, mais seulement avec COUNT(), jamais avec SUM()",
                ],
                0,
            ),
            S(
                "Quelle requête compte séparément les commandes 'payées' et 'en attente' en une seule ligne de résultat ?",
                [
                    "SELECT SUM(CASE WHEN statut = 'payee' THEN 1 ELSE 0 END) AS payees, SUM(CASE WHEN statut = 'attente' THEN 1 ELSE 0 END) AS attente FROM commandes;",
                    "SELECT COUNT(statut = 'payee'), COUNT(statut = 'attente') FROM commandes;",
                    "SELECT statut, COUNT(*) FROM commandes WHERE CASE statut;",
                    "SELECT CASE COUNT(*) WHEN 'payee' THEN statut FROM commandes;",
                ],
            ),
            M(
                "Quelles affirmations sur CASE WHEN combiné à l'agrégation sont vraies ?",
                [
                    "On peut créer des colonnes de comptage conditionnel avec SUM(CASE WHEN ... THEN 1 ELSE 0 END)",
                    "CASE WHEN peut être utilisé dans GROUP BY pour créer des catégories personnalisées",
                ],
                ["CASE WHEN ne peut produire que des valeurs numériques", "Une expression CASE ne peut contenir qu'une seule condition WHEN"],
            ),
            T("CASE WHEN permet de transformer une analyse en plusieurs colonnes de synthèse dans un même SELECT.", True),
            T("CASE WHEN doit obligatoirement être utilisé avec GROUP BY pour fonctionner.", False),
        ],
    ),
    quiz(
        "Synthèse : fonctions de fenêtrage avancées",
        "Comparer ROW_NUMBER, RANK, DENSE_RANK et LAG/LEAD.",
        [
            S(
                "Quelle fonction de fenêtrage permet d'accéder à la valeur de la ligne précédente selon un ordre donné ?",
                ["LAG()", "RANK()", "ROW_NUMBER()", "PARTITION()"],
            ),
            Sx(
                "Quelle fonction de fenêtrage permet d'accéder à la valeur de la ligne suivante ?",
                ["LEAD()", "LAG()", "NEXT()", "FOLLOWING()"],
                0,
            ),
            S(
                "Quelle requête identifie le produit le plus vendu (rang 1) dans chaque catégorie avec RANK() ?",
                [
                    "SELECT * FROM (SELECT *, RANK() OVER (PARTITION BY categorie ORDER BY ventes DESC) AS rg FROM produits) t WHERE rg = 1;",
                    "SELECT * FROM produits WHERE RANK() = 1;",
                    "SELECT * FROM produits ORDER BY RANK(ventes) LIMIT 1;",
                    "SELECT * FROM produits GROUP BY categorie HAVING RANK() = 1;",
                ],
            ),
            M(
                "Quelles affirmations sur les fonctions de fenêtrage avancées sont vraies ?",
                [
                    "LAG et LEAD permettent de comparer une ligne à une ligne voisine sans jointure",
                    "Les fonctions de fenêtrage nécessitent une clause OVER()",
                ],
                ["LAG et LEAD modifient physiquement les données de la table", "RANK() ne peut jamais être utilisé avec PARTITION BY"],
            ),
            T("LAG() et LEAD() sont utiles pour calculer des variations entre une ligne et la ligne précédente ou suivante.", True),
            T("Une fonction de fenêtrage doit obligatoirement réduire le nombre de lignes du résultat final.", False),
        ],
    ),
    quiz(
        "Synthèse : UNION, jointures et NULL ensemble",
        "Combiner des techniques d'ensembles, de jointures et de gestion du NULL.",
        [
            S(
                "Quelle requête liste tous les emails de contact, qu'ils proviennent de la table clients ou fournisseurs, sans doublons ?",
                [
                    "SELECT email FROM clients UNION SELECT email FROM fournisseurs;",
                    "SELECT email FROM clients JOIN fournisseurs ON email;",
                    "SELECT email FROM clients, fournisseurs;",
                    "SELECT email FROM clients INTERSECT fournisseurs;",
                ],
            ),
            Sx(
                "Pourquoi privilégier COALESCE plutôt qu'une simple comparaison pour gérer un NULL dans un calcul ?",
                [
                    "Parce qu'une opération arithmétique avec NULL retourne NULL, COALESCE permet de fournir une valeur de remplacement",
                    "Parce que COALESCE est plus rapide dans tous les cas sans exception",
                    "Parce que NULL n'existe pas réellement en SQL",
                    "Parce que COALESCE convertit automatiquement le type de la colonne",
                ],
                0,
            ),
            S(
                "Quelle requête additionne le total des ventes en traitant les remises NULL comme 0 ?",
                [
                    "SELECT SUM(montant - COALESCE(remise, 0)) FROM ventes;",
                    "SELECT SUM(montant - remise) FROM ventes;",
                    "SELECT SUM(montant) - SUM(NULL) FROM ventes;",
                    "SELECT SUM(montant - IFNULL()) FROM ventes;",
                ],
            ),
            M(
                "Quelles affirmations sur la combinaison UNION/jointures/NULL sont correctes ?",
                [
                    "UNION peut combiner les résultats de requêtes provenant de tables différentes ayant une structure compatible",
                    "Une valeur NULL dans une opération arithmétique propage généralement NULL au résultat",
                ],
                ["UNION fusionne automatiquement les structures de tables différentes sans condition", "NULL est traité comme une chaîne vide dans tous les calculs"],
            ),
            T("COALESCE est une fonction utile pour remplacer les valeurs NULL par une valeur par défaut dans un calcul.", True),
            T("UNION ALL élimine systématiquement les valeurs NULL du résultat final.", False),
        ],
    ),
]
