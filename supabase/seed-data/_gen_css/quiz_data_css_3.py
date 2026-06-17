# -*- coding: utf-8 -*-
"""Quiz 21-30 : Positionnement (static/relative/absolute/fixed/sticky) + z-index + display/overflow."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Le positionnement static et relative",
        "Les bases du positionnement CSS avec position: static et relative.",
        [
            S("Quelle est la valeur par défaut de la propriété `position` pour tous les éléments HTML ?",
              ["static", "relative", "absolute", "fixed"]),
            S("Avec `position: relative`, par rapport à quoi un élément est-il décalé lorsqu'on utilise `top` et `left` ?",
              ["Par rapport à sa position normale dans le flux", "Par rapport à la fenêtre du navigateur", "Par rapport au document entier", "Par rapport à son parent le plus proche, quel que soit son positionnement"]),
            S("Un élément en `position: static` peut-il être déplacé avec les propriétés `top`, `left`, `right`, `bottom` ?",
              ["Non, ces propriétés sont ignorées en position static", "Oui, sans aucune restriction", "Oui, mais uniquement avec `top`", "Oui, uniquement en combinaison avec flexbox"]),
            M("Quels effets a `position: relative` sur le flux du document et sur les éléments enfants ?",
              ["L'élément reste dans le flux normal du document", "Il devient une référence pour les enfants en position absolute"], {0, 1}, ["Il sort systématiquement du flux", "Il force l'élément à occuper toute la largeur de la page"]),
            T("La position relative est souvent utilisée comme conteneur de référence pour des enfants positionnés en absolute.", True),
            T("`position: static` retire l'élément du flux normal du document.", False),
        ],
    )

    quiz(
        "Positionnement absolute et fixed",
        "Sortir un élément du flux normal pour le positionner précisément.",
        [
            S("Par rapport à quoi un élément en `position: absolute` est-il positionné par défaut, en l'absence d'ancêtre positionné ?",
              ["Le bloc englobant initial (généralement la fenêtre/document)", "Son parent direct, toujours", "Le centre de l'écran", "L'élément précédent dans le DOM"]),
            S("Quelle propriété sur un ancêtre permet de devenir le référentiel de positionnement d'un descendant en `position: absolute` ?",
              ["Tout positionnement autre que static (relative, absolute, fixed ou sticky)", "display: block", "overflow: hidden", "float: left"]),
            S("Quelle est la particularité de `position: fixed` par rapport au défilement de la page ?",
              ["L'élément reste fixe à l'écran même lors du défilement", "L'élément défile normalement avec le contenu", "L'élément est centré automatiquement", "L'élément disparaît lors du défilement"]),
            M("Quels effets produit `position: absolute` sur un élément ?",
              ["Il sort du flux normal du document", "Il n'affecte plus la position des éléments frères restés dans le flux"], {0, 1}, ["Il conserve sa taille de bloc complète comme en flux normal", "Il devient automatiquement centré horizontalement"]),
            T("Un élément `position: fixed` est positionné par rapport à la fenêtre d'affichage (viewport), sauf cas particulier d'ancêtre avec transform.", True),
            T("`position: absolute` conserve l'élément dans le flux normal du document comme `position: static`.", False),
        ],
    )

    quiz(
        "Le positionnement sticky",
        "Un comportement hybride entre relative et fixed pour des en-têtes ou menus persistants.",
        [
            S("Quel comportement décrit le mieux `position: sticky` ?",
              ["L'élément se comporte comme relative jusqu'à atteindre un seuil de défilement, puis devient fixe", "L'élément est toujours fixe dès le chargement de la page", "L'élément disparaît dès qu'on commence à défiler", "L'élément se comporte exactement comme absolute"]),
            S("Quelle propriété est indispensable pour qu'un élément `position: sticky` s'active lors du défilement ?",
              ["Au moins une des propriétés top, bottom, left ou right", "z-index", "display: block", "overflow: visible sur le body uniquement"]),
            S("Pourquoi un élément `position: sticky` peut-il ne pas fonctionner comme attendu dans certains cas ?",
              ["Un ancêtre avec overflow: hidden ou auto peut limiter son champ d'action", "sticky est incompatible avec Flexbox", "sticky ne fonctionne que sur les balises <div>", "sticky désactive automatiquement le défilement de la page"]),
            M("Quelles affirmations sur `position: sticky` sont correctes ?",
              ["Il reste dans le flux normal jusqu'à activation", "Son comportement dépend de la zone de défilement de son conteneur parent"], {0, 1}, ["Il nécessite obligatoirement JavaScript pour fonctionner", "Il ne peut jamais être utilisé pour un en-tête de tableau"]),
            T("`position: sticky` est couramment utilisé pour fixer un en-tête de section pendant le défilement d'une longue page.", True),
            T("Un élément sticky reste figé pour toujours à l'écran même après défilement complet de son conteneur parent.", False),
        ],
    )

    quiz(
        "z-index et contexte d'empilement",
        "Gérer l'ordre de superposition des éléments positionnés.",
        [
            S("Quelle propriété permet de contrôler l'ordre de superposition (devant/derrière) des éléments positionnés ?",
              ["z-index", "order", "layer", "depth"]),
            S("La propriété `z-index` fonctionne-t-elle sur un élément en `position: static` ?",
              ["Non, elle n'a aucun effet sans position différente de static", "Oui, toujours", "Oui, mais uniquement sur les images", "Oui, uniquement en mode flexbox"]),
            S("Entre deux éléments positionnés avec `z-index: 5` et `z-index: 10`, lequel apparaît visuellement au-dessus ?",
              ["Celui avec z-index: 10", "Celui avec z-index: 5", "Cela dépend uniquement de l'ordre dans le HTML", "Les deux se superposent à égalité"]),
            M("Quelles propriétés CSS peuvent créer un nouveau contexte d'empilement ?",
              ["position avec z-index différent de auto", "opacity inférieure à 1"], {0, 1}, ["color", "text-align"]),
            T("Un `z-index` négatif permet de placer un élément derrière son parent ou d'autres éléments.", True),
            T("Le contexte d'empilement créé par un parent limite la portée du z-index de ses enfants par rapport aux éléments extérieurs à ce contexte.", True),
        ],
    )

    quiz(
        "display: block, inline et inline-block",
        "Les valeurs fondamentales de la propriété display et leurs différences de comportement.",
        [
            S("Quelle propriété de base contrôle si un élément génère une boîte de type bloc ou en ligne ?",
              ["display", "position", "float", "visibility"]),
            S("Un élément en `display: inline` accepte-t-il les propriétés `width` et `height` ?",
              ["Non, ces propriétés sont ignorées sur un élément inline standard", "Oui, sans restriction", "Oui, mais uniquement la largeur", "Oui, mais uniquement la hauteur"]),
            S("Quelle valeur de `display` permet à un élément de se comporter comme un bloc en acceptant largeur/hauteur tout en restant sur la même ligne que d'autres éléments ?",
              ["inline-block", "block", "inline", "flex"]),
            M("Quelles caractéristiques décrivent un élément en `display: block` ?",
              ["Il occupe toute la largeur disponible par défaut", "Il commence sur une nouvelle ligne"], {0, 1}, ["Il s'aligne toujours horizontalement avec ses voisins", "Il ignore systématiquement la propriété width"]),
            T("Par défaut, une balise <span> est un élément inline alors qu'une balise <div> est un élément block.", True),
            T("Un élément `display: inline` démarre toujours sur une nouvelle ligne, comme un élément block.", False),
        ],
    )

    quiz(
        "display: none et visibility: hidden",
        "Deux façons de masquer un élément avec des effets différents sur la mise en page.",
        [
            S("Quelle différence essentielle existe entre `display: none` et `visibility: hidden` ?",
              ["display: none retire l'élément du rendu et de l'espace occupé, visibility: hidden conserve l'espace", "Les deux sont strictement identiques", "visibility: hidden retire l'élément du DOM", "display: none ne fonctionne que sur les images"]),
            S("Un élément avec `visibility: hidden` peut-il recevoir des clics ou interactions ?",
              ["Non, il est invisible et non interactif tout en conservant sa place", "Oui, il reste cliquable normalement", "Oui, uniquement au survol", "Cela dépend du navigateur uniquement"]),
            S("Quelle valeur de `display` rend un élément totalement absent de l'arbre d'accessibilité et du rendu visuel ?",
              ["none", "contents", "inline", "block"]),
            M("Quelles affirmations sur `display: none` sont vraies ?",
              ["L'élément n'occupe plus aucun espace dans la mise en page", "L'élément n'est plus accessible aux lecteurs d'écran"], {0, 1}, ["L'élément reste visible mais grisé", "L'élément conserve son espace réservé comme avec visibility: hidden"]),
            T("`display: none` supprime visuellement l'élément tout en le laissant présent dans le DOM HTML.", True),
            T("`visibility: hidden` conserve l'espace occupé par l'élément dans la mise en page, contrairement à `display: none`.", True),
        ],
    )

    quiz(
        "display: contents et display: flex/grid",
        "Les valeurs modernes de display pour structurer les layouts.",
        [
            S("Quelle valeur de `display` fait disparaître la boîte de l'élément tout en conservant ses enfants dans le rendu ?",
              ["contents", "none", "inline", "block"]),
            S("Quelle valeur de `display` transforme un élément en conteneur flexible pour ses enfants directs ?",
              ["flex", "block", "table", "inline-block"]),
            S("Quelle valeur de `display` transforme un élément en conteneur de grille CSS ?",
              ["grid", "flex", "table", "block"]),
            M("Quelles valeurs de display créent un nouveau contexte de mise en page pour les enfants directs ?",
              ["flex", "grid"], {0, 1}, ["contents", "none"]),
            T("`display: contents` permet de retirer la boîte d'un conteneur tout en laissant ses enfants se comporter comme s'ils étaient des enfants directs de son parent.", True),
            T("`display: grid` et `display: flex` produisent strictement le même algorithme de positionnement des enfants.", False),
        ],
    )

    quiz(
        "La propriété overflow",
        "Gérer le contenu qui dépasse les limites d'une boîte.",
        [
            S("Quelle valeur de `overflow` ajoute des barres de défilement uniquement si le contenu dépasse la boîte ?",
              ["auto", "visible", "hidden", "scroll"]),
            S("Quelle valeur de `overflow` masque purement et simplement tout contenu qui dépasse la boîte ?",
              ["hidden", "visible", "auto", "clip"]),
            S("Quelle est la valeur par défaut de la propriété `overflow` ?",
              ["visible", "hidden", "auto", "scroll"]),
            M("Quelles propriétés permettent de contrôler le débordement séparément pour chaque axe ?",
              ["overflow-x", "overflow-y"], {0, 1}, ["overflow-top", "overflow-left"]),
            T("`overflow: scroll` affiche toujours les barres de défilement, même si le contenu ne dépasse pas la boîte.", True),
            T("`overflow: hidden` empêche tout débordement visuel du contenu, ce qui peut couper du texte ou des images.", True),
        ],
    )

    quiz(
        "Float et clear : technique historique",
        "Comprendre le float, son usage historique et la nécessité du clear.",
        [
            S("À quoi servait historiquement la propriété `float` avant l'arrivée de Flexbox et Grid ?",
              ["À créer des mises en page en colonnes en faisant flotter les éléments côte à côte", "À centrer verticalement un texte", "À animer des transitions de couleur", "À définir la transparence d'un élément"]),
            S("Quel problème courant la propriété `clear` permet-elle de résoudre ?",
              ["Empêcher un élément de remonter aux côtés d'éléments flottants précédents", "Supprimer toutes les marges d'un élément", "Réinitialiser la couleur de fond d'un élément", "Centrer un élément horizontalement"]),
            S("Que se passe-t-il pour un conteneur parent dont tous les enfants sont flottants, sans technique de clearfix ?",
              ["Le parent peut s'effondrer en hauteur car il ne \"voit\" plus la hauteur des enfants flottants", "Le parent s'agrandit automatiquement sans problème", "Le parent devient automatiquement display: flex", "Aucun effet, le float n'influence jamais la hauteur du parent"]),
            M("Pourquoi Flexbox et Grid sont-ils aujourd'hui préférés au float pour les mises en page modernes ?",
              ["Ils offrent un contrôle natif de l'alignement et de la distribution de l'espace", "Ils évitent les effets de bord comme l'effondrement du conteneur parent"], {0, 1}, ["float a été supprimé de la spécification CSS3", "float ne fonctionne plus dans les navigateurs récents"]),
            T("La technique du clearfix a été largement utilisée pour forcer un conteneur à englober correctement ses enfants flottants.", True),
            T("La propriété float a été totalement retirée des spécifications CSS modernes et ne doit plus jamais être utilisée.", False),
        ],
    )
