// Generator for css.json — authored content, emits validated JSON.
import { writeFileSync } from "node:fs";

const T = (q, t = 13) => ({ type: "truefalse", time_limit: t, statement: q.s,
  answers: [ { text: "Vrai", is_correct: q.v }, { text: "Faux", is_correct: !q.v } ] });
const S = (s, correct, others, t = 20) => ({ type: "single", time_limit: t, statement: s,
  answers: [ { text: correct, is_correct: true }, ...others.map(o => ({ text: o, is_correct: false })) ] });
const M = (s, corrects, wrongs, t = 27) => ({ type: "multiple", time_limit: t, statement: s,
  answers: [ ...corrects.map(c => ({ text: c, is_correct: true })), ...wrongs.map(w => ({ text: w, is_correct: false })) ] });

const quizzes = [];
const Q = (title, description, questions) => quizzes.push({ title, description, questions });

// ============ ASSEMBLED BELOW ============

// 1
Q("Les sélecteurs de base (Débutant)", "Apprends à cibler les éléments avec les sélecteurs fondamentaux du CSS.", [
  S("Quel sélecteur cible tous les éléments d'une page ?", "*", [".tout", "#all", "all"]),
  S("Quel caractère précède un sélecteur de classe ?", ".", ["#", "@", "&"]),
  S("Quel caractère précède un sélecteur d'identifiant (id) ?", "#", [".", "$", "%"]),
  M("Lesquels de ces sélecteurs sont valides en CSS ?", ["p (type)", ".rouge (classe)", "#menu (id)"], ["@bloc", "%titre"]),
  T({ s: "Un sélecteur de type comme « p » cible toutes les balises <p> de la page.", v: true }),
  S("Comment cibler un élément <a> situé à l'intérieur d'un <nav> (descendant) ?", "nav a", ["nav>a uniquement", "nav+a", "nav~a"]),
]);

// 2
Q("Spécificité et cascade (Intermédiaire)", "Comprends comment le navigateur tranche entre plusieurs règles en conflit.", [
  S("Quel sélecteur a la plus forte spécificité parmi ceux-ci ?", "#id", [".classe", "élément type", "* (universel)"]),
  S("En cas d'égalité de spécificité, quelle règle l'emporte ?", "La dernière déclarée dans le code", ["La première déclarée", "Celle avec le moins de propriétés", "Une au hasard"]),
  T({ s: "« !important » permet de forcer une déclaration à l'emporter sur la spécificité normale.", v: true }),
  M("Quels facteurs entrent dans le calcul de la spécificité ?", ["Le nombre d'id", "Le nombre de classes", "Le nombre de sélecteurs de type"], ["La longueur du nom de classe", "L'ordre alphabétique"]),
  S("Le sélecteur universel « * » contribue à quelle valeur de spécificité ?", "Zéro (il n'ajoute rien)", ["Autant qu'une classe", "Autant qu'un id", "Autant qu'un élément"]),
  S("Entre une règle dans une feuille externe et une règle en attribut « style », laquelle gagne (sans !important) ?", "Le style en ligne (attribut style)", ["La feuille externe", "Aucune, conflit ignoré", "Celle écrite en premier"]),
]);

// 3
Q("Le modèle de boîte (Débutant)", "Découvre comment chaque élément est entouré de padding, bordure et marge.", [
  S("Dans le modèle de boîte standard, quelle couche est la plus interne ?", "Le contenu (content)", ["La marge (margin)", "La bordure (border)", "Le padding"]),
  S("Quel ordre, de l'intérieur vers l'extérieur, est correct ?", "content, padding, border, margin", ["margin, border, padding, content", "content, border, padding, margin", "padding, content, margin, border"]),
  T({ s: "La marge (margin) est transparente et ne possède pas de couleur de fond.", v: true }),
  M("Quelles propriétés font partie du modèle de boîte ?", ["padding", "border", "margin"], ["font-size", "color"]),
  S("Avec « box-sizing: content-box » (valeur par défaut), à quoi correspond « width » ?", "À la largeur du contenu seul", ["Au contenu + padding + bordure", "À toute la boîte marges comprises", "Au contenu + marge"]),
  S("Quelle propriété permet d'inclure padding et bordure dans la largeur déclarée ?", "box-sizing: border-box", ["overflow: hidden", "display: block", "width: auto"]),
]);

