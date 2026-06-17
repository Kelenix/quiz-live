// Part 4: tableaux + listes (quizzes 16-20)
export const part4 = [
{
  title: "Construire un tableau HTML : structure de base",
  description: "Les balises essentielles pour créer un tableau de données simple et bien structuré.",
  questions: [
    { statement: "Quelle balise délimite l'ensemble d'un tableau HTML ?", type: "single", time_limit: 20, answers: [
      { text: "<table>", is_correct: true }, { text: "<grid>", is_correct: false }, { text: "<tab>", is_correct: false }, { text: "<tdata>", is_correct: false } ] },
    { statement: "Quelle balise représente une ligne dans un tableau HTML ?", type: "single", time_limit: 20, answers: [
      { text: "<tr>", is_correct: true }, { text: "<row>", is_correct: false }, { text: "<line>", is_correct: false }, { text: "<td-row>", is_correct: false } ] },
    { statement: "Quelle balise représente une cellule d'en-tête dans un tableau, généralement affichée en gras et centrée par défaut ?", type: "single", time_limit: 20, answers: [
      { text: "<th>", is_correct: true }, { text: "<head>", is_correct: false }, { text: "<title>", is_correct: false }, { text: "<header>", is_correct: false } ] },
    { statement: "La balise <td> représente une cellule de donnée standard dans une ligne de tableau.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Il est obligatoire d'utiliser des tableaux HTML pour réaliser la mise en page générale d'un site web moderne.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces balises, lesquelles sont valides à l'intérieur d'un élément <table> ?", type: "multiple", time_limit: 30, answers: [
      { text: "<tr>", is_correct: true }, { text: "<caption>", is_correct: true }, { text: "<thead>", is_correct: true }, { text: "<li>", is_correct: false } ] },
    { statement: "Quelle balise fournit un titre ou une légende descriptive pour l'ensemble d'un tableau ?", type: "single", time_limit: 20, answers: [
      { text: "<caption>", is_correct: true }, { text: "<title>", is_correct: false }, { text: "<legend>", is_correct: false }, { text: "<th colspan>", is_correct: false } ] },
    { statement: "Lesquelles de ces affirmations sur les tableaux HTML sont correctes ?", type: "multiple", time_limit: 30, answers: [
      { text: "Chaque <tr> peut contenir plusieurs <td> ou <th>", is_correct: true }, { text: "<caption> doit être placé juste après la balise ouvrante <table>", is_correct: true }, { text: "Un tableau peut comporter un nombre de colonnes différent d'une ligne à l'autre grâce à colspan", is_correct: true }, { text: "<table> ne peut contenir aucun attribut", is_correct: false } ] }
  ]
},
{
  title: "thead, tbody, tfoot : organiser sémantiquement un tableau",
  description: "Structurer un tableau complexe en regroupant en-tête, corps et pied pour plus de clarté et d'accessibilité.",
  questions: [
    { statement: "Quel élément regroupe les lignes d'en-tête d'un tableau HTML ?", type: "single", time_limit: 20, answers: [
      { text: "<thead>", is_correct: true }, { text: "<theader>", is_correct: false }, { text: "<tophead>", is_correct: false }, { text: "<tr-head>", is_correct: false } ] },
    { statement: "Quel élément regroupe les lignes contenant les données principales d'un tableau ?", type: "single", time_limit: 20, answers: [
      { text: "<tbody>", is_correct: true }, { text: "<tcontent>", is_correct: false }, { text: "<tdata>", is_correct: false }, { text: "<tmain>", is_correct: false } ] },
    { statement: "Quel élément regroupe les lignes de pied de tableau, par exemple pour afficher des totaux ?", type: "single", time_limit: 20, answers: [
      { text: "<tfoot>", is_correct: true }, { text: "<tbottom>", is_correct: false }, { text: "<tend>", is_correct: false }, { text: "<tsummary>", is_correct: false } ] },
    { statement: "Un tableau HTML peut fonctionner correctement même sans utiliser <thead>, <tbody> ou <tfoot>, en plaçant les <tr> directement dans <table>.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "L'élément <tfoot> doit obligatoirement être positionné après <tbody> dans le code source HTML pour être valide.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces avantages, lesquels sont apportés par l'usage de thead/tbody/tfoot dans un tableau ?", type: "multiple", time_limit: 30, answers: [
      { text: "Une meilleure structuration sémantique pour les technologies d'assistance", is_correct: true }, { text: "La possibilité de cibler ces groupes facilement en CSS", is_correct: true }, { text: "Un en-tête qui peut rester visible lors de l'impression sur plusieurs pages", is_correct: true }, { text: "La suppression automatique des bordures du tableau", is_correct: false } ] },
    { statement: "Combien d'éléments <tbody> au maximum un tableau HTML peut-il contenir selon la spécification ?", type: "single", time_limit: 20, answers: [
      { text: "Plusieurs <tbody> sont autorisés dans un même tableau", is_correct: true }, { text: "Un seul <tbody> est autorisé", is_correct: false }, { text: "Aucun, <tbody> est déprécié", is_correct: false }, { text: "Exactement deux <tbody>", is_correct: false } ] },
    { statement: "<thead> ne peut contenir qu'une seule ligne <tr> au maximum.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] }
  ]
},
{
  title: "Fusionner des cellules avec colspan et rowspan",
  description: "Maîtriser la fusion de cellules horizontale et verticale dans un tableau HTML.",
  questions: [
    { statement: "Quel attribut HTML permet à une cellule de fusionner plusieurs colonnes horizontalement ?", type: "single", time_limit: 20, answers: [
      { text: "colspan", is_correct: true }, { text: "rowspan", is_correct: false }, { text: "merge", is_correct: false }, { text: "colwidth", is_correct: false } ] },
    { statement: "Quel attribut HTML permet à une cellule de fusionner plusieurs lignes verticalement ?", type: "single", time_limit: 20, answers: [
      { text: "rowspan", is_correct: true }, { text: "colspan", is_correct: false }, { text: "vmerge", is_correct: false }, { text: "rowheight", is_correct: false } ] },
    { statement: "Si une cellule possède colspan=\"3\", combien de colonnes occupe-t-elle visuellement dans le tableau ?", type: "single", time_limit: 20, answers: [
      { text: "3", is_correct: true }, { text: "1", is_correct: false }, { text: "2", is_correct: false }, { text: "Cela dépend du rowspan", is_correct: false } ] },
    { statement: "Lorsqu'une cellule utilise rowspan=\"2\", il faut généralement retirer une cellule correspondante dans la ligne suivante pour que l'alignement du tableau reste correct.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "colspan et rowspan ne peuvent jamais être utilisés simultanément sur la même cellule.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces éléments, sur lesquels les attributs colspan et rowspan peuvent-ils être appliqués ?", type: "multiple", time_limit: 30, answers: [
      { text: "<td>", is_correct: true }, { text: "<th>", is_correct: true }, { text: "<tr>", is_correct: false }, { text: "<table>", is_correct: false } ] },
    { statement: "Quelle est la valeur par défaut implicite de colspan et rowspan si ces attributs ne sont pas précisés sur une cellule ?", type: "single", time_limit: 20, answers: [
      { text: "1", is_correct: true }, { text: "0", is_correct: false }, { text: "auto", is_correct: false }, { text: "100%", is_correct: false } ] },
    { statement: "Un mauvais usage de colspan/rowspan peut désaligner visuellement les colonnes du reste du tableau.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] }
  ]
},
{
  title: "Listes ordonnées, non ordonnées et de définition",
  description: "Choisir la bonne structure de liste HTML selon la nature du contenu à présenter.",
  questions: [
    { statement: "Quelle balise crée une liste non ordonnée, généralement affichée avec des puces ?", type: "single", time_limit: 20, answers: [
      { text: "<ul>", is_correct: true }, { text: "<ol>", is_correct: false }, { text: "<list>", is_correct: false }, { text: "<dl>", is_correct: false } ] },
    { statement: "Quelle balise crée une liste ordonnée, généralement affichée avec une numérotation ?", type: "single", time_limit: 20, answers: [
      { text: "<ol>", is_correct: true }, { text: "<ul>", is_correct: false }, { text: "<orderlist>", is_correct: false }, { text: "<numlist>", is_correct: false } ] },
    { statement: "Quelle balise représente un élément individuel à l'intérieur d'une liste <ul> ou <ol> ?", type: "single", time_limit: 20, answers: [
      { text: "<li>", is_correct: true }, { text: "<item>", is_correct: false }, { text: "<elem>", is_correct: false }, { text: "<entry>", is_correct: false } ] },
    { statement: "La balise <dl> permet de créer une liste de définitions associant des termes à leurs descriptions.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "L'attribut start sur <ol> n'a aucun effet sur le numéro de départ de la numérotation.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces balises, lesquelles sont utilisées pour structurer une liste de définitions en HTML ?", type: "multiple", time_limit: 30, answers: [
      { text: "<dl>", is_correct: true }, { text: "<dt>", is_correct: true }, { text: "<dd>", is_correct: true }, { text: "<dh>", is_correct: false } ] },
    { statement: "Quel attribut de <ol> permet d'inverser l'ordre de numérotation, par exemple pour un compte à rebours ?", type: "single", time_limit: 20, answers: [
      { text: "reversed", is_correct: true }, { text: "invert", is_correct: false }, { text: "desc", is_correct: false }, { text: "countdown", is_correct: false } ] },
    { statement: "Il est possible d'imbriquer une liste <ul> entière à l'intérieur d'un élément <li> d'une autre liste.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] }
  ]
},
{
  title: "Listes imbriquées et bonnes pratiques de structuration",
  description: "Construire des menus et des structures de contenu complexes grâce aux listes imbriquées.",
  questions: [
    { statement: "Pour créer un sous-menu de navigation imbriqué dans un menu HTML, quelle structure est la plus appropriée sémantiquement ?", type: "single", time_limit: 20, answers: [
      { text: "Une liste <ul> imbriquée dans un <li> de la liste parente", is_correct: true }, { text: "Un nouveau <nav> complètement séparé", is_correct: false }, { text: "Un <table> imbriqué", is_correct: false }, { text: "Plusieurs <div> sans relation hiérarchique", is_correct: false } ] },
    { statement: "Dans une liste de définitions <dl>, peut-on associer plusieurs <dd> à un même <dt> ?", type: "single", time_limit: 20, answers: [
      { text: "Oui, un terme peut avoir plusieurs descriptions associées", is_correct: true }, { text: "Non, c'est strictement interdit", is_correct: false }, { text: "Seulement si on utilise l'attribut multiple", is_correct: false }, { text: "Seulement dans une liste imbriquée", is_correct: false } ] },
    { statement: "Utiliser des listes <ul>/<li> plutôt que des <div> empilés pour un menu de navigation améliore généralement l'accessibilité.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Un élément <li> doit obligatoirement être un enfant direct de <body> pour être valide en HTML.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces affirmations à propos des listes imbriquées en HTML, lesquelles sont vraies ?", type: "multiple", time_limit: 30, answers: [
      { text: "Une <ol> peut être imbriquée dans un <li> d'une <ul>", is_correct: true }, { text: "Les lecteurs d'écran annoncent généralement le niveau d'imbrication des listes", is_correct: true }, { text: "On peut combiner plusieurs niveaux de menus déroulants grâce à des listes imbriquées", is_correct: true }, { text: "Une liste imbriquée doit obligatoirement réutiliser le même type (ul ou ol) que sa liste parente", is_correct: false } ] },
    { statement: "Quel est l'intérêt principal d'utiliser des listes sémantiques plutôt que de simples paragraphes séparés par des <br> pour énumérer des éléments ?", type: "single", time_limit: 20, answers: [
      { text: "Cela communique clairement la structure énumérative du contenu aux navigateurs et technologies d'assistance", is_correct: true }, { text: "Cela réduit la taille du fichier CSS", is_correct: false }, { text: "Cela empêche tout style visuel personnalisé", is_correct: false }, { text: "Cela accélère le rendu graphique du processeur", is_correct: false } ] },
    { statement: "L'attribut type sur <ol> (par exemple type=\"i\") permet de changer le style de numérotation affiché (chiffres romains, lettres, etc.).", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] }
  ]
}
];
