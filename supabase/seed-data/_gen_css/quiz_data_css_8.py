# -*- coding: utf-8 -*-
"""Quiz 71-80 : Responsive design, variables CSS, fonctions CSS (calc, clamp, min, max)."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Les bases du responsive design",
        "Adapter une mise en page à différentes tailles d'écran.",
        [
            S("Quelle règle CSS permet d'appliquer des styles selon la largeur de l'écran ?",
              ["@media", "@supports", "@font-face", "@responsive"]),
            S("Que signifie l'approche \"mobile-first\" en développement CSS responsive ?",
              ["Concevoir d'abord les styles pour mobile, puis ajouter des règles pour les écrans plus grands", "Concevoir uniquement pour les écrans de bureau", "Interdire l'utilisation de media queries", "Utiliser uniquement des unités fixes en pixels"]),
            S("Comment appelle-t-on les seuils de largeur d'écran où la mise en page change via une media query ?",
              ["Des breakpoints", "Des checkpoints", "Des keyframes", "Des viewports fixes"]),
            M("Quels éléments sont typiquement pris en compte pour rendre un site responsive ?",
              ["Les media queries", "Les unités relatives comme % ou rem"], {0, 1}, ["Les pseudo-éléments ::before", "La règle @font-face"]),
            T("L'approche mobile-first consiste généralement à utiliser `min-width` dans les media queries pour ajouter des styles aux écrans plus larges.", True),
            T("Le responsive design ne concerne que la largeur de l'écran et jamais l'orientation de l'appareil.", False),
        ],
    )

    quiz(
        "La règle @media et ses conditions",
        "Écrire des media queries précises pour cibler des conditions d'affichage.",
        [
            S("Quelle syntaxe de media query applique des styles uniquement quand la largeur de l'écran est inférieure ou égale à 768px ?",
              ["@media (max-width: 768px) { ... }", "@media (min-width: 768px) { ... }", "@media screen { width: 768px; }", "@media print (768px) { ... }"]),
            S("Quel type de media cible spécifiquement l'impression d'une page ?",
              ["print", "screen", "speech", "paper"]),
            S("Quelle condition de media query cible les écrans à haute densité de pixels (comme les écrans Retina) ?",
              ["min-resolution ou -webkit-min-device-pixel-ratio", "min-width", "orientation", "aspect-ratio"]),
            M("Quels opérateurs logiques peuvent être utilisés pour combiner des conditions dans une media query ?",
              ["and", "or"], {0, 1}, ["xor", "not-equal"]),
            T("On peut combiner plusieurs conditions dans une même media query, par exemple `@media (min-width: 600px) and (max-width: 900px)`.", True),
            T("La règle @media ne peut cibler que la largeur de l'écran et aucune autre caractéristique.", False),
        ],
    )

    quiz(
        "Stratégies de breakpoints",
        "Choisir et organiser des points de rupture cohérents pour un design adaptatif.",
        [
            S("Pourquoi privilégier des breakpoints basés sur le contenu plutôt que sur des appareils spécifiques ?",
              ["Parce que la diversité des appareils rend obsolète une liste figée de résolutions précises", "Parce que cela réduit le nombre de propriétés CSS disponibles", "Parce que c'est une obligation de la spécification CSS3", "Parce que cela empêche l'utilisation de Flexbox"]),
            S("Que signifie generalement un breakpoint \"large\" autour de 1024px et plus dans une approche courante ?",
              ["Le ciblage des écrans de type tablette large ou ordinateur de bureau", "Le ciblage exclusif des montres connectées", "Le ciblage des imprimantes", "Le ciblage des écrans de moins de 320px"]),
            S("Quelle unité est généralement déconseillée pour définir les breakpoints eux-mêmes par rapport à em ou rem dans certains contextes d'accessibilité (zoom) ?",
              ["px peut être moins flexible en cas de zoom texte selon le navigateur", "rem", "em", "Aucune différence n'existe jamais entre ces unités"]),
            M("Quelles bonnes pratiques sont associées à une stratégie de breakpoints efficace ?",
              ["Tester sur plusieurs tailles réelles d'écran", "Adapter les breakpoints au contenu plutôt qu'à des appareils figés"], {0, 1}, ["Définir un seul breakpoint unique pour tous les sites", "Éviter complètement les unités relatives"]),
            T("Une bonne pratique consiste à tester un design responsive sur plusieurs largeurs intermédiaires, pas seulement sur les breakpoints exacts.", True),
            T("Il est impossible d'avoir plus de deux breakpoints dans une feuille de style CSS.", False),
        ],
    )

    quiz(
        "Les variables CSS (custom properties)",
        "Déclarer et réutiliser des valeurs dynamiques avec --variable et var().",
        [
            S("Comment déclare-t-on une variable CSS (propriété personnalisée) ?",
              ["Avec un nom préfixé par deux tirets, comme --couleur-principale: #333;", "Avec un nom préfixé par un dollar, comme $couleur;", "Avec un nom préfixé par arobase, comme @couleur;", "Avec le mot-clé var seul, comme var couleur;"]),
            S("Quelle fonction permet de récupérer la valeur d'une variable CSS définie avec --nom ?",
              ["var()", "calc()", "attr()", "env()"]),
            S("Sur quel sélecteur déclare-t-on souvent les variables CSS globales d'un site ?",
              [":root", "body", "html *", "head"]),
            M("Quels avantages offrent les variables CSS par rapport aux pré-processeurs comme Sass pour les valeurs réutilisables ?",
              ["Elles peuvent être modifiées dynamiquement via JavaScript ou media queries au moment de l'exécution", "Elles respectent la cascade et peuvent être redéfinies localement dans un sélecteur"], {0, 1}, ["Elles ne fonctionnent que dans les fichiers .scss", "Elles remplacent obligatoirement toutes les unités CSS"]),
            T("La fonction `var()` accepte un second paramètre optionnel utilisé comme valeur de repli si la variable n'est pas définie, par exemple `var(--couleur, blue)`.", True),
            T("Une variable CSS définie dans un sélecteur spécifique peut redéfinir localement une variable globale déclarée sur :root.", True),
        ],
    )

    quiz(
        "Portée et héritage des variables CSS",
        "Comprendre comment les custom properties suivent la cascade et l'héritage.",
        [
            S("Les variables CSS personnalisées suivent-elles les règles d'héritage de la cascade comme les autres propriétés héritées ?",
              ["Oui, une variable définie sur un parent est accessible par ses descendants via var()", "Non, les variables CSS ne sont jamais héritées", "Oui, mais uniquement dans les media queries", "Non, elles doivent être redéfinies sur chaque élément individuellement"]),
            S("Que se passe-t-il si on appelle `var(--inconnue)` alors que la variable `--inconnue` n'a jamais été définie, sans valeur de repli ?",
              ["La déclaration utilisant cette variable est invalide et ignorée", "Le navigateur utilise automatiquement la couleur noire", "Une erreur JavaScript est levée", "La page entière refuse de se charger"]),
            S("Peut-on utiliser une variable CSS à l'intérieur d'une media query pour changer sa valeur selon la taille d'écran ?",
              ["Oui, en redéfinissant la variable dans le bloc de la media query", "Non, les variables CSS sont figées dès leur première déclaration", "Oui, mais uniquement avec JavaScript activé", "Non, cela nécessite obligatoirement Sass"]),
            M("Quelles affirmations sur le comportement des variables CSS sont vraies ?",
              ["Elles peuvent être redéfinies à différents niveaux de la cascade", "Leur valeur calculée dépend du contexte dans lequel var() est utilisé"], {0, 1}, ["Elles sont calculées une seule fois au chargement et ne changent jamais", "Elles ne peuvent contenir que des couleurs"]),
            T("Les variables CSS personnalisées peuvent contenir n'importe quelle valeur CSS valide, pas seulement des couleurs (tailles, polices, etc.).", True),
            T("Une variable CSS définie localement dans une classe spécifique peut surcharger une variable de même nom définie sur :root pour les éléments concernés.", True),
        ],
    )

    quiz(
        "La fonction calc()",
        "Effectuer des calculs dynamiques directement dans les valeurs CSS.",
        [
            S("Quelle fonction CSS permet d'effectuer des calculs combinant différentes unités, comme des pourcentages et des pixels ?",
              ["calc()", "var()", "clamp()", "attr()"]),
            S("Que fait la déclaration `width: calc(100% - 50px);` ?",
              ["Elle définit une largeur égale à 100% du parent moins 50 pixels", "Elle définit une largeur fixe de 50 pixels uniquement", "Elle provoque une erreur car on ne peut pas mélanger % et px", "Elle ignore le pourcentage et applique seulement 50px"]),
            S("Quelle règle de syntaxe est obligatoire autour des opérateurs + et - à l'intérieur de calc() ?",
              ["Ils doivent être entourés d'espaces", "Ils doivent être collés sans espace aux valeurs", "Ils doivent être entre parenthèses additionnelles toujours", "Ils doivent être précédés d'un point-virgule"]),
            M("Quelles opérations mathématiques sont prises en charge par la fonction calc() ?",
              ["Addition", "Soustraction", "Multiplication"], {0, 1, 2}, ["Racine carrée native sans sqrt()", "Exponentiation native sans pow()"]),
            T("La fonction calc() permet de mélanger des unités différentes dans un même calcul, comme vh et px.", True),
            T("La fonction calc() ne peut être utilisée que pour la propriété width et aucune autre propriété CSS.", False),
        ],
    )

    quiz(
        "clamp(), min() et max()",
        "Définir des valeurs fluides et bornées sans recourir à de multiples media queries.",
        [
            S("Que fait la fonction `clamp(1rem, 2vw, 3rem)` ?",
              ["Elle retourne une valeur fluide comprise entre 1rem (minimum) et 3rem (maximum), basée sur 2vw", "Elle retourne toujours exactement 2vw sans limite", "Elle retourne la somme des trois valeurs", "Elle ignore les deux premières valeurs"]),
            S("Quelle fonction CSS retourne la plus petite des valeurs fournies en argument ?",
              ["min()", "max()", "clamp()", "calc()"]),
            S("Quelle fonction CSS retourne la plus grande des valeurs fournies en argument ?",
              ["max()", "min()", "clamp()", "var()"]),
            M("Pour quels cas d'usage les fonctions clamp(), min() et max() sont-elles particulièrement utiles ?",
              ["Définir une taille de police fluide sans multiples media queries", "Empêcher un élément de devenir trop petit ou trop grand"], {0, 1}, ["Charger une police personnalisée", "Définir une transition d'animation"]),
            T("`clamp(min, valeur-préférée, max)` permet de créer une taille de police responsive en une seule ligne, sans media query.", True),
            T("La fonction min() retourne systématiquement la première valeur listée dans ses arguments, peu importe sa taille réelle.", False),
        ],
    )

    quiz(
        "minmax() et les grilles responsives avancées",
        "Approfondir l'usage de minmax() dans des contextes de mise en page flexible.",
        [
            S("Dans quel contexte la fonction `minmax()` est-elle principalement utilisée ?",
              ["Dans les déclarations grid-template-columns ou grid-template-rows", "Dans la propriété color", "Dans la règle @font-face", "Dans la propriété text-align"]),
            S("Que fait `minmax(0, 1fr)` dans une définition de grille, comparé à simplement `1fr` ?",
              ["Elle empêche la colonne de dépasser son contenu en largeur minimale implicite, autorisant un rétrécissement complet jusqu'à 0", "Elle bloque totalement la colonne à 0 pixel visible", "Elle est strictement identique à auto", "Elle empêche tout redimensionnement de la colonne"]),
            S("Peut-on utiliser deux fonctions comme `minmax()` et `repeat()` ensemble dans la même déclaration grid-template-columns ?",
              ["Oui, c'est une combinaison très courante pour des grilles responsives", "Non, ce sont des fonctions mutuellement exclusives", "Oui, mais seulement dans grid-template-rows", "Non, cela génère systématiquement une erreur"]),
            M("Quelles fonctions CSS acceptent des bornes minimales et/ou maximales en argument ?",
              ["minmax()", "clamp()"], {0, 1}, ["var()", "url()"]),
            T("`minmax()` est spécifique au module CSS Grid Layout et ne s'utilise pas dans Flexbox de la même façon.", True),
            T("La fonction minmax() ne peut accepter que deux valeurs fixes en pixels, jamais de mots-clés comme auto ou 0.", False),
        ],
    )

    quiz(
        "Container queries et unités modernes",
        "Une approche plus récente du responsive basée sur la taille du conteneur plutôt que du viewport.",
        [
            S("Quelle règle CSS récente permet d'appliquer des styles selon la taille d'un conteneur parent plutôt que celle du viewport ?",
              ["@container", "@media", "@supports", "@scope"]),
            S("Quelle propriété doit être définie sur un élément pour qu'il devienne une référence pour les container queries ?",
              ["container-type", "display: container", "position: container", "contain-query"]),
            S("Quel est l'avantage principal des container queries par rapport aux media queries classiques ?",
              ["Elles permettent d'adapter un composant selon l'espace réellement disponible, indépendamment de la largeur totale de l'écran", "Elles sont plus rapides à écrire syntaxiquement", "Elles remplacent entièrement Flexbox", "Elles ne fonctionnent que sur mobile"]),
            M("Quelles affirmations sur les container queries sont vraies ?",
              ["Elles nécessitent de déclarer un type de containment sur un ancêtre", "Elles sont particulièrement utiles pour des composants réutilisables dans des contextes variés"], {0, 1}, ["Elles remplacent obligatoirement toutes les media queries existantes", "Elles ne peuvent cibler que la hauteur d'un conteneur"]),
            T("Les container queries permettent à un même composant de s'adapter différemment selon l'espace disponible dans son conteneur, même si la largeur du viewport reste identique.", True),
            T("Les container queries étaient disponibles dès la première version de CSS, avant même les media queries.", False),
        ],
    )