// 4
Q("Les unités de mesure (Intermédiaire)", "Maîtrise px, em, rem, pourcentages et unités de viewport.", [
  S("L'unité « rem » est relative à quelle taille de police ?", "Celle de l'élément racine <html>", ["Celle de l'élément parent", "Celle de l'élément lui-même", "Toujours 16px fixe"]),
  S("L'unité « em » pour font-size est relative à quoi ?", "À la taille de police de l'élément parent", ["À l'élément racine", "À la largeur du viewport", "À 1 pixel"]),
  T({ s: "L'unité « vw » correspond à 1 % de la largeur du viewport.", v: true }),
  M("Quelles unités sont relatives (et non absolues) ?", ["em", "rem", "%"], ["px", "cm"]),
  S("Que représente l'unité « vh » ?", "1 % de la hauteur du viewport", ["1 % de la largeur du viewport", "La hauteur de la police", "1 caractère"]),
  S("L'unité « ch » est basée sur la largeur de quel caractère dans la police courante ?", "Le caractère « 0 » (zéro)", ["La lettre « m »", "La lettre « x »", "L'espace"]),
]);

// 5
Q("La propriété display (Débutant)", "Comprends block, inline, inline-block et none.", [
  S("Quelle valeur de display fait qu'un élément occupe toute la largeur disponible et passe à la ligne ?", "block", ["inline", "none", "inline-block"]),
  S("Quel élément est « inline » par défaut ?", "<span>", ["<div>", "<p>", "<section>"]),
  T({ s: "Un élément en « display: none » est retiré du flux et n'occupe aucun espace.", v: true }),
  M("Quelles valeurs permettent à un élément inline d'accepter une width et une height ?", ["inline-block", "block", "flex"], ["inline", "none"]),
  S("Quelle différence clé sépare « inline » de « inline-block » ?", "inline-block accepte width/height, pas inline", ["inline-block est invisible", "inline occupe toute la ligne", "Il n'y a aucune différence"]),
  S("Quel élément est « block » par défaut ?", "<div>", ["<a>", "<span>", "<strong>"]),
]);

// 6
Q("Les couleurs en CSS (Débutant)", "Hex, rgb, rgba, hsl et mots-clés de couleur.", [
  S("Que signifie le « a » dans rgba() ?", "Le canal alpha (opacité)", ["L'angle", "L'amplitude", "L'accent"]),
  S("Combien de chiffres hexadécimaux comporte une couleur hex complète comme #ff8800 ?", "6", ["3", "4", "8"]),
  T({ s: "Le mot-clé « transparent » équivaut à une couleur totalement transparente.", v: true }),
  M("Quelles notations de couleur sont valides en CSS ?", ["#ff0000", "rgb(255,0,0)", "hsl(0,100%,50%)"], ["color(rouge)", "#zz0011"]),
  S("Dans hsl(), que représente le premier paramètre ?", "La teinte (hue), en degrés", ["La saturation", "La luminosité", "L'opacité"]),
  S("Que vaut la couleur représentée par le mot-clé « currentColor » ?", "La valeur courante de la propriété color", ["Toujours noir", "Toujours blanc", "Une couleur aléatoire"]),
]);

// 7
Q("Flexbox : les fondamentaux (Intermédiaire)", "Active un conteneur flex et aligne ses enfants.", [
  S("Quelle déclaration active un conteneur flex ?", "display: flex", ["display: block", "position: flex", "flex: on"]),
  S("Quelle propriété définit l'axe principal (horizontal ou vertical) ?", "flex-direction", ["justify-content", "align-items", "flex-wrap"]),
  S("Sur quel axe agit « justify-content » ?", "L'axe principal", ["L'axe transversal", "L'axe vertical uniquement", "Aucun axe"]),
  M("Quelles sont des valeurs valides de justify-content ?", ["center", "space-between", "flex-start"], ["middle", "justify"]),
  T({ s: "Par défaut, flex-direction vaut « row » (les éléments s'alignent en ligne).", v: true }),
  S("Quelle propriété aligne les éléments flex sur l'axe transversal ?", "align-items", ["justify-content", "flex-grow", "order"]),
]);

