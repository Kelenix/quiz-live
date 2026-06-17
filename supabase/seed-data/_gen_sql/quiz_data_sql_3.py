from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "UNION et UNION ALL",
        "Combiner les résultats de plusieurs requêtes SELECT.",
        [
            S(
                "Quelle requête combine les clients de 2023 et 2024 sans doublons ?",
                [
                    "SELECT * FROM clients_2023 UNION SELECT * FROM clients_2024;",
                    "SELECT * FROM clients_2023 JOIN SELECT * FROM clients_2024;",
                    "SELECT * FROM clients_2023 ADD SELECT * FROM clients_2024;",
                    "SELECT * FROM clients_2023, clients_2024;",
                ],
            ),
            Sx(
                "Quelle est la différence entre UNION et UNION ALL ?",
                [
                    "UNION élimine les doublons, UNION ALL les conserve",
                    "UNION ALL élimine les doublons, UNION les conserve",
                    "Il n'y a aucune différence entre les deux",
                    "UNION ALL ne peut combiner que deux colonnes maximum",
                ],
                0,
            ),
            S(
                "Quelle condition les requêtes combinées par UNION doivent-elles respecter ?",
                [
                    "Avoir le même nombre de colonnes avec des types compatibles",
                    "Provenir obligatoirement de la même table",
                    "Avoir des noms de colonnes identiques uniquement",
                    "Contenir uniquement des colonnes numériques",
                ],
            ),
            M(
                "Quelles affirmations sur UNION sont correctes ?",
                [
                    "UNION ALL est généralement plus rapide que UNION car il ne déduplique pas",
                    "Les colonnes combinées doivent être en nombre identique dans chaque SELECT",
                ],
                ["UNION peut combiner des requêtes ayant un nombre de colonnes différent", "UNION ALL trie automatiquement les résultats finaux"],
            ),
            T("UNION ALL conserve les lignes en double issues des différentes requêtes combinées.", True),
            T("UNION peut uniquement combiner exactement deux requêtes SELECT, jamais plus.", False),
        ],
    ),
    quiz(
        "INTERSECT et EXCEPT",
        "Trouver les lignes communes ou la différence entre deux ensembles.",
        [
            S(
                "Quelle requête retourne les clients présents à la fois dans la table A et la table B ?",
                [
                    "SELECT * FROM A INTERSECT SELECT * FROM B;",
                    "SELECT * FROM A UNION SELECT * FROM B;",
                    "SELECT * FROM A EXCEPT SELECT * FROM B;",
                    "SELECT * FROM A JOIN B ON A.id != B.id;",
                ],
            ),
            Sx(
                "Que retourne `SELECT * FROM A EXCEPT SELECT * FROM B;` ?",
                [
                    "Les lignes présentes dans A mais absentes de B",
                    "Les lignes présentes dans B mais absentes de A",
                    "Les lignes communes à A et B",
                    "Toutes les lignes de A et de B réunies",
                ],
                0,
            ),
            S(
                "Quel opérateur d'ensemble permet de trouver les éléments communs à deux requêtes ?",
                ["INTERSECT", "UNION ALL", "EXCEPT", "JOIN COMMON"],
            ),
            M(
                "Quelles affirmations sur INTERSECT et EXCEPT sont vraies ?",
                [
                    "INTERSECT retourne uniquement les lignes communes aux deux requêtes",
                    "EXCEPT est sensible à l'ordre des requêtes (A EXCEPT B diffère de B EXCEPT A)",
                ],
                ["INTERSECT conserve systématiquement les doublons", "EXCEPT est strictement identique à UNION"],
            ),
            T("INTERSECT et EXCEPT exigent généralement le même nombre de colonnes dans les requêtes combinées.", True),
            T("MINUS est parfois utilisé comme synonyme d'EXCEPT dans certains SGBD comme Oracle.", True),
        ],
    ),
    quiz(
        "INSERT : ajouter des données",
        "Insérer une ou plusieurs lignes dans une table.",
        [
            S(
                "Quelle requête insère un nouveau client avec nom et email ?",
                [
                    "INSERT INTO clients (nom, email) VALUES ('Dupont', 'dupont@mail.com');",
                    "INSERT clients (nom, email) = ('Dupont', 'dupont@mail.com');",
                    "ADD INTO clients (nom, email) VALUES ('Dupont', 'dupont@mail.com');",
                    "INSERT INTO clients SET nom = 'Dupont', email = 'dupont@mail.com';",
                ],
            ),
            Sx(
                "Que se passe-t-il si on omet une colonne NOT NULL sans valeur par défaut lors d'un INSERT ?",
                [
                    "Une erreur est levée car la contrainte NOT NULL n'est pas respectée",
                    "La colonne reçoit automatiquement la valeur NULL sans erreur",
                    "La ligne est insérée avec une chaîne vide",
                    "L'insertion réussit toujours sans condition",
                ],
                0,
            ),
            S(
                "Quelle syntaxe permet d'insérer plusieurs lignes en une seule instruction INSERT ?",
                [
                    "INSERT INTO produits (nom, prix) VALUES ('A', 10), ('B', 20);",
                    "INSERT INTO produits (nom, prix) VALUES ('A', 10) AND ('B', 20);",
                    "INSERT INTO produits (nom, prix) MULTI VALUES ('A',10),('B',20);",
                    "INSERT ALL INTO produits VALUES ('A', 10), ('B', 20);",
                ],
            ),
            M(
                "Quelles affirmations sur INSERT sont correctes ?",
                [
                    "On peut insérer le résultat d'un SELECT avec INSERT INTO ... SELECT",
                    "L'ordre des valeurs dans VALUES doit correspondre à l'ordre des colonnes listées",
                ],
                ["INSERT ne peut jamais insérer plus d'une ligne à la fois", "INSERT modifie automatiquement les lignes déjà existantes"],
            ),
            T("INSERT INTO ... SELECT permet de copier des données d'une table vers une autre.", True),
            T("INSERT INTO nécessite obligatoirement de préciser toutes les colonnes de la table, sans exception.", False),
        ],
    ),
    quiz(
        "UPDATE : modifier des données",
        "Mettre à jour des lignes existantes avec UPDATE et WHERE.",
        [
            S(
                "Quelle requête met à jour le prix du produit dont l'id est 5 ?",
                [
                    "UPDATE produits SET prix = 99 WHERE id = 5;",
                    "UPDATE produits prix = 99 WHERE id = 5;",
                    "SET produits prix = 99 WHERE id = 5;",
                    "UPDATE produits VALUES prix = 99 WHERE id = 5;",
                ],
            ),
            Sx(
                "Que se passe-t-il si on exécute UPDATE sans clause WHERE ?",
                [
                    "Toutes les lignes de la table sont mises à jour",
                    "Aucune ligne n'est mise à jour par sécurité",
                    "Une erreur de syntaxe est systématiquement levée",
                    "Seule la première ligne est mise à jour",
                ],
                0,
            ),
            S(
                "Quelle requête augmente de 10% le prix de tous les produits de la catégorie 'Jouets' ?",
                [
                    "UPDATE produits SET prix = prix * 1.10 WHERE categorie = 'Jouets';",
                    "UPDATE produits SET prix += 10 WHERE categorie = 'Jouets';",
                    "UPDATE produits prix = prix * 1.10 categorie = 'Jouets';",
                    "SET prix = prix * 1.10 FROM produits WHERE categorie = 'Jouets';",
                ],
            ),
            M(
                "Quelles affirmations sur UPDATE sont vraies ?",
                [
                    "UPDATE peut modifier plusieurs colonnes en une seule instruction",
                    "Sans WHERE, UPDATE affecte toutes les lignes de la table",
                ],
                ["UPDATE crée toujours une nouvelle table", "UPDATE ne peut modifier qu'une seule ligne à la fois"],
            ),
            T("Il est recommandé de tester la clause WHERE d'un UPDATE avec un SELECT avant de l'exécuter.", True),
            T("UPDATE ne peut jamais utiliser d'expression arithmétique dans la clause SET.", False),
        ],
    ),
    quiz(
        "DELETE : supprimer des données",
        "Supprimer des lignes avec DELETE, et différencier DELETE de TRUNCATE.",
        [
            S(
                "Quelle requête supprime tous les clients de la ville 'Marseille' ?",
                [
                    "DELETE FROM clients WHERE ville = 'Marseille';",
                    "DELETE clients WHERE ville = 'Marseille';",
                    "REMOVE FROM clients WHERE ville = 'Marseille';",
                    "DELETE FROM clients VALUES ville = 'Marseille';",
                ],
            ),
            Sx(
                "Que se passe-t-il si on exécute DELETE FROM produits; sans clause WHERE ?",
                [
                    "Toutes les lignes de la table produits sont supprimées",
                    "La table produits elle-même est supprimée (DROP)",
                    "Rien ne se passe, une clause WHERE est obligatoire",
                    "Seule la dernière ligne insérée est supprimée",
                ],
                0,
            ),
            S(
                "Quelle est une différence clé entre DELETE et TRUNCATE ?",
                [
                    "DELETE peut cibler des lignes précises avec WHERE, TRUNCATE vide toute la table",
                    "TRUNCATE peut cibler des lignes précises avec WHERE, DELETE vide toute la table",
                    "DELETE et TRUNCATE sont strictement identiques en tout point",
                    "TRUNCATE ne fonctionne que sur les vues",
                ],
            ),
            M(
                "Quelles affirmations sur DELETE sont correctes ?",
                [
                    "DELETE FROM table; sans WHERE supprime toutes les lignes",
                    "DELETE peut généralement être annulé par ROLLBACK dans une transaction",
                ],
                ["DELETE supprime aussi la définition de la table", "DELETE est toujours plus rapide que TRUNCATE quel que soit le contexte"],
            ),
            T("DELETE supprime des lignes de données mais conserve la structure de la table.", True),
            T("TRUNCATE permet de supprimer une seule ligne précise grâce à une clause WHERE.", False),
        ],
    ),
    quiz(
        "Clé primaire (PRIMARY KEY)",
        "Garantir l'unicité et l'identification de chaque ligne d'une table.",
        [
            S(
                "Quelle instruction définit la colonne id comme clé primaire lors de la création de la table ?",
                [
                    "CREATE TABLE clients (id INT PRIMARY KEY, nom TEXT);",
                    "CREATE TABLE clients (id INT MAIN KEY, nom TEXT);",
                    "CREATE TABLE clients (id INT UNIQUE KEY PRIMARY, nom TEXT);",
                    "CREATE TABLE clients (id INT, nom TEXT) AS PRIMARY KEY id;",
                ],
            ),
            Sx(
                "Quelles propriétés caractérisent une clé primaire ?",
                [
                    "Unique et non NULL pour chaque ligne de la table",
                    "Peut contenir des doublons mais jamais NULL",
                    "Peut être NULL mais jamais en double",
                    "Doit toujours être une colonne de type texte",
                ],
                0,
            ),
            S(
                "Une table peut-elle avoir plusieurs colonnes formant une clé primaire composite ?",
                [
                    "Oui, une clé primaire peut être composée de plusieurs colonnes",
                    "Non, une clé primaire ne peut porter que sur une seule colonne",
                    "Non, c'est interdit par le standard SQL",
                    "Oui, mais uniquement avec des colonnes de type texte",
                ],
            ),
            M(
                "Quelles affirmations sur PRIMARY KEY sont vraies ?",
                [
                    "Une table ne peut avoir qu'une seule clé primaire",
                    "Une clé primaire crée généralement un index automatiquement",
                ],
                ["Une clé primaire autorise les valeurs NULL", "Une clé primaire peut être dupliquée entre plusieurs lignes"],
            ),
            T("La clé primaire garantit qu'aucune ligne ne partage la même valeur d'identifiant.", True),
            T("Il est possible de définir deux clés primaires différentes sur la même table.", False),
        ],
    ),
    quiz(
        "Clé étrangère (FOREIGN KEY)",
        "Lier deux tables et garantir l'intégrité référentielle.",
        [
            S(
                "Quelle instruction crée une clé étrangère reliant commandes.client_id à clients.id ?",
                [
                    "CREATE TABLE commandes (id INT PRIMARY KEY, client_id INT, FOREIGN KEY (client_id) REFERENCES clients(id));",
                    "CREATE TABLE commandes (id INT PRIMARY KEY, client_id INT LINKED clients(id));",
                    "CREATE TABLE commandes (client_id INT REFERENCES TO clients.id);",
                    "CREATE TABLE commandes (client_id INT FOREIGN clients(id));",
                ],
            ),
            Sx(
                "Que garantit une contrainte FOREIGN KEY ?",
                [
                    "Que la valeur référencée existe bien dans la table parente",
                    "Que la colonne ne peut jamais contenir de valeur NULL",
                    "Que la colonne est automatiquement indexée comme clé primaire",
                    "Que la table parente sera supprimée si la table enfant l'est",
                ],
                0,
            ),
            S(
                "Que se passe-t-il généralement si on tente de supprimer un client référencé par une commande, sans règle ON DELETE particulière ?",
                [
                    "La suppression échoue à cause de la contrainte d'intégrité référentielle",
                    "Le client est supprimé et la commande aussi automatiquement",
                    "Le client est supprimé et client_id devient NULL automatiquement",
                    "La suppression réussit toujours sans aucune conséquence",
                ],
            ),
            M(
                "Quelles affirmations sur les clés étrangères sont correctes ?",
                [
                    "Une clé étrangère référence en général une clé primaire ou unique d'une autre table",
                    "ON DELETE CASCADE permet de supprimer automatiquement les lignes enfants liées",
                ],
                ["Une clé étrangère doit obligatoirement porter le même nom que la colonne référencée", "Une table ne peut avoir qu'une seule clé étrangère"],
            ),
            T("Les clés étrangères contribuent à maintenir l'intégrité référentielle entre les tables.", True),
            T("Une colonne avec une contrainte FOREIGN KEY ne peut référencer qu'une colonne de la même table.", False),
        ],
    ),
    quiz(
        "Contraintes UNIQUE et NOT NULL",
        "Empêcher les doublons et les valeurs manquantes sur une colonne.",
        [
            S(
                "Quelle instruction garantit qu'aucun email ne sera dupliqué dans la table clients ?",
                [
                    "CREATE TABLE clients (id INT PRIMARY KEY, email TEXT UNIQUE);",
                    "CREATE TABLE clients (id INT PRIMARY KEY, email TEXT DISTINCT);",
                    "CREATE TABLE clients (id INT PRIMARY KEY, email TEXT NO DUPLICATE);",
                    "CREATE TABLE clients (id INT PRIMARY KEY, email TEXT SINGLE);",
                ],
            ),
            Sx(
                "Une contrainte UNIQUE autorise-t-elle la valeur NULL ?",
                [
                    "Oui, en général plusieurs NULL sont autorisés selon le SGBD",
                    "Non, NULL est toujours interdit avec UNIQUE",
                    "Non, UNIQUE équivaut exactement à NOT NULL",
                    "Oui, mais une seule valeur NULL au maximum pour toute la base",
                ],
                0,
            ),
            S(
                "Quelle contrainte empêche une colonne d'être vide (NULL) ?",
                ["NOT NULL", "UNIQUE", "DEFAULT", "CHECK"],
            ),
            M(
                "Quelles affirmations sur UNIQUE et NOT NULL sont vraies ?",
                [
                    "NOT NULL impose qu'une valeur soit toujours fournie pour la colonne",
                    "UNIQUE peut s'appliquer à plusieurs colonnes combinées",
                ],
                ["UNIQUE et PRIMARY KEY sont rigoureusement la même contrainte sans aucune différence", "NOT NULL garantit l'unicité des valeurs"],
            ),
            T("Une colonne peut être à la fois UNIQUE et NOT NULL.", True),
            T("La contrainte NOT NULL empêche les doublons mais autorise les valeurs vides.", False),
        ],
    ),
    quiz(
        "Contraintes CHECK et DEFAULT",
        "Valider des règles métier et définir des valeurs par défaut.",
        [
            S(
                "Quelle instruction garantit que le prix d'un produit est toujours positif ?",
                [
                    "CREATE TABLE produits (id INT PRIMARY KEY, prix NUMERIC CHECK (prix > 0));",
                    "CREATE TABLE produits (id INT PRIMARY KEY, prix NUMERIC POSITIVE);",
                    "CREATE TABLE produits (id INT PRIMARY KEY, prix NUMERIC VALIDATE prix > 0);",
                    "CREATE TABLE produits (id INT PRIMARY KEY, prix NUMERIC RULE (prix > 0));",
                ],
            ),
            Sx(
                "Quelle clause permet d'attribuer automatiquement la valeur 'actif' à une colonne statut si aucune valeur n'est fournie ?",
                [
                    "statut TEXT DEFAULT 'actif'",
                    "statut TEXT AUTO 'actif'",
                    "statut TEXT INIT 'actif'",
                    "statut TEXT = 'actif'",
                ],
                0,
            ),
            S(
                "Quelle contrainte CHECK garantit qu'une colonne age est toujours comprise entre 0 et 120 ?",
                [
                    "CHECK (age >= 0 AND age <= 120)",
                    "CHECK age BETWEEN 0, 120",
                    "VALIDATE (age >= 0 AND age <= 120)",
                    "CHECK (age IN (0, 120))",
                ],
            ),
            M(
                "Quelles affirmations sur CHECK et DEFAULT sont correctes ?",
                [
                    "CHECK permet de définir une règle de validation au niveau de la colonne ou de la table",
                    "DEFAULT fournit une valeur automatique lorsqu'aucune n'est précisée à l'insertion",
                ],
                ["CHECK empêche systématiquement toute valeur NULL", "DEFAULT empêche la modification ultérieure de la colonne"],
            ),
            T("Une contrainte CHECK peut combiner plusieurs conditions avec AND ou OR.", True),
            T("La valeur DEFAULT s'applique même si l'utilisateur fournit explicitement une valeur lors de l'INSERT.", False),
        ],
    ),
    quiz(
        "ALTER TABLE : modifier la structure d'une table",
        "Ajouter, modifier ou supprimer des colonnes existantes.",
        [
            S(
                "Quelle instruction ajoute une colonne telephone à la table clients ?",
                [
                    "ALTER TABLE clients ADD COLUMN telephone TEXT;",
                    "ALTER clients ADD telephone TEXT COLUMN;",
                    "UPDATE TABLE clients ADD telephone TEXT;",
                    "ALTER TABLE clients NEW COLUMN telephone TEXT;",
                ],
            ),
            Sx(
                "Quelle instruction supprime la colonne fax de la table clients ?",
                [
                    "ALTER TABLE clients DROP COLUMN fax;",
                    "ALTER TABLE clients REMOVE fax;",
                    "DELETE COLUMN fax FROM clients;",
                    "ALTER TABLE clients DROP fax COLUMN;",
                ],
                0,
            ),
            S(
                "Quelle instruction renomme la table 'clients' en 'customers' (syntaxe courante) ?",
                [
                    "ALTER TABLE clients RENAME TO customers;",
                    "ALTER TABLE clients RENAME customers;",
                    "RENAME TABLE clients customers;",
                    "ALTER clients NAME TO customers;",
                ],
            ),
            M(
                "Quelles opérations sont possibles avec ALTER TABLE ?",
                [
                    "Ajouter une nouvelle colonne",
                    "Modifier le type d'une colonne existante",
                ],
                ["Insérer de nouvelles lignes de données", "Créer une nouvelle base de données"],
            ),
            T("ALTER TABLE fait partie du langage DDL (Data Definition Language).", True),
            T("ALTER TABLE permet d'insérer des lignes de données dans une table.", False),
        ],
    ),
    quiz(
        "DDL, DML et DCL : les familles de commandes SQL",
        "Distinguer les commandes de définition, manipulation et contrôle des données.",
        [
            S(
                "À quelle famille appartient l'instruction CREATE TABLE ?",
                ["DDL (Data Definition Language)", "DML (Data Manipulation Language)", "DCL (Data Control Language)", "TCL (Transaction Control Language)"],
            ),
            Sx(
                "À quelle famille appartiennent INSERT, UPDATE et DELETE ?",
                ["DML (Data Manipulation Language)", "DDL (Data Definition Language)", "DCL (Data Control Language)", "DQL uniquement, jamais DML"],
                0,
            ),
            S(
                "À quelle famille appartiennent GRANT et REVOKE ?",
                ["DCL (Data Control Language)", "DDL (Data Definition Language)", "DML (Data Manipulation Language)", "TCL (Transaction Control Language)"],
            ),
            M(
                "Quelles instructions appartiennent au DDL ?",
                ["CREATE TABLE", "DROP TABLE"],
                ["SELECT", "INSERT"],
            ),
            T("DROP TABLE supprime définitivement la structure et les données d'une table.", True),
            T("SELECT fait partie du DCL (Data Control Language).", False),
        ],
    ),
    quiz(
        "GRANT et REVOKE : gérer les droits d'accès",
        "Notions de base sur le contrôle des permissions en SQL.",
        [
            S(
                "Quelle instruction donne le droit SELECT sur la table clients à l'utilisateur alice ?",
                [
                    "GRANT SELECT ON clients TO alice;",
                    "GRANT alice SELECT ON clients;",
                    "ALLOW SELECT clients TO alice;",
                    "GRANT SELECT clients FOR alice;",
                ],
            ),
            Sx(
                "Quelle instruction retire le droit INSERT sur la table produits à l'utilisateur bob ?",
                [
                    "REVOKE INSERT ON produits FROM bob;",
                    "REVOKE bob INSERT ON produits;",
                    "DENY INSERT produits TO bob;",
                    "REVOKE INSERT produits FOR bob;",
                ],
                0,
            ),
            S(
                "GRANT et REVOKE appartiennent à quelle famille de commandes SQL ?",
                ["DCL (Data Control Language)", "DDL (Data Definition Language)", "DML (Data Manipulation Language)", "TCL (Transaction Control Language)"],
            ),
            M(
                "Quelles affirmations sur GRANT/REVOKE sont correctes ?",
                [
                    "GRANT attribue des privilèges à un utilisateur ou un rôle",
                    "REVOKE retire des privilèges précédemment accordés",
                ],
                ["GRANT supprime des lignes de la table cible", "REVOKE crée automatiquement un nouvel utilisateur"],
            ),
            T("Les privilèges accordés par GRANT peuvent inclure SELECT, INSERT, UPDATE ou DELETE.", True),
            T("REVOKE permet d'ajouter de nouveaux privilèges à un utilisateur.", False),
        ],
    ),
]
