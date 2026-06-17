# -*- coding: utf-8 -*-
"""Quiz 61-70 : Transitions, animations, transformations."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Les bases des transitions CSS",
        "Animer en douceur le changement de valeur d'une propriété CSS.",
        [
            S("Quelle propriété raccourcie permet de définir une transition CSS en une seule déclaration ?",
              ["transition", "animation", "transform", "keyframes"]),
            S("Quelle propriété indique la durée d'une transition CSS ?",
              ["transition-duration", "transition-delay", "transition-property", "transition-timing-function"]),
            S("Quelle propriété précise quelles propriétés CSS doivent être animées lors d'une transition ?",
              ["transition-property", "transition-duration", "transition-delay", "transition-timing-function"]),
            M("Quelles informations sont nécessaires pour qu'une transition CSS fonctionne correctement ?",
              ["Une propriété CSS qui change de valeur", "Une durée de transition supérieure à 0"], {0, 1}, ["Une règle @keyframes obligatoire", "Un script JavaScript obligatoire"]),
            T("Une transition CSS nécessite un événement (comme :hover) ou un changement d'état pour se déclencher visuellement.", True),
            T("Les transitions CSS nécessitent obligatoirement la règle @keyframes pour fonctionner.", False),
        ],
    )

    quiz(
        "transition-timing-function et les courbes d'accélération",
        "Contrôler le rythme d'une transition avec des fonctions d'accélération.",
        [
            S("Quelle valeur de `transition-timing-function` produit une vitesse constante du début à la fin ?",
              ["linear", "ease-in", "ease-out", "ease-in-out"]),
            S("Quelle valeur de `transition-timing-function` commence lentement puis accélère vers la fin ?",
              ["ease-in", "ease-out", "linear", "step-end"]),
            S("Quelle fonction CSS permet de définir une courbe de Bézier personnalisée pour une transition ?",
              ["cubic-bezier()", "linear-gradient()", "calc()", "steps-curve()"]),
            M("Quelles valeurs sont des mots-clés valides pour transition-timing-function ?",
              ["ease", "ease-in-out"], {0, 1}, ["bounce-extreme", "smooth-max"]),
            T("`ease-in-out` combine une accélération en début de transition et une décélération en fin de transition.", True),
            T("La fonction `steps()` permet de créer une transition qui progresse par paliers discrets plutôt que de façon continue.", True),
        ],
    )

    quiz(
        "Les animations CSS avec @keyframes",
        "Créer des séquences d'animation complexes avec des étapes définies.",
        [
            S("Quelle règle CSS permet de définir les étapes d'une animation personnalisée ?",
              ["@keyframes", "@media", "@font-face", "@supports"]),
            S("Quelle propriété associe un élément à une animation définie par @keyframes ?",
              ["animation-name", "transition-name", "animation-property", "keyframe-link"]),
            S("Dans une règle @keyframes, quels mots-clés peuvent délimiter le début et la fin d'une animation ?",
              ["from et to", "start et end", "begin et finish", "open et close"]),
            M("Quelles propriétés permettent de contrôler une animation CSS définie via @keyframes ?",
              ["animation-duration", "animation-iteration-count"], {0, 1}, ["transition-delay", "transform-origin"]),
            T("On peut utiliser des pourcentages (comme 0%, 50%, 100%) à l'intérieur de @keyframes pour définir des étapes intermédiaires précises.", True),
            T("Une règle @keyframes peut uniquement définir deux étapes : le début et la fin, jamais d'étapes intermédiaires.", False),
        ],
    )

    quiz(
        "animation-iteration-count et animation-direction",
        "Contrôler la répétition et le sens de lecture d'une animation.",
        [
            S("Quelle valeur de `animation-iteration-count` fait jouer une animation indéfiniment en boucle ?",
              ["infinite", "loop", "repeat", "forever"]),
            S("Quelle propriété détermine si une animation doit être jouée normalement, à l'envers, ou en alternance ?",
              ["animation-direction", "animation-fill-mode", "animation-name", "animation-play-state"]),
            S("Quelle valeur de `animation-direction` fait jouer l'animation à l'endroit, puis à l'envers, en alternance à chaque répétition ?",
              ["alternate", "normal", "reverse", "alternate-reverse uniquement pour la première itération"]),
            M("Quelles valeurs sont valides pour la propriété `animation-direction` ?",
              ["normal", "reverse", "alternate"], {0, 1, 2}, ["infinite", "ease-in"]),
            T("`animation-iteration-count: 3;` signifie que l'animation se répète exactement trois fois avant de s'arrêter.", True),
            T("La propriété `animation-play-state` permet de mettre en pause ou de relancer une animation CSS via du code ou une interaction.", True),
        ],
    )

    quiz(
        "animation-fill-mode et l'état final d'une animation",
        "Déterminer quelles valeurs de style s'appliquent avant et après l'animation.",
        [
            S("Quelle propriété détermine si les styles définis dans la dernière étape d'une animation restent appliqués après sa fin ?",
              ["animation-fill-mode", "animation-direction", "animation-delay", "animation-timing-function"]),
            S("Quelle valeur de `animation-fill-mode` conserve les styles de la dernière étape (100%) après la fin de l'animation ?",
              ["forwards", "backwards", "none", "both-reverse"]),
            S("Quelle valeur de `animation-fill-mode` applique les styles définis à 0% dès avant le démarrage de l'animation (utile avec un délai) ?",
              ["backwards", "forwards", "none", "normal"]),
            M("Quelles valeurs sont valides pour `animation-fill-mode` ?",
              ["forwards", "backwards", "both"], {0, 1, 2}, ["infinite", "alternate"]),
            T("Sans `animation-fill-mode: forwards`, un élément animé peut revenir à son état CSS d'origine une fois l'animation terminée.", True),
            T("`animation-fill-mode` contrôle la vitesse de l'animation au cours du temps.", False),
        ],
    )

    quiz(
        "Les transformations 2D : translate, rotate et scale",
        "Déplacer, faire pivoter et redimensionner des éléments avec transform.",
        [
            S("Quelle fonction CSS de transform déplace un élément sans affecter le flux normal du document ?",
              ["translate()", "rotate()", "scale()", "skew()"]),
            S("Quelle fonction CSS de transform fait pivoter un élément autour d'un point central par défaut ?",
              ["rotate()", "translate()", "scale()", "perspective()"]),
            S("Quelle fonction CSS de transform agrandit ou réduit la taille visuelle d'un élément ?",
              ["scale()", "translate()", "rotate()", "skew()"]),
            M("Quelles fonctions sont valides à l'intérieur de la propriété `transform` ?",
              ["translate()", "rotate()", "scale()"], {0, 1, 2}, ["transition()", "animation()"]),
            T("La propriété `transform` permet de combiner plusieurs fonctions de transformation dans une seule déclaration, comme `transform: rotate(45deg) scale(1.2);`.", True),
            T("Utiliser `transform: translate()` modifie la position des autres éléments dans le flux du document, comme le ferait `margin`.", False),
        ],
    )

    quiz(
        "skew(), transform-origin et transformations combinées",
        "Approfondir les transformations CSS avec l'inclinaison et le point d'origine.",
        [
            S("Que fait la fonction `skew()` appliquée à un élément ?",
              ["Elle incline (déforme) l'élément selon un angle donné", "Elle le fait pivoter complètement", "Elle le rend transparent", "Elle inverse ses couleurs"]),
            S("Quelle propriété définit le point fixe autour duquel s'effectuent les transformations comme rotate ou scale ?",
              ["transform-origin", "transform-point", "anchor-point", "transform-center"]),
            S("Quelle est la valeur par défaut de `transform-origin` ?",
              ["Le centre de l'élément (50% 50%)", "Le coin supérieur gauche (0 0)", "Le coin inférieur droit (100% 100%)", "Aucune valeur par défaut, elle est obligatoire"]),
            M("Quelles fonctions de transform permettent de déformer ou incliner un élément selon un ou deux axes ?",
              ["skewX()", "skewY()"], {0, 1}, ["translateZ()", "scale3d()"]),
            T("Modifier `transform-origin` à `0 0` fait pivoter un élément autour de son coin supérieur gauche au lieu de son centre.", True),
            T("`transform: scale(2)` agrandit un élément en doublant sa taille visuelle sur les deux axes par défaut.", True),
        ],
    )

    quiz(
        "Transformations 3D et perspective",
        "Donner de la profondeur aux transformations avec rotateX, rotateY et perspective.",
        [
            S("Quelle propriété CSS permet de définir la distance de l'observateur pour créer un effet de profondeur 3D ?",
              ["perspective", "transform-depth", "z-index", "transform-3d"]),
            S("Quelle fonction de transform fait pivoter un élément autour de l'axe horizontal (X), créant un effet de bascule vers l'avant ou l'arrière ?",
              ["rotateX()", "rotateY()", "rotateZ()", "rotate()"]),
            S("Quelle fonction de transform fait pivoter un élément autour de l'axe vertical (Y), comme une porte qui s'ouvre ?",
              ["rotateY()", "rotateX()", "rotateZ()", "skewY()"]),
            M("Quelles propriétés ou valeurs sont liées aux transformations 3D en CSS ?",
              ["perspective", "transform-style: preserve-3d"], {0, 1}, ["text-align", "line-height"]),
            T("`transform-style: preserve-3d` permet aux enfants d'un élément de conserver leur positionnement tridimensionnel par rapport à leur parent transformé.", True),
            T("Les transformations 3D comme rotateX et rotateY n'ont aucun intérêt visuel sans la propriété perspective définie sur un ancêtre.", False),
        ],
    )

    quiz(
        "Performance des animations CSS",
        "Optimiser les animations pour un rendu fluide dans le navigateur.",
        [
            S("Pourquoi animer `transform` et `opacity` est-il généralement plus performant qu'animer `width` ou `top` ?",
              ["Ils peuvent souvent être traités par le compositeur graphique sans recalculer la mise en page (reflow)", "Ils sont les seules propriétés animables en CSS", "Ils ne fonctionnent que sur les navigateurs mobiles", "Ils nécessitent toujours JavaScript pour s'animer"]),
            S("Quelle propriété CSS peut indiquer au navigateur qu'un élément va être animé, pour optimiser son rendu en amont ?",
              ["will-change", "transform-hint", "animation-priority", "render-hint"]),
            S("Que risque de provoquer une animation fréquente de la propriété `width` sur de nombreux éléments d'une page complexe ?",
              ["Des recalculs de mise en page (reflow) coûteux en performance", "Aucun impact, toutes les propriétés sont équivalentes en coût", "Une accélération automatique du rendu", "Un blocage total du navigateur"]),
            M("Quelles propriétés sont généralement considérées comme peu coûteuses à animer car gérées par le compositeur graphique ?",
              ["transform", "opacity"], {0, 1}, ["width", "margin"]),
            T("Limiter l'usage de `will-change` aux éléments réellement animés évite de consommer inutilement de la mémoire graphique.", True),
            T("Toutes les propriétés CSS ont strictement le même coût de calcul lorsqu'elles sont animées en boucle.", False),
        ],
    )

    quiz(
        "Combiner transitions, animations et transformations",
        "Construire des interactions fluides en associant plusieurs techniques CSS.",
        [
            S("Quelle est la principale différence entre une transition CSS et une animation CSS avec @keyframes ?",
              ["La transition réagit à un changement d'état alors que l'animation peut se jouer automatiquement avec des étapes définies", "Ce sont des synonymes stricts", "Les transitions nécessitent toujours JavaScript", "Les animations ne peuvent pas être répétées"]),
            S("Peut-on appliquer une transition sur la propriété `transform` elle-même ?",
              ["Oui, par exemple pour animer en douceur un changement de rotate() ou scale() au survol", "Non, transform est incompatible avec transition", "Oui, mais uniquement avec translate()", "Non, cela nécessite obligatoirement @keyframes"]),
            S("Pourquoi utiliser `:hover` combiné à `transition` est une technique courante pour des boutons interactifs ?",
              ["Pour offrir un retour visuel fluide au survol sans recourir à JavaScript", "Parce que c'est la seule façon de changer une couleur en CSS", "Parce que cela améliore automatiquement le référencement SEO", "Parce que :hover ne fonctionne qu'avec des animations @keyframes"]),
            M("Quelles techniques permettent de créer un effet de survol animé sur un bouton sans JavaScript ?",
              [":hover combiné à transition", "transform combiné à transition"], {0, 1}, ["@media print", "@font-face"]),
            T("On peut combiner plusieurs propriétés CSS animées en même temps dans une seule déclaration `transition: color 0.3s, transform 0.3s;`.", True),
            T("Une animation @keyframes ne peut jamais être déclenchée automatiquement au chargement de la page sans interaction de l'utilisateur.", False),
        ],
    )
