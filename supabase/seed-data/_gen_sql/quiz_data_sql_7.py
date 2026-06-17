from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "Opérateurs de comparaison sur chaînes et nombres",
        "Comparer correctement des valeurs textuelles et numériques.",
        [
            S(
                "Quelle requête sélectionne les produits dont le nom est exactement 'Clavier' (sensible à la casse selon le SGBD) ?",
                [
                    "SELECT * FROM produits WHERE nom = 'Clavier';",
                    "SELECT * FROM produits WHERE nom LIKE Clavier;",
                    "SELECT * FROM produits WHERE nom == 'Clavier';",
                    "SELECT * FROM produits WHERE nom IS 'Clavier';",
                ],
            ),
            Sx(
                "Quel opérateur compare deux valeurs pour vérifier qu'elles sont strictement égales en SQL standard ?",
                ["=", "==", ":=", "EQUALS"],
                0,
            ),
            S(
                "Quelle requête trouve les commandes dont le montant est supérieur ou égal à 100 ?",
                [
                    "SELECT * FROM commandes WHERE montant >= 100;",
                    "SELECT * FROM commandes WHERE montant =< 100;",
                    "SELECT * FROM commandes WHERE montant > = 100;",
                    "SELECT * FROM commandes WHERE montant GE 100;",
                ],
            ),
            M(
                "Quelles affirmations sur les comparaisons en SQL sont vraies ?",
                [
                    "Les chaînes de texte sont généralement comparées selon un ordre lexicographique",
                    "Les opérateurs de comparaison fonctionnent aussi bien sur les nombres que sur le texte ou les dates",
                ],
                ["L'opérateur = ne peut jamais être utilisé avec du texte", "Comparer deux nombres avec > nécessite obligatoirement une conversion en texte"],
            ),
            T("La comparaison de chaînes de texte peut être sensible à la casse selon la configuration du SGBD.", True),
            T("L'opérateur de comparaison == est la syntaxe standard SQL pour tester l'égalité.", False),
        ],
    ),
    quiz(
        "Les jokers % et _ approfondis avec LIKE",
        "Construire des motifs de recherche plus précis avec LIKE.",
        [
            S(
                "Quelle requête trouve les références produits composées exactement de 5 caractères commençant par 'A' ?",
                [
                    "SELECT * FROM produits WHERE reference LIKE 'A____';",
                    "SELECT * FROM produits WHERE reference LIKE 'A%%%%%';",
                    "SELECT * FROM produits WHERE reference LIKE 'A_5';",
                    "SELECT * FROM produits WHERE LENGTH(reference) LIKE 'A';",
                ],
            ),
            Sx(
                "Quel motif LIKE permet de trouver les chaînes se terminant par '.com' ?",
                ["'%.com'", "'.com%'", "'_.com_'", "'.com'"],
                0,
            ),
            S(
                "Quelle requête trouve les noms de produits ne contenant PAS le mot 'test' ?",
                [
                    "SELECT * FROM produits WHERE nom NOT LIKE '%test%';",
                    "SELECT * FROM produits WHERE nom != '%test%';",
                    "SELECT * FROM produits WHERE NOT nom LIKE 'test';",
                    "SELECT * FROM produits WHERE nom EXCLUDE '%test%';",
                ],
            ),
            M(
                "Quelles affirmations sur les motifs LIKE sont vraies ?",
                [
                    "Le caractère % représente zéro, un ou plusieurs caractères",
                    "NOT LIKE permet d'exclure les chaînes correspondant à un motif donné",
                ],
                ["Le caractère _ représente zéro ou plusieurs caractères", "LIKE ne peut jamais être combiné avec NOT"],
            ),
            T("On peut combiner plusieurs jokers % et _ dans un même motif LIKE.", True),
            T("Le caractère _ dans un motif LIKE représente toujours zéro caractère.", False),
        ],
    ),
    quiz(
        "Modélisation : relations one-to-one",
        "Identifier et modéliser les relations un-à-un entre entités.",
        [
            S(
                "Quel exemple illustre typiquement une relation one-to-one ?",
                [
                    "Un utilisateur et son profil détaillé unique (table utilisateurs et table profils)",
                    "Un client et ses multiples commandes",
                    "Un produit et ses multiples catégories",
                    "Un étudiant et ses multiples cours suivis",
                ],
            ),
            Sx(
                "Comment représente-t-on souvent une relation one-to-one entre deux tables ?",
                [
                    "Avec une clé étrangère unique (contrainte UNIQUE) dans une des deux tables",
                    "Avec une table de jointure intermédiaire obligatoire",
                    "En fusionnant systématiquement les deux tables en une seule sans exception",
                    "Il est impossible de modéliser une relation one-to-one en SQL",
                ],
                0,
            ),
            S(
                "Pourquoi sépare-t-on parfois des données en relation one-to-one en deux tables plutôt qu'une seule ?",
                [
                    "Pour isoler des données peu consultées ou sensibles, ou des colonnes optionnelles",
                    "Parce que SQL interdit plus de 10 colonnes par table",
                    "Parce qu'une table ne peut contenir qu'un seul type de donnée",
                    "Cela n'a jamais aucun intérêt pratique",
                ],
            ),
            M(
                "Quelles affirmations sur les relations one-to-one sont vraies ?",
                [
                    "Une contrainte UNIQUE sur la clé étrangère garantit le caractère one-to-one de la relation",
                    "Une relation one-to-one peut parfois être fusionnée en une seule table par simplicité",
                ],
                ["Une relation one-to-one nécessite toujours une table de jointure intermédiaire", "Une relation one-to-one est identique à une relation many-to-many"],
            ),
            T("Une relation one-to-one signifie qu'une ligne d'une table correspond à au plus une ligne d'une autre table.", True),
            T("Une relation one-to-one nécessite obligatoirement trois tables pour être représentée.", False),
        ],
    ),
    quiz(
        "Sous-requêtes avec NOT IN et pièges du NULL",
        "Identifier les pièges classiques de NOT IN en présence de NULL.",
        [
            S(
                "Quelle requête tente de trouver les clients n'ayant jamais commandé via NOT IN ?",
                [
                    "SELECT * FROM clients WHERE id NOT IN (SELECT client_id FROM commandes);",
                    "SELECT * FROM clients WHERE id NOT EXISTS commandes;",
                    "SELECT * FROM clients WHERE id != ALL commandes;",
                    "SELECT * FROM clients WHERE NOT id IN commandes;",
                ],
            ),
            Sx(
                "Quel piège classique peut survenir si la sous-requête de NOT IN contient une valeur NULL ?",
                [
                    "La requête peut ne retourner aucune ligne du tout, même si elle semble correcte",
                    "La requête provoque toujours une erreur de syntaxe",
                    "NULL est automatiquement ignoré sans aucun impact sur le résultat",
                    "NOT IN se comporte alors exactement comme NOT EXISTS sans différence",
                ],
                0,
            ),
            S(
                "Quelle alternative à NOT IN est souvent recommandée pour éviter les pièges liés à NULL ?",
                [
                    "Utiliser NOT EXISTS avec une sous-requête corrélée",
                    "Utiliser UNION ALL à la place",
                    "Utiliser GROUP BY systématiquement",
                    "Il n'existe aucune alternative possible",
                ],
            ),
            M(
                "Quelles affirmations sur NOT IN et NULL sont vraies ?",
                [
                    "Si la liste de NOT IN contient un NULL, le résultat global peut devenir vide de façon contre-intuitive",
                    "NOT EXISTS est souvent plus sûr que NOT IN en présence de valeurs NULL potentielles",
                ],
                ["NOT IN gère toujours parfaitement les valeurs NULL sans aucun piège", "NULL n'a aucune incidence sur le comportement de NOT IN"],
            ),
            T("Il est recommandé de filtrer les NULL avant d'utiliser NOT IN avec une sous-requête, ou de préférer NOT EXISTS.", True),
            T("NOT IN se comporte toujours de façon strictement identique à NOT EXISTS, quelle que soit la présence de NULL.", False),
        ],
    ),
    quiz(
        "Triggers AFTER et cas d'usage avancés",
        "Approfondir les triggers déclenchés après une opération.",
        [
            S(
                "Quel type de trigger est typiquement utilisé pour journaliser une modification après qu'elle a eu lieu ?",
                ["AFTER UPDATE", "BEFORE SELECT", "INSTEAD OF SELECT", "ON COMMIT ONLY"],
            ),
            Sx(
                "Pourquoi un trigger AFTER DELETE est-il adapté pour archiver les lignes supprimées ?",
                [
                    "Parce qu'il se déclenche une fois la suppression effectuée, permettant de capturer les anciennes valeurs",
                    "Parce qu'il empêche systématiquement la suppression",
                    "Parce qu'il s'exécute avant que la suppression ne soit confirmée",
                    "Un trigger AFTER DELETE ne peut jamais accéder aux anciennes valeurs",
                ],
                0,
            ),
            S(
                "Quel risque potentiel est associé à un usage excessif de triggers complexes ?",
                [
                    "Une logique métier difficile à suivre et des effets de bord cachés lors des opérations",
                    "Une impossibilité totale d'insérer des données",
                    "La suppression automatique de toutes les contraintes",
                    "Aucun risque, les triggers n'ont jamais d'effet de bord",
                ],
            ),
            M(
                "Quelles affirmations sur les triggers AFTER sont vraies ?",
                [
                    "Ils peuvent être utilisés pour maintenir des tables d'audit ou d'historique",
                    "Ils s'exécutent après que l'opération déclenchante a été appliquée",
                ],
                ["Ils empêchent toujours l'opération déclenchante de s'exécuter", "Ils ne peuvent réagir qu'aux opérations SELECT"],
            ),
            T("Un trigger peut être configuré pour se déclencher sur INSERT, UPDATE ou DELETE selon le besoin.", True),
            T("Un trigger AFTER INSERT s'exécute avant que la ligne ne soit réellement insérée dans la table.", False),
        ],
    ),
    quiz(
        "EXCEPT/MINUS et analyse de différences",
        "Identifier les écarts entre deux ensembles de données avec EXCEPT.",
        [
            S(
                "Quelle requête trouve les produits présents dans le catalogue mais jamais commandés ?",
                [
                    "SELECT id FROM produits EXCEPT SELECT produit_id FROM commandes;",
                    "SELECT id FROM produits INTERSECT SELECT produit_id FROM commandes;",
                    "SELECT id FROM produits UNION SELECT produit_id FROM commandes;",
                    "SELECT id FROM produits WHERE id = commandes.produit_id;",
                ],
            ),
            Sx(
                "Quelle alternative à EXCEPT utilise une sous-requête avec NOT IN pour le même résultat ?",
                [
                    "SELECT id FROM produits WHERE id NOT IN (SELECT produit_id FROM commandes);",
                    "SELECT id FROM produits WHERE id IN (SELECT produit_id FROM commandes);",
                    "SELECT id FROM produits WHERE id EXISTS commandes;",
                    "SELECT id FROM produits MINUS commandes.id;",
                ],
                0,
            ),
            S(
                "Dans certains SGBD comme Oracle, quel mot-clé est utilisé à la place d'EXCEPT ?",
                ["MINUS", "DIFF", "SUBTRACT", "WITHOUT"],
            ),
            M(
                "Quelles affirmations sur EXCEPT sont vraies ?",
                [
                    "EXCEPT retourne les lignes de la première requête absentes du résultat de la seconde",
                    "EXCEPT élimine les doublons du résultat final par défaut",
                ],
                ["EXCEPT retourne toujours toutes les lignes des deux requêtes réunies", "EXCEPT nécessite que les deux requêtes proviennent de la même table physique"],
            ),
            T("L'ordre des requêtes autour de EXCEPT a une influence directe sur le résultat obtenu.", True),
            T("EXCEPT est strictement équivalent à INTERSECT dans tous les cas.", False),
        ],
    ),
    quiz(
        "Sous-requêtes corrélées avec UPDATE",
        "Mettre à jour une table en utilisant des valeurs calculées via corrélation.",
        [
            S(
                "Quelle requête met à jour le champ total_commandes de chaque client avec le nombre réel de ses commandes ?",
                [
                    "UPDATE clients c SET total_commandes = (SELECT COUNT(*) FROM commandes co WHERE co.client_id = c.id);",
                    "UPDATE clients SET total_commandes = COUNT(*) FROM commandes;",
                    "UPDATE clients c SET total_commandes = COUNT(commandes);",
                    "UPDATE clients SET total_commandes = (SELECT COUNT(*) FROM commandes);",
                ],
            ),
            Sx(
                "Pourquoi la sous-requête de cet UPDATE doit-elle référencer c.id (alias de la table externe) ?",
                [
                    "Pour calculer un résultat spécifique à chaque ligne de clients plutôt qu'une valeur globale",
                    "Parce que c'est obligatoire syntaxiquement même sans corrélation",
                    "Pour empêcher toute mise à jour de la table",
                    "Cela n'a aucune utilité particulière",
                ],
                0,
            ),
            S(
                "Quelle requête met à jour le prix des produits pour qu'il corresponde à la moyenne de leur catégorie ?",
                [
                    "UPDATE produits p SET prix = (SELECT AVG(prix) FROM produits WHERE categorie = p.categorie);",
                    "UPDATE produits SET prix = AVG(prix) GROUP BY categorie;",
                    "UPDATE produits SET prix = AVG(prix);",
                    "UPDATE produits p SET prix = AVG(p.prix) WHERE categorie = p.categorie;",
                ],
            ),
            M(
                "Quelles affirmations sur les sous-requêtes corrélées dans UPDATE sont vraies ?",
                [
                    "Elles permettent de calculer une valeur différente pour chaque ligne mise à jour",
                    "Elles référencent la table cible de l'UPDATE via un alias",
                ],
                ["Elles ne peuvent jamais utiliser de fonction d'agrégation", "Elles s'exécutent une seule fois pour toute la table sans tenir compte de chaque ligne"],
            ),
            T("Une sous-requête corrélée dans un UPDATE est réévaluée pour chaque ligne mise à jour.", True),
            T("Un UPDATE avec sous-requête corrélée ne peut jamais utiliser AVG, SUM ou COUNT.", False),
        ],
    ),
    quiz(
        "Transactions concurrentes et verrous (notions)",
        "Comprendre les problèmes classiques liés à la concurrence d'accès.",
        [
            S(
                "Que désigne le terme 'lecture sale' (dirty read) en gestion de transactions ?",
                [
                    "Lire des données modifiées par une transaction non encore validée (committée)",
                    "Lire des données après leur suppression définitive",
                    "Lire une table vide par erreur",
                    "Lire des données dans le désordre alphabétique",
                ],
            ),
            Sx(
                "Quel mécanisme empêche généralement deux transactions de modifier simultanément la même ligne de façon incohérente ?",
                [
                    "Les verrous (locks) posés sur les lignes ou tables concernées",
                    "La suppression automatique de la table concernée",
                    "L'absence totale de contrôle, par conception du SQL",
                    "Le redémarrage systématique du serveur de base de données",
                ],
                0,
            ),
            S(
                "Quel niveau d'isolation est généralement le plus strict, limitant le plus les anomalies de concurrence ?",
                ["SERIALIZABLE", "READ UNCOMMITTED", "READ COMMITTED basique", "Aucun niveau n'existe en SQL"],
            ),
            M(
                "Quelles affirmations sur la concurrence des transactions sont vraies ?",
                [
                    "Un niveau d'isolation plus strict peut réduire la performance en cas de forte concurrence",
                    "Les verrous permettent d'éviter certaines incohérences entre transactions simultanées",
                ],
                ["La concurrence n'a jamais d'impact sur les résultats des transactions", "READ UNCOMMITTED est le niveau d'isolation le plus strict possible"],
            ),
            T("Des transactions concurrentes mal isolées peuvent produire des lectures incohérentes (dirty read, phantom read).", True),
            T("Le niveau d'isolation SERIALIZABLE autorise systématiquement les lectures sales (dirty reads).", False),
        ],
    ),
    quiz(
        "Vues avec agrégation et jointures",
        "Créer des vues combinant calculs et jointures pour simplifier l'accès aux données.",
        [
            S(
                "Quelle vue affiche, pour chaque client, son nombre total de commandes ?",
                [
                    "CREATE VIEW stats_clients AS SELECT c.id, c.nom, COUNT(co.id) AS nb_commandes FROM clients c LEFT JOIN commandes co ON c.id = co.client_id GROUP BY c.id, c.nom;",
                    "CREATE VIEW stats_clients AS SELECT COUNT(*) FROM clients;",
                    "CREATE VIEW stats_clients SELECT client_id FROM commandes GROUP BY client_id;",
                    "CREATE TABLE stats_clients AS SELECT * FROM clients JOIN commandes;",
                ],
            ),
            Sx(
                "Quel avantage offre une vue combinant jointure et agrégation par rapport à répéter la requête partout ?",
                [
                    "Elle centralise la logique et simplifie les requêtes futures qui s'appuient sur cette vue",
                    "Elle supprime totalement le besoin des tables sources",
                    "Elle empêche toute mise à jour future des données",
                    "Elle accélère systématiquement toutes les requêtes sans exception",
                ],
                0,
            ),
            S(
                "Quelle requête interroge simplement la vue stats_clients pour les clients ayant plus de 5 commandes ?",
                [
                    "SELECT * FROM stats_clients WHERE nb_commandes > 5;",
                    "SELECT * FROM stats_clients HAVING nb_commandes > 5;",
                    "SELECT * FROM clients WHERE nb_commandes > 5;",
                    "SELECT * FROM stats_clients GROUP BY nb_commandes > 5;",
                ],
            ),
            M(
                "Quelles affirmations sur les vues agrégées sont vraies ?",
                [
                    "Une vue peut inclure GROUP BY, JOIN et des fonctions d'agrégation",
                    "Interroger une vue agrégée revient à exécuter la requête sous-jacente",
                ],
                ["Une vue agrégée stocke physiquement le résultat calculé de façon permanente par défaut", "Une vue ne peut jamais contenir de LEFT JOIN"],
            ),
            T("Une vue peut simplifier l'accès à des données complexes provenant de plusieurs tables agrégées.", True),
            T("Une vue standard (non matérialisée) recalcule son résultat à chaque interrogation.", True),
        ],
    ),
    quiz(
        "Conversion de types (CAST)",
        "Convertir explicitement une valeur d'un type vers un autre.",
        [
            S(
                "Quelle syntaxe convertit la colonne texte prix_texte en valeur numérique ?",
                [
                    "CAST(prix_texte AS NUMERIC)",
                    "CONVERT_TO(prix_texte, NUMERIC)",
                    "prix_texte::FORCE_NUMERIC",
                    "TO_NUMBER_ONLY(prix_texte)",
                ],
            ),
            Sx(
                "Pourquoi peut-il être nécessaire d'utiliser CAST avant de comparer deux colonnes ?",
                [
                    "Parce que les colonnes peuvent avoir des types différents incompatibles pour une comparaison directe",
                    "Parce que CAST est obligatoire avant chaque requête SELECT",
                    "Parce que sans CAST, aucune colonne ne peut être affichée",
                    "CAST n'a aucune utilité réelle en SQL",
                ],
                0,
            ),
            S(
                "Quelle expression convertit une date en chaîne de caractères pour l'afficher dans un rapport ?",
                [
                    "CAST(date_commande AS TEXT)",
                    "TEXT(date_commande) AS DATE",
                    "date_commande AS TEXT()",
                    "STRING_OF(date_commande)",
                ],
            ),
            M(
                "Quelles affirmations sur CAST sont vraies ?",
                [
                    "CAST permet de convertir explicitement un type de données vers un autre",
                    "Une conversion peut échouer si la valeur source n'est pas compatible avec le type cible",
                ],
                ["CAST modifie définitivement le type de la colonne dans la table", "CAST ne peut être utilisé que sur des colonnes numériques"],
            ),
            T("CAST(valeur AS type) est une syntaxe standard pour convertir explicitement un type de données.", True),
            T("CAST modifie la définition permanente du type de colonne dans le schéma de la table.", False),
        ],
    ),
    quiz(
        "Sous-requêtes pour le top-N par groupe",
        "Trouver les meilleurs éléments de chaque catégorie avec des sous-requêtes ou fenêtrage.",
        [
            S(
                "Quelle requête trouve le produit le plus cher de chaque catégorie en utilisant une fonction de fenêtrage ?",
                [
                    "SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY categorie ORDER BY prix DESC) AS rg FROM produits) t WHERE rg = 1;",
                    "SELECT categorie, MAX(prix) FROM produits;",
                    "SELECT * FROM produits ORDER BY prix DESC LIMIT 1;",
                    "SELECT * FROM produits GROUP BY categorie HAVING prix = MAX(prix);",
                ],
            ),
            Sx(
                "Pourquoi `SELECT categorie, MAX(prix) FROM produits GROUP BY categorie;` ne donne-t-il pas directement le nom du produit le plus cher ?",
                [
                    "Parce que GROUP BY agrège les lignes et ne permet pas d'afficher facilement une colonne non agrégée comme le nom sans risque d'ambiguïté",
                    "Parce que MAX() ne fonctionne jamais avec GROUP BY",
                    "Parce que cette requête est invalide et ne s'exécute jamais",
                    "Parce que categorie ne peut pas apparaître dans le SELECT avec GROUP BY",
                ],
                0,
            ),
            S(
                "Quelle approche alternative aux fonctions de fenêtrage permet de trouver le top-1 par catégorie via une sous-requête corrélée ?",
                [
                    "SELECT * FROM produits p WHERE prix = (SELECT MAX(prix) FROM produits WHERE categorie = p.categorie);",
                    "SELECT * FROM produits WHERE prix = MAX(prix);",
                    "SELECT * FROM produits GROUP BY categorie WHERE prix = MAX(prix);",
                    "SELECT * FROM produits ORDER BY categorie LIMIT 1;",
                ],
            ),
            M(
                "Quelles affirmations sur le calcul du top-N par groupe sont vraies ?",
                [
                    "Les fonctions de fenêtrage comme ROW_NUMBER() simplifient ce type de calcul",
                    "Une sous-requête corrélée avec MAX() est une alternative possible aux fonctions de fenêtrage",
                ],
                ["GROUP BY seul suffit toujours à afficher la ligne complète du maximum", "Le calcul du top-N par groupe est impossible en SQL"],
            ),
            T("Les fonctions de fenêtrage facilitent grandement le calcul du top-N par groupe par rapport aux approches plus anciennes.", True),
            T("GROUP BY combiné à MAX() retourne automatiquement toutes les colonnes de la ligne correspondant au maximum.", False),
        ],
    ),
    quiz(
        "Bilan : DDL, DML, contraintes et requêtes combinées",
        "Synthèse transversale sur la conception et l'interrogation d'une base SQL.",
        [
            S(
                "Quelle séquence d'instructions est cohérente pour créer une table puis y insérer une ligne ?",
                [
                    "CREATE TABLE puis INSERT INTO",
                    "INSERT INTO puis CREATE TABLE",
                    "DROP TABLE puis INSERT INTO",
                    "ALTER TABLE puis CREATE TABLE",
                ],
            ),
            Sx(
                "Pourquoi est-il important de définir les contraintes (clé primaire, clé étrangère) dès la création de la table ?",
                [
                    "Pour garantir l'intégrité des données dès le départ plutôt que de corriger des problèmes après coup",
                    "Parce que les contraintes ne peuvent jamais être ajoutées après coup, même par ALTER TABLE",
                    "Parce que cela accélère systématiquement toutes les requêtes sans exception",
                    "Les contraintes n'ont en réalité aucun impact réel sur l'application",
                ],
                0,
            ),
            S(
                "Quelle requête combine une jointure, un filtre, un regroupement et un tri en une seule instruction ?",
                [
                    "SELECT c.ville, COUNT(*) FROM clients c JOIN commandes co ON c.id = co.client_id WHERE co.montant > 50 GROUP BY c.ville ORDER BY COUNT(*) DESC;",
                    "SELECT c.ville FROM clients c GROUP BY co.montant WHERE COUNT(*) > 50;",
                    "SELECT c.ville, COUNT(*) FROM clients c ORDER BY co.montant JOIN commandes co;",
                    "SELECT COUNT(*) FROM clients JOIN commandes WHERE GROUP BY ORDER BY;",
                ],
            ),
            M(
                "Quelles affirmations résument bien les familles de commandes SQL ?",
                [
                    "Le DDL définit la structure (CREATE, ALTER, DROP)",
                    "Le DML manipule les données (SELECT, INSERT, UPDATE, DELETE)",
                ],
                ["Le DCL sert à trier les résultats d'une requête", "Le DDL et le DML désignent exactement la même chose"],
            ),
            T("Une base de données bien conçue combine généralement DDL pour la structure et DML pour l'exploitation des données.", True),
            T("Le DML (INSERT, UPDATE, DELETE) sert à définir la structure des tables.", False),
        ],
    ),
]
