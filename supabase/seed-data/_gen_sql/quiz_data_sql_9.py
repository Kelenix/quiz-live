from helpers_sql import S, Sx, M, T, quiz

QUIZZES = [
    quiz(
        "CROSS JOIN et combinaisons de variantes produit",
        "Utiliser le produit cartésien pour générer toutes les combinaisons possibles.",
        [
            S(
                "Quelle requête génère toutes les combinaisons possibles de tailles et de couleurs pour un produit ?",
                [
                    "SELECT * FROM tailles CROSS JOIN couleurs;",
                    "SELECT * FROM tailles INNER JOIN couleurs ON tailles.id = couleurs.id;",
                    "SELECT * FROM tailles UNION couleurs;",
                    "SELECT * FROM tailles WHERE couleurs.id IS NOT NULL;",
                ],
            ),
            Sx(
                "Si la table tailles contient 4 lignes et couleurs en contient 6, combien de lignes produit un CROSS JOIN entre les deux ?",
                ["24", "10", "6", "4"],
                0,
            ),
            S(
                "Quel risque existe-t-il si on utilise par erreur une virgule entre deux tables sans condition de jointure dans la clause FROM ?",
                [
                    "On obtient involontairement un produit cartésien (équivalent à un CROSS JOIN)",
                    "La requête est automatiquement rejetée par le SGBD",
                    "Seules les lignes correspondantes sont retournées comme avec INNER JOIN",
                    "Aucune ligne n'est retournée",
                ],
            ),
            M(
                "Quelles affirmations sur CROSS JOIN sont vraies ?",
                [
                    "CROSS JOIN peut être utile pour générer des combinaisons exhaustives de variantes",
                    "Un CROSS JOIN sur de grandes tables peut produire un volume de données très important",
                ],
                ["CROSS JOIN nécessite obligatoirement une clause ON", "CROSS JOIN élimine automatiquement les doublons générés"],
            ),
            T("CROSS JOIN sans condition de filtre peut générer un nombre de lignes égal au produit du nombre de lignes des deux tables.", True),
            T("CROSS JOIN est strictement identique à un LEFT JOIN dans tous les cas.", False),
        ],
    ),
    quiz(
        "Synthèse : choisir entre vue, CTE et table temporaire",
        "Comparer trois approches pour structurer des requêtes intermédiaires complexes.",
        [
            S(
                "Quelle option est la plus adaptée pour réutiliser une logique de requête complexe dans de nombreuses requêtes futures, de façon permanente ?",
                ["Créer une vue (CREATE VIEW)", "Utiliser uniquement une CTE ponctuelle", "Ne rien faire et copier-coller la requête partout", "Utiliser uniquement LIMIT"],
            ),
            Sx(
                "Quelle option est la plus adaptée pour structurer une requête complexe en plusieurs étapes nommées, sans persistance au-delà de la requête ?",
                [
                    "Une CTE (WITH ... AS)",
                    "Une vue matérialisée permanente",
                    "Une nouvelle base de données entière",
                    "Un trigger AFTER INSERT",
                ],
                0,
            ),
            S(
                "Dans quel contexte une table temporaire peut-elle être préférée à une CTE ?",
                [
                    "Quand le résultat intermédiaire doit être réutilisé plusieurs fois dans une session longue avec de gros volumes",
                    "Quand on veut simplement trier un résultat final",
                    "Quand on a besoin d'une seule valeur scalaire",
                    "Les tables temporaires ne sont jamais utiles en pratique",
                ],
            ),
            M(
                "Quelles affirmations sur vue/CTE/table temporaire sont vraies ?",
                [
                    "Une vue est persistante dans le schéma jusqu'à sa suppression explicite",
                    "Une CTE n'existe que pendant l'exécution de la requête qui la définit",
                ],
                ["Les trois approches sont rigoureusement interchangeables dans absolument tous les contextes", "Une table temporaire est automatiquement convertie en vue"],
            ),
            T("Le choix entre vue, CTE et table temporaire dépend du besoin de réutilisation, de persistance et de volume de données.", True),
            T("Une CTE est automatiquement sauvegardée de façon permanente dans le schéma de la base de données.", False),
        ],
    ),
    quiz(
        "Synthèse : opérateurs arithmétiques et priorité des opérations",
        "Maîtriser l'ordre d'évaluation des opérateurs dans une expression SQL.",
        [
            S(
                "Quel est le résultat de l'expression `2 + 3 * 4` selon les règles de priorité standard ?",
                ["14", "20", "9", "24"],
            ),
            Sx(
                "Comment forcer l'addition à être évaluée avant la multiplication dans `2 + 3 * 4` ?",
                ["En utilisant des parenthèses : (2 + 3) * 4", "En inversant simplement l'ordre des nombres", "Ce n'est jamais possible en SQL", "En utilisant CAST"],
                0,
            ),
            S(
                "Quelle requête calcule correctement le prix remisé avec parenthèses explicites pour éviter toute ambiguïté ?",
                [
                    "SELECT prix - (prix * remise_pourcentage / 100) AS prix_final FROM produits;",
                    "SELECT prix - prix * remise_pourcentage / 100 AS prix_final FROM produits;",
                    "Les deux requêtes précédentes donnent strictement le même résultat numérique",
                    "SELECT prix * remise_pourcentage - 100 / prix FROM produits;",
                ],
                2,
            ),
            M(
                "Quelles affirmations sur la priorité des opérateurs arithmétiques sont vraies ?",
                [
                    "La multiplication et la division ont généralement une priorité plus élevée que l'addition et la soustraction",
                    "Les parenthèses permettent de clarifier ou modifier l'ordre d'évaluation souhaité",
                ],
                ["L'addition est toujours évaluée avant la multiplication par défaut", "Les parenthèses n'ont aucun effet sur le résultat d'un calcul SQL"],
            ),
            T("Utiliser des parenthèses dans les expressions arithmétiques améliore la lisibilité et évite les erreurs d'interprétation.", True),
            T("En SQL, la division est toujours évaluée après l'addition par défaut, sans aucune règle de priorité.", False),
        ],
    ),
]