// 8
Q("CSS Grid : les bases (Intermédiaire)", "Crée des grilles avec colonnes, lignes et l'unité fr.", [
  S("Quelle déclaration active une grille ?", "display: grid", ["display: flex", "grid: on", "position: grid"]),
  S("Quelle propriété définit les colonnes d'une grille ?", "grid-template-columns", ["grid-columns", "columns", "grid-cols"]),
  S("Que représente l'unité « fr » dans une grille ?", "Une fraction de l'espace disponible", ["Un pixel français", "Un pourcentage du parent", "Une fraction de seconde"]),
  M("Quelles valeurs créent trois colonnes égales ?", ["repeat(3, 1fr)", "1fr 1fr 1fr"], ["3 columns", "33% 33%"]),
  T({ s: "La propriété « gap » définit l'espacement entre les cellules d'une grille.", v: true }),
  S("Que fait minmax(100px, 1fr) sur une colonne ?", "Fixe une taille entre 100px et 1 fraction", ["Crée 100 colonnes", "Limite à exactement 100px", "Désactive la colonne"]),
]);

// 9
Q("La propriété position (Intermédiaire)", "static, relative, absolute, fixed et sticky.", [
  S("Quelle est la valeur par défaut de la propriété position ?", "static", ["relative", "absolute", "fixed"]),
  S("Par rapport à quoi un élément « position: absolute » se positionne-t-il ?", "Son ancêtre positionné le plus proche", ["Toujours le <body>", "Le viewport", "Son élément suivant"]),
  S("Que fait « position: fixed » ?", "Fixe l'élément par rapport au viewport", ["Le fixe au parent", "Le retire du DOM", "Le centre automatiquement"]),
  M("Quelles valeurs de position sortent l'élément du flux normal ?", ["absolute", "fixed"], ["static", "relative"]),
  T({ s: "« position: relative » décale l'élément tout en conservant sa place dans le flux.", v: true }),
  S("Quelle valeur combine le comportement relatif puis fixe selon le défilement ?", "sticky", ["absolute", "static", "fixed"]),
]);

// 10
Q("Pseudo-classes courantes (Intermédiaire)", ":hover, :focus, :first-child, :nth-child et autres.", [
  S("Quelle pseudo-classe s'active au survol de la souris ?", ":hover", [":focus", ":active", ":visited"]),
  S("Quelle pseudo-classe cible un élément qui a le focus clavier ?", ":focus", [":hover", ":checked", ":target"]),
  S("Que cible « li:first-child » ?", "Le premier <li> parmi ses frères", ["Le dernier <li>", "Tous les <li>", "Le <li> survolé"]),
  M("Quelles pseudo-classes existent réellement en CSS ?", [":hover", ":nth-child()", ":not()"], [":onclick", ":mousedown"]),
  T({ s: "« :nth-child(2n) » cible les éléments de rang pair.", v: true }),
  S("Que fait la pseudo-classe « :not(.actif) » ?", "Cible les éléments n'ayant pas la classe actif", ["Cible uniquement .actif", "Désactive l'élément", "Cache l'élément"]),
]);

// 11
Q("Pseudo-éléments ::before et ::after (Intermédiaire)", "Génère du contenu décoratif sans toucher au HTML.", [
  S("Quelle propriété est obligatoire pour qu'un ::before s'affiche ?", "content", ["display", "color", "position"]),
  S("Combien de deux-points utilise la syntaxe moderne d'un pseudo-élément ?", "Deux (::)", ["Un (:)", "Trois (:::)", "Aucun"]),
  T({ s: "Le contenu généré par ::before n'apparaît pas dans le DOM HTML.", v: true }),
  M("Que peut-on faire avec ::before et ::after ?", ["Ajouter une icône décorative", "Insérer du texte généré", "Créer un effet de surbrillance"], ["Ajouter un écouteur d'événement JS", "Modifier la base de données"]),
  S("Où ::after insère-t-il son contenu ?", "Juste après le contenu de l'élément", ["Avant l'élément", "À la fin de la page", "Dans le <head>"]),
  S("Quelle valeur de content crée un pseudo-élément vide mais présent ?", "content: \"\"", ["content: none", "content: empty", "content: null"]),
]);

