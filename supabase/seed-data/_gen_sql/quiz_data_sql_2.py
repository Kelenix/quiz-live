from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "Fonctions d'agrégation : COUNT et SUM",
        "Compter et additionner des valeurs avec COUNT et SUM.",
        [
            S(
                "Quelle requête compte le nombre total de clients ?",
                [
                    "SELECT COUNT(*) FROM clients;",
                    "SELECT SUM(*) FROM clients;",
                    "SELECT TOTAL(*) FROM clients;",
                    "SELECT COUNT(ALL) FROM clients;",
                ],
            ),
            Sx(
                "Quelle est la différence entre COUNT(*) et COUNT(colonne) ?",
                [
                    "COUNT(colonne) ignore les valeurs NULL de cette colonne, COUNT(*) compte toutes les lignes",
                    "Il n'y a aucune différence, les deux comptent toujours toutes les lignes",
                    "COUNT(*) ignore les NULL et COUNT(colonne) compte toutes les lignes",
                    "COUNT(colonne) ne fonctionne qu'avec des colonnes textuelles",
                ],
                0,
            ),
            S(
                "Quelle requête calcule le chiffre d'affaires total de la table commandes (colonne montant) ?",
                [
                    "SELECT SUM(montant) FROM commandes;",
                    "SELECT COUNT(montant) FROM commandes;",
                    "SELECT TOTAL(montant) FROM commandes;",
                    "SELECT ADD(montant) FROM commandes;",
                ],
            ),
            M(
                "Quelles affirmations sur COUNT et SUM sont vraies ?",
                [
                    "SUM ignore les valeurs NULL dans son calcul",
                    "COUNT(*) compte toutes les lignes, NULL inclus",
                ],
                ["SUM() ne peut être utilisé que sur des colonnes de type texte", "COUNT(*) ignore systématiquement les doublons"],
            ),
            T("SUM(colonne) additionne les valeurs non NULL de la colonne spécifiée.", True),
            T("COUNT(colonne) compte aussi les valeurs NULL de cette colonne.", False),
        ],
    ),
    quiz(
        "Fonctions d'agrégation : AVG, MIN, MAX",
        "Calculer moyenne, minimum et maximum d'un ensemble de valeurs.",
        [
            S(
                "Quelle requête calcule le prix moyen des produits ?",
                [
                    "SELECT AVG(prix) FROM produits;",
                    "SELECT MEAN(prix) FROM produits;",
                    "SELECT MOYENNE(prix) FROM produits;",
                    "SELECT AVERAGE(prix) FROM produits;",
                ],
            ),
            S(
                "Quelle requête retourne le produit le moins cher (juste le prix minimal) ?",
                [
                    "SELECT MIN(prix) FROM produits;",
                    "SELECT LOWEST(prix) FROM produits;",
                    "SELECT MAX(prix) FROM produits;",
                    "SELECT FIRST(prix) FROM produits;",
                ],
            ),
            Sx(
                "Quelle fonction retourne la valeur la plus élevée d'une colonne ?",
                ["MAX()", "TOP()", "GREATEST()", "HIGH()"],
                0,
            ),
            M(
                "Parmi ces fonctions, lesquelles sont des fonctions d'agrégation standard en SQL ?",
                ["AVG", "MIN"],
                ["TRIM", "CONCAT"],
            ),
            T("MIN() et MAX() peuvent être utilisées sur des colonnes de type date.", True),
            T("AVG() prend en compte les valeurs NULL en les comptant comme zéro.", False),
        ],
    ),
    quiz(
        "GROUP BY : regrouper les données",
        "Utiliser GROUP BY pour agréger des données par catégorie.",
        [
            S(
                "Quelle requête compte le nombre de clients par ville ?",
                [
                    "SELECT ville, COUNT(*) FROM clients GROUP BY ville;",
                    "SELECT ville, COUNT(*) FROM clients ORDER BY ville;",
                    "SELECT COUNT(*) FROM clients GROUP ville;",
                    "SELECT ville, COUNT(*) FROM clients WHERE GROUP BY ville;",
                ],
            ),
            Sx(
                "Quelle règle s'applique aux colonnes listées dans SELECT lorsqu'on utilise GROUP BY ?",
                [
                    "Toute colonne non agrégée doit figurer dans le GROUP BY",
                    "Aucune colonne ne peut apparaître dans le SELECT à part celles du GROUP BY",
                    "Le GROUP BY interdit toute fonction d'agrégation",
                    "Le GROUP BY doit toujours contenir toutes les colonnes de la table",
                ],
                0,
            ),
            S(
                "Quelle requête calcule le chiffre d'affaires total par client (table commandes avec colonnes client_id, montant) ?",
                [
                    "SELECT client_id, SUM(montant) FROM commandes GROUP BY client_id;",
                    "SELECT client_id, SUM(montant) FROM commandes ORDER BY client_id;",
                    "SELECT SUM(montant) FROM commandes GROUP client_id;",
                    "SELECT client_id, montant FROM commandes GROUP BY SUM(montant);",
                ],
            ),
            M(
                "Quelles affirmations sur GROUP BY sont correctes ?",
                [
                    "GROUP BY est souvent utilisé avec des fonctions d'agrégation comme COUNT ou SUM",
                    "On peut grouper sur plusieurs colonnes à la fois",
                ],
                ["GROUP BY supprime automatiquement les colonnes non utilisées de la table", "GROUP BY doit obligatoirement précéder la clause FROM"],
            ),
            T("GROUP BY s'exécute logiquement après la clause WHERE.", True),
            T("GROUP BY peut être utilisé sans aucune fonction d'agrégation dans le SELECT.", True),
        ],
    ),
    quiz(
        "HAVING : filtrer après agrégation",
        "Comprendre la différence entre WHERE et HAVING.",
        [
            S(
                "Quelle requête retourne les villes ayant plus de 10 clients ?",
                [
                    "SELECT ville, COUNT(*) FROM clients GROUP BY ville HAVING COUNT(*) > 10;",
                    "SELECT ville, COUNT(*) FROM clients WHERE COUNT(*) > 10 GROUP BY ville;",
                    "SELECT ville, COUNT(*) FROM clients GROUP BY ville WHERE COUNT(*) > 10;",
                    "SELECT ville FROM clients HAVING COUNT(*) > 10;",
                ],
            ),
            Sx(
                "Quelle est la principale différence entre WHERE et HAVING ?",
                [
                    "WHERE filtre les lignes avant agrégation, HAVING filtre les groupes après agrégation",
                    "WHERE et HAVING sont strictement identiques et interchangeables",
                    "HAVING filtre les lignes avant le GROUP BY, WHERE filtre après",
                    "WHERE ne peut être utilisé qu'avec des fonctions d'agrégation",
                ],
                0,
            ),
            S(
                "Quelle requête est correcte pour trouver les catégories dont le prix moyen dépasse 50 ?",
                [
                    "SELECT categorie, AVG(prix) FROM produits GROUP BY categorie HAVING AVG(prix) > 50;",
                    "SELECT categorie, AVG(prix) FROM produits WHERE AVG(prix) > 50 GROUP BY categorie;",
                    "SELECT categorie FROM produits HAVING AVG(prix) > 50;",
                    "SELECT categorie, AVG(prix) FROM produits GROUP BY categorie WHERE AVG(prix) > 50;",
                ],
            ),
            M(
                "Quelles affirmations sur HAVING sont vraies ?",
                [
                    "HAVING peut contenir des fonctions d'agrégation comme COUNT() ou SUM()",
                    "HAVING s'utilise typiquement après un GROUP BY",
                ],
                ["HAVING remplace systématiquement la clause WHERE dans toute requête", "HAVING s'exécute avant le GROUP BY"],
            ),
            T("On ne peut pas utiliser une fonction d'agrégation directement dans une clause WHERE.", True),
            T("HAVING peut être utilisé sans GROUP BY dans une requête.", True),
        ],
    ),
    quiz(
        "INNER JOIN : la jointure interne",
        "Combiner deux tables avec une jointure interne classique.",
        [
            S(
                "Quelle requête retourne les commandes avec le nom du client associé (tables commandes et clients liées par client_id) ?",
                [
                    "SELECT c.nom, co.* FROM commandes co INNER JOIN clients c ON co.client_id = c.id;",
                    "SELECT c.nom, co.* FROM commandes co, clients c;",
                    "SELECT c.nom, co.* FROM commandes co INNER JOIN clients c WHERE co.client_id = c.id;",
                    "SELECT c.nom, co.* FROM commandes co JOIN ON clients c;",
                ],
            ),
            Sx(
                "Que retourne un INNER JOIN entre deux tables ?",
                [
                    "Uniquement les lignes ayant une correspondance dans les deux tables",
                    "Toutes les lignes des deux tables, correspondance ou non",
                    "Uniquement les lignes de la table de gauche",
                    "Uniquement les lignes qui n'ont pas de correspondance",
                ],
                0,
            ),
            S(
                "Quel mot-clé est nécessaire pour préciser la condition de jointure d'un INNER JOIN ?",
                ["ON", "WHERE", "USING ONLY", "MATCH"],
            ),
            M(
                "Quelles affirmations sur INNER JOIN sont correctes ?",
                [
                    "INNER JOIN peut être écrit simplement JOIN dans la plupart des SGBD",
                    "INNER JOIN exclut les lignes sans correspondance dans l'autre table",
                ],
                ["INNER JOIN retourne toujours plus de lignes qu'un LEFT JOIN", "INNER JOIN ne nécessite jamais de condition ON"],
            ),
            T("INNER JOIN est le type de jointure par défaut quand on écrit simplement JOIN.", True),
            T("INNER JOIN conserve les lignes d'une table même sans correspondance dans l'autre.", False),
        ],
    ),
    quiz(
        "LEFT JOIN et RIGHT JOIN",
        "Conserver toutes les lignes d'une table même sans correspondance.",
        [
            S(
                "Quelle requête retourne TOUS les clients, avec leurs commandes si elles existent ?",
                [
                    "SELECT c.*, co.* FROM clients c LEFT JOIN commandes co ON c.id = co.client_id;",
                    "SELECT c.*, co.* FROM clients c INNER JOIN commandes co ON c.id = co.client_id;",
                    "SELECT c.*, co.* FROM clients c RIGHT JOIN commandes co ON c.id = co.client_id;",
                    "SELECT c.*, co.* FROM commandes co LEFT JOIN clients c;",
                ],
            ),
            Sx(
                "Avec un LEFT JOIN, que contiennent les colonnes de la table de droite quand il n'y a pas de correspondance ?",
                ["NULL", "0", "Une chaîne vide", "Une erreur est levée"],
                0,
            ),
            S(
                "Quelle requête est équivalente à `B LEFT JOIN A ON ...` en utilisant RIGHT JOIN ?",
                [
                    "A RIGHT JOIN B ON ...",
                    "B RIGHT JOIN A ON ...",
                    "A LEFT JOIN B ON ... avec les tables échangées arbitrairement",
                    "Il n'existe aucun équivalent avec RIGHT JOIN",
                ],
            ),
            M(
                "Quelles affirmations sur LEFT JOIN sont vraies ?",
                [
                    "LEFT JOIN conserve toutes les lignes de la table de gauche",
                    "LEFT JOIN peut produire des valeurs NULL pour les colonnes de la table de droite",
                ],
                ["LEFT JOIN exclut toujours les lignes sans correspondance", "LEFT JOIN est strictement identique à INNER JOIN"],
            ),
            T("RIGHT JOIN conserve toutes les lignes de la table mentionnée à droite du mot-clé JOIN.", True),
            T("LEFT JOIN est moins utilisé en pratique que RIGHT JOIN car il serait obsolète.", False),
        ],
    ),
    quiz(
        "FULL OUTER JOIN et CROSS JOIN",
        "Combiner toutes les lignes ou produire un produit cartésien.",
        [
            S(
                "Que retourne un FULL OUTER JOIN entre deux tables A et B ?",
                [
                    "Toutes les lignes de A et B, avec NULL là où il n'y a pas de correspondance",
                    "Uniquement les lignes communes aux deux tables",
                    "Uniquement les lignes de A",
                    "Le produit cartésien de A et B",
                ],
            ),
            Sx(
                "Que produit un CROSS JOIN entre une table de 3 lignes et une table de 4 lignes ?",
                ["12 lignes (produit cartésien)", "7 lignes (somme)", "3 lignes", "4 lignes"],
                0,
            ),
            S(
                "Quelle requête réalise un produit cartésien explicite entre tailles et couleurs ?",
                [
                    "SELECT * FROM tailles CROSS JOIN couleurs;",
                    "SELECT * FROM tailles FULL JOIN couleurs;",
                    "SELECT * FROM tailles, couleurs ON 1=1;",
                    "SELECT * FROM tailles UNION couleurs;",
                ],
            ),
            M(
                "Quelles affirmations sont correctes ?",
                [
                    "CROSS JOIN ne nécessite pas de condition ON",
                    "FULL OUTER JOIN combine le comportement de LEFT JOIN et RIGHT JOIN",
                ],
                ["CROSS JOIN filtre automatiquement les doublons", "FULL OUTER JOIN est supporté de façon identique par tous les SGBD sans exception"],
            ),
            T("Un CROSS JOIN peut générer un très grand nombre de lignes si les tables sont volumineuses.", True),
            T("FULL OUTER JOIN ne retourne jamais de valeurs NULL dans son résultat.", False),
        ],
    ),
    quiz(
        "L'auto-jointure (self join)",
        "Joindre une table à elle-même pour exploiter des relations internes.",
        [
            S(
                "Quelle requête trouve les employés et le nom de leur manager dans la même table employes (colonnes id, nom, manager_id) ?",
                [
                    "SELECT e.nom AS employe, m.nom AS manager FROM employes e JOIN employes m ON e.manager_id = m.id;",
                    "SELECT e.nom, m.nom FROM employes e, employes m WHERE e.id = m.id;",
                    "SELECT nom, manager_id FROM employes SELF JOIN employes;",
                    "SELECT e.nom FROM employes e JOIN manager_id ON e.id;",
                ],
            ),
            Sx(
                "Pourquoi est-il indispensable d'utiliser des alias dans une auto-jointure ?",
                [
                    "Pour distinguer les deux occurrences de la même table dans la requête",
                    "Parce que SQL interdit de citer deux fois le même nom de table",
                    "Pour accélérer l'exécution de la requête",
                    "Les alias ne sont en réalité jamais nécessaires dans une auto-jointure",
                ],
                0,
            ),
            S(
                "Quel type de relation est typiquement modélisé par une auto-jointure ?",
                [
                    "Une relation hiérarchique au sein d'une même entité (ex: employé/manager)",
                    "Une relation entre deux tables totalement différentes",
                    "Une relation many-to-many entre trois tables",
                    "Une contrainte d'unicité",
                ],
            ),
            M(
                "Quelles affirmations sur l'auto-jointure sont vraies ?",
                [
                    "Une auto-jointure utilise deux alias différents pour la même table",
                    "Une auto-jointure peut utiliser INNER JOIN ou LEFT JOIN",
                ],
                ["Une auto-jointure nécessite obligatoirement deux tables physiquement distinctes", "Une auto-jointure est interdite en SQL standard"],
            ),
            T("Une auto-jointure permet de comparer des lignes d'une table entre elles.", True),
            T("Il est impossible d'utiliser un LEFT JOIN dans le cadre d'une auto-jointure.", False),
        ],
    ),
    quiz(
        "Jointures multiples sur plusieurs tables",
        "Enchaîner plusieurs jointures dans une seule requête.",
        [
            S(
                "Quelle requête joint commandes, clients et produits pour afficher le nom du client et du produit ?",
                [
                    "SELECT c.nom, p.nom FROM commandes co JOIN clients c ON co.client_id = c.id JOIN produits p ON co.produit_id = p.id;",
                    "SELECT c.nom, p.nom FROM commandes co, clients c, produits p;",
                    "SELECT c.nom, p.nom FROM commandes co JOIN clients c, produits p ON co.client_id = c.id;",
                    "SELECT c.nom, p.nom FROM commandes co JOIN clients JOIN produits;",
                ],
            ),
            Sx(
                "Combien de clauses ON sont nécessaires pour joindre 3 tables avec deux INNER JOIN successifs ?",
                ["2", "1", "3", "0"],
                0,
            ),
            S(
                "Quelle pratique est recommandée lorsqu'on enchaîne plusieurs jointures ?",
                [
                    "Utiliser des alias courts et cohérents pour chaque table",
                    "Éviter complètement les alias pour plus de clarté",
                    "Toujours utiliser des sous-requêtes plutôt que des jointures",
                    "Ne jamais nommer explicitement les colonnes dans le SELECT",
                ],
            ),
            M(
                "Quelles affirmations sur les jointures multiples sont correctes ?",
                [
                    "On peut mélanger INNER JOIN et LEFT JOIN dans la même requête",
                    "L'ordre des jointures peut influencer la lisibilité de la requête",
                ],
                ["Une requête SQL ne peut joindre que deux tables maximum", "Chaque jointure supplémentaire nécessite une nouvelle instruction SELECT séparée"],
            ),
            T("Il est possible de joindre plus de deux tables dans une seule requête SELECT.", True),
            T("Chaque jointure ajoutée doit obligatoirement utiliser le même type de jointure que la précédente.", False),
        ],
    ),
    quiz(
        "EXISTS vs IN",
        "Comparer deux façons de tester l'existence de lignes liées.",
        [
            S(
                "Quelle requête utilise EXISTS pour trouver les clients ayant au moins une commande ?",
                [
                    "SELECT * FROM clients c WHERE EXISTS (SELECT 1 FROM commandes co WHERE co.client_id = c.id);",
                    "SELECT * FROM clients c WHERE EXISTS commandes;",
                    "SELECT * FROM clients c WHERE c.id EXISTS commandes.client_id;",
                    "SELECT * FROM clients c EXISTS JOIN commandes co;",
                ],
            ),
            Sx(
                "Quelle est une différence pratique souvent citée entre EXISTS et IN ?",
                [
                    "EXISTS s'arrête dès qu'une ligne correspondante est trouvée, ce qui peut être plus efficace sur de grosses sous-requêtes",
                    "IN ne peut jamais être utilisé avec une sous-requête",
                    "EXISTS ne fonctionne qu'avec des nombres",
                    "IN et EXISTS sont rigoureusement identiques dans tous les cas, sans aucune nuance",
                ],
                0,
            ),
            S(
                "Quelle requête utilise IN pour trouver les produits commandés au moins une fois ?",
                [
                    "SELECT * FROM produits WHERE id IN (SELECT produit_id FROM commandes);",
                    "SELECT * FROM produits WHERE id EXISTS (SELECT produit_id FROM commandes);",
                    "SELECT * FROM produits WHERE id = ANY commandes;",
                    "SELECT * FROM produits IN commandes;",
                ],
            ),
            M(
                "Quelles affirmations sur EXISTS et IN sont vraies ?",
                [
                    "EXISTS retourne un booléen logique (vrai/faux) selon qu'une ligne existe ou non",
                    "IN compare une valeur à une liste ou au résultat d'une sous-requête",
                ],
                ["EXISTS ne peut jamais contenir de sous-requête corrélée", "IN ne peut être utilisé qu'avec des valeurs littérales, jamais une sous-requête"],
            ),
            T("NOT EXISTS permet de trouver les lignes qui n'ont aucune correspondance dans une sous-requête.", True),
            T("EXISTS exige que la sous-requête retourne exactement une colonne nommée explicitement.", False),
        ],
    ),
    quiz(
        "Sous-requêtes non corrélées",
        "Utiliser une sous-requête indépendante dans une clause WHERE ou FROM.",
        [
            S(
                "Quelle requête trouve les produits plus chers que le prix moyen de tous les produits ?",
                [
                    "SELECT * FROM produits WHERE prix > (SELECT AVG(prix) FROM produits);",
                    "SELECT * FROM produits WHERE prix > AVG(prix);",
                    "SELECT * FROM produits HAVING prix > AVG(prix);",
                    "SELECT * FROM produits WHERE prix > AVG(SELECT prix FROM produits);",
                ],
            ),
            Sx(
                "Qu'est-ce qui caractérise une sous-requête non corrélée ?",
                [
                    "Elle peut être exécutée de façon indépendante, sans référence à la requête externe",
                    "Elle doit obligatoirement référencer une colonne de la requête externe",
                    "Elle ne peut retourner qu'une seule ligne",
                    "Elle ne peut jamais être utilisée dans une clause WHERE",
                ],
                0,
            ),
            S(
                "Quelle requête utilise une sous-requête dans la clause FROM ?",
                [
                    "SELECT * FROM (SELECT client_id, COUNT(*) AS nb FROM commandes GROUP BY client_id) AS stats;",
                    "SELECT * FROM commandes WHERE stats > 0;",
                    "SELECT stats.* FROM stats;",
                    "SELECT * FROM commandes JOIN (COUNT(*));",
                ],
            ),
            M(
                "Quelles affirmations sur les sous-requêtes non corrélées sont correctes ?",
                [
                    "Elles peuvent être placées dans WHERE, FROM ou SELECT",
                    "Elles sont évaluées une seule fois, indépendamment des lignes de la requête externe",
                ],
                ["Elles doivent obligatoirement contenir une jointure", "Elles ne peuvent jamais utiliser de fonction d'agrégation"],
            ),
            T("Une sous-requête utilisée dans le FROM doit obligatoirement recevoir un alias dans la plupart des SGBD.", True),
            T("Une sous-requête non corrélée dépend systématiquement de chaque ligne de la requête externe.", False),
        ],
    ),
    quiz(
        "Sous-requêtes corrélées",
        "Comprendre les sous-requêtes qui référencent la requête externe.",
        [
            S(
                "Quelle requête trouve les employés gagnant plus que la moyenne de leur propre département (sous-requête corrélée) ?",
                [
                    "SELECT * FROM employes e WHERE salaire > (SELECT AVG(salaire) FROM employes WHERE departement = e.departement);",
                    "SELECT * FROM employes WHERE salaire > AVG(salaire) GROUP BY departement;",
                    "SELECT * FROM employes e WHERE salaire > (SELECT AVG(salaire) FROM employes);",
                    "SELECT * FROM employes e HAVING salaire > AVG(salaire);",
                ],
            ),
            Sx(
                "Qu'est-ce qui distingue une sous-requête corrélée d'une sous-requête classique ?",
                [
                    "Elle référence une colonne de la requête externe et est ré-évaluée pour chaque ligne",
                    "Elle ne peut jamais contenir de fonction d'agrégation",
                    "Elle s'exécute une seule fois pour toute la requête, comme une sous-requête non corrélée",
                    "Elle ne peut être utilisée que dans la clause SELECT",
                ],
                0,
            ),
            S(
                "Quelle requête utilise EXISTS avec une sous-requête corrélée pour trouver les clients ayant commandé un produit précis ?",
                [
                    "SELECT * FROM clients c WHERE EXISTS (SELECT 1 FROM commandes co WHERE co.client_id = c.id AND co.produit_id = 5);",
                    "SELECT * FROM clients WHERE EXISTS produit_id = 5;",
                    "SELECT * FROM clients c WHERE co.produit_id = 5;",
                    "SELECT * FROM clients WHERE IN (SELECT produit_id FROM commandes);",
                ],
            ),
            M(
                "Quelles affirmations sur les sous-requêtes corrélées sont vraies ?",
                [
                    "Elles peuvent être plus coûteuses en performance car ré-évaluées par ligne",
                    "Elles sont fréquemment utilisées avec EXISTS ou NOT EXISTS",
                ],
                ["Elles ne peuvent jamais être réécrites sous forme de jointure", "Elles s'exécutent indépendamment de la requête externe"],
            ),
            T("Une sous-requête corrélée référence au moins une colonne de la table de la requête externe.", True),
            T("Une sous-requête corrélée est toujours plus rapide qu'une jointure équivalente.", False),
        ],
    ),
]
