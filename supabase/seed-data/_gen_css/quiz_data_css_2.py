# -*- coding: utf-8 -*-
"""Quiz 11-20 : Modele de boite (box-sizing, margin, padding, border) + cascade et heritage."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Le modèle de boîte CSS",
        "Les fondations du box model : contenu, padding, bordure et marge.",
        [
            S("Dans le modèle de boîte CSS, quel élément se trouve juste autour du contenu, avant la bordure ?",
              ["Le padding", "La marge (margin)", "La bordure (border)", "L'outline"]),
            S("Quelle propriété définit l'espace extérieur autour d'une boîte, en dehors de sa bordure ?",
              ["margin", "padding", "border", "gap"]),
            S("Quelle propriété définit l'espace intérieur entre le contenu et la bordure d'une boîte ?",
              ["padding", "margin", "border-spacing", "spacing"]),
            M("Quelles propriétés font partie intégrante du modèle de boîte CSS standard ?",
              ["padding", "border"], {0, 1}, ["color", "font-size"]),
            T("Dans le modèle de boîte standard (content-box), la largeur définie par `width` ne comprend pas le padding ni la bordure.", True),
            T("La marge (margin) fait partie de la largeur visible et colorée d'une boîte.", False),
        ],
    )

    quiz(
        "box-sizing : content-box vs border-box",
        "Maîtriser le calcul des dimensions réelles d'un élément selon box-sizing.",
        [
            S("Quelle valeur de `box-sizing` inclut le padding et la bordure dans la largeur totale définie par `width` ?",
              ["border-box", "content-box", "padding-box", "margin-box"]),
            S("Avec `box-sizing: content-box` (valeur par défaut), que représente la propriété `width` ?",
              ["Uniquement la largeur du contenu, sans padding ni bordure", "La largeur totale incluant padding et bordure", "La largeur incluant la marge", "La largeur de l'élément parent"]),
            S("Un élément a `width: 200px`, `padding: 20px` et `border: 5px` avec `box-sizing: border-box`. Quelle est sa largeur totale visible ?",
              ["200px", "250px", "240px", "230px"]),
            M("Quels sont les avantages couramment cités de `box-sizing: border-box` en développement web ?",
              ["Calcul de largeur plus prévisible", "Évite les dépassements inattendus lors de l'ajout de padding"], {0, 1}, ["Réduit automatiquement la taille de la police", "Supprime le besoin de définir une largeur"]),
            T("`box-sizing: border-box` est souvent appliqué globalement via `* { box-sizing: border-box; }` pour simplifier les calculs de mise en page.", True),
            T("La propriété `box-sizing` affecte le calcul de la propriété `margin`.", False),
        ],
    )

    quiz(
        "Marges : fusion et astuces",
        "Comprendre le comportement parfois surprenant des marges verticales.",
        [
            S("Comment appelle-t-on le phénomène où deux marges verticales adjacentes fusionnent en une seule marge égale à la plus grande des deux ?",
              ["Le collapsing des marges (margin collapse)", "L'héritage des marges", "La cascade des marges", "Le débordement de marge"]),
            S("Quelle valeur permet de centrer horizontalement un bloc ayant une largeur définie, via les marges ?",
              ["margin: 0 auto;", "margin: auto 0;", "margin: center;", "align: center;"]),
            S("Quelle est la syntaxe pour définir une marge de 10px en haut, 20px à droite, 10px en bas et 20px à gauche en une seule déclaration ?",
              ["margin: 10px 20px;", "margin: 10px 20px 10px;", "margin: 20px 10px;", "margin: 10px 20px 20px 10px;"]),
            M("Dans quels contextes le collapsing (fusion) des marges verticales peut se produire ?",
              ["Entre deux blocs frères en flux normal", "Entre la marge d'un parent et celle de son premier enfant sans bordure ni padding"], {0, 1}, ["Entre deux éléments flex enfants d'un conteneur flex", "Entre deux colonnes d'une grille CSS"]),
            T("Une marge négative peut être utilisée pour faire chevaucher des éléments.", True),
            T("Le collapsing des marges s'applique également aux marges horizontales (gauche/droite).", False),
        ],
    )

    quiz(
        "Bordures CSS",
        "Styliser le contour des éléments avec les propriétés border.",
        [
            S("Quelle propriété raccourcie permet de définir en une seule fois l'épaisseur, le style et la couleur d'une bordure ?",
              ["border", "outline", "border-style", "frame"]),
            S("Quelle valeur de `border-style` rend une bordure invisible tout en conservant son épaisseur dans le calcul de la boîte ?",
              ["none n'occupe aucun espace, mais hidden conserve l'espace réservé", "dotted", "solid", "double"]),
            S("Quelle propriété permet d'arrondir les coins d'une boîte ?",
              ["border-radius", "border-corner", "corner-radius", "box-radius"]),
            M("Quelles valeurs sont des styles de bordure valides en CSS ?",
              ["solid", "dashed"], {0, 1}, ["wavy-line", "zigzag"]),
            T("`border-radius: 50%` appliqué à un élément carré permet d'obtenir un cercle parfait.", True),
            T("La propriété `outline` modifie la taille de la boîte au même titre que `border`.", False),
        ],
    )

    quiz(
        "Cascade et héritage CSS",
        "Comprendre comment les styles se transmettent et se combinent dans une page.",
        [
            S("Comment appelle-t-on le mécanisme par lequel certaines propriétés CSS se transmettent automatiquement des parents vers leurs enfants ?",
              ["L'héritage (inheritance)", "La cascade", "La spécificité", "Le flux normal"]),
            S("Quelle propriété est héritée par défaut par les éléments enfants ?",
              ["color", "border", "margin", "padding"]),
            S("Quelle valeur CSS force explicitement un élément à hériter la valeur d'une propriété de son parent, même si elle n'est pas héritée par défaut ?",
              ["inherit", "initial", "unset", "revert"]),
            M("Quelles propriétés CSS sont généralement héritées par défaut ?",
              ["font-family", "line-height"], {0, 1}, ["margin", "border"]),
            T("La propriété `border` est héritée par défaut par les éléments enfants.", False),
            T("La cascade CSS détermine quelle règle s'applique en tenant compte de l'origine, de la spécificité et de l'ordre d'apparition.", True),
        ],
    )

    quiz(
        "Le mot-clé !important et ses effets",
        "Comprendre l'impact de !important sur la cascade et la spécificité.",
        [
            S("Quel est l'effet de `!important` ajouté à une déclaration CSS ?",
              ["Cette déclaration prime sur les autres règles normales, quelle que soit leur spécificité", "Elle augmente la taille de police de 10%", "Elle force l'application de la règle uniquement sur mobile", "Elle ignore la règle si une classe est présente"]),
            S("Que se passe-t-il si deux règles utilisent toutes deux `!important` sur la même propriété ?",
              ["La spécificité normale et l'ordre d'apparition redéterminent le gagnant entre elles", "La première règle du fichier l'emporte toujours, peu importe sa position", "Aucune des deux règles n'est appliquée", "Le navigateur affiche une erreur de syntaxe"]),
            S("Pourquoi l'usage excessif de `!important` est-il généralement déconseillé ?",
              ["Il complique la maintenance et le débogage de la cascade", "Il ralentit le chargement de la page de façon significative", "Il est interdit par la spécification CSS3", "Il empêche l'utilisation de media queries"]),
            M("Dans quels cas l'utilisation ponctuelle de `!important` peut être justifiée ?",
              ["Surcharger un style généré dynamiquement par un script tiers", "Forcer un style critique d'accessibilité difficile à cibler autrement"], {0, 1}, ["Remplacer systématiquement toute organisation de la spécificité", "Accélérer le rendu CSS du navigateur"]),
            T("`!important` s'écrit après la valeur de la propriété, par exemple `color: red !important;`.", True),
            T("`!important` modifie la valeur calculée de la spécificité affichée par les outils de développement comme un point supplémentaire dans le sélecteur.", False),
        ],
    )

    quiz(
        "Calcul de la spécificité en pratique",
        "Comparer la force de différents sélecteurs combinés dans des cas concrets.",
        [
            S("Entre `.classe` et `#identifiant`, quel sélecteur l'emporte en cas de conflit ?",
              ["#identifiant", ".classe", "Les deux ont la même force", "Cela dépend de l'ordre alphabétique"]),
            S("Entre `div.actif` et `.actif`, quel sélecteur a la spécificité la plus forte ?",
              ["div.actif", ".actif", "Les deux sont strictement identiques", "Aucun des deux n'est valide"]),
            S("Combien de sélecteurs de classe sont présents dans `.card.featured.highlighted` ?",
              ["3", "1", "2", "0"]),
            M("Lesquelles de ces affirmations sur la spécificité sont vraies ?",
              ["Un id l'emporte sur n'importe quel nombre de classes seules", "Plusieurs classes combinées augmentent la spécificité totale"], {0, 1}, ["Un sélecteur d'élément l'emporte toujours sur une classe", "L'ordre alphabétique des sélecteurs influence la spécificité"]),
            T("Le sélecteur `body #main .content p` a une spécificité plus élevée que `.content p` seul.", True),
            T("Ajouter un pseudo-élément comme `::before` à un sélecteur n'a aucun impact sur sa spécificité.", False),
        ],
    )

    quiz(
        "Unités relatives à la taille de police",
        "Différencier em, rem et leurs comportements en cascade.",
        [
            S("À quoi est relative l'unité `rem` ?",
              ["À la taille de police de l'élément racine (html)", "À la taille de police de l'élément parent direct", "À la largeur de la fenêtre", "À la taille de la police par défaut du navigateur uniquement sur mobile"]),
            S("À quoi est relative l'unité `em` lorsqu'elle définit une taille de police ?",
              ["À la taille de police de l'élément parent", "À la taille de police de l'élément racine", "À la largeur du conteneur", "À la hauteur de la fenêtre"]),
            S("Pourquoi l'unité `rem` est-elle souvent préférée à `em` pour éviter des effets de cascade indésirables ?",
              ["Parce qu'elle ne dépend pas de la taille de police des parents imbriqués", "Parce qu'elle est plus rapide à calculer pour le navigateur", "Parce qu'elle ne peut pas être utilisée avec des media queries", "Parce qu'elle est obligatoire en CSS3"]),
            M("Quelles unités sont basées sur la taille de la police (et non sur une dimension fixe ou la fenêtre) ?",
              ["em", "rem"], {0, 1}, ["vh", "px"]),
            T("Si plusieurs éléments imbriqués utilisent `em` pour `font-size`, l'effet peut se cumuler en cascade et produire une taille de texte inattendue.", True),
            T("L'unité `rem` est affectée par la taille de police définie sur l'élément parent direct.", False),
        ],
    )

    quiz(
        "Unités de viewport et pourcentages",
        "Adapter les dimensions à la fenêtre du navigateur avec vh, vw et %.",
        [
            S("Que représente l'unité `vh` en CSS ?",
              ["1% de la hauteur de la fenêtre d'affichage (viewport)", "1% de la largeur de la fenêtre d'affichage", "1 pixel relatif à la résolution de l'écran", "1% de la hauteur de l'élément parent"]),
            S("Que représente l'unité `vw` en CSS ?",
              ["1% de la largeur de la fenêtre d'affichage (viewport)", "1% de la hauteur de la fenêtre d'affichage", "1% de la largeur de l'élément parent", "Une unité fixe de 1 pixel"]),
            S("Un élément avec `width: 50%` à l'intérieur d'un conteneur de 800px de large aura quelle largeur ?",
              ["400px", "50px", "800px", "Indéterminée sans connaître la hauteur"]),
            M("Quelles unités sont relatives à la taille du viewport (fenêtre d'affichage) ?",
              ["vh", "vw"], {0, 1}, ["em", "ch"]),
            T("`height: 100vh` fait en sorte qu'un élément occupe toute la hauteur visible de la fenêtre du navigateur.", True),
            T("L'unité `%` pour la largeur d'un élément est toujours relative à la largeur de l'écran physique, indépendamment du parent.", False),
        ],
    )

    quiz(
        "L'unité ch et les caractères",
        "Une unité de mesure basée sur la largeur des caractères typographiques.",
        [
            S("Sur quoi est basée l'unité `ch` en CSS ?",
              ["La largeur du caractère \"0\" dans la police utilisée", "La hauteur de ligne de l'élément", "Le nombre total de caractères affichés à l'écran", "La largeur moyenne de tous les caractères Unicode"]),
            S("Dans quel cas l'unité `ch` est-elle particulièrement utile ?",
              ["Pour limiter la largeur d'un bloc de texte à un nombre de caractères approximatif", "Pour définir la hauteur d'une image", "Pour centrer un élément verticalement", "Pour définir un dégradé de couleur"]),
            S("Que fait la déclaration `max-width: 60ch;` sur un paragraphe ?",
              ["Elle limite la largeur du paragraphe à environ 60 caractères pour améliorer la lisibilité", "Elle limite le paragraphe à exactement 60 mots", "Elle force le texte à occuper 60% de la largeur de l'écran", "Elle n'a aucun effet sur la mise en page"]),
            M("Quelles unités CSS sont basées sur des caractéristiques typographiques de la police active ?",
              ["em", "ch"], {0, 1}, ["vh", "vw"]),
            T("L'unité `ch` est couramment recommandée pour optimiser la lisibilité des longues colonnes de texte.", True),
            T("L'unité `ch` est toujours strictement égale à la largeur de tous les caractères, y compris les majuscules larges.", False),
        ],
    )
