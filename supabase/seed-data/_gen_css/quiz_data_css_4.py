# -*- coding: utf-8 -*-
"""Quiz 31-40 : Flexbox."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Introduction à Flexbox",
        "Les bases pour créer un conteneur flexible et ses items.",
        [
            S("Quelle propriété transforme un élément en conteneur flexible ?",
              ["display: flex", "position: flex", "flex: container", "layout: flex"]),
            S("Comment appelle-t-on les enfants directs d'un conteneur flex ?",
              ["Les flex items", "Les flex parents", "Les flex blocks", "Les flex rows"]),
            S("Quel axe est l'axe principal (main axis) par défaut dans un conteneur flex ?",
              ["L'axe horizontal (row)", "L'axe vertical (column)", "L'axe diagonal", "Il n'y a pas d'axe par défaut"]),
            M("Quelles propriétés s'appliquent au conteneur flex lui-même (et non à ses items) ?",
              ["flex-direction", "justify-content"], {0, 1}, ["flex-grow", "order"]),
            T("Flexbox est conçu principalement pour des mises en page unidimensionnelles (une ligne ou une colonne à la fois).", True),
            T("Pour activer Flexbox, il faut obligatoirement utiliser `display: inline-flex` et jamais `display: flex`.", False),
        ],
    )

    quiz(
        "flex-direction et flex-wrap",
        "Contrôler l'orientation et le retour à la ligne des éléments flexibles.",
        [
            S("Quelle valeur de `flex-direction` aligne les items en colonne, de haut en bas ?",
              ["column", "row", "row-reverse", "wrap"]),
            S("Quelle valeur de `flex-direction` inverse l'ordre visuel des items sur une ligne horizontale ?",
              ["row-reverse", "column", "row", "column-reverse"]),
            S("Quelle propriété permet aux flex items de passer à la ligne suivante quand ils ne tiennent plus sur une seule ligne ?",
              ["flex-wrap", "flex-direction", "overflow-wrap", "flex-flow"]),
            M("Quelles valeurs sont valides pour la propriété `flex-wrap` ?",
              ["wrap", "nowrap"], {0, 1}, ["reverse", "auto"]),
            T("La propriété raccourcie `flex-flow` permet de définir en une seule déclaration `flex-direction` et `flex-wrap`.", True),
            T("Par défaut, sans précision de `flex-wrap`, les flex items ne passent jamais à la ligne suivante.", True),
        ],
    )

    quiz(
        "justify-content : alignement sur l'axe principal",
        "Distribuer l'espace disponible entre les flex items le long de l'axe principal.",
        [
            S("Quelle valeur de `justify-content` centre les items le long de l'axe principal ?",
              ["center", "flex-start", "stretch", "baseline"]),
            S("Quelle valeur de `justify-content` répartit un espace égal entre les items, sans espace avant le premier ni après le dernier ?",
              ["space-between", "space-around", "space-evenly", "center"]),
            S("Quelle valeur de `justify-content` ajoute un espace égal autour de chaque item, y compris avant le premier et après le dernier ?",
              ["space-evenly", "space-between", "flex-end", "stretch"]),
            M("Quelles valeurs de `justify-content` permettent de répartir de l'espace vide entre les éléments ?",
              ["space-between", "space-around"], {0, 1}, ["flex-start", "stretch"]),
            T("`justify-content` agit le long de l'axe principal du conteneur flex, qui dépend de `flex-direction`.", True),
            T("`justify-content: flex-end` aligne les items au début de l'axe principal.", False),
        ],
    )

    quiz(
        "align-items et align-self : axe secondaire",
        "Aligner les flex items perpendiculairement à l'axe principal.",
        [
            S("Quelle propriété aligne les flex items le long de l'axe secondaire (transversal) du conteneur ?",
              ["align-items", "justify-content", "flex-wrap", "order"]),
            S("Quelle valeur de `align-items` étire les items pour qu'ils remplissent toute la hauteur disponible du conteneur (valeur par défaut) ?",
              ["stretch", "center", "flex-start", "baseline"]),
            S("Quelle propriété permet de modifier l'alignement transversal d'un seul flex item, indépendamment des autres ?",
              ["align-self", "align-items", "justify-self", "place-self"]),
            M("Quelles valeurs sont valides à la fois pour `align-items` et `align-self` ?",
              ["center", "flex-start"], {0, 1}, ["space-between", "space-around"]),
            T("`align-self` permet à un flex item individuel de surcharger la valeur d'`align-items` définie sur le conteneur parent.", True),
            T("`align-items: baseline` aligne les items selon leur ligne de base typographique.", True),
        ],
    )

    quiz(
        "flex-grow, flex-shrink et flex-basis",
        "Contrôler la façon dont les flex items grandissent, rétrécissent et leur taille de base.",
        [
            S("Quelle propriété détermine la capacité d'un flex item à grandir pour occuper l'espace disponible restant ?",
              ["flex-grow", "flex-shrink", "flex-basis", "flex-order"]),
            S("Quelle propriété détermine la taille initiale d'un flex item avant toute distribution d'espace supplémentaire ?",
              ["flex-basis", "flex-grow", "flex-shrink", "width-base"]),
            S("Si deux flex items ont `flex-grow: 1` et `flex-grow: 2`, comment l'espace restant est-il réparti entre eux ?",
              ["Le second reçoit deux fois plus d'espace supplémentaire que le premier", "Les deux reçoivent exactement la même quantité d'espace", "Le premier reçoit tout l'espace restant", "Aucun espace n'est distribué sans flex-basis défini"]),
            M("Que contrôle la propriété raccourcie `flex` lorsqu'elle est écrite avec trois valeurs (ex: `flex: 1 1 200px`) ?",
              ["flex-grow", "flex-shrink"], {0, 1}, ["flex-direction", "order"]),
            T("`flex-shrink: 0` empêche un flex item de rétrécir, même si l'espace du conteneur est insuffisant pour tous les items.", True),
            T("`flex-grow: 0` (valeur par défaut) signifie que l'item ne grandira pas pour occuper l'espace libre supplémentaire.", True),
        ],
    )

    quiz(
        "La propriété order et le réagencement visuel",
        "Modifier l'ordre d'affichage des flex items sans changer le HTML.",
        [
            S("Quelle propriété permet de modifier l'ordre d'affichage visuel d'un flex item sans changer l'ordre dans le HTML ?",
              ["order", "flex-direction", "z-index", "position"]),
            S("Quelle est la valeur par défaut de la propriété `order` pour tous les flex items ?",
              ["0", "1", "auto", "-1"]),
            S("Si un item a `order: -1` et que tous les autres ont la valeur par défaut, où apparaîtra-t-il visuellement ?",
              ["Avant tous les autres items", "Après tous les autres items", "Au centre du conteneur", "Cela n'a aucun effet visuel"]),
            M("Quelles affirmations sur la propriété `order` sont vraies ?",
              ["Elle ne modifie pas l'ordre réel des éléments dans le DOM", "Elle peut accepter des valeurs négatives"], {0, 1}, ["Elle nécessite obligatoirement Grid et non Flexbox", "Elle modifie la spécificité CSS des sélecteurs"]),
            T("Modifier `order` peut avoir un impact sur l'ordre de tabulation perçu par les technologies d'assistance, ce qui est un point d'attention en accessibilité.", True),
            T("La propriété `order` modifie physiquement la position des balises dans le code source HTML.", False),
        ],
    )

    quiz(
        "align-content et la gestion du multi-lignes",
        "Distribuer l'espace entre plusieurs lignes flex lorsque flex-wrap est actif.",
        [
            S("Dans quel cas la propriété `align-content` a-t-elle un effet visible sur un conteneur flex ?",
              ["Lorsqu'il y a plusieurs lignes flex (flex-wrap actif) et de l'espace vertical disponible", "Toujours, quel que soit le nombre de lignes", "Uniquement en display: grid", "Uniquement si flex-direction vaut row-reverse"]),
            S("Quelle est la différence principale entre `align-items` et `align-content` dans un conteneur flex ?",
              ["align-items aligne les items dans une ligne, align-content distribue l'espace entre les lignes", "Ce sont des synonymes stricts", "align-content s'applique uniquement aux images", "align-items ne fonctionne qu'en mode column"]),
            S("Quelle valeur d'`align-content` rapproche toutes les lignes flex au début de l'axe secondaire ?",
              ["flex-start", "space-between", "stretch", "space-evenly"]),
            M("Quelles valeurs sont communes aux propriétés `align-content` et `justify-content` ?",
              ["center", "space-between"], {0, 1}, ["baseline", "stretch"]),
            T("`align-content` n'a aucun effet si le conteneur flex ne comporte qu'une seule ligne d'items.", True),
            T("`align-content` et `align-items` contrôlent strictement la même chose dans tous les cas.", False),
        ],
    )

    quiz(
        "Centrage parfait avec Flexbox",
        "La technique classique pour centrer un élément horizontalement et verticalement.",
        [
            S("Quelle combinaison de propriétés permet de centrer parfaitement un enfant flex horizontalement et verticalement ?",
              ["justify-content: center; et align-items: center;", "margin: auto; uniquement", "text-align: center; et vertical-align: middle;", "position: absolute; uniquement"]),
            S("Pourquoi Flexbox est-il souvent cité comme une solution simple pour le centrage, comparé aux anciennes techniques ?",
              ["Il évite les astuces complexes avec position absolute et transform", "Il fonctionne uniquement sur les images", "Il remplace complètement les media queries", "Il nécessite JavaScript pour s'activer"]),
            S("Que fait `margin: auto` sur un flex item le long de l'axe principal lorsqu'il reste de l'espace disponible ?",
              ["Il absorbe l'espace disponible pour centrer ou repousser l'item", "Il n'a aucun effet en contexte flex", "Il supprime le padding de l'item", "Il force l'item à occuper toute la largeur"]),
            M("Quelles propriétés combinées permettent un centrage flexible classique ?",
              ["justify-content", "align-items"], {0, 1}, ["text-decoration", "list-style"]),
            T("Le centrage via Flexbox fonctionne aussi bien pour du texte que pour des images ou des boîtes complexes.", True),
            T("Pour centrer verticalement avec Flexbox, le conteneur doit obligatoirement avoir `flex-direction: column`.", False),
        ],
    )

    quiz(
        "flex-basis et calcul de la taille minimale",
        "Approfondir le comportement de flex-basis et de min-width/min-height implicite.",
        [
            S("Que se passe-t-il par défaut si `flex-basis` est défini sur `auto` (valeur par défaut) ?",
              ["La taille de base de l'item est déterminée par sa propriété width/height ou son contenu", "L'item occupe toujours toute la largeur disponible", "L'item est totalement ignoré dans le calcul de flex", "flex-basis: auto équivaut toujours à 0"]),
            S("Quelle propriété raccourcie regroupe flex-grow, flex-shrink et flex-basis ?",
              ["flex", "flex-flow", "flex-set", "flex-all"]),
            S("Que signifie la valeur raccourcie `flex: 1` appliquée à un flex item ?",
              ["Équivaut généralement à flex-grow: 1; flex-shrink: 1; flex-basis: 0%;", "Cela fixe une largeur exacte de 1px", "Cela désactive totalement la flexibilité de l'item", "Cela équivaut à display: block"]),
            M("Quelles affirmations sur `min-width` par défaut des flex items sont vraies ?",
              ["Les flex items ont une valeur implicite de min-width: auto qui peut empêcher leur rétrécissement total", "Cette valeur implicite peut nécessiter min-width: 0 pour permettre un rétrécissement complet"], {0, 1}, ["min-width est toujours 0 par défaut sur un flex item", "flex-shrink ignore totalement min-width"]),
            T("Définir `flex-basis: 0` combiné à flex-grow permet une distribution proportionnelle stricte de l'espace, indépendamment du contenu initial.", True),
            T("`flex-basis` ne peut accepter que des valeurs en pixels, jamais de pourcentages.", False),
        ],
    )
