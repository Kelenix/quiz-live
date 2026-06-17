// Part 2: formulaires (quizzes 6-10)
export const part2 = [
{
  title: "Les types d'input HTML5 et leur usage",
  description: "Tour d'horizon des principaux types de champs de saisie introduits avec HTML5.",
  questions: [
    { statement: "Quel type d'input HTML5 affiche un sélecteur de date natif dans la plupart des navigateurs modernes ?", type: "single", time_limit: 20, answers: [
      { text: "<input type=\"date\">", is_correct: true }, { text: "<input type=\"calendar\">", is_correct: false }, { text: "<input type=\"datetime\">", is_correct: false }, { text: "<input type=\"day\">", is_correct: false } ] },
    { statement: "Quel type d'input est le plus adapté pour saisir une adresse e-mail avec validation native du format ?", type: "single", time_limit: 20, answers: [
      { text: "type=\"text\"", is_correct: false }, { text: "type=\"email\"", is_correct: true }, { text: "type=\"mail\"", is_correct: false }, { text: "type=\"address\"", is_correct: false } ] },
    { statement: "Quel type d'input affiche un curseur (slider) pour choisir une valeur numérique dans une plage ?", type: "single", time_limit: 20, answers: [
      { text: "type=\"range\"", is_correct: true }, { text: "type=\"slider\"", is_correct: false }, { text: "type=\"scale\"", is_correct: false }, { text: "type=\"number\"", is_correct: false } ] },
    { statement: "Le type d'input \"number\" empêche totalement, y compris côté serveur, la soumission de valeurs non numériques.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Le type d'input \"password\" masque visuellement les caractères saisis à l'écran.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Parmi ces valeurs, lesquelles sont des types valides pour l'attribut type d'un <input> en HTML5 ?", type: "multiple", time_limit: 30, answers: [
      { text: "color", is_correct: true }, { text: "tel", is_correct: true }, { text: "search", is_correct: true }, { text: "paragraph", is_correct: false } ] },
    { statement: "Quel type d'input permet de proposer un sélecteur de couleur natif à l'utilisateur ?", type: "single", time_limit: 20, answers: [
      { text: "type=\"color\"", is_correct: true }, { text: "type=\"palette\"", is_correct: false }, { text: "type=\"rgb\"", is_correct: false }, { text: "type=\"hex\"", is_correct: false } ] },
    { statement: "Lesquels de ces types d'input déclenchent l'affichage d'un clavier virtuel adapté sur mobile ?", type: "multiple", time_limit: 30, answers: [
      { text: "tel", is_correct: true }, { text: "email", is_correct: true }, { text: "number", is_correct: true }, { text: "hidden", is_correct: false } ] }
  ]
},
{
  title: "Label, fieldset et legend : structurer un formulaire",
  description: "Les bonnes pratiques pour associer correctement les libellés aux champs et grouper les contrôles.",
  questions: [
    { statement: "Quel attribut de <label> doit correspondre à l'id d'un champ pour les associer explicitement ?", type: "single", time_limit: 20, answers: [
      { text: "for", is_correct: true }, { text: "name", is_correct: false }, { text: "target", is_correct: false }, { text: "link", is_correct: false } ] },
    { statement: "Quel élément permet de regrouper visuellement et sémantiquement plusieurs champs liés d'un formulaire ?", type: "single", time_limit: 20, answers: [
      { text: "<fieldset>", is_correct: true }, { text: "<group>", is_correct: false }, { text: "<formgroup>", is_correct: false }, { text: "<section>", is_correct: false } ] },
    { statement: "Quel élément, placé en premier enfant d'un <fieldset>, fournit un titre descriptif au groupe de champs ?", type: "single", time_limit: 20, answers: [
      { text: "<caption>", is_correct: false }, { text: "<legend>", is_correct: true }, { text: "<title>", is_correct: false }, { text: "<label>", is_correct: false } ] },
    { statement: "Associer un <label> à un champ de formulaire améliore l'accessibilité car les lecteurs d'écran annoncent le libellé lié.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Il est impossible d'imbriquer directement un <input> à l'intérieur d'un <label> ; il faut toujours utiliser l'attribut for.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces affirmations sur <fieldset> et <legend>, lesquelles sont correctes ?", type: "multiple", time_limit: 30, answers: [
      { text: "<fieldset> peut contenir plusieurs champs de types différents", is_correct: true }, { text: "<legend> améliore l'accessibilité d'un groupe de champs", is_correct: true }, { text: "L'attribut disabled sur <fieldset> désactive tous les champs qu'il contient", is_correct: true }, { text: "<legend> doit obligatoirement être placé en dernier enfant", is_correct: false } ] },
    { statement: "Cliquer sur le texte d'un <label> correctement associé à une case à cocher permet de cocher/décocher cette case.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Quel est l'avantage principal d'englober un <input type=\"checkbox\"> directement dans un <label> plutôt que d'utiliser uniquement l'attribut for ?", type: "single", time_limit: 20, answers: [
      { text: "Cela évite de devoir donner un id unique au champ", is_correct: true }, { text: "Cela rend le champ obligatoire automatiquement", is_correct: false }, { text: "Cela change le type du champ", is_correct: false }, { text: "Cela améliore les performances réseau", is_correct: false } ] }
  ]
},
{
  title: "Validation HTML5 native : required, pattern, min et max",
  description: "Exploitez les attributs de validation intégrés au navigateur pour fiabiliser la saisie utilisateur.",
  questions: [
    { statement: "Quel attribut booléen rend un champ de formulaire obligatoire avant soumission ?", type: "single", time_limit: 20, answers: [
      { text: "required", is_correct: true }, { text: "mandatory", is_correct: false }, { text: "needed", is_correct: false }, { text: "must", is_correct: false } ] },
    { statement: "Quel attribut permet de définir une expression régulière que la valeur d'un champ texte doit respecter ?", type: "single", time_limit: 20, answers: [
      { text: "pattern", is_correct: true }, { text: "regex", is_correct: false }, { text: "format", is_correct: false }, { text: "validate", is_correct: false } ] },
    { statement: "Sur un <input type=\"number\">, quels attributs permettent de limiter respectivement la valeur minimale et maximale acceptée ?", type: "single", time_limit: 20, answers: [
      { text: "min et max", is_correct: true }, { text: "low et high", is_correct: false }, { text: "start et end", is_correct: false }, { text: "floor et ceil", is_correct: false } ] },
    { statement: "La validation HTML5 native (required, pattern, etc.) dispense totalement de revalider les données côté serveur.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "L'attribut maxlength limite le nombre maximal de caractères qu'un utilisateur peut saisir dans un champ texte.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Parmi ces attributs, lesquels participent à la validation native des formulaires HTML5 ?", type: "multiple", time_limit: 30, answers: [
      { text: "required", is_correct: true }, { text: "pattern", is_correct: true }, { text: "minlength", is_correct: true }, { text: "colspan", is_correct: false } ] },
    { statement: "Quelle pseudo-classe CSS cible un champ de formulaire dont la valeur actuelle ne respecte pas les règles de validation ?", type: "single", time_limit: 20, answers: [
      { text: ":invalid", is_correct: true }, { text: ":error", is_correct: false }, { text: ":wrong", is_correct: false }, { text: ":bad-input", is_correct: false } ] },
    { statement: "Quelle méthode JavaScript native permet de vérifier la validité d'un formulaire avant un traitement personnalisé ?", type: "single", time_limit: 20, answers: [
      { text: "form.checkValidity()", is_correct: true }, { text: "form.isValid()", is_correct: false }, { text: "form.validate()", is_correct: false }, { text: "form.testInputs()", is_correct: false } ] }
  ]
},
{
  title: "Select, option et optgroup : les listes déroulantes",
  description: "Construire des listes de choix structurées et accessibles avec les éléments de formulaire dédiés.",
  questions: [
    { statement: "Quel élément HTML permet de créer une liste déroulante de choix ?", type: "single", time_limit: 20, answers: [
      { text: "<select>", is_correct: true }, { text: "<dropdown>", is_correct: false }, { text: "<list>", is_correct: false }, { text: "<choice>", is_correct: false } ] },
    { statement: "Quel attribut booléen sur <select> permet de sélectionner plusieurs options simultanément ?", type: "single", time_limit: 20, answers: [
      { text: "multiple", is_correct: true }, { text: "multi", is_correct: false }, { text: "many", is_correct: false }, { text: "checkbox", is_correct: false } ] },
    { statement: "Quel élément permet de regrouper visuellement plusieurs <option> sous un même libellé dans un <select> ?", type: "single", time_limit: 20, answers: [
      { text: "<optgroup>", is_correct: true }, { text: "<group>", is_correct: false }, { text: "<optlist>", is_correct: false }, { text: "<category>", is_correct: false } ] },
    { statement: "Un <option> sans attribut value utilise automatiquement son contenu textuel comme valeur soumise.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "L'élément <datalist> sert exclusivement à afficher des tableaux de données.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces affirmations sur <datalist>, lesquelles sont correctes ?", type: "multiple", time_limit: 30, answers: [
      { text: "Il propose des suggestions d'autocomplétion pour un champ <input>", is_correct: true }, { text: "Il est associé à un input via l'attribut list", is_correct: true }, { text: "Il contient des éléments <option>", is_correct: true }, { text: "Il remplace obligatoirement le <select>", is_correct: false } ] },
    { statement: "Quel attribut sur <option> permet de pré-sélectionner ce choix par défaut à l'affichage ?", type: "single", time_limit: 20, answers: [
      { text: "selected", is_correct: true }, { text: "default", is_correct: false }, { text: "checked", is_correct: false }, { text: "active", is_correct: false } ] },
    { statement: "L'attribut size sur un élément <select> permet d'afficher plusieurs options visibles simultanément sans dérouler la liste.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] }
  ]
},
{
  title: "Textarea, boutons et soumission de formulaire",
  description: "Les éléments de saisie longue et les contrôles permettant de déclencher l'envoi des données.",
  questions: [
    { statement: "Quel élément HTML permet de saisir un texte multi-lignes, comme un message ou un commentaire ?", type: "single", time_limit: 20, answers: [
      { text: "<textarea>", is_correct: true }, { text: "<input type=\"text\" multiline>", is_correct: false }, { text: "<text>", is_correct: false }, { text: "<longtext>", is_correct: false } ] },
    { statement: "Quelle est la valeur par défaut de l'attribut type d'un élément <button> placé dans un <form> ?", type: "single", time_limit: 20, answers: [
      { text: "submit", is_correct: true }, { text: "button", is_correct: false }, { text: "reset", is_correct: false }, { text: "click", is_correct: false } ] },
    { statement: "Quel attribut d'un <button> permet d'éviter qu'il ne déclenche la soumission du formulaire englobant ?", type: "single", time_limit: 20, answers: [
      { text: "type=\"button\"", is_correct: true }, { text: "novalidate", is_correct: false }, { text: "disabled", is_correct: false }, { text: "readonly", is_correct: false } ] },
    { statement: "Contrairement à <input>, l'élément <textarea> définit ses dimensions visibles via les attributs rows et cols plutôt que via son contenu textuel direct.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "L'attribut novalidate placé sur un <form> force la validation HTML5 native même si l'utilisateur clique sur un bouton de type reset.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces éléments, lesquels peuvent déclencher la soumission d'un formulaire HTML ?", type: "multiple", time_limit: 30, answers: [
      { text: "<button type=\"submit\">", is_correct: true }, { text: "<input type=\"submit\">", is_correct: true }, { text: "<input type=\"image\">", is_correct: true }, { text: "<input type=\"reset\">", is_correct: false } ] },
    { statement: "Quel attribut HTML d'un <form> définit l'URL vers laquelle les données seront envoyées lors de la soumission ?", type: "single", time_limit: 20, answers: [
      { text: "action", is_correct: true }, { text: "target", is_correct: false }, { text: "destination", is_correct: false }, { text: "url", is_correct: false } ] },
    { statement: "Quel attribut de <form> précise la méthode HTTP utilisée pour envoyer les données (par exemple GET ou POST) ?", type: "single", time_limit: 20, answers: [
      { text: "method", is_correct: true }, { text: "type", is_correct: false }, { text: "mode", is_correct: false }, { text: "protocol", is_correct: false } ] }
  ]
}
];
