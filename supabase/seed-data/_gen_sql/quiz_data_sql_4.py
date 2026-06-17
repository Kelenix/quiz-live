from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "Les index : principes de base",
        "Comprendre à quoi servent les index dans une base de données.",
        [
            S(
                "Quelle instruction crée un index sur la colonne email de la table clients ?",
                [
                    "CREATE INDEX idx_email ON clients (email);",
                    "CREATE INDEX clients ON email;",
                    "ADD INDEX email TO clients;",
                    "CREATE INDEX ON clients SET email;",
                ],
            ),
            Sx(
                "Quel est le principal objectif d'un index ?",
                [
                    "Accélérer la recherche et le filtrage de lignes sur une colonne",
                    "Empêcher toute modification de la colonne indexée",
                    "Supprimer automatiquement les doublons de la colonne",
                    "Convertir le type de données de la colonne",
                ],
                0,
            ),
            S(
                "Sur quel type de colonne est-il particulièrement pertinent de créer un index ?",
                [
                    "Une colonne fréquemment utilisée dans les clauses WHERE ou JOIN",
                    "Une colonne jamais utilisée dans les requêtes",
                    "Une colonne contenant des valeurs très volumineuses sans recherche associée",
                    "Une colonne mise à jour en continu et jamais lue",
                ],
            ),
            M(
                "Quelles affirmations sur les index sont vraies ?",
                [
                    "Un index peut accélérer les requêtes de lecture",
                    "La clé primaire est généralement indexée automatiquement",
                ],
                ["Un index élimine totalement le besoin de clause WHERE", "Un index garantit que les données ne pourront jamais être nulles"],
            ),
            T("Un index occupe de l'espace disque supplémentaire en plus des données de la table.", True),
            T("Créer un index n'a strictement aucun impact sur la rapidité des opérations d'écriture.", False),
        ],
    ),
    quiz(
        "Index : avantages et coûts",
        "Peser les bénéfices d'un index face à ses inconvénients.",
        [
            S(
                "Quel est un avantage typique de l'utilisation d'un index ?",
                [
                    "Des recherches plus rapides sur la colonne indexée",
                    "Une réduction automatique de la taille de la table",
                    "Une suppression automatique des contraintes",
                    "Une garantie d'unicité sur toutes les colonnes de la table",
                ],
            ),
            Sx(
                "Quel est un inconvénient potentiel de la multiplication des index sur une table ?",
                [
                    "Les opérations INSERT, UPDATE et DELETE peuvent devenir plus lentes",
                    "Les requêtes SELECT deviennent systématiquement plus lentes",
                    "La table devient automatiquement en lecture seule",
                    "Les contraintes CHECK sont désactivées",
                ],
                0,
            ),
            S(
                "Pourquoi est-il déconseillé d'indexer une colonne avec très peu de valeurs distinctes (ex: un booléen) ?",
                [
                    "L'index apporte peu de gain car il ne permet pas de filtrer efficacement",
                    "Cela rend la colonne immuable définitivement",
                    "C'est techniquement impossible dans tous les SGBD",
                    "Cela transforme automatiquement la colonne en clé primaire",
                ],
            ),
            M(
                "Quelles affirmations sur le coût des index sont correctes ?",
                [
                    "Chaque index doit être mis à jour à chaque modification des données indexées",
                    "Trop d'index peuvent ralentir les écritures sans bénéfice proportionnel en lecture",
                ],
                ["Les index sont toujours gratuits en espace de stockage", "Les index accélèrent toujours les opérations d'écriture"],
            ),
            T("Le choix des colonnes à indexer doit tenir compte des requêtes les plus fréquentes de l'application.", True),
            T("Il est recommandé d'indexer systématiquement toutes les colonnes d'une table sans réflexion.", False),
        ],
    ),
    quiz(
        "Normalisation : la première forme normale (1NF)",
        "Éliminer les groupes répétitifs et garantir l'atomicité des données.",
        [
            S(
                "Quelle condition une table doit-elle respecter pour être en 1NF ?",
                [
                    "Chaque colonne contient une valeur atomique, sans liste ni groupe répétitif",
                    "Chaque colonne doit contenir uniquement des nombres",
                    "La table ne doit avoir aucune clé primaire",
                    "Chaque ligne doit contenir au moins une valeur NULL",
                ],
            ),
            Sx(
                "Quel exemple viole la première forme normale (1NF) ?",
                [
                    "Une colonne 'telephones' contenant '0601020304, 0611223344' dans une seule cellule",
                    "Une colonne 'email' contenant une seule adresse par ligne",
                    "Une colonne 'id' de type entier unique",
                    "Une colonne 'date_naissance' de type date",
                ],
                0,
            ),
            S(
                "Quelle solution permet de respecter la 1NF pour des numéros de téléphone multiples ?",
                [
                    "Créer une table séparée téléphones liée par une clé étrangère",
                    "Stocker tous les numéros séparés par des virgules dans une seule colonne",
                    "Limiter chaque client à un seul numéro pour toujours",
                    "Ignorer la 1NF car elle n'est pas obligatoire",
                ],
            ),
            M(
                "Quelles affirmations sur la 1NF sont vraies ?",
                [
                    "La 1NF exige l'atomicité des valeurs de chaque colonne",
                    "La 1NF interdit les colonnes contenant des listes de valeurs",
                ],
                ["La 1NF exige qu'il n'y ait aucune clé primaire", "La 1NF est moins stricte que la 3NF"],
            ),
            T("La 1NF est considérée comme le niveau de normalisation le plus basique.", True),
            T("Une table en 1NF peut contenir une colonne avec plusieurs valeurs séparées par des virgules.", False),
        ],
    ),
    quiz(
        "Normalisation : 2NF et 3NF",
        "Éliminer les dépendances partielles et transitives.",
        [
            S(
                "Quelle condition supplémentaire impose la deuxième forme normale (2NF) par rapport à la 1NF ?",
                [
                    "Chaque attribut non-clé doit dépendre entièrement de la clé primaire complète",
                    "Chaque table doit contenir au moins deux clés primaires",
                    "Toutes les colonnes doivent être de type texte",
                    "Aucune colonne ne peut référencer une autre table",
                ],
            ),
            Sx(
                "Quel problème la troisième forme normale (3NF) cherche-t-elle à éliminer ?",
                [
                    "Les dépendances transitives entre attributs non-clés",
                    "Les valeurs NULL dans les colonnes obligatoires",
                    "Les contraintes UNIQUE redondantes",
                    "Les jointures multiples dans les requêtes",
                ],
                0,
            ),
            S(
                "Dans une table commandes(id, client_id, ville_client) où ville_client dépend de client_id et non de id, quelle est la forme normale violée ?",
                [
                    "2NF, car ville_client ne dépend pas directement de la clé primaire id",
                    "1NF, car la colonne ville_client contient une liste",
                    "Aucune, la table est parfaitement normalisée",
                    "3NF uniquement, jamais la 2NF",
                ],
            ),
            M(
                "Quelles affirmations sur la normalisation sont correctes ?",
                [
                    "La normalisation vise à réduire la redondance des données",
                    "Une table en 3NF est nécessairement en 2NF et en 1NF",
                ],
                ["La normalisation augmente toujours les performances de lecture sans aucune contrepartie", "La 2NF s'applique uniquement aux tables sans clé primaire"],
            ),
            T("La dénormalisation est parfois choisie volontairement pour améliorer les performances de lecture.", True),
            T("Une base de données doit obligatoirement atteindre la 3NF pour fonctionner correctement.", False),
        ],
    ),
    quiz(
        "Transactions et propriétés ACID",
        "Garantir la fiabilité des opérations avec les transactions.",
        [
            S(
                "Que signifie l'acronyme ACID appliqué aux transactions ?",
                [
                    "Atomicité, Cohérence, Isolation, Durabilité",
                    "Accès, Contrôle, Index, Données",
                    "Automatisation, Cache, Intégrité, Disponibilité",
                    "Atomicité, Compression, Isolation, Disponibilité",
                ],
            ),
            Sx(
                "Que garantit la propriété d'atomicité d'une transaction ?",
                [
                    "Soit toutes les opérations de la transaction réussissent, soit aucune n'est appliquée",
                    "Les transactions s'exécutent toujours plus vite",
                    "Les données sont automatiquement dupliquées sur plusieurs serveurs",
                    "Chaque transaction doit contenir une seule instruction SQL",
                ],
                0,
            ),
            S(
                "Quelle propriété ACID garantit que les résultats d'une transaction validée persistent même après une panne ?",
                ["La durabilité (Durability)", "L'isolation (Isolation)", "La cohérence (Consistency)", "L'atomicité (Atomicity)"],
            ),
            M(
                "Quelles affirmations sur les transactions sont correctes ?",
                [
                    "Une transaction regroupe un ensemble d'opérations exécutées comme un tout",
                    "L'isolation limite les interférences entre transactions concurrentes",
                ],
                ["Une transaction ne peut jamais être annulée une fois commencée", "ACID signifie que les transactions sont toujours instantanées"],
            ),
            T("La cohérence garantit que la base reste dans un état valide avant et après la transaction.", True),
            T("Une transaction ne peut contenir qu'une seule instruction SQL au maximum.", False),
        ],
    ),
    quiz(
        "COMMIT, ROLLBACK et niveaux d'isolation",
        "Valider ou annuler une transaction, et gérer la concurrence.",
        [
            S(
                "Quelle instruction valide définitivement les modifications effectuées dans une transaction ?",
                ["COMMIT;", "SAVE;", "CONFIRM;", "APPLY;"],
            ),
            Sx(
                "Quelle instruction annule toutes les modifications effectuées depuis le début de la transaction ?",
                ["ROLLBACK;", "CANCEL;", "UNDO;", "RESET;"],
                0,
            ),
            S(
                "Quelle instruction démarre explicitement une nouvelle transaction dans de nombreux SGBD ?",
                ["BEGIN TRANSACTION;", "START QUERY;", "OPEN TRANSACTION;", "NEW TRANSACTION;"],
            ),
            M(
                "Quelles affirmations sur les niveaux d'isolation sont correctes ?",
                [
                    "Un niveau d'isolation élevé réduit les risques de lectures incohérentes entre transactions concurrentes",
                    "READ COMMITTED et SERIALIZABLE sont des exemples de niveaux d'isolation",
                ],
                ["Le niveau d'isolation n'a aucun impact sur les performances", "ROLLBACK valide définitivement les modifications"],
            ),
            T("Après un COMMIT réussi, les modifications de la transaction sont normalement irréversibles via ROLLBACK.", True),
            T("ROLLBACK permet de valider de façon permanente les modifications d'une transaction.", False),
        ],
    ),
    quiz(
        "Les vues (CREATE VIEW)",
        "Créer des requêtes réutilisables sous forme de vues virtuelles.",
        [
            S(
                "Quelle instruction crée une vue affichant uniquement les clients parisiens ?",
                [
                    "CREATE VIEW clients_paris AS SELECT * FROM clients WHERE ville = 'Paris';",
                    "CREATE TABLE VIEW clients_paris SELECT * FROM clients WHERE ville = 'Paris';",
                    "CREATE VIEW clients_paris VALUES (SELECT * FROM clients WHERE ville = 'Paris');",
                    "NEW VIEW clients_paris FROM clients WHERE ville = 'Paris';",
                ],
            ),
            Sx(
                "Une vue stocke-t-elle physiquement ses propres données indépendamment des tables sources ?",
                [
                    "Non, une vue classique exécute sa requête sous-jacente à chaque utilisation",
                    "Oui, une vue duplique toujours les données des tables sources",
                    "Oui, mais uniquement pour les vues contenant un GROUP BY",
                    "Non, une vue ne peut jamais être interrogée avec SELECT",
                ],
                0,
            ),
            S(
                "Quel est un avantage principal de l'utilisation des vues ?",
                [
                    "Simplifier des requêtes complexes réutilisées fréquemment",
                    "Augmenter la taille physique de la base de données",
                    "Remplacer totalement le besoin de tables",
                    "Empêcher toute lecture des données sources",
                ],
            ),
            M(
                "Quelles affirmations sur les vues sont vraies ?",
                [
                    "Une vue peut être interrogée avec SELECT comme une table",
                    "Certaines vues simples peuvent être mises à jour (INSERT/UPDATE) selon le SGBD",
                ],
                ["Une vue remplace obligatoirement la table d'origine", "Une vue ne peut jamais contenir de jointure"],
            ),
            T("DROP VIEW permet de supprimer une vue sans affecter les données des tables sources.", True),
            T("Une vue duplique physiquement toutes les données de la requête à chaque création.", False),
        ],
    ),
    quiz(
        "CTE : l'expression WITH ... AS",
        "Structurer des requêtes complexes avec des Common Table Expressions.",
        [
            S(
                "Quelle syntaxe définit une CTE nommée ventes_resume ?",
                [
                    "WITH ventes_resume AS (SELECT client_id, SUM(montant) AS total FROM commandes GROUP BY client_id) SELECT * FROM ventes_resume;",
                    "CREATE CTE ventes_resume (SELECT client_id, SUM(montant) FROM commandes);",
                    "SELECT * FROM (CTE ventes_resume AS SELECT ...);",
                    "WITH ventes_resume = SELECT client_id, SUM(montant) FROM commandes;",
                ],
            ),
            Sx(
                "Quel est l'un des principaux intérêts d'une CTE par rapport à une sous-requête imbriquée ?",
                [
                    "Améliorer la lisibilité en nommant et en structurant des étapes intermédiaires",
                    "Empêcher toute utilisation de jointures dans la requête",
                    "Remplacer obligatoirement toutes les vues existantes",
                    "Interdire l'usage de fonctions d'agrégation",
                ],
                0,
            ),
            S(
                "Une CTE peut-elle être référencée plusieurs fois dans la requête principale qui la suit ?",
                [
                    "Oui, une même CTE peut être utilisée plusieurs fois dans la requête",
                    "Non, une CTE ne peut être utilisée qu'une seule fois",
                    "Non, une CTE doit toujours être convertie en vue avant réutilisation",
                    "Oui, mais seulement si elle contient un GROUP BY",
                ],
            ),
            M(
                "Quelles affirmations sur les CTE sont correctes ?",
                [
                    "Une requête peut définir plusieurs CTE séparées par des virgules après WITH",
                    "Une CTE existe uniquement pendant l'exécution de la requête qui la définit",
                ],
                ["Une CTE est stockée de façon permanente comme une table", "WITH ... AS ne peut jamais être combiné avec une jointure"],
            ),
            T("Les CTE peuvent rendre une requête complexe plus lisible en la découpant en étapes nommées.", True),
            T("Une CTE est automatiquement persistée dans le schéma de la base après son exécution.", False),
        ],
    ),
    quiz(
        "CTE récursive : notions de base",
        "Utiliser WITH RECURSIVE pour parcourir des structures hiérarchiques.",
        [
            S(
                "Quel mot-clé introduit une CTE récursive dans la plupart des SGBD ?",
                ["WITH RECURSIVE", "RECURSIVE WITH", "WITH LOOP", "WITH REPEAT"],
            ),
            Sx(
                "Pour quel type de besoin une CTE récursive est-elle particulièrement adaptée ?",
                [
                    "Parcourir une hiérarchie comme un organigramme employé/manager",
                    "Calculer une simple somme sur une colonne",
                    "Trier les résultats par ordre alphabétique",
                    "Supprimer des doublons dans une table",
                ],
                0,
            ),
            S(
                "Une CTE récursive est composée de deux parties combinées par quel opérateur typiquement ?",
                ["UNION ou UNION ALL entre le cas de base et le cas récursif", "INTERSECT entre les deux parties", "JOIN entre les deux parties", "EXCEPT entre les deux parties"],
            ),
            M(
                "Quelles affirmations sur les CTE récursives sont vraies ?",
                [
                    "Elles contiennent un cas de base (ancre) et un cas récursif",
                    "Elles peuvent être utilisées pour explorer des arborescences ou des graphes",
                ],
                ["Elles ne peuvent jamais utiliser UNION ALL", "Elles sont interdites dans le standard SQL"],
            ),
            T("Une CTE récursive mal conçue peut potentiellement boucler indéfiniment sans condition d'arrêt.", True),
            T("WITH RECURSIVE ne peut être utilisé qu'avec des données numériques.", False),
        ],
    ),
    quiz(
        "Fonctions de fenêtrage : ROW_NUMBER et RANK",
        "Numéroter et classer des lignes sans les regrouper.",
        [
            S(
                "Quelle fonction attribue un numéro unique et séquentiel à chaque ligne selon un ordre donné ?",
                ["ROW_NUMBER()", "COUNT()", "GROUP_NUMBER()", "SEQ()"],
            ),
            Sx(
                "Quelle est la différence entre RANK() et DENSE_RANK() en cas d'égalité (ex aequo) ?",
                [
                    "RANK() laisse des trous dans le classement après une égalité, DENSE_RANK() non",
                    "DENSE_RANK() laisse des trous, RANK() jamais",
                    "Les deux fonctions sont strictement identiques en toutes circonstances",
                    "RANK() ne peut être utilisé qu'avec PARTITION BY",
                ],
                0,
            ),
            S(
                "Quelle requête numérote les employés par salaire décroissant au sein de chaque département ?",
                [
                    "SELECT nom, ROW_NUMBER() OVER (PARTITION BY departement ORDER BY salaire DESC) FROM employes;",
                    "SELECT nom, ROW_NUMBER() GROUP BY departement ORDER BY salaire DESC FROM employes;",
                    "SELECT nom, RANK(departement) OVER salaire DESC FROM employes;",
                    "SELECT nom, ROW_NUMBER(salaire) FROM employes PARTITION departement;",
                ],
            ),
            M(
                "Quelles affirmations sur les fonctions de fenêtrage sont correctes ?",
                [
                    "Elles permettent de calculer un résultat sans réduire le nombre de lignes retournées, contrairement à GROUP BY",
                    "PARTITION BY définit des sous-ensembles de lignes sur lesquels la fonction est appliquée séparément",
                ],
                ["Elles remplacent obligatoirement la clause WHERE", "ROW_NUMBER() retourne toujours la même valeur pour toutes les lignes"],
            ),
            T("La clause OVER() est indispensable pour utiliser une fonction de fenêtrage comme ROW_NUMBER().", True),
            T("RANK() et ROW_NUMBER() produisent toujours exactement le même résultat, sans aucune différence.", False),
        ],
    ),
    quiz(
        "PARTITION BY et agrégats de fenêtrage",
        "Calculer des agrégats par groupe sans perdre le détail des lignes.",
        [
            S(
                "Quelle requête calcule le salaire moyen par département tout en affichant chaque employé individuellement ?",
                [
                    "SELECT nom, departement, AVG(salaire) OVER (PARTITION BY departement) FROM employes;",
                    "SELECT nom, departement, AVG(salaire) FROM employes GROUP BY departement;",
                    "SELECT nom, AVG(salaire) PARTITION departement FROM employes;",
                    "SELECT nom, departement FROM employes HAVING AVG(salaire);",
                ],
            ),
            Sx(
                "Quelle est la principale différence entre une fonction de fenêtrage avec PARTITION BY et un GROUP BY classique ?",
                [
                    "PARTITION BY conserve toutes les lignes individuelles, GROUP BY les regroupe en une ligne par groupe",
                    "GROUP BY conserve toutes les lignes, PARTITION BY les regroupe",
                    "Les deux produisent toujours exactement le même nombre de lignes en sortie",
                    "PARTITION BY ne peut être utilisé qu'avec COUNT()",
                ],
                0,
            ),
            S(
                "Quelle requête calcule le total cumulé des ventes triées par date avec une fonction de fenêtrage ?",
                [
                    "SELECT date_vente, SUM(montant) OVER (ORDER BY date_vente) FROM ventes;",
                    "SELECT date_vente, SUM(montant) GROUP BY date_vente ORDER BY date_vente;",
                    "SELECT date_vente, CUMUL(montant) FROM ventes;",
                    "SELECT date_vente, SUM(montant) PARTITION ORDER date_vente FROM ventes;",
                ],
            ),
            M(
                "Quelles affirmations sur PARTITION BY sont vraies ?",
                [
                    "PARTITION BY peut être combiné avec ORDER BY au sein de la clause OVER()",
                    "Sans PARTITION BY, la fonction de fenêtrage s'applique sur l'ensemble du résultat",
                ],
                ["PARTITION BY supprime les lignes ne correspondant pas à la partition", "PARTITION BY est obligatoire pour utiliser une fonction de fenêtrage"],
            ),
            T("Les fonctions de fenêtrage comme SUM() OVER() permettent de calculer des totaux cumulés (running totals).", True),
            T("PARTITION BY est strictement obligatoire pour pouvoir utiliser la clause OVER().", False),
        ],
    ),
    quiz(
        "Types de données SQL",
        "Connaître les principaux types de données utilisés dans les colonnes SQL.",
        [
            S(
                "Quel type de données convient pour stocker un identifiant entier ?",
                ["INT", "TEXT", "BOOLEAN", "DATE"],
            ),
            Sx(
                "Quel type est généralement utilisé pour stocker une valeur monétaire avec précision exacte ?",
                ["DECIMAL ou NUMERIC", "FLOAT uniquement", "BOOLEAN", "TEXT systématiquement"],
                0,
            ),
            S(
                "Quel type de données stocke une valeur vrai/faux ?",
                ["BOOLEAN", "VARCHAR", "INT obligatoirement", "DATE"],
            ),
            M(
                "Quels types sont couramment utilisés pour stocker du texte ?",
                ["VARCHAR", "TEXT"],
                ["DATE", "BOOLEAN"],
            ),
            T("VARCHAR(n) limite généralement la longueur maximale de la chaîne stockée à n caractères.", True),
            T("Le type FLOAT garantit toujours une précision décimale exacte, sans aucune approximation.", False),
        ],
    ),
    quiz(
        "Modélisation de données : schémas et relations",
        "Notions de base sur la conception d'un modèle relationnel (ER).",
        [
            S(
                "Dans un modèle entité-association, qu'est-ce qu'une 'entité' ?",
                [
                    "Un objet ou concept du monde réel représenté par une table",
                    "Une contrainte CHECK sur une colonne",
                    "Une fonction d'agrégation SQL",
                    "Un type d'index particulier",
                ],
            ),
            Sx(
                "Comment modélise-t-on généralement une relation many-to-many (plusieurs-à-plusieurs) entre deux tables ?",
                [
                    "Avec une table de jointure (table associative) contenant les deux clés étrangères",
                    "En ajoutant une colonne unique dans chacune des deux tables",
                    "C'est impossible à modéliser en SQL relationnel",
                    "En fusionnant systématiquement les deux tables en une seule",
                ],
                0,
            ),
            S(
                "Quelle relation correspond à un client pouvant passer plusieurs commandes, chaque commande appartenant à un seul client ?",
                ["Une relation one-to-many (un-à-plusieurs)", "Une relation many-to-many", "Une relation one-to-one", "Aucune relation n'est nécessaire"],
            ),
            M(
                "Quelles affirmations sur la modélisation relationnelle sont correctes ?",
                [
                    "Une clé étrangère est souvent utilisée pour représenter une relation one-to-many",
                    "Un schéma relationnel décrit les tables, leurs colonnes et leurs relations",
                ],
                ["Toutes les relations doivent obligatoirement être many-to-many", "Un modèle relationnel interdit toute relation entre tables"],
            ),
            T("Une table associative (de jointure) contient généralement deux clés étrangères pointant vers les deux tables liées.", True),
            T("Une relation one-to-one ne peut jamais exister dans un modèle relationnel.", False),
        ],
    ),
]
