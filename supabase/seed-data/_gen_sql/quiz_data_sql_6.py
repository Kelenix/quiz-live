from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "WHERE avancé : combiner AND, OR et NOT",
        "Construire des conditions complexes avec les opérateurs logiques.",
        [
            S(
                "Quelle requête sélectionne les produits de la catégorie 'Sport' OU dont le prix est inférieur à 20 ?",
                [
                    "SELECT * FROM produits WHERE categorie = 'Sport' OR prix < 20;",
                    "SELECT * FROM produits WHERE categorie = 'Sport' AND prix < 20;",
                    "SELECT * FROM produits WHERE categorie = 'Sport', prix < 20;",
                    "SELECT * FROM produits WHERE categorie = 'Sport' THEN prix < 20;",
                ],
            ),
            Sx(
                "Que fait l'opérateur NOT placé devant une condition WHERE ?",
                [
                    "Il inverse le résultat logique de la condition",
                    "Il transforme la condition en agrégation",
                    "Il supprime la ligne de la table définitivement",
                    "Il n'a aucun effet en SQL standard",
                ],
                0,
            ),
            S(
                "Quelle requête utilise des parenthèses pour prioriser correctement AND et OR ?",
                [
                    "SELECT * FROM produits WHERE (categorie = 'Sport' OR categorie = 'Loisir') AND prix < 50;",
                    "SELECT * FROM produits WHERE categorie = 'Sport' OR categorie = 'Loisir' AND prix < 50;",
                    "SELECT * FROM produits WHERE categorie = 'Sport' AND OR prix < 50;",
                    "SELECT * FROM produits WHERE NOT (categorie, prix);",
                ],
            ),
            M(
                "Quelles affirmations sur les opérateurs logiques WHERE sont vraies ?",
                [
                    "AND a généralement une priorité plus forte que OR sans parenthèses",
                    "Les parenthèses permettent de clarifier l'ordre d'évaluation des conditions",
                ],
                ["OR exige que toutes les conditions soient vraies simultanément", "NOT IN et IN sont rigoureusement identiques"],
            ),
            T("Combiner AND, OR et NOT permet de construire des filtres complexes dans une clause WHERE.", True),
            T("Les parenthèses n'ont aucune influence sur l'évaluation d'une condition combinant AND et OR.", False),
        ],
    ),
    quiz(
        "Sous-requêtes dans la clause SELECT",
        "Afficher des valeurs calculées par sous-requête comme colonne supplémentaire.",
        [
            S(
                "Quelle requête affiche, pour chaque produit, le nombre de fois où il a été commandé ?",
                [
                    "SELECT p.nom, (SELECT COUNT(*) FROM commandes co WHERE co.produit_id = p.id) AS nb_commandes FROM produits p;",
                    "SELECT p.nom, COUNT(*) FROM produits p;",
                    "SELECT p.nom, nb_commandes FROM produits p WHERE COUNT(*) > 0;",
                    "SELECT p.nom, (SELECT * FROM commandes) FROM produits p;",
                ],
            ),
            Sx(
                "Quelle contrainte s'applique à une sous-requête utilisée directement dans la clause SELECT ?",
                [
                    "Elle doit retourner une seule valeur scalaire par ligne",
                    "Elle doit obligatoirement retourner plusieurs lignes",
                    "Elle ne peut jamais référencer la requête externe",
                    "Elle doit toujours contenir un GROUP BY",
                ],
                0,
            ),
            S(
                "Quelle requête affiche le nom du client et la date de sa commande la plus récente ?",
                [
                    "SELECT c.nom, (SELECT MAX(date_commande) FROM commandes co WHERE co.client_id = c.id) AS derniere_commande FROM clients c;",
                    "SELECT c.nom, MAX(date_commande) FROM clients c;",
                    "SELECT c.nom, derniere_commande FROM clients c GROUP BY date_commande;",
                    "SELECT c.nom FROM clients c WHERE MAX(date_commande);",
                ],
            ),
            M(
                "Quelles affirmations sur les sous-requêtes en clause SELECT sont vraies ?",
                [
                    "Elles peuvent être corrélées à la requête externe via une colonne commune",
                    "Elles s'exécutent généralement une fois par ligne du résultat externe si corrélées",
                ],
                ["Elles peuvent retourner plusieurs colonnes sans aucune restriction", "Elles remplacent obligatoirement toute jointure équivalente"],
            ),
            T("Une sous-requête scalaire utilisée dans le SELECT peut être corrélée à la ligne courante de la requête externe.", True),
            T("Une sous-requête placée dans le SELECT doit toujours retourner plusieurs colonnes.", False),
        ],
    ),
    quiz(
        "Index composites et colonnes multiples",
        "Créer des index portant sur plusieurs colonnes à la fois.",
        [
            S(
                "Quelle instruction crée un index sur les colonnes nom et prenom combinées ?",
                [
                    "CREATE INDEX idx_nom_prenom ON clients (nom, prenom);",
                    "CREATE INDEX idx_nom_prenom ON clients (nom) AND (prenom);",
                    "CREATE INDEX ON clients (nom + prenom);",
                    "CREATE MULTI INDEX clients (nom, prenom);",
                ],
            ),
            Sx(
                "Quel facteur est important à prendre en compte pour l'ordre des colonnes dans un index composite ?",
                [
                    "L'ordre des colonnes dans les requêtes WHERE les plus fréquentes",
                    "L'ordre alphabétique des colonnes, sans exception",
                    "La taille en octets de chaque colonne uniquement",
                    "Aucun facteur n'a d'importance, l'ordre est toujours indifférent",
                ],
                0,
            ),
            S(
                "Pourquoi un index composite (nom, prenom) peut-il accélérer une requête filtrant uniquement sur nom ?",
                [
                    "Parce que nom est la première colonne de l'index, qui peut donc être utilisée seule efficacement",
                    "Parce que tous les index sont interchangeables quel que soit leur ordre",
                    "Parce que prenom n'a aucune incidence sur les performances",
                    "Ce n'est jamais possible, un index composite est inutile sans toutes ses colonnes",
                ],
            ),
            M(
                "Quelles affirmations sur les index composites sont vraies ?",
                [
                    "Un index composite porte sur plusieurs colonnes combinées",
                    "L'ordre des colonnes dans l'index influence son efficacité selon les requêtes",
                ],
                ["Un index composite ne peut jamais comporter plus de deux colonnes", "Un index composite remplace obligatoirement tous les index simples existants"],
            ),
            T("Un index composite peut être plus efficace qu'un index simple pour des requêtes filtrant sur plusieurs colonnes ensemble.", True),
            T("Un index composite (a, b) est toujours inutile pour des requêtes filtrant uniquement sur a.", False),
        ],
    ),
    quiz(
        "Vues et sécurité des données",
        "Utiliser les vues pour restreindre l'accès à certaines colonnes ou lignes.",
        [
            S(
                "Quelle vue permet de masquer la colonne sensible salaire de la table employes pour certains utilisateurs ?",
                [
                    "CREATE VIEW employes_public AS SELECT id, nom, departement FROM employes;",
                    "CREATE VIEW employes_public AS SELECT * FROM employes WHERE salaire IS NULL;",
                    "CREATE VIEW employes_public HIDE salaire FROM employes;",
                    "CREATE TABLE employes_public AS SELECT id, nom FROM employes WHERE salaire > 0;",
                ],
            ),
            Sx(
                "Quel est un cas d'usage courant des vues pour la sécurité des données ?",
                [
                    "Exposer uniquement un sous-ensemble de colonnes ou de lignes à certains utilisateurs",
                    "Empêcher toute lecture des données par quiconque",
                    "Chiffrer automatiquement les données stockées",
                    "Supprimer automatiquement les lignes sensibles de la table source",
                ],
                0,
            ),
            S(
                "Quelle instruction permet de donner uniquement le droit SELECT sur une vue à un utilisateur, sans accès direct à la table source ?",
                [
                    "GRANT SELECT ON employes_public TO utilisateur;",
                    "GRANT ALL ON employes TO utilisateur;",
                    "ALLOW VIEW employes_public TO utilisateur;",
                    "GRANT VIEW SELECT employes_public utilisateur;",
                ],
            ),
            M(
                "Quelles affirmations sur les vues et la sécurité sont correctes ?",
                [
                    "Une vue peut restreindre les colonnes visibles d'une table sensible",
                    "On peut accorder des privilèges sur une vue indépendamment de la table source",
                ],
                ["Une vue donne automatiquement accès à toutes les colonnes de la table source", "Les vues ne peuvent jamais être utilisées à des fins de sécurité"],
            ),
            T("Les vues peuvent contribuer à limiter l'exposition de données sensibles à certains utilisateurs.", True),
            T("Une vue donne systématiquement les mêmes droits que la table sous-jacente, sans aucune restriction possible.", False),
        ],
    ),
    quiz(
        "GROUP BY avec jointures",
        "Agréger des données provenant de plusieurs tables jointes.",
        [
            S(
                "Quelle requête calcule le total des ventes par nom de client, en combinant deux tables ?",
                [
                    "SELECT c.nom, SUM(co.montant) FROM clients c JOIN commandes co ON c.id = co.client_id GROUP BY c.nom;",
                    "SELECT c.nom, SUM(co.montant) FROM clients c, commandes co GROUP BY co.montant;",
                    "SELECT SUM(co.montant) FROM clients c JOIN commandes co GROUP BY co.client_id;",
                    "SELECT c.nom FROM clients c JOIN commandes co ON c.id = co.client_id SUM(co.montant);",
                ],
            ),
            Sx(
                "Pourquoi est-il important de regrouper sur la clé primaire ou un identifiant unique plutôt que sur le nom lors d'un GROUP BY après jointure ?",
                [
                    "Parce que deux clients différents pourraient porter le même nom et seraient alors regroupés à tort",
                    "Parce que les noms ne peuvent jamais être groupés en SQL",
                    "Parce qu'un identifiant numérique est toujours plus rapide qu'un texte sans aucune exception",
                    "Cela n'a aucune importance dans la pratique",
                ],
                0,
            ),
            S(
                "Quelle requête liste les catégories de produits avec le nombre total d'unités vendues (table lignes_commande) ?",
                [
                    "SELECT p.categorie, SUM(lc.quantite) FROM produits p JOIN lignes_commande lc ON p.id = lc.produit_id GROUP BY p.categorie;",
                    "SELECT p.categorie, SUM(lc.quantite) FROM produits p, lignes_commande lc GROUP BY lc.quantite;",
                    "SELECT SUM(lc.quantite) FROM produits p JOIN lignes_commande lc;",
                    "SELECT p.categorie FROM produits p GROUP BY SUM(lc.quantite);",
                ],
            ),
            M(
                "Quelles affirmations sur GROUP BY après une jointure sont vraies ?",
                [
                    "Le GROUP BY s'applique sur le résultat combiné de la jointure",
                    "On peut filtrer les groupes obtenus avec HAVING après une jointure",
                ],
                ["Une jointure empêche systématiquement l'utilisation de GROUP BY", "GROUP BY doit obligatoirement précéder la clause JOIN dans la requête"],
            ),
            T("Il est possible de combiner JOIN, GROUP BY et HAVING dans une seule requête pour produire un rapport agrégé.", True),
            T("GROUP BY ne peut jamais être utilisé après une jointure entre deux tables.", False),
        ],
    ),
    quiz(
        "Comparaison de dates et intervalles",
        "Filtrer et calculer des écarts entre des colonnes de type date.",
        [
            S(
                "Quelle requête sélectionne les commandes passées au cours des 30 derniers jours (fonction générique) ?",
                [
                    "SELECT * FROM commandes WHERE date_commande >= CURRENT_DATE - INTERVAL '30 days';",
                    "SELECT * FROM commandes WHERE date_commande = LAST 30;",
                    "SELECT * FROM commandes WHERE date_commande BETWEEN 30;",
                    "SELECT * FROM commandes WHERE date_commande - 30 = CURRENT_DATE;",
                ],
            ),
            Sx(
                "Comment calcule-t-on généralement le nombre de jours entre deux dates en SQL ?",
                [
                    "En soustrayant la date la plus ancienne de la date la plus récente",
                    "En utilisant uniquement la fonction CONCAT",
                    "Cela est impossible à calculer en SQL",
                    "En multipliant les deux dates entre elles",
                ],
                0,
            ),
            S(
                "Quelle requête trouve les clients inscrits avant le 1er janvier 2023 ?",
                [
                    "SELECT * FROM clients WHERE date_inscription < '2023-01-01';",
                    "SELECT * FROM clients WHERE date_inscription BEFORE '2023-01-01';",
                    "SELECT * FROM clients WHERE date_inscription = '2023-01-01' MINUS 1;",
                    "SELECT * FROM clients WHERE date_inscription PAST '2023-01-01';",
                ],
            ),
            M(
                "Quelles affirmations sur les comparaisons de dates sont vraies ?",
                [
                    "Les opérateurs <, >, <= et >= fonctionnent sur les colonnes de type date",
                    "Le format de date attendu peut varier légèrement selon le SGBD utilisé",
                ],
                ["Les dates ne peuvent jamais être comparées entre elles", "CURRENT_DATE retourne toujours une valeur fixe identique chaque jour"],
            ),
            T("Soustraire deux dates permet souvent d'obtenir un nombre de jours d'écart entre elles.", True),
            T("Il est impossible de filtrer des lignes selon une plage de dates avec BETWEEN.", False),
        ],
    ),
    quiz(
        "Sous-requêtes dans la clause FROM (tables dérivées)",
        "Construire des requêtes basées sur des résultats intermédiaires nommés.",
        [
            S(
                "Quelle requête utilise une table dérivée pour calculer le total par client puis filtrer les plus gros clients ?",
                [
                    "SELECT * FROM (SELECT client_id, SUM(montant) AS total FROM commandes GROUP BY client_id) t WHERE t.total > 1000;",
                    "SELECT * FROM commandes WHERE SUM(montant) > 1000;",
                    "SELECT client_id, SUM(montant) FROM commandes HAVING total > 1000;",
                    "SELECT * FROM commandes GROUP BY client_id WHERE total > 1000;",
                ],
            ),
            Sx(
                "Pourquoi une table dérivée (sous-requête en FROM) doit-elle recevoir un alias dans la plupart des SGBD ?",
                [
                    "Parce que la syntaxe SQL l'exige pour pouvoir référencer cette table dérivée",
                    "Parce que cela améliore uniquement l'esthétique du code, sans nécessité technique",
                    "Parce qu'un alias transforme la sous-requête en vue permanente",
                    "Ce n'est jamais nécessaire, aucun SGBD ne l'exige",
                ],
                0,
            ),
            S(
                "Quelle requête combine une table dérivée avec une jointure pour enrichir les données agrégées ?",
                [
                    "SELECT c.nom, t.total FROM clients c JOIN (SELECT client_id, SUM(montant) AS total FROM commandes GROUP BY client_id) t ON c.id = t.client_id;",
                    "SELECT c.nom, t.total FROM clients c, (SUM(montant));",
                    "SELECT c.nom FROM clients c JOIN commandes GROUP BY client_id;",
                    "SELECT t.total FROM (clients JOIN commandes);",
                ],
            ),
            M(
                "Quelles affirmations sur les tables dérivées sont vraies ?",
                [
                    "Une table dérivée permet de réutiliser un résultat intermédiaire dans la requête principale",
                    "Une table dérivée peut elle-même être jointe à d'autres tables",
                ],
                ["Une table dérivée est stockée de façon permanente dans le schéma", "Une table dérivée ne peut jamais contenir de GROUP BY"],
            ),
            T("Une table dérivée (sous-requête en FROM) n'existe que pendant l'exécution de la requête qui la contient.", True),
            T("Il est interdit de joindre une table dérivée à une table classique.", False),
        ],
    ),
    quiz(
        "Index unique et performance des recherches",
        "Comprendre l'index UNIQUE et son rôle combiné performance/intégrité.",
        [
            S(
                "Quelle instruction crée un index garantissant l'unicité des emails dans la table clients ?",
                [
                    "CREATE UNIQUE INDEX idx_email ON clients (email);",
                    "CREATE INDEX UNIQUE clients (email);",
                    "CREATE INDEX idx_email ON clients (email) DISTINCT;",
                    "ALTER INDEX clients ADD UNIQUE email;",
                ],
            ),
            Sx(
                "Quelle différence existe-t-il entre un index UNIQUE et une simple contrainte UNIQUE ?",
                [
                    "Une contrainte UNIQUE crée généralement automatiquement un index UNIQUE sous-jacent dans la plupart des SGBD",
                    "Un index UNIQUE ne garantit jamais l'unicité des valeurs",
                    "Une contrainte UNIQUE ne peut jamais être appliquée à une colonne texte",
                    "Il n'existe aucun lien entre les deux notions",
                ],
                0,
            ),
            S(
                "Pourquoi un index UNIQUE peut-il accélérer une recherche par email tout en garantissant l'absence de doublons ?",
                [
                    "Parce qu'il combine structure de recherche rapide et contrainte d'unicité en une seule structure",
                    "Parce qu'il transforme automatiquement la colonne en clé primaire",
                    "Parce qu'il supprime les doublons existants automatiquement à sa création",
                    "Un index UNIQUE n'a aucun effet sur la vitesse de recherche",
                ],
            ),
            M(
                "Quelles affirmations sur les index UNIQUE sont vraies ?",
                [
                    "Un index UNIQUE empêche l'insertion de deux lignes avec la même valeur indexée",
                    "Un index UNIQUE peut accélérer les recherches sur la colonne concernée",
                ],
                ["Un index UNIQUE autorise un nombre illimité de doublons", "Un index UNIQUE doit obligatoirement porter sur la clé primaire"],
            ),
            T("Un index UNIQUE empêche l'insertion de valeurs dupliquées sur la colonne indexée.", True),
            T("Un index UNIQUE ne peut être créé que sur la colonne définie comme clé primaire.", False),
        ],
    ),
    quiz(
        "Agrégats et filtrage NULL combinés",
        "Étudier l'effet de NULL sur les fonctions d'agrégation et les filtres.",
        [
            S(
                "Quelle requête trouve les clients dont la ville n'est ni NULL ni vide ?",
                [
                    "SELECT * FROM clients WHERE ville IS NOT NULL AND ville <> '';",
                    "SELECT * FROM clients WHERE ville != NULL OR ville = '';",
                    "SELECT * FROM clients WHERE ville IS NOT EMPTY;",
                    "SELECT * FROM clients WHERE NOT ville;",
                ],
            ),
            Sx(
                "Quel est l'effet d'une valeur NULL sur le résultat de AVG(colonne) ?",
                [
                    "Les lignes NULL sont ignorées dans le calcul de la moyenne",
                    "Chaque NULL est compté comme 0 dans le calcul",
                    "La présence d'un seul NULL rend tout le résultat NULL",
                    "AVG() refuse de s'exécuter si des NULL sont présents",
                ],
                0,
            ),
            S(
                "Quelle requête compte les clients ayant un email renseigné, sans tenir compte des NULL ?",
                [
                    "SELECT COUNT(email) FROM clients;",
                    "SELECT COUNT(*) FROM clients WHERE email = NULL;",
                    "SELECT COUNT(ALL) FROM clients WHERE email IS NULL;",
                    "SELECT SUM(email) FROM clients;",
                ],
            ),
            M(
                "Quelles affirmations sur NULL et les agrégations sont vraies ?",
                [
                    "COUNT(colonne) exclut les valeurs NULL de cette colonne du comptage",
                    "SUM(colonne) ignore les valeurs NULL dans son addition",
                ],
                ["MAX() et MIN() retournent toujours NULL si une seule valeur de la colonne est NULL", "AVG() compte les valeurs NULL comme des zéros"],
            ),
            T("Les fonctions d'agrégation comme SUM, AVG, MIN, MAX ignorent généralement les valeurs NULL dans leur calcul.", True),
            T("COUNT(*) ignore les lignes contenant des valeurs NULL dans n'importe quelle colonne.", False),
        ],
    ),
    quiz(
        "DDL : CREATE TABLE complet",
        "Construire une instruction CREATE TABLE avec plusieurs contraintes combinées.",
        [
            S(
                "Quelle instruction crée une table produits avec un id auto-incrémenté en clé primaire, un nom obligatoire et un prix positif ?",
                [
                    "CREATE TABLE produits (id SERIAL PRIMARY KEY, nom TEXT NOT NULL, prix NUMERIC CHECK (prix > 0));",
                    "CREATE TABLE produits (id SERIAL, nom TEXT, prix NUMERIC) PRIMARY KEY id;",
                    "CREATE produits TABLE (id PRIMARY, nom NOT NULL, prix CHECK > 0);",
                    "CREATE TABLE produits id SERIAL PRIMARY KEY, nom TEXT NOT NULL, prix NUMERIC;",
                ],
            ),
            Sx(
                "Que se passe-t-il si on tente de créer une table avec un nom déjà utilisé par une table existante, sans précaution particulière ?",
                [
                    "Une erreur est levée car le nom de table doit être unique dans le schéma",
                    "La table existante est automatiquement remplacée sans avertissement",
                    "Les deux tables coexistent sous le même nom sans problème",
                    "La nouvelle définition est simplement ignorée silencieusement",
                ],
                0,
            ),
            S(
                "Quelle clause permet d'éviter une erreur si la table existe déjà lors de sa création (syntaxe courante) ?",
                [
                    "CREATE TABLE IF NOT EXISTS produits (...);",
                    "CREATE TABLE produits IGNORE EXISTING (...);",
                    "CREATE OR REPLACE produits (...);",
                    "CREATE TABLE produits SAFE (...);",
                ],
            ),
            M(
                "Quelles affirmations sur CREATE TABLE sont correctes ?",
                [
                    "On peut combiner plusieurs contraintes (PRIMARY KEY, NOT NULL, CHECK) dans une même définition",
                    "CREATE TABLE fait partie du langage DDL",
                ],
                ["CREATE TABLE insère automatiquement des données dans la nouvelle table", "Une table ne peut contenir qu'une seule colonne au maximum"],
            ),
            T("Une instruction CREATE TABLE peut définir simultanément le type, les contraintes et les valeurs par défaut de chaque colonne.", True),
            T("CREATE TABLE permet d'insérer directement des lignes de données dans la nouvelle table créée.", False),
        ],
    ),
    quiz(
        "DROP et gestion du schéma",
        "Supprimer des objets de la base de données avec DROP.",
        [
            S(
                "Quelle instruction supprime définitivement la table produits et toutes ses données ?",
                ["DROP TABLE produits;", "DELETE TABLE produits;", "REMOVE TABLE produits;", "TRUNCATE SCHEMA produits;"],
            ),
            Sx(
                "Quelle est la différence entre DROP TABLE et TRUNCATE TABLE ?",
                [
                    "DROP TABLE supprime aussi la structure de la table, TRUNCATE ne vide que les données",
                    "TRUNCATE supprime la structure, DROP ne vide que les données",
                    "Les deux instructions sont rigoureusement identiques",
                    "DROP TABLE ne peut être utilisé que sur des vues",
                ],
                0,
            ),
            S(
                "Quelle instruction supprime une vue nommée clients_actifs ?",
                ["DROP VIEW clients_actifs;", "DELETE VIEW clients_actifs;", "REMOVE VIEW clients_actifs;", "DROP TABLE clients_actifs;"],
            ),
            M(
                "Quelles affirmations sur DROP sont vraies ?",
                [
                    "DROP TABLE est une opération généralement irréversible sans sauvegarde",
                    "On peut utiliser DROP pour supprimer des vues, des index ou des tables",
                ],
                ["DROP TABLE conserve toujours une copie de sauvegarde automatique", "DROP ne peut s'appliquer qu'aux colonnes, jamais aux tables"],
            ),
            T("DROP TABLE supprime à la fois les données et la définition structurelle de la table.", True),
            T("TRUNCATE TABLE supprime la structure de la table en plus de ses données.", False),
        ],
    ),
    quiz(
        "Bonnes pratiques de nommage et lisibilité SQL",
        "Adopter des conventions claires pour des requêtes maintenables.",
        [
            S(
                "Quelle pratique favorise la lisibilité d'une requête comportant plusieurs jointures ?",
                [
                    "Utiliser des alias de table courts et cohérents (ex: c pour clients, co pour commandes)",
                    "Toujours utiliser SELECT * sans jamais préciser les colonnes",
                    "Éviter systématiquement les sauts de ligne dans la requête",
                    "Nommer chaque table avec un nom différent à chaque requête",
                ],
            ),
            Sx(
                "Pourquoi évite-t-on souvent SELECT * dans du code de production ?",
                [
                    "Parce que cela peut ramener des colonnes inutiles et rendre la requête fragile aux changements de schéma",
                    "Parce que SELECT * est une syntaxe invalide en SQL standard",
                    "Parce que SELECT * empêche systématiquement l'utilisation de WHERE",
                    "Parce que SELECT * ne fonctionne qu'avec une seule table",
                ],
                0,
            ),
            S(
                "Quelle convention de nommage est couramment recommandée pour les tables et colonnes ?",
                [
                    "Des noms en minuscules avec underscores, clairs et descriptifs",
                    "Des noms aléatoires générés automatiquement",
                    "Des noms identiques pour toutes les colonnes de la base",
                    "Des noms exclusivement en majuscules accentuées",
                ],
            ),
            M(
                "Quelles affirmations sur les bonnes pratiques SQL sont vraies ?",
                [
                    "Préciser explicitement les colonnes dans le SELECT améliore la maintenabilité",
                    "Des alias clairs facilitent la lecture des requêtes avec plusieurs jointures",
                ],
                ["Le formatage du code SQL n'a aucune influence sur sa lisibilité", "Il est recommandé de ne jamais commenter une requête complexe"],
            ),
            T("Adopter des conventions de nommage cohérentes facilite la maintenance d'une base de données sur le long terme.", True),
            T("L'utilisation systématique de SELECT * est toujours considérée comme la meilleure pratique en production.", False),
        ],
    ),
]
