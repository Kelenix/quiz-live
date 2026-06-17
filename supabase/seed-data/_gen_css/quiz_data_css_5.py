# -*- coding: utf-8 -*-
"""Quiz 41-50 : CSS Grid."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Introduction à CSS Grid",
        "Découvrir le système de grille bidimensionnel de CSS.",
        [
            S("Quelle propriété transforme un élément en conteneur de grille CSS ?",
              ["display: grid", "display: flex", "position: grid", "layout: grid"]),
            S("Quelle est la principale différence entre Flexbox et Grid en termes de dimensions gérées ?",
              ["Grid gère deux dimensions (lignes et colonnes) alors que Flexbox est principalement unidimensionnel", "Flexbox gère deux dimensions et Grid une seule", "Les deux sont strictement identiques", "Grid ne fonctionne que pour les images"]),
            S("Comment appelle-t-on les enfants directs d'un conteneur grid ?",
              ["Les grid items", "Les grid cells uniquement", "Les flex items", "Les grid parents"]),
            M("Quelles propriétés s'appliquent directement sur le conteneur grid ?",
              ["grid-template-columns", "grid-template-rows"], {0, 1}, ["grid-area", "justify-self"]),
            T("CSS Grid permet de créer des mises en page complexes en lignes et colonnes sans recourir à des éléments flottants.", True),
            T("Un conteneur grid ne peut définir que des colonnes, jamais de lignes explicites.", False),
        ],
    )

    quiz(
        "grid-template-columns et grid-template-rows",
        "Définir la structure des colonnes et lignes d'une grille.",
        [
            S("Quelle propriété définit le nombre et la taille des colonnes d'une grille ?",
              ["grid-template-columns", "grid-template-rows", "grid-gap", "grid-area"]),
            S("Que fait la déclaration `grid-template-columns: repeat(3, 1fr);` ?",
              ["Elle crée trois colonnes de largeur égale", "Elle crée une seule colonne répétée trois fois en hauteur", "Elle crée trois lignes de hauteur égale", "Elle limite la grille à 3 pixels de large"]),
            S("Que fait la fonction `repeat()` dans une déclaration de grille ?",
              ["Elle répète un motif de colonnes ou de lignes un certain nombre de fois", "Elle duplique le contenu des cellules", "Elle inverse l'ordre des colonnes", "Elle anime la grille en boucle"]),
            M("Quelles propriétés permettent de définir la structure de base d'une grille CSS ?",
              ["grid-template-columns", "grid-template-rows"], {0, 1}, ["flex-wrap", "justify-content"]),
            T("`grid-template-columns: 1fr 2fr;` crée deux colonnes où la seconde est deux fois plus large que la première.", True),
            T("Il est impossible de mélanger des unités fixes (px) et l'unité fr dans une même déclaration grid-template-columns.", False),
        ],
    )

    quiz(
        "L'unité fr et la répartition flexible de l'espace",
        "Comprendre la fraction d'espace disponible (fr) propre à CSS Grid.",
        [
            S("Que représente l'unité `fr` dans CSS Grid ?",
              ["Une fraction de l'espace disponible dans le conteneur grid", "Une unité fixe équivalente à 1 pixel", "Un pourcentage de la fenêtre du navigateur", "Une unité réservée aux marges uniquement"]),
            S("Avec `grid-template-columns: 1fr 1fr 2fr;`, quelle proportion de l'espace total occupe la troisième colonne ?",
              ["La moitié de l'espace total (2 parts sur 4)", "Un quart de l'espace total", "Toute la largeur disponible", "Un tiers de l'espace total"]),
            S("Peut-on combiner l'unité `fr` avec des valeurs fixes comme `200px` dans la même déclaration de grille ?",
              ["Oui, par exemple grid-template-columns: 200px 1fr;", "Non, ce sont des unités incompatibles", "Oui, mais uniquement avec grid-template-rows", "Non, cela génère systématiquement une erreur de syntaxe"]),
            M("Quelles affirmations sur l'unité `fr` sont correctes ?",
              ["Elle répartit l'espace restant après soustraction des tailles fixes", "Elle est spécifique à CSS Grid (et à certaines propriétés Flexbox apparentées)"], {0, 1}, ["Elle est identique à une valeur en pourcentage dans tous les cas", "Elle ne peut être utilisée qu'une seule fois par grille"]),
            T("L'unité `fr` facilite la création de colonnes proportionnelles sans calculs manuels en pourcentage.", True),
            T("`grid-template-columns: 1fr 1fr;` crée systématiquement deux colonnes de largeur identique uniquement si l'espace total est divisible par deux pixels exacts.", False),
        ],
    )

    quiz(
        "L'espacement avec gap",
        "Créer des espaces réguliers entre les lignes et colonnes d'une grille ou d'un conteneur flex.",
        [
            S("Quelle propriété permet de définir un espace uniforme entre toutes les cellules d'une grille ?",
              ["gap", "margin", "padding", "spacing"]),
            S("Quelle propriété définit spécifiquement l'espace entre les colonnes d'une grille ?",
              ["column-gap", "row-gap", "grid-spacing", "gutter"]),
            S("Quelle propriété définit spécifiquement l'espace entre les lignes d'une grille ?",
              ["row-gap", "column-gap", "grid-margin", "line-gap"]),
            M("Sur quels types de conteneurs la propriété `gap` peut-elle être utilisée en CSS moderne ?",
              ["Les conteneurs grid", "Les conteneurs flex"], {0, 1}, ["Les éléments en position absolute uniquement", "Les pseudo-éléments uniquement"]),
            T("La propriété `gap` remplace avantageusement l'utilisation de marges sur chaque cellule pour créer un espacement régulier.", True),
            T("La propriété `gap` crée un espace supplémentaire avant la première colonne et après la dernière.", False),
        ],
    )

    quiz(
        "grid-area et le placement nommé",
        "Positionner des éléments dans la grille en nommant des zones.",
        [
            S("Quelle propriété permet d'assigner un nom de zone à un grid item pour le placer facilement ?",
              ["grid-area", "grid-name", "area-template", "grid-zone"]),
            S("Quelle propriété du conteneur permet de visualiser et nommer la disposition globale des zones sous forme de schéma textuel ?",
              ["grid-template-areas", "grid-template-columns", "grid-gap", "grid-flow"]),
            S("Dans `grid-template-areas`, quelle valeur spéciale indique qu'une cellule de la grille reste vide ?",
              ["Un point .", "Le mot none", "Le mot empty", "Une chaîne vide \"\""]),
            M("Quelles propriétés permettent de placer un item en utilisant directement les numéros de ligne et de colonne plutôt que des noms de zone ?",
              ["grid-column", "grid-row"], {0, 1}, ["grid-template-areas", "justify-items"]),
            T("`grid-area` peut aussi servir de raccourci pour grid-row-start, grid-column-start, grid-row-end et grid-column-end.", True),
            T("Les noms définis dans grid-template-areas doivent former des rectangles cohérents, sans former de formes en L irrégulières.", True),
        ],
    )

    quiz(
        "Alignement dans CSS Grid",
        "Positionner le contenu des cellules et la grille elle-même avec justify-items et align-items.",
        [
            S("Quelle propriété aligne horizontalement le contenu de chaque cellule de grille (sur l'axe des colonnes) ?",
              ["justify-items", "align-items", "justify-content", "place-content"]),
            S("Quelle propriété aligne verticalement le contenu de chaque cellule de grille (sur l'axe des lignes) ?",
              ["align-items", "justify-items", "align-self uniquement", "text-align"]),
            S("Quelle propriété raccourcie combine justify-items et align-items en une seule déclaration ?",
              ["place-items", "place-content", "grid-align", "align-all"]),
            M("Quelles propriétés permettent d'aligner un grid item individuel, indépendamment des autres items ?",
              ["justify-self", "align-self"], {0, 1}, ["justify-items", "grid-template-rows"]),
            T("`justify-content` et `justify-items` n'ont pas le même rôle : le premier positionne la grille entière, le second positionne le contenu dans chaque cellule.", True),
            T("`place-items: center;` équivaut à définir à la fois `align-items: center;` et `justify-items: center;`.", True),
        ],
    )

    quiz(
        "Grilles implicites et explicites",
        "Comprendre la différence entre les lignes/colonnes définies et générées automatiquement.",
        [
            S("Qu'est-ce qu'une grille \"implicite\" en CSS Grid ?",
              ["Des lignes ou colonnes générées automatiquement quand des items dépassent la grille explicite définie", "Une grille créée uniquement par JavaScript", "Une grille sans aucune colonne visible", "Une grille qui ne peut contenir qu'une seule cellule"]),
            S("Quelle propriété permet de définir la taille des lignes générées implicitement ?",
              ["grid-auto-rows", "grid-template-rows uniquement", "grid-gap", "row-height"]),
            S("Quelle propriété contrôle si les nouveaux items débordant la grille explicite remplissent d'abord les lignes ou les colonnes ?",
              ["grid-auto-flow", "grid-template-areas", "grid-direction", "flex-flow"]),
            M("Quelles propriétés concernent spécifiquement la grille implicite (générée automatiquement) ?",
              ["grid-auto-columns", "grid-auto-rows"], {0, 1}, ["grid-template-columns", "grid-template-areas"]),
            T("Si plus d'items que de cellules explicites sont ajoutés à une grille, CSS Grid crée automatiquement des lignes implicites pour les accueillir.", True),
            T("`grid-auto-flow: dense` tente de combler les espaces vides en réorganisant l'ordre de placement automatique des items.", True),
        ],
    )

    quiz(
        "La fonction minmax() et les grilles responsives",
        "Créer des grilles flexibles qui s'adaptent à la taille de l'écran sans media queries.",
        [
            S("Que fait la fonction `minmax(150px, 1fr)` dans une déclaration grid-template-columns ?",
              ["Elle définit une taille de colonne qui ne descend jamais sous 150px mais peut grandir jusqu'à 1fr", "Elle fixe une taille exacte de 150 pixels", "Elle limite le nombre de colonnes à 150", "Elle est uniquement utilisable avec grid-template-rows"]),
            S("Que fait la combinaison `repeat(auto-fit, minmax(200px, 1fr))` ?",
              ["Elle crée autant de colonnes de 200px minimum que possible, en étirant les colonnes existantes pour remplir l'espace", "Elle crée toujours exactement 200 colonnes", "Elle désactive le retour à la ligne automatique", "Elle équivaut à display: flex; flex-wrap: nowrap;"]),
            S("Quelle est la différence principale entre `auto-fit` et `auto-fill` dans repeat() ?",
              ["auto-fit étire les colonnes existantes pour combler l'espace vide, auto-fill conserve les emplacements vides de la taille définie", "Ce sont des synonymes stricts sans différence", "auto-fill ne fonctionne qu'avec des pourcentages", "auto-fit ne peut être utilisé qu'une seule fois par page"]),
            M("Pourquoi `minmax()` est-elle utile pour des grilles responsives sans media queries ?",
              ["Elle permet à une colonne de s'adapter automatiquement à la largeur de l'écran", "Elle évite d'avoir à écrire des breakpoints fixes pour des grilles de cartes par exemple"], {0, 1}, ["Elle remplace systématiquement la propriété gap", "Elle est incompatible avec repeat()"]),
            T("La combinaison `repeat(auto-fit, minmax())` est une technique très populaire pour créer des grilles de cartes responsives sans aucune media query.", True),
            T("La fonction `minmax()` ne peut être utilisée qu'à l'intérieur de grid-template-rows, jamais dans grid-template-columns.", False),
        ],
    )

    quiz(
        "Grilles imbriquées et sous-grilles",
        "Combiner Grid avec d'autres conteneurs et explorer le concept de subgrid.",
        [
            S("Peut-on imbriquer un conteneur flex à l'intérieur d'une cellule de grille CSS ?",
              ["Oui, un grid item peut lui-même être un conteneur flex ou grid", "Non, c'est interdit par la spécification", "Oui, mais seulement sur la première ligne", "Non, cela génère une erreur de rendu"]),
            S("Que permet la valeur `subgrid` pour grid-template-columns/rows ?",
              ["Un élément grid imbriqué peut hériter des pistes (tracks) de la grille parente", "Elle crée une grille totalement indépendante du parent", "Elle est un synonyme strict de repeat()", "Elle supprime toutes les colonnes de l'enfant"]),
            S("Pourquoi combiner Grid pour la structure générale et Flexbox pour l'alignement interne d'une carte est une pratique courante ?",
              ["Grid excelle en disposition bidimensionnelle, Flexbox excelle pour aligner du contenu sur un seul axe", "Flexbox et Grid sont mutuellement exclusifs sur une même page", "Grid ne peut pas contenir de texte", "Flexbox est obsolète depuis l'arrivée de Grid"]),
            M("Quelles affirmations sur les grilles imbriquées sont vraies ?",
              ["Une cellule de grille peut contenir sa propre grille indépendante", "Sans subgrid, une grille imbriquée ne partage pas automatiquement les pistes de la grille parente"], {0, 1}, ["Une grille imbriquée hérite obligatoirement de toutes les propriétés du parent", "subgrid est disponible depuis la première version de CSS"]),
            T("Le support de `subgrid` permet d'aligner précisément les colonnes d'une grille enfant sur celles de la grille parente.", True),
            T("Une grille CSS ne peut jamais être utilisée à l'intérieur d'un conteneur Flexbox.", False),
        ],
    )
