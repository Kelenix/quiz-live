from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "SELECT : les fondamentaux",
        "Découvrir la syntaxe de base de l'instruction SELECT.",
        [
            S(
                "Quelle requête sélectionne toutes les colonnes de la table clients ?",
                ["SELECT * FROM clients;", "SELECT ALL clients;", "GET * FROM clients;", "SELECT clients.*;"],
            ),
            S(
                "Quelle instruction permet de récupérer uniquement les colonnes nom et email de la table clients ?",
                [
                    "SELECT nom, email FROM clients;",
                    "SELECT nom AND email FROM clients;",
                    "GET nom, email FROM clients;",
                    "SELECT nom, email IN clients;",
                ],
            ),
            Sx(
                "Quel mot-clé permet de renommer une colonne dans le résultat d'une requête ?",
                ["RENAME", "AS", "ALIAS", "LABEL"],
                1,
            ),
            M(
                "Parmi ces clauses, lesquelles peuvent apparaître dans une instruction SELECT ?",
                ["WHERE", "ORDER BY", "FROM"],
                ["LOOP", "DEFINE"],
            ),
            T("L'instruction SELECT permet uniquement de lire des données, sans les modifier.", True),
            T("La requête `SELECT * FROM clients` retourne uniquement la première ligne de la table.", False),
        ],
    ),
    quiz(
        "DISTINCT et alias de colonnes",
        "Éliminer les doublons et renommer les colonnes dans les résultats.",
        [
            S(
                "Quelle requête retourne la liste des villes distinctes présentes dans la table clients ?",
                [
                    "SELECT DISTINCT ville FROM clients;",
                    "SELECT UNIQUE ville FROM clients;",
                    "SELECT ville DISTINCT FROM clients;",
                    "SELECT * DISTINCT FROM clients;",
                ],
            ),
            S(
                "Quelle requête affiche la colonne prix sous l'alias prix_ttc ?",
                [
                    "SELECT prix AS prix_ttc FROM produits;",
                    "SELECT prix RENAME prix_ttc FROM produits;",
                    "SELECT prix -> prix_ttc FROM produits;",
                    "SELECT prix : prix_ttc FROM produits;",
                ],
            ),
            Sx(
                "DISTINCT s'applique sur quoi exactement quand on écrit `SELECT DISTINCT a, b FROM t;` ?",
                [
                    "Sur la colonne a uniquement",
                    "Sur la combinaison des colonnes a et b",
                    "Sur la colonne b uniquement",
                    "Sur toute la table t",
                ],
                1,
            ),
            M(
                "Quelles affirmations sur DISTINCT sont correctes ?",
                [
                    "DISTINCT élimine les lignes en doublon du résultat",
                    "DISTINCT peut ralentir une requête sur de gros volumes",
                ],
                ["DISTINCT modifie les données stockées dans la table", "DISTINCT trie obligatoirement les résultats par ordre alphabétique"],
            ),
            T("Un alias défini avec AS peut être utilisé pour renommer une colonne ou une table.", True),
            T("DISTINCT peut être combiné avec plusieurs colonnes pour dédupliquer sur leur combinaison.", True),
        ],
    ),
    quiz(
        "La clause WHERE et les opérateurs de comparaison",
        "Filtrer les lignes avec WHERE et les opérateurs =, <>, <, >.",
        [
            S(
                "Quelle requête sélectionne les clients dont la ville est 'Lyon' ?",
                [
                    "SELECT * FROM clients WHERE ville = 'Lyon';",
                    "SELECT * FROM clients WHERE ville == Lyon;",
                    "SELECT * FROM clients FILTER ville = 'Lyon';",
                    "SELECT * FROM clients WHEN ville = 'Lyon';",
                ],
            ),
            Sx(
                "Quel opérateur signifie 'différent de' en SQL standard ?",
                ["!==", "<>", "=/=", "NOT="],
                1,
            ),
            S(
                "Quelle requête retourne les produits dont le prix est strictement supérieur à 100 ?",
                [
                    "SELECT * FROM produits WHERE prix > 100;",
                    "SELECT * FROM produits WHERE prix =< 100;",
                    "SELECT * FROM produits HAVING prix > 100;",
                    "SELECT * FROM produits WHERE prix >> 100;",
                ],
            ),
            M(
                "Parmi ces opérateurs, lesquels sont valides dans une clause WHERE ?",
                [">=", "<="],
                ["=>", "=<"],
            ),
            T("La clause WHERE filtre les lignes avant tout regroupement éventuel (GROUP BY).", True),
            T("L'opérateur != n'est jamais accepté par aucun système de gestion de base de données.", False),
        ],
    ),
    quiz(
        "LIKE et la recherche de motifs textuels",
        "Utiliser LIKE avec les jokers % et _ pour filtrer du texte.",
        [
            S(
                "Quelle requête sélectionne les clients dont le nom commence par 'Mar' ?",
                [
                    "SELECT * FROM clients WHERE nom LIKE 'Mar%';",
                    "SELECT * FROM clients WHERE nom LIKE '%Mar';",
                    "SELECT * FROM clients WHERE nom = 'Mar%';",
                    "SELECT * FROM clients WHERE nom CONTAINS 'Mar';",
                ],
            ),
            Sx(
                "Dans un motif LIKE, que représente le caractère _ (underscore) ?",
                [
                    "Exactement un caractère quelconque",
                    "Zéro ou plusieurs caractères",
                    "Un espace obligatoire",
                    "Le début de la chaîne",
                ],
                0,
            ),
            S(
                "Quelle requête trouve les emails contenant 'gmail' n'importe où dans la chaîne ?",
                [
                    "SELECT * FROM clients WHERE email LIKE '%gmail%';",
                    "SELECT * FROM clients WHERE email LIKE 'gmail';",
                    "SELECT * FROM clients WHERE email LIKE '_gmail_';",
                    "SELECT * FROM clients WHERE email = '%gmail%';",
                ],
            ),
            M(
                "Quelles requêtes utilisent correctement la syntaxe LIKE ?",
                [
                    "SELECT * FROM clients WHERE nom LIKE 'A%';",
                    "SELECT * FROM clients WHERE nom NOT LIKE '%z';",
                ],
                ["SELECT * FROM clients WHERE nom LIKE A%;", "SELECT * FROM clients LIKE nom = 'A%';"],
            ),
            T("Le motif 'A_' avec LIKE correspond à toute chaîne de exactement deux caractères commençant par A.", True),
            T("LIKE est uniquement utilisable avec des colonnes numériques.", False),
        ],
    ),
    quiz(
        "BETWEEN et IN : filtrer des plages et des listes",
        "Simplifier les conditions WHERE avec BETWEEN et IN.",
        [
            S(
                "Quelle requête est équivalente à `prix >= 10 AND prix <= 50` ?",
                [
                    "SELECT * FROM produits WHERE prix BETWEEN 10 AND 50;",
                    "SELECT * FROM produits WHERE prix RANGE 10 TO 50;",
                    "SELECT * FROM produits WHERE prix IN (10, 50);",
                    "SELECT * FROM produits WHERE prix BETWEEN 10, 50;",
                ],
            ),
            S(
                "Quelle requête sélectionne les clients dont la ville est 'Paris', 'Lyon' ou 'Nice' ?",
                [
                    "SELECT * FROM clients WHERE ville IN ('Paris', 'Lyon', 'Nice');",
                    "SELECT * FROM clients WHERE ville = ('Paris', 'Lyon', 'Nice');",
                    "SELECT * FROM clients WHERE ville BETWEEN 'Paris' AND 'Nice';",
                    "SELECT * FROM clients WHERE ville ANY ('Paris', 'Lyon', 'Nice');",
                ],
            ),
            Sx(
                "BETWEEN 10 AND 50 inclut-il les bornes 10 et 50 ?",
                ["Oui, les deux bornes sont incluses", "Non, aucune borne n'est incluse", "Seule la borne inférieure est incluse", "Seule la borne supérieure est incluse"],
                0,
            ),
            M(
                "Quelles requêtes sont syntaxiquement valides ?",
                [
                    "SELECT * FROM produits WHERE categorie IN ('Sport', 'Loisir');",
                    "SELECT * FROM produits WHERE prix NOT BETWEEN 0 AND 5;",
                ],
                ["SELECT * FROM produits WHERE categorie IN Sport, Loisir;", "SELECT * FROM produits WHERE prix NOT IN BETWEEN 0 AND 5;"],
            ),
            T("`ville IN ('Paris', 'Lyon')` est équivalent à `ville = 'Paris' OR ville = 'Lyon'`.", True),
            T("NOT IN ne peut jamais être utilisé avec une liste de valeurs littérales.", False),
        ],
    ),
    quiz(
        "ORDER BY : trier les résultats",
        "Maîtriser le tri ascendant et descendant avec ORDER BY.",
        [
            S(
                "Quelle requête trie les produits par prix croissant ?",
                [
                    "SELECT * FROM produits ORDER BY prix ASC;",
                    "SELECT * FROM produits SORT BY prix;",
                    "SELECT * FROM produits ORDER BY prix DESC;",
                    "SELECT * FROM produits GROUP BY prix ASC;",
                ],
            ),
            Sx(
                "Quel mot-clé indique un tri décroissant dans ORDER BY ?",
                ["ASC", "DESC", "DOWN", "REVERSE"],
                1,
            ),
            S(
                "Par défaut, sans préciser ASC ou DESC, ORDER BY trie dans quel ordre ?",
                ["Croissant (ASC)", "Décroissant (DESC)", "Aléatoire", "Selon l'ordre d'insertion uniquement"],
            ),
            M(
                "Quelles requêtes trient correctement par plusieurs colonnes ?",
                [
                    "SELECT * FROM clients ORDER BY ville ASC, nom DESC;",
                    "SELECT * FROM clients ORDER BY ville, nom;",
                ],
                ["SELECT * FROM clients ORDER BY ville AND nom;", "SELECT * FROM clients SORT ville, nom;"],
            ),
            T("ORDER BY peut trier sur une colonne qui n'apparaît pas dans la liste SELECT.", True),
            T("ORDER BY doit obligatoirement être placé avant la clause WHERE dans une requête.", False),
        ],
    ),
    quiz(
        "LIMIT et OFFSET : paginer les résultats",
        "Restreindre et paginer le nombre de lignes retournées.",
        [
            S(
                "Quelle requête retourne uniquement les 5 premiers résultats ?",
                [
                    "SELECT * FROM produits LIMIT 5;",
                    "SELECT TOP 5 * FROM produits LIMIT;",
                    "SELECT * FROM produits MAX 5;",
                    "SELECT * FROM produits ROWS 5;",
                ],
            ),
            S(
                "Quelle clause permet de sauter les 10 premières lignes avant de retourner les suivantes ?",
                ["OFFSET 10", "SKIP 10", "START 10", "FROM 10"],
            ),
            Sx(
                "Que retourne `SELECT * FROM produits ORDER BY prix DESC LIMIT 3 OFFSET 2;` ?",
                [
                    "Les 3 produits classés 3e, 4e et 5e par prix décroissant",
                    "Les 2 produits les plus chers seulement",
                    "Tous les produits sauf les 3 premiers",
                    "Les 3 produits les moins chers",
                ],
                0,
            ),
            M(
                "Quelles affirmations sur LIMIT/OFFSET sont vraies ?",
                [
                    "LIMIT/OFFSET est souvent utilisé pour la pagination",
                    "Sans ORDER BY, l'ordre des lignes limitées n'est pas garanti",
                ],
                ["LIMIT modifie les données présentes dans la table", "OFFSET est obligatoire dès qu'on utilise LIMIT"],
            ),
            T("LIMIT permet de restreindre le nombre de lignes renvoyées par une requête.", True),
            T("Toutes les bases de données SQL utilisent exactement la même syntaxe pour la pagination.", False),
        ],
    ),
    quiz(
        "Combiner WHERE, ORDER BY et LIMIT",
        "Assembler filtrage, tri et limitation dans une même requête.",
        [
            S(
                "Quelle requête retourne les 3 clients les plus jeunes habitant à Paris ?",
                [
                    "SELECT * FROM clients WHERE ville = 'Paris' ORDER BY age ASC LIMIT 3;",
                    "SELECT * FROM clients ORDER BY age ASC WHERE ville = 'Paris' LIMIT 3;",
                    "SELECT * FROM clients LIMIT 3 WHERE ville = 'Paris' ORDER BY age;",
                    "SELECT * FROM clients WHERE ville = 'Paris' LIMIT 3 ORDER BY age;",
                ],
            ),
            Sx(
                "Dans une requête SQL, quel est l'ordre logique correct des clauses suivantes ?",
                [
                    "SELECT, FROM, WHERE, ORDER BY, LIMIT",
                    "SELECT, ORDER BY, FROM, WHERE, LIMIT",
                    "FROM, LIMIT, WHERE, SELECT, ORDER BY",
                    "WHERE, SELECT, FROM, LIMIT, ORDER BY",
                ],
                0,
            ),
            S(
                "Quelle requête sélectionne les 10 produits les plus chers de la catégorie 'Informatique' ?",
                [
                    "SELECT * FROM produits WHERE categorie = 'Informatique' ORDER BY prix DESC LIMIT 10;",
                    "SELECT * FROM produits WHERE categorie = 'Informatique' ORDER BY prix ASC LIMIT 10;",
                    "SELECT TOP 10 * FROM produits WHERE categorie = 'Informatique';",
                    "SELECT * FROM produits LIMIT 10 WHERE categorie = 'Informatique';",
                ],
            ),
            M(
                "Quelles requêtes sont écrites dans un ordre de clauses valide ?",
                [
                    "SELECT nom FROM clients WHERE age > 18 ORDER BY nom;",
                    "SELECT nom FROM clients ORDER BY nom LIMIT 5;",
                ],
                ["SELECT nom ORDER BY nom FROM clients;", "SELECT nom FROM clients LIMIT 5 WHERE age > 18;"],
            ),
            T("La clause WHERE doit toujours précéder la clause ORDER BY dans une requête SELECT.", True),
            T("LIMIT s'applique avant le tri ORDER BY dans l'ordre logique d'exécution.", False),
        ],
    ),
    quiz(
        "Gestion du NULL : IS NULL et COALESCE",
        "Comprendre la valeur NULL et les fonctions pour la gérer.",
        [
            S(
                "Quelle requête sélectionne les clients sans numéro de téléphone renseigné ?",
                [
                    "SELECT * FROM clients WHERE telephone IS NULL;",
                    "SELECT * FROM clients WHERE telephone = NULL;",
                    "SELECT * FROM clients WHERE telephone = '';",
                    "SELECT * FROM clients WHERE telephone IS EMPTY;",
                ],
            ),
            Sx(
                "Que retourne `COALESCE(NULL, NULL, 'défaut')` ?",
                ["'défaut'", "NULL", "Une erreur", "Une chaîne vide"],
                0,
            ),
            S(
                "Quelle requête remplace les valeurs NULL de la colonne remise par 0 dans le résultat affiché ?",
                [
                    "SELECT COALESCE(remise, 0) FROM produits;",
                    "SELECT IFEMPTY(remise, 0) FROM produits;",
                    "SELECT remise OR 0 FROM produits;",
                    "SELECT NULLIF(remise, 0) FROM produits;",
                ],
            ),
            M(
                "Quelles affirmations sur NULL sont correctes ?",
                [
                    "NULL représente une valeur absente ou inconnue",
                    "`NULL = NULL` ne renvoie pas TRUE en SQL standard",
                ],
                ["NULL est équivalent à la valeur zéro", "NULL est équivalent à une chaîne vide ''"],
            ),
            T("La fonction COALESCE retourne la première valeur non NULL de sa liste d'arguments.", True),
            T("On peut tester si une colonne est NULL avec l'opérateur `colonne = NULL`.", False),
        ],
    ),
    quiz(
        "Expressions CASE",
        "Créer des colonnes conditionnelles avec CASE WHEN.",
        [
            S(
                "Quelle syntaxe correspond à une expression CASE simple correcte ?",
                [
                    "CASE WHEN prix > 100 THEN 'Cher' ELSE 'Abordable' END",
                    "CASE prix > 100 THEN 'Cher' OR 'Abordable'",
                    "IF prix > 100 THEN 'Cher' ELSE 'Abordable'",
                    "CASE (prix > 100) -> 'Cher' : 'Abordable'",
                ],
            ),
            Sx(
                "Que se passe-t-il si aucune condition WHEN n'est vraie et qu'il n'y a pas de ELSE dans un CASE ?",
                ["L'expression retourne NULL", "Une erreur est levée systématiquement", "Elle retourne 0", "Elle retourne une chaîne vide"],
                0,
            ),
            S(
                "Quelle requête classe les produits en 'Cher' si prix > 50, sinon 'Abordable' ?",
                [
                    "SELECT nom, CASE WHEN prix > 50 THEN 'Cher' ELSE 'Abordable' END FROM produits;",
                    "SELECT nom, CASE prix > 50 'Cher' 'Abordable' FROM produits;",
                    "SELECT nom, IF(prix > 50, 'Cher', 'Abordable') CASE FROM produits;",
                    "SELECT nom, WHEN prix > 50 THEN 'Cher' FROM produits;",
                ],
            ),
            M(
                "Quelles affirmations sur CASE WHEN sont vraies ?",
                [
                    "CASE peut être utilisé dans la clause SELECT, WHERE ou ORDER BY",
                    "Plusieurs conditions WHEN peuvent être empilées dans un même CASE",
                ],
                ["CASE ne fonctionne qu'avec des colonnes numériques", "CASE remplace obligatoirement la clause WHERE"],
            ),
            T("Une expression CASE doit se terminer par le mot-clé END.", True),
            T("CASE WHEN ne peut être utilisé que dans les instructions UPDATE.", False),
        ],
    ),
    quiz(
        "Opérateurs arithmétiques en SQL",
        "Effectuer des calculs sur les colonnes numériques dans une requête.",
        [
            S(
                "Quelle requête calcule le prix TTC à partir du prix HT avec une TVA de 20% ?",
                [
                    "SELECT prix_ht * 1.20 AS prix_ttc FROM produits;",
                    "SELECT prix_ht + 20 AS prix_ttc FROM produits;",
                    "SELECT prix_ht % 20 AS prix_ttc FROM produits;",
                    "SELECT prix_ht ^ 1.20 AS prix_ttc FROM produits;",
                ],
            ),
            Sx(
                "Quel opérateur SQL standard correspond au modulo (reste de division entière) ?",
                ["%", "MOD seulement, jamais %", "//", "DIV"],
                0,
            ),
            S(
                "Quelle requête calcule la marge en soustrayant le coût du prix de vente ?",
                [
                    "SELECT prix_vente - cout AS marge FROM produits;",
                    "SELECT prix_vente DIFF cout AS marge FROM produits;",
                    "SELECT cout - prix_vente AS marge FROM produits;",
                    "SELECT prix_vente MINUS cout AS marge FROM produits;",
                ],
            ),
            M(
                "Quels opérateurs arithmétiques sont valides en SQL ?",
                ["+", "*"],
                ["=>", "<-"],
            ),
            T("On peut combiner plusieurs opérateurs arithmétiques dans une même expression SELECT.", True),
            T("L'opérateur de division en SQL est représenté par le symbole \\ (backslash).", False),
        ],
    ),
    quiz(
        "Fonctions de chaînes de caractères",
        "Manipuler du texte avec CONCAT, SUBSTRING, UPPER, LOWER et TRIM.",
        [
            S(
                "Quelle fonction permet de concaténer le prénom et le nom en une seule colonne ?",
                [
                    "CONCAT(prenom, ' ', nom)",
                    "JOIN(prenom, nom)",
                    "MERGE(prenom, nom)",
                    "prenom PLUS nom",
                ],
            ),
            Sx(
                "Que fait la fonction UPPER('sql') ?",
                ["Retourne 'SQL'", "Retourne 'Sql'", "Retourne 'sql' inchangé", "Lève une erreur"],
                0,
            ),
            S(
                "Quelle fonction retire les espaces inutiles au début et à la fin d'une chaîne ?",
                ["TRIM(chaine)", "CLEAN(chaine)", "STRIP_ALL(chaine)", "REMOVE_SPACE(chaine)"],
            ),
            M(
                "Quelles fonctions sont des fonctions de chaînes courantes en SQL ?",
                ["LOWER", "SUBSTRING"],
                ["AVG", "COUNT"],
            ),
            T("SUBSTRING permet d'extraire une portion d'une chaîne de caractères à partir d'une position donnée.", True),
            T("La fonction LOWER met en majuscules tous les caractères d'une chaîne.", False),
        ],
    ),
    quiz(
        "Fonctions de date",
        "Travailler avec les dates : extraction, calculs et formats.",
        [
            S(
                "Quelle fonction retourne la date et l'heure actuelles dans la plupart des SGBD ?",
                ["NOW()", "TODAY()", "CURRENT_TIME_FULL()", "GET_DATE_NOW()"],
            ),
            Sx(
                "Quelle fonction permet d'extraire l'année d'une colonne de type date ?",
                ["EXTRACT(YEAR FROM date_col)", "YEAR_OF(date_col)", "GET_YEAR(date_col)", "date_col.YEAR"],
                0,
            ),
            S(
                "Quelle requête sélectionne les commandes passées en 2024 (colonne date_commande) ?",
                [
                    "SELECT * FROM commandes WHERE EXTRACT(YEAR FROM date_commande) = 2024;",
                    "SELECT * FROM commandes WHERE date_commande = 2024;",
                    "SELECT * FROM commandes WHERE YEAR(date_commande) IS 2024;",
                    "SELECT * FROM commandes WHERE date_commande LIKE '2024';",
                ],
            ),
            M(
                "Quelles affirmations sur les dates en SQL sont correctes ?",
                [
                    "On peut généralement soustraire deux dates pour obtenir un nombre de jours",
                    "Les fonctions de date varient légèrement d'un SGBD à un autre",
                ],
                ["Les dates sont toujours stockées comme des chaînes de texte", "Il est impossible de comparer deux dates avec des opérateurs comme < ou >"],
            ),
            T("La fonction NOW() ou équivalente retourne la date et l'heure du moment de l'exécution.", True),
            T("Toutes les bases de données SQL utilisent exactement le même nom de fonction pour la date courante.", False),
        ],
    ),
]
