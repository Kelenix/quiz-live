from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "Sous-requêtes dans HAVING",
        "Filtrer des groupes en comparant à une valeur calculée par sous-requête.",
        [
            S(
                "Quelle requête trouve les clients dont le total des commandes dépasse la moyenne globale des totaux par client ?",
                [
                    "SELECT client_id, SUM(montant) FROM commandes GROUP BY client_id HAVING SUM(montant) > (SELECT AVG(total) FROM (SELECT SUM(montant) AS total FROM commandes GROUP BY client_id) t);",
                    "SELECT client_id, SUM(montant) FROM commandes WHERE SUM(montant) > AVG(montant);",
                    "SELECT client_id FROM commandes HAVING AVG(montant);",
                    "SELECT client_id, SUM(montant) FROM commandes GROUP BY client_id WHERE SUM(montant) > AVG(montant);",
                ],
            ),
            Sx(
                "Une sous-requête dans HAVING peut-elle contenir elle-même une agrégation ?",
                [
                    "Oui, c'est une pratique courante pour comparer un groupe à une statistique globale",
                    "Non, HAVING interdit toute sous-requête",
                    "Non, une sous-requête dans HAVING ne peut jamais contenir AVG ou SUM",
                    "Oui, mais seulement si elle ne retourne aucune ligne",
                ],
                0,
            ),
            S(
                "Quelle requête trouve les catégories ayant un nombre de produits supérieur à celui de la catégorie 'Divers' ?",
                [
                    "SELECT categorie, COUNT(*) FROM produits GROUP BY categorie HAVING COUNT(*) > (SELECT COUNT(*) FROM produits WHERE categorie = 'Divers');",
                    "SELECT categorie FROM produits WHERE COUNT(*) > 'Divers';",
                    "SELECT categorie, COUNT(*) FROM produits GROUP BY categorie WHERE categorie != 'Divers';",
                    "SELECT categorie FROM produits HAVING categorie = 'Divers';",
                ],
            ),
            M(
                "Quelles affirmations sur les sous-requêtes dans HAVING sont vraies ?",
                [
                    "Elles permettent de comparer un groupe à une valeur de référence calculée dynamiquement",
                    "Elles s'exécutent après le regroupement effectué par GROUP BY",
                ],
                ["Elles ne peuvent jamais référencer une autre table que celle du GROUP BY", "HAVING ne peut contenir que des constantes littérales"],
            ),
            T("HAVING peut comparer le résultat d'une agrégation à une valeur retournée par une sous-requête.", True),
            T("Une sous-requête dans HAVING ne peut jamais utiliser une fonction d'agrégation comme AVG().", False),
        ],
    ),
    quiz(
        "INNER JOIN avec conditions supplémentaires",
        "Combiner une jointure avec des filtres additionnels dans WHERE ou ON.",
        [
            S(
                "Quelle requête joint commandes et clients en filtrant uniquement les commandes de plus de 100 ?",
                [
                    "SELECT * FROM commandes co JOIN clients c ON co.client_id = c.id WHERE co.montant > 100;",
                    "SELECT * FROM commandes co JOIN clients c ON co.client_id = c.id AND co.montant > 100 WHERE TRUE;",
                    "SELECT * FROM commandes co JOIN clients c WHERE co.montant > 100 ON co.client_id = c.id;",
                    "Les deux premières propositions sont correctes et peuvent donner un résultat équivalent",
                ],
                3,
            ),
            Sx(
                "Quelle est la différence entre placer une condition dans ON plutôt que dans WHERE pour un LEFT JOIN ?",
                [
                    "Une condition dans ON filtre avant la jointure (table de droite), une condition dans WHERE filtre après, ce qui peut changer le résultat",
                    "Il n'existe absolument aucune différence quel que soit le type de jointure",
                    "ON ne peut jamais contenir de condition autre que l'égalité des clés",
                    "WHERE ne peut être utilisé qu'avec INNER JOIN",
                ],
                0,
            ),
            S(
                "Quelle requête combine une jointure et un tri pour afficher les commandes par client, du plus récent au plus ancien ?",
                [
                    "SELECT c.nom, co.date_commande FROM clients c JOIN commandes co ON c.id = co.client_id ORDER BY co.date_commande DESC;",
                    "SELECT c.nom, co.date_commande FROM clients c, commandes co ORDER DESC date_commande;",
                    "SELECT c.nom FROM clients c JOIN commandes co ORDER BY date_commande;",
                    "SELECT c.nom, co.date_commande FROM clients c JOIN commandes co SORT date_commande DESC;",
                ],
            ),
            M(
                "Quelles affirmations sur les conditions de jointure sont vraies ?",
                [
                    "La clause ON définit la condition de correspondance entre les deux tables",
                    "Pour un LEFT JOIN, une condition sur la table de droite placée dans WHERE peut annuler l'effet du LEFT JOIN",
                ],
                ["WHERE et ON sont toujours strictement équivalents pour tous les types de jointure", "ON ne peut contenir qu'une seule égalité entre clés primaires"],
            ),
            T("Pour un INNER JOIN simple, placer une condition dans ON ou dans WHERE donne généralement le même résultat final.", True),
            T("Pour un LEFT JOIN, déplacer une condition de la clause ON vers WHERE ne change jamais le résultat.", False),
        ],
    ),
    quiz(
        "Hiérarchies et requêtes récursives",
        "Explorer une structure arborescente avec une CTE récursive.",
        [
            S(
                "Quelle structure de table est typique pour représenter une hiérarchie d'employés avec managers ?",
                [
                    "employes(id, nom, manager_id) où manager_id référence employes.id",
                    "employes(id, nom) et managers(id, nom) totalement séparées sans lien",
                    "Une seule colonne contenant tous les noms séparés par des virgules",
                    "Une hiérarchie ne peut pas être représentée en SQL relationnel",
                ],
            ),
            Sx(
                "Dans une CTE récursive parcourant une hiérarchie, que représente le cas de base (ancre) ?",
                [
                    "Le point de départ de la récursion, par exemple les employés sans manager (racine)",
                    "La dernière itération de la récursion uniquement",
                    "Une condition d'erreur empêchant la récursion",
                    "Le nombre maximal de niveaux autorisés",
                ],
                0,
            ),
            S(
                "Quelle requête (structure générale) permet de lister tous les subordonnés directs et indirects d'un manager donné via CTE récursive ?",
                [
                    "WITH RECURSIVE subordonnes AS (SELECT id FROM employes WHERE manager_id = 1 UNION ALL SELECT e.id FROM employes e JOIN subordonnes s ON e.manager_id = s.id) SELECT * FROM subordonnes;",
                    "SELECT * FROM employes WHERE manager_id = 1 RECURSIVE;",
                    "SELECT * FROM employes GROUP BY manager_id RECURSIVE;",
                    "WITH subordonnes SELECT * FROM employes LOOP manager_id = 1;",
                ],
            ),
            M(
                "Quelles affirmations sur les hiérarchies en SQL sont vraies ?",
                [
                    "Une auto-jointure simple suffit pour récupérer un seul niveau de hiérarchie (ex: manager direct)",
                    "Une CTE récursive permet de parcourir un nombre de niveaux hiérarchiques inconnu à l'avance",
                ],
                ["Les hiérarchies ne peuvent être représentées qu'avec des triggers", "Une auto-jointure simple suffit toujours pour tous les niveaux hiérarchiques"],
            ),
            T("Une CTE récursive est particulièrement adaptée pour parcourir des structures hiérarchiques de profondeur variable.", True),
            T("Toute hiérarchie de profondeur supérieure à 2 niveaux est impossible à interroger en SQL.", False),
        ],
    ),
    quiz(
        "Index et plans d'exécution (notions)",
        "Comprendre comment un index influence le plan d'exécution d'une requête.",
        [
            S(
                "Quelle commande permet généralement d'observer le plan d'exécution d'une requête dans de nombreux SGBD ?",
                ["EXPLAIN", "DESCRIBE PLAN", "SHOW EXECUTION", "ANALYZE ONLY"],
            ),
            Sx(
                "Que peut révéler un plan d'exécution concernant l'usage des index ?",
                [
                    "Si la requête utilise un index existant ou réalise un parcours complet de la table (full scan)",
                    "Le contenu exact des données stockées dans la table",
                    "Le nombre exact d'utilisateurs connectés à la base",
                    "Le code source de la procédure stockée appelée",
                ],
                0,
            ),
            S(
                "Pourquoi une requête peut-elle ignorer un index existant et faire un parcours complet de la table ?",
                [
                    "Parce que l'optimiseur estime parfois qu'un scan complet est plus rapide selon la sélectivité de la condition",
                    "Parce que les index ne sont jamais réellement utilisés en pratique",
                    "Parce qu'un index ne peut être utilisé que par les instructions INSERT",
                    "Parce que la table est automatiquement verrouillée dès qu'un index existe",
                ],
            ),
            M(
                "Quelles affirmations sur les plans d'exécution sont vraies ?",
                [
                    "Le plan d'exécution aide à diagnostiquer les requêtes lentes",
                    "L'optimiseur de requêtes choisit la stratégie d'exécution selon les statistiques disponibles",
                ],
                ["Le plan d'exécution modifie automatiquement la structure de la table", "Un index garantit toujours d'être utilisé par l'optimiseur, sans exception"],
            ),
            T("Analyser un plan d'exécution peut aider à décider si un nouvel index serait bénéfique pour une requête.", True),
            T("L'optimiseur de requêtes utilise systématiquement tous les index disponibles sans aucune analyse de coût.", False),
        ],
    ),
    quiz(
        "Schémas et organisation des bases de données",
        "Notions de schéma, base de données et organisation logique.",
        [
            S(
                "Qu'est-ce qu'un schéma dans une base de données relationnelle ?",
                [
                    "Un espace de noms logique regroupant des tables, vues et autres objets",
                    "Une copie de sauvegarde automatique de la base",
                    "Un type de jointure particulier",
                    "Une contrainte d'unicité sur une colonne",
                ],
            ),
            Sx(
                "Quel est l'avantage d'organiser les tables en plusieurs schémas au sein d'une même base ?",
                [
                    "Séparer logiquement les objets par domaine fonctionnel et faciliter la gestion des droits",
                    "Empêcher totalement toute requête SQL sur la base",
                    "Dupliquer automatiquement chaque table dans tous les schémas",
                    "Cela n'apporte strictement aucun avantage",
                ],
                0,
            ),
            S(
                "Quelle instruction fait référence explicitement à une table nommée clients dans le schéma ventes ?",
                ["SELECT * FROM ventes.clients;", "SELECT * FROM clients@ventes;", "SELECT * FROM clients IN ventes;", "SELECT * FROM ventes:clients;"],
            ),
            M(
                "Quelles affirmations sur les schémas sont vraies ?",
                [
                    "Un schéma peut contenir plusieurs tables et vues",
                    "Les droits d'accès peuvent souvent être gérés au niveau du schéma",
                ],
                ["Une base de données ne peut contenir qu'un seul schéma au maximum", "Un schéma est identique à une transaction"],
            ),
            T("Un schéma permet d'organiser logiquement les objets d'une base de données.", True),
            T("Une base de données relationnelle ne peut techniquement contenir qu'une seule table en tout.", False),
        ],
    ),
    quiz(
        "Clés candidates et clés composites",
        "Distinguer clé primaire, clé candidate et clé composite.",
        [
            S(
                "Qu'est-ce qu'une clé candidate dans une table ?",
                [
                    "Une colonne ou un ensemble de colonnes pouvant potentiellement servir de clé primaire",
                    "Une colonne contenant uniquement des valeurs NULL",
                    "Une colonne calculée automatiquement par un trigger",
                    "Une colonne réservée exclusivement aux clés étrangères",
                ],
            ),
            Sx(
                "Qu'est-ce qu'une clé primaire composite ?",
                [
                    "Une clé primaire formée de plusieurs colonnes combinées garantissant l'unicité ensemble",
                    "Une clé primaire qui change de valeur à chaque requête",
                    "Une clé étrangère dupliquée plusieurs fois",
                    "Un index secondaire sans contrainte d'unicité",
                ],
                0,
            ),
            S(
                "Dans une table de jointure ligne_commande(commande_id, produit_id, quantite), quelle est une clé primaire composite plausible ?",
                ["(commande_id, produit_id)", "quantite seule", "commande_id seul s'il n'est pas unique en lui-même", "Aucune clé primaire n'est nécessaire"],
            ),
            M(
                "Quelles affirmations sur les clés candidates et composites sont vraies ?",
                [
                    "Une table peut avoir plusieurs clés candidates mais une seule est choisie comme clé primaire",
                    "Une clé composite combine plusieurs colonnes pour garantir l'unicité",
                ],
                ["Une clé candidate doit obligatoirement être numérique", "Une table ne peut avoir qu'une seule clé candidate possible"],
            ),
            T("Les clés candidates non choisies comme clé primaire peuvent tout de même recevoir une contrainte UNIQUE.", True),
            T("Une clé composite ne peut jamais être utilisée comme clé primaire d'une table.", False),
        ],
    ),
    quiz(
        "Vues matérialisées (notions)",
        "Différencier une vue classique d'une vue matérialisée.",
        [
            S(
                "Quelle est la principale différence entre une vue classique et une vue matérialisée ?",
                [
                    "La vue matérialisée stocke physiquement le résultat, recalculé périodiquement, contrairement à la vue classique",
                    "Une vue matérialisée ne peut jamais être interrogée avec SELECT",
                    "Une vue classique stocke toujours les données physiquement, la matérialisée jamais",
                    "Il n'existe aucune différence entre les deux notions",
                ],
            ),
            Sx(
                "Dans quel contexte une vue matérialisée est-elle particulièrement utile ?",
                [
                    "Pour des calculs coûteux et répétitifs dont le résultat n'a pas besoin d'être strictement à jour en temps réel",
                    "Pour des données qui changent à chaque milliseconde sans tolérance au moindre délai",
                    "Pour remplacer systématiquement toutes les tables d'une base",
                    "Les vues matérialisées n'ont aucun cas d'usage réel",
                ],
                0,
            ),
            S(
                "Quel terme désigne l'opération qui met à jour le contenu stocké d'une vue matérialisée ?",
                ["Le rafraîchissement (refresh)", "La normalisation", "Le verrouillage", "La troncature"],
            ),
            M(
                "Quelles affirmations sur les vues matérialisées sont vraies ?",
                [
                    "Elles peuvent améliorer les performances de lecture pour des requêtes coûteuses récurrentes",
                    "Leur contenu peut devenir périmé si elles ne sont pas rafraîchies régulièrement",
                ],
                ["Elles sont toujours automatiquement et instantanément synchronisées avec les tables sources", "Elles ne peuvent jamais contenir d'agrégation"],
            ),
            T("Une vue matérialisée occupe de l'espace de stockage car elle conserve physiquement son résultat.", True),
            T("Une vue classique (non matérialisée) stocke physiquement ses données comme une table normale.", False),
        ],
    ),
    quiz(
        "GROUP BY, ROLLUP et sous-totaux (notions)",
        "Découvrir les extensions de GROUP BY pour des rapports avec sous-totaux.",
        [
            S(
                "Quel est l'objectif principal d'une extension comme ROLLUP dans une requête GROUP BY ?",
                [
                    "Ajouter automatiquement des lignes de sous-totaux et de total général au résultat groupé",
                    "Supprimer toutes les lignes en double du résultat",
                    "Empêcher l'utilisation de fonctions d'agrégation",
                    "Convertir le résultat en une seule colonne texte",
                ],
            ),
            Sx(
                "Dans un rapport de ventes par région et par année avec ROLLUP, quelles lignes supplémentaires peuvent apparaître ?",
                [
                    "Des lignes de sous-total par région et une ligne de total général",
                    "Uniquement des lignes individuelles sans aucun total",
                    "Des lignes dupliquées identiques aux lignes de détail",
                    "Aucune ligne supplémentaire n'est jamais ajoutée",
                ],
                0,
            ),
            S(
                "Quelle alternative portable existe si ROLLUP n'est pas disponible dans un SGBD donné ?",
                [
                    "Combiner plusieurs requêtes avec UNION ALL pour simuler les sous-totaux",
                    "Utiliser uniquement WHERE pour obtenir le même résultat",
                    "Il n'existe aucune alternative possible",
                    "Utiliser TRUNCATE pour générer les sous-totaux",
                ],
            ),
            M(
                "Quelles affirmations sur les rapports avec sous-totaux sont vraies ?",
                [
                    "Ces rapports sont utiles pour des tableaux de bord avec plusieurs niveaux d'agrégation",
                    "Certains SGBD proposent des extensions dédiées comme ROLLUP ou GROUPING SETS",
                ],
                ["Un GROUP BY simple suffit toujours à générer automatiquement les sous-totaux", "Ces fonctionnalités sont strictement identiques dans tous les SGBD sans variation"],
            ),
            T("Les rapports avec sous-totaux combinent souvent plusieurs niveaux de regroupement dans un même résultat.", True),
            T("GROUP BY seul, sans extension particulière, génère automatiquement une ligne de total général.", False),
        ],
    ),
    quiz(
        "Sécurité et injection SQL (notions de base)",
        "Comprendre les risques liés à la construction non sécurisée de requêtes.",
        [
            S(
                "Qu'est-ce qu'une injection SQL ?",
                [
                    "Une technique consistant à insérer du code SQL malveillant via une entrée utilisateur non sécurisée",
                    "Une fonction SQL standard pour insérer des données",
                    "Un type de jointure particulier entre deux tables",
                    "Une contrainte garantissant l'intégrité des données",
                ],
            ),
            Sx(
                "Quelle pratique aide à se protéger contre les injections SQL côté application ?",
                [
                    "Utiliser des requêtes paramétrées (prepared statements) plutôt que de concaténer des chaînes",
                    "Concaténer directement les entrées utilisateur dans la requête SQL",
                    "Désactiver complètement toutes les contraintes de la base",
                    "Donner tous les droits GRANT ALL à chaque utilisateur",
                ],
                0,
            ),
            S(
                "Pourquoi une requête comme `SELECT * FROM users WHERE nom = '` + saisie + `';` est-elle risquée ?",
                [
                    "Parce qu'une saisie malveillante peut modifier la structure logique de la requête",
                    "Parce que SELECT ne peut jamais être utilisé avec WHERE",
                    "Parce que cette syntaxe est interdite par tous les SGBD",
                    "Il n'y a aucun risque particulier dans cette construction",
                ],
            ),
            M(
                "Quelles affirmations sur la sécurité SQL sont vraies ?",
                [
                    "Les requêtes paramétrées séparent le code SQL des données fournies par l'utilisateur",
                    "Limiter les privilèges GRANT accordés à chaque utilisateur réduit l'impact d'une faille",
                ],
                ["L'injection SQL est impossible dès qu'on utilise une base de données relationnelle", "Concaténer des entrées utilisateur dans une requête est toujours totalement sûr"],
            ),
            T("Une bonne gestion des privilèges (GRANT/REVOKE) limite les dégâts potentiels d'une injection SQL réussie.", True),
            T("Les requêtes paramétrées augmentent le risque d'injection SQL par rapport à la concaténation de chaînes.", False),
        ],
    ),
    quiz(
        "Fonctions de chaînes avancées : LENGTH, REPLACE, POSITION",
        "Aller plus loin dans la manipulation de texte avec des fonctions courantes.",
        [
            S(
                "Quelle fonction retourne le nombre de caractères d'une chaîne ?",
                ["LENGTH(chaine)", "SIZE(chaine)", "COUNT_CHARS(chaine)", "WIDTH(chaine)"],
            ),
            Sx(
                "Quelle fonction remplace toutes les occurrences d'un caractère ou d'une sous-chaîne dans un texte ?",
                ["REPLACE(chaine, ancien, nouveau)", "SWAP(chaine, ancien, nouveau)", "CHANGE(chaine, ancien, nouveau)", "ALTER_TEXT(chaine, ancien, nouveau)"],
                0,
            ),
            S(
                "Quelle requête remplace tous les tirets par des espaces dans la colonne reference ?",
                [
                    "SELECT REPLACE(reference, '-', ' ') FROM produits;",
                    "SELECT REPLACE(reference, ' ', '-') FROM produits;",
                    "SELECT SWAP(reference, '-', ' ') FROM produits;",
                    "SELECT reference REPLACE '-', ' ' FROM produits;",
                ],
            ),
            M(
                "Quelles affirmations sur les fonctions de chaînes avancées sont vraies ?",
                [
                    "LENGTH() est utile pour valider la longueur d'une donnée saisie",
                    "REPLACE() peut être combiné avec d'autres fonctions de chaînes dans une même expression",
                ],
                ["LENGTH() retourne toujours un nombre négatif", "REPLACE() ne fonctionne que sur des colonnes numériques"],
            ),
            T("Les fonctions de chaînes peuvent être combinées entre elles pour transformer un texte en plusieurs étapes.", True),
            T("LENGTH() retourne la valeur numérique stockée dans la colonne plutôt que le nombre de caractères.", False),
        ],
    ),
    quiz(
        "GROUP BY avec filtre combiné WHERE et HAVING",
        "Appliquer un filtre avant et après l'agrégation dans une même requête.",
        [
            S(
                "Quelle requête calcule le total des commandes 2024 par client, en ne gardant que les clients ayant dépensé plus de 500 ?",
                [
                    "SELECT client_id, SUM(montant) FROM commandes WHERE EXTRACT(YEAR FROM date_commande) = 2024 GROUP BY client_id HAVING SUM(montant) > 500;",
                    "SELECT client_id, SUM(montant) FROM commandes HAVING EXTRACT(YEAR FROM date_commande) = 2024 GROUP BY client_id WHERE SUM(montant) > 500;",
                    "SELECT client_id, SUM(montant) FROM commandes GROUP BY client_id WHERE SUM(montant) > 500 AND EXTRACT(YEAR FROM date_commande) = 2024;",
                    "SELECT client_id FROM commandes WHERE SUM(montant) > 500;",
                ],
            ),
            Sx(
                "Dans la requête précédente, pourquoi le filtre sur l'année est-il dans WHERE et non dans HAVING ?",
                [
                    "Parce qu'il s'applique à chaque ligne individuelle avant l'agrégation, pas à un résultat agrégé",
                    "Parce que WHERE et HAVING sont interchangeables sans aucune différence",
                    "Parce que HAVING ne peut jamais contenir de fonction EXTRACT",
                    "Parce que WHERE doit toujours être placé après GROUP BY",
                ],
                0,
            ),
            S(
                "Quelle requête combine un filtre WHERE sur la catégorie et un HAVING sur le nombre de produits par catégorie ?",
                [
                    "SELECT categorie, COUNT(*) FROM produits WHERE actif = TRUE GROUP BY categorie HAVING COUNT(*) >= 5;",
                    "SELECT categorie, COUNT(*) FROM produits HAVING actif = TRUE GROUP BY categorie WHERE COUNT(*) >= 5;",
                    "SELECT categorie FROM produits GROUP BY categorie WHERE COUNT(*) >= 5 HAVING actif = TRUE;",
                    "SELECT categorie, COUNT(*) FROM produits WHERE COUNT(*) >= 5 GROUP BY categorie;",
                ],
            ),
            M(
                "Quelles affirmations sur la combinaison WHERE + GROUP BY + HAVING sont vraies ?",
                [
                    "WHERE filtre les lignes individuelles avant le regroupement",
                    "HAVING filtre les groupes après application des fonctions d'agrégation",
                ],
                ["WHERE et HAVING s'exécutent toujours exactement au même moment", "HAVING doit obligatoirement précéder WHERE dans l'ordre d'écriture de la requête"],
            ),
            T("Une requête peut combiner WHERE, GROUP BY et HAVING pour filtrer à deux niveaux différents.", True),
            T("WHERE peut contenir directement une fonction d'agrégation comme SUM() sans aucune restriction.", False),
        ],
    ),
    quiz(
        "DEFAULT, AUTO_INCREMENT et génération de valeurs",
        "Générer automatiquement des valeurs par défaut ou incrémentales.",
        [
            S(
                "Quelle syntaxe est couramment utilisée pour qu'une colonne id s'incrémente automatiquement (style PostgreSQL) ?",
                ["id SERIAL PRIMARY KEY", "id AUTO PRIMARY KEY", "id INCREMENT(1) KEY", "id NUMBER++ PRIMARY KEY"],
            ),
            Sx(
                "Quelle clause attribue la date du jour par défaut à une colonne date_creation si aucune valeur n'est fournie ?",
                ["DEFAULT CURRENT_DATE", "AUTO CURRENT_DATE", "INIT CURRENT_DATE", "= CURRENT_DATE"],
                0,
            ),
            S(
                "Que se passe-t-il si on insère explicitement une valeur dans une colonne avec DEFAULT déjà définie ?",
                [
                    "La valeur explicitement fournie est utilisée à la place de la valeur par défaut",
                    "Une erreur est systématiquement levée",
                    "La valeur par défaut est utilisée malgré tout, en priorité",
                    "Les deux valeurs sont combinées automatiquement",
                ],
            ),
            M(
                "Quelles affirmations sur DEFAULT et l'auto-incrémentation sont vraies ?",
                [
                    "Une colonne auto-incrémentée évite de devoir gérer manuellement les identifiants uniques",
                    "La syntaxe d'auto-incrémentation varie selon le SGBD utilisé",
                ],
                ["DEFAULT empêche systématiquement toute insertion explicite de valeur", "Toutes les colonnes d'une table doivent obligatoirement avoir une valeur DEFAULT"],
            ),
            T("Une colonne définie avec une valeur DEFAULT n'est pas obligatoirement renseignée lors de l'INSERT.", True),
            T("La syntaxe d'auto-incrémentation est rigoureusement identique dans absolument tous les SGBD.", False),
        ],
    ),
    quiz(
        "Comparer EXISTS, IN et JOIN pour une même question métier",
        "Choisir la bonne technique selon le contexte pour tester l'existence d'une relation.",
        [
            S(
                "Quelle requête utilisant JOIN trouve les clients ayant commandé le produit 'Souris' (avec un risque de doublons si plusieurs commandes correspondent) ?",
                [
                    "SELECT DISTINCT c.* FROM clients c JOIN commandes co ON c.id = co.client_id JOIN produits p ON co.produit_id = p.id WHERE p.nom = 'Souris';",
                    "SELECT c.* FROM clients c WHERE p.nom = 'Souris';",
                    "SELECT c.* FROM clients c JOIN produits p ON p.nom = 'Souris';",
                    "SELECT c.* FROM clients c, produits p WHERE p.nom = 'Souris' GROUP BY c.id;",
                ],
            ),
            Sx(
                "Pourquoi EXISTS est-il souvent préféré à JOIN quand on veut juste tester une existence sans afficher les colonnes de l'autre table ?",
                [
                    "Parce qu'EXISTS évite les doublons potentiels et peut s'arrêter dès qu'une correspondance est trouvée",
                    "Parce que JOIN ne peut jamais être utilisé avec WHERE",
                    "Parce qu'EXISTS retourne toujours plus de colonnes que JOIN",
                    "Il n'y a aucune différence de comportement entre les deux approches",
                ],
                0,
            ),
            S(
                "Quelle requête avec EXISTS est équivalente à la question 'clients ayant commandé le produit Souris' sans risque de doublons ?",
                [
                    "SELECT * FROM clients c WHERE EXISTS (SELECT 1 FROM commandes co JOIN produits p ON co.produit_id = p.id WHERE co.client_id = c.id AND p.nom = 'Souris');",
                    "SELECT * FROM clients c WHERE c.id IN produits.nom;",
                    "SELECT * FROM clients WHERE EXISTS 'Souris';",
                    "SELECT * FROM clients c JOIN EXISTS commandes;",
                ],
            ),
            M(
                "Quelles affirmations sur le choix entre EXISTS, IN et JOIN sont vraies ?",
                [
                    "JOIN peut produire des doublons si la relation n'est pas one-to-one",
                    "EXISTS est souvent adapté pour des tests d'existence purs, sans besoin d'afficher de colonnes liées",
                ],
                ["IN, EXISTS et JOIN produisent toujours mathématiquement le même nombre de lignes sans exception", "JOIN ne peut jamais provoquer de doublons, quel que soit le contexte"],
            ),
            T("Le choix entre EXISTS, IN ou JOIN dépend souvent du besoin réel (existence simple vs affichage de colonnes liées) et des performances attendues.", True),
            T("DISTINCT n'a jamais d'utilité après un JOIN, quelle que soit la cardinalité de la relation.", False),
        ],
    ),
    quiz(
        "Synthèse : conception d'un schéma e-commerce simplifié",
        "Appliquer les notions de modélisation à un cas concret de boutique en ligne.",
        [
            S(
                "Dans un schéma e-commerce simple (clients, commandes, produits, lignes_commande), quelle table relie commandes et produits en gérant les quantités ?",
                ["lignes_commande", "clients", "commandes", "produits"],
            ),
            Sx(
                "Pourquoi une table lignes_commande est-elle nécessaire plutôt que de relier directement commandes à produits ?",
                [
                    "Parce qu'une commande peut contenir plusieurs produits et un produit peut apparaître dans plusieurs commandes (many-to-many) avec une quantité associée",
                    "Parce qu'une commande ne peut contenir qu'un seul produit",
                    "Parce que les produits ne peuvent jamais être commandés plusieurs fois",
                    "Cette table n'a en réalité aucune utilité",
                ],
                0,
            ),
            S(
                "Quelle requête calcule le montant total d'une commande à partir de lignes_commande (colonnes quantite, prix_unitaire) ?",
                [
                    "SELECT commande_id, SUM(quantite * prix_unitaire) FROM lignes_commande GROUP BY commande_id;",
                    "SELECT commande_id, quantite + prix_unitaire FROM lignes_commande;",
                    "SELECT SUM(quantite) FROM lignes_commande GROUP BY prix_unitaire;",
                    "SELECT commande_id, AVG(quantite * prix_unitaire) FROM lignes_commande;",
                ],
            ),
            M(
                "Quelles affirmations sur ce schéma e-commerce sont vraies ?",
                [
                    "clients et commandes ont typiquement une relation one-to-many",
                    "commandes et produits ont typiquement une relation many-to-many via lignes_commande",
                ],
                ["Toutes les relations de ce schéma sont obligatoirement one-to-one", "lignes_commande n'a besoin d'aucune clé étrangère"],
            ),
            T("Une table associative comme lignes_commande contient généralement les clés étrangères vers commandes et produits.", True),
            T("Dans ce modèle, un client ne peut techniquement passer qu'une seule commande dans toute sa vie.", False),
        ],
    ),
    quiz(
        "Synthèse : audit et historisation des données",
        "Concevoir un mécanisme de suivi des modifications avec triggers et tables d'historique.",
        [
            S(
                "Quelle structure de table est typique pour stocker un historique des modifications de prix d'un produit ?",
                [
                    "historique_prix(id, produit_id, ancien_prix, nouveau_prix, date_modification)",
                    "produits(id, nom, prix) sans aucune table supplémentaire",
                    "Une seule colonne 'log' contenant tout le texte en une seule fois",
                    "Il est impossible de tracer un historique en SQL",
                ],
            ),
            Sx(
                "Quel type de trigger serait utilisé pour enregistrer automatiquement chaque changement de prix dans cette table d'historique ?",
                [
                    "Un trigger AFTER UPDATE sur la table produits",
                    "Un trigger BEFORE SELECT sur la table produits",
                    "Un trigger qui s'exécute uniquement au démarrage du serveur",
                    "Aucun trigger n'est nécessaire pour ce besoin",
                ],
                0,
            ),
            S(
                "Quelle requête retourne l'historique des changements de prix d'un produit donné, du plus récent au plus ancien ?",
                [
                    "SELECT * FROM historique_prix WHERE produit_id = 42 ORDER BY date_modification DESC;",
                    "SELECT * FROM historique_prix WHERE produit_id = 42 ORDER BY date_modification ASC LIMIT 1;",
                    "SELECT * FROM produits WHERE id = 42 ORDER BY historique_prix;",
                    "SELECT * FROM historique_prix GROUP BY produit_id HAVING produit_id = 42;",
                ],
            ),
            M(
                "Quelles affirmations sur l'audit de données sont vraies ?",
                [
                    "Les triggers AFTER UPDATE/DELETE sont couramment utilisés pour journaliser les changements",
                    "Une table d'historique permet de conserver une trace des anciennes valeurs",
                ],
                ["L'audit de données est interdit par le langage SQL", "Une table d'historique ne peut jamais contenir de clé étrangère"],
            ),
            T("Historiser les modifications de données est une pratique courante pour la traçabilité et la conformité.", True),
            T("Une table d'historique des modifications ne sert jamais à rien en pratique et est toujours superflue.", False),
        ],
    ),
    quiz(
        "Synthèse : rapports analytiques avec fenêtrage",
        "Construire des rapports avancés combinant agrégats classiques et fonctions de fenêtrage.",
        [
            S(
                "Quelle requête calcule, pour chaque vente, le pourcentage qu'elle représente du total des ventes de sa catégorie ?",
                [
                    "SELECT *, montant * 100.0 / SUM(montant) OVER (PARTITION BY categorie) AS pourcentage FROM ventes;",
                    "SELECT *, montant / SUM(montant) FROM ventes GROUP BY categorie;",
                    "SELECT categorie, montant * 100 FROM ventes;",
                    "SELECT *, montant / COUNT(*) OVER (PARTITION BY categorie) FROM ventes;",
                ],
            ),
            Sx(
                "Quel avantage offre SUM() OVER (PARTITION BY ...) par rapport à un simple GROUP BY pour ce type de rapport ?",
                [
                    "Il permet de conserver chaque ligne de détail tout en affichant un total de référence par groupe",
                    "Il supprime automatiquement toutes les lignes du détail",
                    "Il fonctionne uniquement sans aucune clause PARTITION BY",
                    "Il ne peut jamais être combiné avec une opération arithmétique",
                ],
                0,
            ),
            S(
                "Quelle requête calcule le rang de chaque vendeur selon son chiffre d'affaires total, du meilleur au moins bon ?",
                [
                    "SELECT vendeur_id, SUM(montant) AS total, RANK() OVER (ORDER BY SUM(montant) DESC) AS rang FROM ventes GROUP BY vendeur_id;",
                    "SELECT vendeur_id, RANK() FROM ventes GROUP BY vendeur_id;",
                    "SELECT vendeur_id, SUM(montant) FROM ventes ORDER BY RANK();",
                    "SELECT vendeur_id, MAX(montant) PARTITION BY vendeur_id FROM ventes;",
                ],
            ),
            M(
                "Quelles affirmations sur les rapports analytiques avec fenêtrage sont vraies ?",
                [
                    "On peut combiner une fonction d'agrégation classique (avec GROUP BY) et une fonction de fenêtrage dans des contextes différents de la même analyse",
                    "Les fonctions de fenêtrage permettent de calculer des ratios ou pourcentages par rapport à un total de groupe",
                ],
                ["Les fonctions de fenêtrage ne peuvent jamais être combinées avec des calculs arithmétiques", "RANK() OVER ne peut jamais être combiné avec ORDER BY à l'intérieur de OVER()"],
            ),
            T("Les fonctions de fenêtrage sont particulièrement utiles pour les rapports analytiques nécessitant à la fois le détail et des comparaisons de groupe.", True),
            T("Une fonction de fenêtrage transforme toujours les lignes de détail en une seule ligne agrégée, comme GROUP BY.", False),
        ],
    ),
    quiz(
        "Synthèse : nettoyage et qualité des données",
        "Identifier et corriger des données incohérentes avec des requêtes SQL.",
        [
            S(
                "Quelle requête identifie les doublons potentiels d'emails dans la table clients ?",
                [
                    "SELECT email, COUNT(*) FROM clients GROUP BY email HAVING COUNT(*) > 1;",
                    "SELECT email FROM clients WHERE COUNT(*) > 1;",
                    "SELECT DISTINCT email FROM clients HAVING COUNT(*) > 1;",
                    "SELECT email, COUNT(*) FROM clients WHERE email > 1;",
                ],
            ),
            Sx(
                "Quelle requête nettoie les espaces superflus autour des noms de clients avant de les comparer ?",
                [
                    "SELECT TRIM(nom) FROM clients;",
                    "SELECT CLEAN(nom) FROM clients;",
                    "SELECT nom WITHOUT SPACE FROM clients;",
                    "SELECT REMOVE_SPACES(nom) FROM clients;",
                ],
                0,
            ),
            S(
                "Quelle requête uniformise la casse des emails en minuscules pour éviter les faux doublons ?",
                [
                    "SELECT LOWER(email) FROM clients;",
                    "SELECT UPPER(email) FROM clients;",
                    "SELECT CASE(email) FROM clients;",
                    "SELECT NORMALIZE(email) FROM clients;",
                ],
            ),
            M(
                "Quelles affirmations sur la qualité des données sont vraies ?",
                [
                    "Combiner TRIM et LOWER aide à détecter des doublons qui diffèrent seulement par la casse ou les espaces",
                    "GROUP BY avec HAVING COUNT(*) > 1 est une technique courante pour repérer des doublons",
                ],
                ["La qualité des données n'a aucun impact sur la fiabilité des analyses", "Il est impossible de détecter des doublons avec une requête SQL"],
            ),
            T("Des fonctions comme TRIM, LOWER ou UPPER peuvent aider à normaliser des données avant de les comparer.", True),
            T("Deux emails identiques mais avec une casse différente sont toujours automatiquement considérés comme des doublons sans aucun traitement.", False),
        ],
    ),
    quiz(
        "Synthèse : pagination et tri stable pour une API",
        "Concevoir des requêtes de pagination fiables pour une application.",
        [
            S(
                "Quelle requête retourne la deuxième page de résultats (10 éléments par page) triés par date de création ?",
                [
                    "SELECT * FROM articles ORDER BY date_creation LIMIT 10 OFFSET 10;",
                    "SELECT * FROM articles ORDER BY date_creation LIMIT 10 OFFSET 0;",
                    "SELECT * FROM articles ORDER BY date_creation OFFSET 10;",
                    "SELECT * FROM articles LIMIT 20 OFFSET 10;",
                ],
            ),
            Sx(
                "Pourquoi un tri stable (avec une colonne unique en plus, ex: id) est-il recommandé pour la pagination ?",
                [
                    "Pour éviter que des lignes avec des valeurs de tri identiques n'apparaissent dans un ordre incohérent entre deux pages",
                    "Parce que LIMIT ne fonctionne jamais sans tri",
                    "Parce qu'un tri stable supprime automatiquement les doublons",
                    "Cela n'a aucune importance pratique pour la pagination",
                ],
                0,
            ),
            S(
                "Quelle requête trie de façon stable par date de création puis par id en cas d'égalité ?",
                [
                    "SELECT * FROM articles ORDER BY date_creation, id LIMIT 10 OFFSET 20;",
                    "SELECT * FROM articles ORDER BY date_creation LIMIT 10 OFFSET 20;",
                    "SELECT * FROM articles ORDER BY id ORDER BY date_creation LIMIT 10;",
                    "SELECT * FROM articles LIMIT 10 OFFSET 20 ORDER BY date_creation AND id;",
                ],
            ),
            M(
                "Quelles affirmations sur la pagination SQL sont vraies ?",
                [
                    "OFFSET peut devenir coûteux en performance sur de très grandes tables",
                    "Trier sur une colonne unique supplémentaire évite les ambiguïtés de tri",
                ],
                ["LIMIT et OFFSET garantissent toujours des performances constantes quel que soit le volume de données", "La pagination ne nécessite jamais de clause ORDER BY"],
            ),
            T("Une pagination basée sur LIMIT/OFFSET sans ORDER BY explicite peut donner des résultats incohérents entre deux requêtes.", True),
            T("OFFSET garantit des performances identiques quelle que soit la valeur indiquée, même sur des millions de lignes.", False),
        ],
    ),
    quiz(
        "Synthèse : agrégations conditionnelles avec FILTER ou CASE",
        "Calculer plusieurs métriques conditionnelles dans une seule requête agrégée.",
        [
            S(
                "Quelle requête calcule en une seule ligne le nombre de commandes livrées et le nombre de commandes annulées ?",
                [
                    "SELECT SUM(CASE WHEN statut = 'livree' THEN 1 ELSE 0 END) AS livrees, SUM(CASE WHEN statut = 'annulee' THEN 1 ELSE 0 END) AS annulees FROM commandes;",
                    "SELECT COUNT(statut) FROM commandes GROUP BY statut;",
                    "SELECT statut, COUNT(*) FROM commandes WHERE statut IN ('livree', 'annulee');",
                    "SELECT SUM(statut = 'livree' AND statut = 'annulee') FROM commandes;",
                ],
            ),
            Sx(
                "Pourquoi utiliser CASE WHEN ... THEN 1 ELSE 0 END dans une fonction SUM() plutôt qu'un simple COUNT(*) avec GROUP BY ?",
                [
                    "Pour obtenir plusieurs compteurs conditionnels alignés sur une seule ligne de résultat",
                    "Parce que COUNT(*) ne fonctionne jamais avec GROUP BY",
                    "Parce que CASE WHEN est plus rapide dans tous les cas sans exception",
                    "Cette technique n'apporte rigoureusement aucun bénéfice",
                ],
                0,
            ),
            S(
                "Quelle requête calcule le chiffre d'affaires total uniquement pour les commandes livrées, dans une requête qui agrège toutes les commandes ?",
                [
                    "SELECT SUM(CASE WHEN statut = 'livree' THEN montant ELSE 0 END) AS ca_livre FROM commandes;",
                    "SELECT SUM(montant) FROM commandes WHERE statut = 'livree' GROUP BY statut;",
                    "SELECT montant FROM commandes WHERE statut = 'livree';",
                    "SELECT SUM(montant) FROM commandes HAVING statut = 'livree';",
                ],
            ),
            M(
                "Quelles affirmations sur les agrégations conditionnelles sont vraies ?",
                [
                    "CASE WHEN combiné à SUM ou COUNT permet de calculer plusieurs métriques en une seule ligne",
                    "Cette technique évite d'avoir à écrire plusieurs requêtes séparées pour chaque condition",
                ],
                ["Cette technique ne peut être utilisée qu'avec la fonction AVG()", "CASE WHEN dans une agrégation provoque toujours une erreur de syntaxe"],
            ),
            T("Les agrégations conditionnelles via CASE WHEN sont une technique courante pour des tableaux de bord compacts.", True),
            T("Il est impossible de combiner CASE WHEN avec une fonction d'agrégation comme SUM ou COUNT.", False),
        ],
    ),
    quiz(
        "Synthèse finale : choisir la bonne clause SQL selon le besoin",
        "Récapituler les bons réflexes pour choisir la clause SQL adaptée à chaque situation.",
        [
            S(
                "Pour limiter les lignes retournées selon une condition sur les données brutes, quelle clause utiliser ?",
                ["WHERE", "HAVING", "LIMIT", "GROUP BY"],
            ),
            Sx(
                "Pour filtrer un résultat après une agrégation comme SUM ou COUNT, quelle clause est adaptée ?",
                ["HAVING", "WHERE", "ORDER BY", "DISTINCT"],
                0,
            ),
            S(
                "Pour garantir qu'une colonne ne contient jamais de valeur dupliquée, quelle contrainte choisir ?",
                ["UNIQUE", "DEFAULT", "CHECK uniquement", "NOT NULL uniquement"],
            ),
            M(
                "Quelles associations clause/besoin sont correctes ?",
                [
                    "ORDER BY pour trier le résultat final",
                    "GROUP BY pour regrouper des lignes en vue d'une agrégation",
                ],
                ["WHERE pour filtrer après une agrégation", "DISTINCT pour trier les résultats par ordre alphabétique"],
            ),
            T("Combiner WHERE, GROUP BY, HAVING et ORDER BY dans le bon ordre permet de répondre à des besoins analytiques complexes.", True),
            T("HAVING et WHERE sont strictement interchangeables dans tous les contextes sans aucune nuance.", False),
        ],
    ),
]