// 12
Q("Les transitions CSS (Intermédiaire)", "Anime en douceur les changements de propriétés.", [
  S("Quelle propriété raccourcie regroupe tous les réglages de transition ?", "transition", ["animation", "transform", "@keyframes"]),
  S("Que définit « transition-duration » ?", "La durée de la transition", ["Le délai avant départ", "La propriété animée", "La courbe d'accélération"]),
  S("Quelle valeur de transition-property anime toutes les propriétés modifiables ?", "all", ["none", "auto", "every"]),
  M("Quelles valeurs sont des fonctions de minutage (timing-function) valides ?", ["ease", "linear", "ease-in-out"], ["fast", "smooth"]),
  T({ s: "Une transition se déclenche lorsqu'une propriété change de valeur (ex: au :hover).", v: true }),
  S("Que contrôle « transition-delay » ?", "Le temps d'attente avant le début de la transition", ["La vitesse finale", "Le nombre de répétitions", "La direction"]),
]);

// 13
Q("Les animations @keyframes (Avancé)", "Crée des animations multi-étapes avec keyframes.", [
  S("Quelle règle permet de définir les étapes d'une animation ?", "@keyframes", ["@animation", "@media", "@steps"]),
  S("Quelle propriété indique combien de fois l'animation se répète ?", "animation-iteration-count", ["animation-duration", "animation-delay", "animation-repeat"]),
  S("Quelle valeur fait jouer une animation indéfiniment ?", "infinite", ["loop", "always", "repeat"]),
  M("Quelles propriétés font partie du raccourci « animation » ?", ["animation-name", "animation-duration", "animation-timing-function"], ["animation-color", "animation-width"]),
  T({ s: "Dans @keyframes, les mots-clés « from » et « to » équivalent à 0% et 100%.", v: true }),
  S("Que fait « animation-fill-mode: forwards » ?", "Conserve l'état final après la fin de l'animation", ["Rejoue l'animation à l'envers", "Supprime l'animation", "Met l'animation en pause"]),
]);

// 14
Q("Les transformations 2D (Intermédiaire)", "translate, scale, rotate et skew.", [
  S("Quelle fonction de transform déplace un élément ?", "translate()", ["rotate()", "scale()", "skew()"]),
  S("Quelle fonction agrandit ou rétrécit un élément ?", "scale()", ["translate()", "rotate()", "blur()"]),
  S("Dans quelle unité s'exprime généralement l'angle de rotate() ?", "deg (degrés)", ["px", "%", "rem"]),
  M("Quelles sont des fonctions de transform valides ?", ["translate()", "rotate()", "skew()"], ["move()", "resize()"]),
  T({ s: "« transform-origin » définit le point autour duquel la transformation s'applique.", v: true }),
  S("Que fait « transform: scale(2) » ?", "Double la taille de l'élément", ["Le déplace de 2px", "Le tourne de 2 degrés", "Réduit de moitié"]),
]);

// 15
Q("Media queries et responsive (Intermédiaire)", "Adapte ton design à toutes les tailles d'écran.", [
  S("Quelle règle permet d'appliquer du CSS selon la taille de l'écran ?", "@media", ["@screen", "@responsive", "@query"]),
  S("Quelle condition cible les écrans d'au plus 600px de large ?", "max-width: 600px", ["min-width: 600px", "width: 600px", "size: 600px"]),
  T({ s: "L'approche « mobile-first » écrit d'abord les styles pour mobile puis ajoute des media queries pour les grands écrans.", v: true }),
  M("Quelles caractéristiques peut-on tester dans une media query ?", ["width", "orientation", "prefers-color-scheme"], ["font-name", "user-age"]),
  S("Que cible « @media (orientation: portrait) » ?", "Les écrans plus hauts que larges", ["Les écrans larges", "Les imprimantes", "Le mode sombre"]),
  S("En mobile-first, quelle requête ajoute des styles pour les grands écrans ?", "min-width", ["max-width", "max-height", "any-width"]),
]);

// 16
Q("Variables CSS (Intermédiaire)", "Définis et réutilise des valeurs avec les propriétés personnalisées.", [
  S("Comment déclare-t-on une variable CSS (propriété personnalisée) ?", "--ma-couleur: red;", ["$ma-couleur: red;", "var ma-couleur = red;", "@ma-couleur: red;"]),
  S("Quelle fonction permet d'utiliser une variable CSS ?", "var()", ["use()", "get()", "ref()"]),
  S("Quel sélecteur est idéal pour déclarer des variables globales ?", ":root", ["body uniquement", "*", "html.global"]),
  M("Quels avantages offrent les variables CSS ?", ["Réutilisation des valeurs", "Modification dynamique via JS", "Centralisation du thème"], ["Compilation plus rapide", "Réduction du poids des images"]),
  T({ s: "On peut fournir une valeur de repli avec var(--couleur, blue).", v: true }),
  S("Les variables CSS sont-elles héritées par les éléments enfants ?", "Oui, elles suivent la cascade et l'héritage", ["Non, jamais", "Seulement avec !important", "Seulement dans :root"]),
]);

