# -*- coding: utf-8 -*-
"""Quiz 81-90 : Arrieres-plans, ombres, border-radius, filtres/blend, @supports, architecture BEM."""

def build(quiz, S, Sx, M, T):

    quiz(
        "background-image et le positionnement de fond",
        "Insérer et positionner des images d'arrière-plan en CSS.",
        [
            S("Quelle propriété permet de définir une image en arrière-plan d'un élément ?",
              ["background-image", "background-color", "src", "content"]),
            S("Quelle propriété contrôle la position d'une image de fond à l'intérieur de sa boîte ?",
              ["background-position", "background-repeat", "background-size", "background-attachment"]),
            S("Quelle valeur de `background-position` centre une image de fond horizontalement et verticalement ?",
              ["center center (ou simplement center)", "top left", "bottom right", "0 0"]),
            M("Quelles propriétés font partie de la déclaration raccourcie `background` ?",
              ["background-image", "background-position"], {0, 1}, ["text-align", "font-size"]),
            T("On peut superposer plusieurs images de fond sur un même élément en les séparant par des virgules dans background-image.", True),
            T("`background-image` peut accepter une URL d'image ou un dégradé généré par CSS comme linear-gradient().", True),
        ],
    )

    quiz(
        "background-size, background-repeat et background-attachment",
        "Contrôler la taille, la répétition et le défilement des images de fond.",
        [
            S("Quelle valeur de `background-size` agrandit l'image de fond pour couvrir entièrement la boîte, même en la rognant si nécessaire ?",
              ["cover", "contain", "auto", "100px"]),
            S("Quelle valeur de `background-size` redimensionne l'image pour qu'elle soit entièrement visible sans être rognée, même si cela laisse des espaces vides ?",
              ["contain", "cover", "stretch", "fill"]),
            S("Quelle valeur de `background-repeat` empêche la répétition d'une image de fond ?",
              ["no-repeat", "repeat-x", "repeat-y", "space"]),
            M("Quelles valeurs sont valides pour la propriété `background-repeat` ?",
              ["repeat-x", "repeat-y", "no-repeat"], {0, 1, 2}, ["cover", "contain"]),
            T("`background-attachment: fixed` fait en sorte que l'image de fond reste fixe par rapport à la fenêtre même lors du défilement du contenu.", True),
            T("`background-size: cover` garantit toujours que l'intégralité de l'image reste visible sans aucun rognage.", False),
        ],
    )

    quiz(
        "Les dégradés CSS (gradients)",
        "Créer des transitions de couleurs fluides sans image avec linear-gradient et radial-gradient.",
        [
            S("Quelle fonction CSS crée un dégradé de couleurs en ligne droite, selon un angle donné ?",
              ["linear-gradient()", "radial-gradient()", "conic-gradient()", "color-gradient()"]),
            S("Quelle fonction CSS crée un dégradé de couleurs partant d'un point central et s'étendant en cercle ou en ellipse ?",
              ["radial-gradient()", "linear-gradient()", "conic-gradient()", "circle-gradient()"]),
            S("Dans quelle propriété utilise-t-on généralement les fonctions de dégradé comme linear-gradient() ?",
              ["background-image", "color", "border-color", "text-decoration-color"]),
            M("Quelles fonctions CSS permettent de générer un dégradé de couleurs ?",
              ["linear-gradient()", "radial-gradient()"], {0, 1}, ["box-shadow()", "filter-gradient()"]),
            T("On peut définir l'angle d'un dégradé linéaire, par exemple `linear-gradient(45deg, red, blue)`.", True),
            T("Un dégradé CSS généré par linear-gradient() nécessite obligatoirement une image externe pour fonctionner.", False),
        ],
    )

    quiz(
        "box-shadow : ombres portées sur les boîtes",
        "Ajouter de la profondeur visuelle à un élément avec des ombres.",
        [
            S("Quelle propriété permet d'ajouter une ombre portée à une boîte (élément) ?",
              ["box-shadow", "text-shadow", "filter-shadow", "outline-shadow"]),
            S("Dans `box-shadow: 2px 4px 10px rgba(0,0,0,0.3);`, que représentent généralement les deux premières valeurs ?",
              ["Le décalage horizontal puis vertical de l'ombre", "Le flou puis l'étalement de l'ombre", "La couleur puis l'opacité", "La largeur puis la hauteur de l'élément"]),
            S("Quel mot-clé optionnel dans box-shadow permet de créer une ombre intérieure plutôt qu'extérieure ?",
              ["inset", "inner", "internal", "reverse"]),
            M("Quelles informations peuvent être définies dans une déclaration box-shadow ?",
              ["Le rayon de flou", "La couleur de l'ombre"], {0, 1}, ["La famille de police", "L'orientation du texte"]),
            T("On peut empiler plusieurs ombres sur un même élément en les séparant par des virgules dans box-shadow.", True),
            T("box-shadow ne peut produire que des ombres noires, sans possibilité de changer leur couleur.", False),
        ],
    )

    quiz(
        "text-shadow et border-radius",
        "Ombrer du texte et arrondir les coins des éléments.",
        [
            S("Quelle propriété permet d'ajouter une ombre portée directement sur du texte ?",
              ["text-shadow", "box-shadow", "font-shadow", "outline"]),
            S("Quelle propriété permet d'arrondir les coins d'une boîte rectangulaire ?",
              ["border-radius", "corner-round", "box-corner", "border-curve"]),
            S("Que produit la déclaration `border-radius: 50%;` sur un élément parfaitement carré (largeur égale à la hauteur) ?",
              ["Un cercle parfait", "Un rectangle aux coins légèrement arrondis", "Aucun effet visuel", "Une forme en étoile"]),
            M("Quelles valeurs syntaxiques sont valides pour border-radius selon le nombre de coins à personnaliser ?",
              ["Une seule valeur pour les quatre coins", "Quatre valeurs pour personnaliser chaque coin séparément"], {0, 1}, ["Une valeur en négatif", "Un mot-clé inset obligatoire"]),
            T("border-radius peut accepter des valeurs différentes pour chacun des quatre coins d'une boîte, par exemple `border-radius: 10px 0 10px 0;`.", True),
            T("text-shadow utilise une syntaxe de paramètres similaire à box-shadow, avec décalages, flou et couleur.", True),
        ],
    )

    quiz(
        "Les filtres CSS (filter)",
        "Appliquer des effets visuels comme le flou ou les niveaux de gris avec filter.",
        [
            S("Quelle propriété CSS permet d'appliquer un effet de flou visuel à un élément ?",
              ["filter: blur();", "blur: true;", "box-shadow: blur();", "opacity: blur();"]),
            S("Quelle fonction de `filter` convertit les couleurs d'un élément en niveaux de gris ?",
              ["grayscale()", "blur()", "invert()", "brightness()"]),
            S("Quelle fonction de `filter` inverse les couleurs d'un élément (effet négatif photographique) ?",
              ["invert()", "grayscale()", "contrast()", "hue-rotate()"]),
            M("Quelles fonctions sont valides à l'intérieur de la propriété `filter` ?",
              ["blur()", "brightness()", "contrast()"], {0, 1, 2}, ["translate()", "rotate()"]),
            T("Plusieurs fonctions de filtre peuvent être combinées dans une seule déclaration, comme `filter: blur(2px) grayscale(50%);`.", True),
            T("La propriété filter ne peut jamais être appliquée à des images, uniquement à du texte.", False),
        ],
    )

    quiz(
        "Les modes de fusion (blend modes)",
        "Combiner visuellement des couches avec mix-blend-mode et background-blend-mode.",
        [
            S("Quelle propriété permet de définir comment un élément se fond visuellement avec les éléments situés derrière lui ?",
              ["mix-blend-mode", "background-blend-mode appliqué à l'élément lui-même", "filter-blend", "opacity-mode"]),
            S("Quelle propriété permet de mélanger plusieurs images ou couleurs de fond entre elles sur un même élément ?",
              ["background-blend-mode", "mix-blend-mode", "filter", "blend-image"]),
            S("Quelle valeur de blend mode produit un effet visuel proche d'une multiplication des couleurs, assombrissant généralement le résultat ?",
              ["multiply", "screen", "normal", "lighten"]),
            M("Quelles propriétés CSS permettent d'appliquer des modes de fusion visuelle ?",
              ["mix-blend-mode", "background-blend-mode"], {0, 1}, ["text-align", "vertical-align"]),
            T("`mix-blend-mode` peut créer des effets visuels où la couleur d'un élément interagit avec ce qui se trouve derrière lui dans la pile d'empilement.", True),
            T("Les blend modes CSS sont totalement indépendants des concepts utilisés dans des logiciels de retouche d'image comme Photoshop.", False),
        ],
    )

    quiz(
        "@supports : les feature queries",
        "Détecter le support d'une fonctionnalité CSS avant de l'appliquer.",
        [
            S("À quoi sert la règle `@supports` en CSS ?",
              ["À appliquer des styles uniquement si le navigateur prend en charge une propriété ou valeur CSS donnée", "À charger une police personnalisée", "À définir une animation", "À cibler uniquement l'impression"]),
            S("Quelle syntaxe permet de tester si une propriété CSS est supportée avec @supports ?",
              ["@supports (display: grid) { ... }", "@supports display: grid; { ... }", "@media supports(display: grid) { ... }", "@check (display: grid) { ... }"]),
            S("Quel opérateur permet de tester l'absence de support d'une fonctionnalité avec @supports ?",
              ["not", "without", "except", "exclude"]),
            M("Quels opérateurs logiques peuvent être utilisés à l'intérieur d'une règle @supports ?",
              ["and", "or", "not"], {0, 1, 2}, ["xor", "maybe"]),
            T("@supports est particulièrement utile pour fournir une alternative de mise en page si une fonctionnalité récente comme Grid n'est pas supportée.", True),
            T("@supports ne peut tester que la propriété display et aucune autre propriété CSS.", False),
        ],
    )

    quiz(
        "Architecture CSS : la méthodologie BEM",
        "Structurer ses classes CSS de façon cohérente avec Block, Element, Modifier.",
        [
            S("Que signifie l'acronyme BEM en architecture CSS ?",
              ["Block, Element, Modifier", "Basic, Easy, Modular", "Build, Extend, Maintain", "Bootstrap, Element, Mixin"]),
            S("Dans la convention BEM, quel séparateur est traditionnellement utilisé entre le bloc et son élément ?",
              ["Deux underscores, comme bloc__element", "Un point, comme bloc.element", "Un espace simple", "Une arobase, comme bloc@element"]),
            S("Dans la convention BEM, quel séparateur est traditionnellement utilisé pour indiquer un modificateur ?",
              ["Deux tirets, comme bloc--modificateur", "Deux underscores", "Un point", "Une parenthèse"]),
            M("Quels objectifs poursuit généralement la méthodologie BEM dans un projet CSS ?",
              ["Réduire les conflits de spécificité entre composants", "Faciliter la réutilisation et la lisibilité des classes"], {0, 1}, ["Remplacer entièrement Flexbox", "Interdire l'utilisation de variables CSS"]),
            T("BEM encourage à éviter les sélecteurs CSS imbriqués trop profondément en s'appuyant principalement sur des classes plates.", True),
            T("BEM est une spécification officielle du W3C intégrée nativement au langage CSS.", False),
        ],
    )

    quiz(
        "Styles d'impression avec @media print",
        "Adapter l'apparence d'une page pour une impression papier propre.",
        [
            S("Quelle media query cible spécifiquement l'apparence d'une page lors de son impression ?",
              ["@media print", "@media screen", "@media speech", "@media paper"]),
            S("Quelle propriété est souvent utilisée dans les styles d'impression pour masquer des éléments comme la navigation ou les boutons interactifs ?",
              ["display: none;", "color: white;", "opacity: 1;", "position: sticky;"]),
            S("Pourquoi est-il courant de forcer une couleur de texte sombre sur fond clair dans les styles d'impression ?",
              ["Pour économiser l'encre et garantir la lisibilité sur papier", "Parce que les imprimantes ne supportent pas les couleurs vives", "Parce que cela accélère la vitesse d'impression", "Parce que @media print l'exige obligatoirement par défaut"]),
            M("Quels éléments est-il courant de masquer ou d'adapter spécifiquement dans une feuille de style d'impression ?",
              ["Les menus de navigation", "Les boutons d'action interactifs"], {0, 1}, ["Le contenu textuel principal", "Les titres de section"]),
            T("On peut afficher l'URL d'un lien à côté de son texte uniquement à l'impression grâce à des pseudo-éléments comme ::after combinés à @media print.", True),
            T("@media print ne peut jamais modifier les marges ou la taille de police d'un document.", False),
        ],
    )
