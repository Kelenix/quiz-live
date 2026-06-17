# -*- coding: utf-8 -*-
"""Quiz 51-60 : Couleurs, typographie."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Les notations de couleur hexadécimale",
        "Comprendre le format hexadécimal pour exprimer des couleurs en CSS.",
        [
            S("Combien de caractères hexadécimaux compose un code couleur complet du type #RRGGBB ?",
              ["6", "3", "8", "4"]),
            S("Que représente `#000000` en CSS ?",
              ["Le noir", "Le blanc", "Le rouge", "Le transparent"]),
            S("Que représente `#ffffff` en CSS ?",
              ["Le blanc", "Le noir", "Le bleu", "Le gris moyen"]),
            M("Quelles affirmations sur la notation hexadécimale des couleurs sont vraies ?",
              ["Une notation courte à 3 caractères existe (ex: #fff)", "Un format à 8 caractères (#RRGGBBAA) permet d'inclure la transparence"], {0, 1}, ["Elle ne peut jamais représenter le blanc", "Elle est limitée à 16 couleurs au total"]),
            T("`#f00` est une notation raccourcie valide équivalente à `#ff0000`.", True),
            T("La notation hexadécimale des couleurs est sensible à la casse et `#FFFFFF` est différent de `#ffffff`.", False),
        ],
    )

    quiz(
        "rgb(), rgba() et la transparence",
        "Exprimer des couleurs avec des composantes rouge/vert/bleu et un canal alpha.",
        [
            S("Que signifient les trois premiers paramètres de la fonction `rgb()` ?",
              ["Les intensités de rouge, vert et bleu", "La teinte, la saturation et la luminosité", "La largeur, la hauteur et la profondeur", "Le contraste, la luminosité et la saturation"]),
            S("Quelle fonction CSS permet de définir une couleur avec un canal de transparence (alpha) en plus du rouge/vert/bleu ?",
              ["rgba()", "hsl()", "rgb-alpha()", "color-mix()"]),
            S("Dans `rgba(255, 0, 0, 0.5)`, que représente la valeur `0.5` ?",
              ["Une opacité de 50%", "Une teinte rouge à 50%", "Une luminosité de 50%", "Un demi-pixel de décalage"]),
            M("Quelles valeurs sont valides pour le canal alpha dans rgba() ?",
              ["0", "1", "0.5"], {0, 1, 2}, ["256", "-1"]),
            T("Dans la syntaxe CSS moderne, `rgb()` peut désormais accepter un quatrième paramètre de transparence séparé par une barre oblique, rendant rgba() optionnel.", True),
            T("La fonction `rgb()` accepte uniquement des valeurs en pourcentage et jamais des entiers de 0 à 255.", False),
        ],
    )

    quiz(
        "hsl() : teinte, saturation, luminosité",
        "Une approche plus intuitive de la couleur basée sur le cercle chromatique.",
        [
            S("Que représente le premier paramètre de la fonction `hsl()` ?",
              ["La teinte (hue), exprimée en degrés sur le cercle chromatique", "La luminosité en pourcentage", "La saturation en pourcentage", "Le canal alpha"]),
            S("Dans `hsl(0, 100%, 50%)`, quelle couleur obtient-on généralement ?",
              ["Un rouge vif", "Un vert vif", "Un bleu vif", "Un gris neutre"]),
            S("Que se passe-t-il si on règle la saturation à 0% dans hsl(), quelle que soit la teinte choisie ?",
              ["On obtient une nuance de gris", "On obtient toujours du blanc pur", "On obtient toujours du noir pur", "La couleur devient transparente"]),
            M("Quels avantages présente `hsl()` par rapport à `rgb()` pour ajuster des couleurs ?",
              ["Il est plus intuitif pour éclaircir ou foncer une couleur en changeant la luminosité", "Il permet de faire varier la teinte facilement en modifiant un seul angle"], {0, 1}, ["Il est le seul format accepté par les navigateurs", "Il ne permet pas d'exprimer la transparence avec hsla()"]),
            T("`hsla()` permet d'ajouter un canal de transparence à la notation hsl(), de façon similaire à rgba().", True),
            T("Dans hsl(), une luminosité de 100% donne toujours du blanc, quelle que soit la teinte choisie.", True),
        ],
    )

    quiz(
        "Mots-clés de couleur et opacity",
        "Les noms de couleurs prédéfinis et la propriété d'opacité globale.",
        [
            S("Quel mot-clé CSS représente une couleur totalement transparente ?",
              ["transparent", "none", "hidden", "invisible"]),
            S("Quelle propriété CSS rend un élément entier (avec son contenu) partiellement transparent ?",
              ["opacity", "color", "visibility", "filter-alpha"]),
            S("Quelle est la principale différence entre `opacity: 0.5` et une couleur de fond avec un canal alpha à 0.5 ?",
              ["opacity affecte tout l'élément y compris son contenu, tandis que l'alpha de la couleur n'affecte que cette couleur précise", "Ce sont des synonymes stricts sans aucune différence", "opacity ne peut s'appliquer qu'aux images", "L'alpha de couleur affecte toujours tout l'élément comme opacity"]),
            M("Quelles affirmations sur `opacity` sont vraies ?",
              ["Une valeur de 0 rend l'élément totalement invisible mais toujours présent dans la mise en page", "Une valeur de 1 correspond à une opacité totale (élément pleinement visible)"], {0, 1}, ["opacity supprime l'élément du DOM", "opacity ne peut prendre que des valeurs entières comme 0 ou 1"]),
            T("`opacity: 0` rend un élément invisible mais il continue d'occuper de l'espace et de capter les clics, sauf gestion spécifique avec pointer-events.", True),
            T("Le mot-clé de couleur `red` est strictement équivalent à `#ff0000` dans la plupart des cas.", True),
        ],
    )

    quiz(
        "Les fonctions de police : font-family",
        "Définir des familles de polices avec des solutions de repli (fallback).",
        [
            S("Pourquoi est-il recommandé de fournir plusieurs noms dans la propriété `font-family` ?",
              ["Pour proposer des polices de repli si la première n'est pas disponible sur le système de l'utilisateur", "Pour appliquer toutes les polices en même temps sur le même texte", "Pour augmenter automatiquement la taille du texte", "Parce que CSS exige toujours au moins trois polices"]),
            S("Que représente une famille générique comme `sans-serif` à la fin d'une liste font-family ?",
              ["Une catégorie de police de secours fournie par le système si aucune police spécifique n'est disponible", "Le nom exact d'une police installée sur tous les systèmes", "Un raccourci pour appliquer une police en gras", "Une erreur de syntaxe CSS"]),
            S("Pourquoi entourer de guillemets un nom de police contenant des espaces, comme \"Times New Roman\" ?",
              ["Pour que le navigateur interprète correctement le nom complet comme une seule valeur", "Parce que cela accélère le chargement de la police", "Parce que c'est obligatoire pour toutes les polices, même sans espace", "Pour activer automatiquement le gras"]),
            M("Quelles familles génériques sont reconnues par CSS comme polices de repli ?",
              ["serif", "sans-serif", "monospace"], {0, 1, 2}, ["bold-family", "italic-family"]),
            T("La règle `@font-face` permet de charger une police personnalisée hébergée sur un serveur web.", True),
            T("Il est impossible de définir plusieurs polices de secours séparées par des virgules dans `font-family`.", False),
        ],
    )

    quiz(
        "font-weight, font-style et line-height",
        "Ajuster l'épaisseur, le style et l'espacement vertical du texte.",
        [
            S("Quelle propriété contrôle l'épaisseur (graisse) du texte, comme le gras ?",
              ["font-weight", "font-style", "line-height", "text-decoration"]),
            S("Quelle valeur numérique de `font-weight` correspond généralement au texte normal (non gras) ?",
              ["400", "700", "900", "100"]),
            S("Quelle propriété contrôle l'espacement vertical entre les lignes d'un paragraphe ?",
              ["line-height", "letter-spacing", "word-spacing", "vertical-align"]),
            M("Quelles valeurs sont valides pour la propriété `font-style` ?",
              ["italic", "normal"], {0, 1}, ["bold", "underline"]),
            T("Une valeur de `line-height` sans unité (par exemple 1.5) est généralement recommandée car elle se calcule de façon relative à la taille de police de l'élément.", True),
            T("`font-weight: bold` est strictement identique à `font-weight: 400`.", False),
        ],
    )

    quiz(
        "text-align, text-decoration et transformation du texte",
        "Aligner, décorer et transformer la casse du texte.",
        [
            S("Quelle propriété permet de centrer horizontalement un texte dans son conteneur ?",
              ["text-align", "align-items", "justify-content", "vertical-align"]),
            S("Quelle propriété permet de souligner un texte ?",
              ["text-decoration", "text-align", "font-style", "text-transform"]),
            S("Quelle propriété transforme automatiquement un texte en majuscules sans modifier le contenu HTML d'origine ?",
              ["text-transform: uppercase;", "font-weight: bold;", "text-align: justify;", "font-variant: caps;"]),
            M("Quelles valeurs sont valides pour la propriété `text-align` ?",
              ["center", "justify"], {0, 1}, ["uppercase", "underline"]),
            T("`text-decoration: none;` est souvent utilisée pour retirer le soulignement par défaut des liens.", True),
            T("`text-transform: uppercase` modifie réellement le texte stocké dans le code HTML en majuscules permanentes.", False),
        ],
    )

    quiz(
        "letter-spacing et word-spacing",
        "Ajuster finement l'espacement entre les caractères et les mots.",
        [
            S("Quelle propriété contrôle l'espace entre les caractères individuels d'un texte ?",
              ["letter-spacing", "word-spacing", "line-height", "text-indent"]),
            S("Quelle propriété contrôle l'espace entre les mots d'un texte ?",
              ["word-spacing", "letter-spacing", "line-height", "white-space"]),
            S("Une valeur négative pour `letter-spacing` produit quel effet ?",
              ["Elle rapproche les lettres les unes des autres", "Elle agrandit la taille de la police", "Elle provoque une erreur de syntaxe", "Elle est silencieusement ignorée par tous les navigateurs"]),
            M("Quelles propriétés permettent d'ajuster l'espacement typographique fin d'un texte ?",
              ["letter-spacing", "word-spacing"], {0, 1}, ["color", "font-family"]),
            T("`letter-spacing` accepte des valeurs en unités comme px ou em.", True),
            T("`word-spacing` modifie l'espacement entre les lettres à l'intérieur d'un même mot.", False),
        ],
    )

    quiz(
        "@font-face et le chargement de polices web",
        "Intégrer des polices personnalisées hébergées avec la règle @font-face.",
        [
            S("À quoi sert la règle `@font-face` en CSS ?",
              ["À définir une police personnalisée à charger depuis un fichier ou une URL", "À appliquer une animation à une police", "À définir une feuille de style pour l'impression", "À créer une variable CSS"]),
            S("Quelle propriété à l'intérieur de `@font-face` indique l'emplacement du fichier de police ?",
              ["src", "font-family", "href", "url-font"]),
            S("Quelle propriété de `@font-face` permet de donner un nom utilisable ensuite dans `font-family` ?",
              ["font-family", "src", "font-name", "font-display"]),
            M("Quels formats de fichiers de police sont couramment utilisés avec @font-face sur le web moderne ?",
              ["woff2", "woff"], {0, 1}, ["jpeg", "mp4"]),
            T("La propriété `font-display` dans @font-face permet de contrôler le comportement d'affichage du texte pendant le chargement de la police personnalisée.", True),
            T("Une police chargée via @font-face ne peut jamais être utilisée pour le texte des titres, uniquement pour le corps de texte.", False),
        ],
    )

    quiz(
        "Couleurs et accessibilité du contraste",
        "Choisir des couleurs lisibles en tenant compte du contraste texte/fond.",
        [
            S("Pourquoi le contraste entre la couleur du texte et celle du fond est-il important en CSS ?",
              ["Pour garantir la lisibilité du contenu, notamment pour les personnes malvoyantes", "Pour réduire la taille du fichier CSS", "Pour accélérer le chargement de la page", "Cela n'a aucun impact réel sur l'utilisateur"]),
            S("Quel type de combinaison de couleurs est généralement déconseillé pour la lisibilité d'un texte ?",
              ["Un texte de couleur claire sur un fond de couleur également claire", "Un texte noir sur un fond blanc", "Un texte blanc sur un fond très sombre", "Un texte de couleur foncée sur un fond clair"]),
            S("Quelle propriété CSS seule ne suffit jamais à garantir l'accessibilité, mais demande aussi une vérification de contraste ?",
              ["color associée à background-color", "display", "position", "z-index"]),
            M("Quels facteurs influencent la perception du contraste d'un texte par un utilisateur ?",
              ["La luminosité respective des couleurs de texte et de fond", "La taille de la police utilisée"], {0, 1}, ["Le nombre de balises HTML utilisées", "Le nom de la classe CSS choisie"]),
            T("Les directives d'accessibilité (comme les WCAG) recommandent un ratio de contraste minimal entre le texte et son arrière-plan.", True),
            T("Le contraste des couleurs n'a aucune incidence sur l'accessibilité d'un site pour les personnes malvoyantes.", False),
        ],
    )