// 17
Q("z-index et empilement (Avancé)", "Maîtrise l'ordre d'empilement des éléments.", [
  S("Que contrôle la propriété z-index ?", "L'ordre d'empilement (qui passe devant)", ["La transparence", "La largeur", "La rotation"]),
  S("Sur quel type d'éléments z-index a-t-il un effet (cas classique) ?", "Les éléments positionnés (non static)", ["Tous les éléments sans condition", "Uniquement les images", "Uniquement le body"]),
  T({ s: "Un z-index plus élevé place l'élément au-dessus des éléments à z-index plus faible.", v: true }),
  M("Quelles propriétés peuvent créer un nouveau contexte d'empilement ?", ["opacity inférieure à 1", "transform", "position fixed"], ["color", "font-size"]),
  S("Que se passe-t-il pour z-index sur un élément en « position: static » ?", "Il est ignoré", ["Il fonctionne normalement", "Il provoque une erreur", "Il devient négatif"]),
  S("Un enfant peut-il passer devant un élément situé hors de son contexte d'empilement parent ?", "Non, il reste contraint par le contexte de son parent", ["Oui, toujours", "Seulement avec !important", "Seulement en flex"]),
]);

// 18
Q("La propriété overflow (Intermédiaire)", "Gère le contenu qui dépasse de son conteneur.", [
  S("Quelle valeur d'overflow masque le contenu débordant sans barre de défilement ?", "hidden", ["scroll", "visible", "auto"]),
  S("Quelle est la valeur par défaut de overflow ?", "visible", ["hidden", "scroll", "clip"]),
  S("Quelle valeur affiche une barre de défilement seulement si nécessaire ?", "auto", ["scroll", "visible", "hidden"]),
  M("Quelles valeurs d'overflow sont valides ?", ["visible", "hidden", "scroll"], ["clipped", "rolling"]),
  T({ s: "« overflow: scroll » affiche les barres de défilement même si le contenu ne déborde pas.", v: true }),
  S("Comment gérer le débordement horizontal uniquement ?", "overflow-x", ["overflow-h", "overflow-row", "scroll-x"]),
]);

// 19
Q("Float et clear (Historique)", "Comprends l'ancienne technique de mise en page par flottement.", [
  S("Quelle propriété fait flotter un élément à gauche ?", "float: left", ["align: left", "position: left", "side: left"]),
  S("Quelle propriété empêche un élément de remonter à côté d'un élément flottant ?", "clear", ["float", "stop", "block"]),
  T({ s: "Un parent ne contenant que des éléments flottants peut s'effondrer (hauteur nulle).", v: true }),
  M("Quelles valeurs la propriété clear accepte-t-elle ?", ["left", "right", "both"], ["top", "center"]),
  S("Quelle technique historique force un parent à contenir ses flottants ?", "Le clearfix", ["Le z-index", "Le flexbox-fix", "Le margin auto"]),
  S("Aujourd'hui, quelle approche remplace avantageusement les float pour la mise en page ?", "Flexbox ou Grid", ["Les tableaux HTML", "position: absolute partout", "Les iframes"]),
]);

// 20
Q("Typographie CSS (Intermédiaire)", "font-family, font-weight, line-height et espacements.", [
  S("Quelle propriété définit la graisse (épaisseur) du texte ?", "font-weight", ["font-style", "font-size", "font-family"]),
  S("Quelle valeur de font-weight correspond au gras standard ?", "bold (ou 700)", ["italic", "400", "light"]),
  S("Quelle propriété contrôle l'interligne (hauteur de ligne) ?", "line-height", ["letter-spacing", "word-spacing", "text-indent"]),
  M("Quelles propriétés relèvent de la typographie ?", ["font-family", "letter-spacing", "line-height"], ["padding", "z-index"]),
  T({ s: "« font-family » accepte une liste de polices de repli séparées par des virgules.", v: true }),
  S("Que fait « letter-spacing » ?", "Modifie l'espace entre les lettres", ["L'espace entre les mots", "L'espace entre les lignes", "La taille de police"]),
]);
