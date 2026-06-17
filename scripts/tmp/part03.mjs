import { quiz, S, M, TF } from "./gen-js.mjs";

quiz(
  "Manipulation du DOM : sélection d'éléments",
  "Sélectionner des éléments HTML depuis JavaScript avec les API du DOM.",
  [
    S("Quelle méthode sélectionne le PREMIER élément correspondant à un sélecteur CSS donné ?", 0, ["document.querySelector()", "document.getElementsByClassName()", "document.querySelectorAll()", "document.selectFirst()"]),
    S("Quelle méthode retourne TOUS les éléments correspondant à un sélecteur CSS, sous forme de NodeList ?", 2, ["document.querySelector()", "document.getElementById()", "document.querySelectorAll()", "document.getAll()"]),
    S("Quelle méthode sélectionne un élément par son attribut `id` ?", 0, ["document.getElementById()", "document.getElementByClass()", "document.querySelectorId()", "document.findById()"]),
    TF("`document.querySelectorAll('.item')` retourne une véritable Array avec toutes ses méthodes natives comme map() directement.", false),
    TF("`document.getElementById` retourne `null` si aucun élément ne correspond à l'identifiant donné.", true),
    M("Quelles méthodes permettent de sélectionner des éléments du DOM ?", [0, 1, 2], [
      "querySelector",
      "querySelectorAll",
      "getElementsByTagName",
      "selectElementBy",
    ]),
    S("Que faut-il faire pour convertir une NodeList en véritable tableau JavaScript ?", 0, [
      "Utiliser Array.from(nodeList) ou [...nodeList]",
      "C'est automatique, NodeList est déjà un Array",
      "Utiliser nodeList.toArray()",
      "Ce n'est pas possible",
    ]),
    S("Quel sélecteur CSS utilisé dans `querySelector` cible un élément ayant la classe 'actif' ?", 1, ["'#actif'", "'.actif'", "'actif'", "'[actif]'"]),
  ]
);

quiz(
  "Manipulation du DOM : créer et modifier des éléments",
  "Créer dynamiquement des éléments et gérer leurs classes CSS via le DOM.",
  [
    S("Quelle méthode crée un nouvel élément HTML en JavaScript ?", 1, ["document.newElement()", "document.createElement()", "document.makeElement()", "document.addElement()"]),
    S("Quelle méthode insère un élément enfant à la fin d'un élément parent ?", 0, ["parent.appendChild(enfant)", "parent.addChild(enfant)", "parent.insert(enfant)", "parent.push(enfant)"]),
    S("Quelle propriété permet de définir le contenu textuel d'un élément sans interpréter de HTML ?", 1, ["innerHTML", "textContent", "outerHTML", "value"]),
    TF("`element.innerHTML = '<b>texte</b>'` interprète la chaîne comme du HTML et crée les balises correspondantes.", true),
    TF("`classList.toggle('actif')` ajoute la classe si elle est absente et la retire si elle est déjà présente.", true),
    M("Quelles méthodes de `classList` permettent de manipuler les classes CSS d'un élément ?", [0, 1, 2], [
      "add()",
      "remove()",
      "toggle()",
      "delete()",
    ]),
    S("Quelle méthode supprime définitivement un élément du DOM (sur l'élément lui-même, API moderne) ?", 0, ["element.remove()", "element.delete()", "element.destroy()", "element.clear()"]),
    S("Que fait `element.setAttribute('data-id', '42')` ?", 0, [
      "Ajoute ou met à jour l'attribut data-id avec la valeur '42'",
      "Supprime l'attribut data-id",
      "Lit la valeur actuelle de data-id",
      "Crée un nouvel élément avec cet attribut",
    ]),
  ]
);

quiz(
  "Gestion des événements DOM",
  "Écouter et réagir aux événements utilisateur avec addEventListener.",
  [
    S("Quelle méthode attache un gestionnaire d'événement à un élément sans écraser les gestionnaires existants ?", 0, ["element.addEventListener()", "element.onclick = fn", "element.setEvent()", "element.bindEvent()"]),
    S("Quelle méthode retire un gestionnaire d'événement précédemment ajouté ?", 1, ["element.deleteEventListener()", "element.removeEventListener()", "element.offEvent()", "element.clearListener()"]),
    S("Quelle méthode de l'objet événement empêche le comportement par défaut du navigateur (ex : soumission de formulaire) ?", 2, ["event.stop()", "event.cancel()", "event.preventDefault()", "event.block()"]),
    TF("La phase de 'bubbling' (propagation) fait remonter un événement de l'élément cible vers ses ancêtres dans le DOM.", true),
    TF("La phase de 'capturing' fait descendre l'événement depuis la racine du document vers l'élément cible, avant la phase de bubbling.", true),
    M("Quelles méthodes ou propriétés sont liées à la gestion d'événements DOM ?", [0, 1, 2], [
      "event.preventDefault()",
      "event.stopPropagation()",
      "event.target",
      "event.cancelBubbleNow()",
    ]),
    S("Que fait `event.stopPropagation()` ?", 0, [
      "Empêche l'événement de continuer sa propagation vers les autres éléments (bubbling/capturing)",
      "Empêche le comportement par défaut du navigateur",
      "Supprime l'écouteur d'événement",
      "Arrête toute exécution de JavaScript",
    ]),
    S("À quoi correspond `event.target` dans un gestionnaire d'événement ?", 0, [
      "L'élément exact sur lequel l'événement s'est produit",
      "L'élément sur lequel addEventListener a été appelé uniquement",
      "Toujours le document entier",
      "Le nom de l'événement sous forme de chaîne",
    ]),
  ]
);

quiz(
  "JSON : parse et stringify",
  "Sérialiser et désérialiser des données entre objets JavaScript et JSON.",
  [
    S("Quelle méthode convertit un objet JavaScript en chaîne JSON ?", 1, ["JSON.parse()", "JSON.stringify()", "JSON.toString()", "Object.toJSON()"]),
    S("Quelle méthode convertit une chaîne JSON en objet JavaScript ?", 0, ["JSON.parse()", "JSON.stringify()", "JSON.toObject()", "Object.parse()"]),
    S("Que retourne `JSON.stringify({a: 1, b: undefined})` ?", 2, ["'{\"a\":1,\"b\":undefined}'", "'{\"a\":1,\"b\":null}'", "'{\"a\":1}'", "Une erreur"]),
    TF("`JSON.parse('{invalide}')` lève une SyntaxError car la chaîne n'est pas un JSON valide.", true),
    TF("JSON.stringify peut sérialiser des fonctions et elles apparaissent dans le résultat sous forme de texte du code source.", false),
    M("Quelles valeurs JavaScript sont correctement sérialisées par JSON.stringify (incluses dans le résultat) ?", [0, 1, 2], [
      "Les chaînes de caractères",
      "Les nombres",
      "Les objets et tableaux imbriqués",
      "Les fonctions (incluses telles quelles)",
    ]),
    S("Quel est le second argument optionnel utile de `JSON.stringify(obj, null, 2)` ?", 0, [
      "Le nombre d'espaces utilisés pour l'indentation (mise en forme lisible)",
      "Le nombre maximal de propriétés à inclure",
      "La profondeur maximale de récursion",
      "Le séparateur entre les propriétés",
    ]),
    S("Que retourne `typeof JSON.parse('42')` ?", 0, ["'number'", "'string'", "'object'", "'undefined'"]),
  ]
);

quiz(
  "Classes en JavaScript : bases et héritage",
  "Définir des classes, des constructeurs et utiliser l'héritage avec extends.",
  [
    S("Quel mot-clé permet de définir une classe en JavaScript moderne (ES6+) ?", 0, ["class", "struct", "object", "type"]),
    S("Quelle méthode spéciale est appelée automatiquement lors de la création d'une instance avec `new` ?", 2, ["init()", "new()", "constructor()", "create()"]),
    S("Quel mot-clé permet à une classe d'hériter d'une autre classe ?", 1, ["implements", "extends", "inherits", "with"]),
    TF("Dans le constructeur d'une classe enfant, on doit appeler `super()` avant d'utiliser `this` si la classe hérite d'une classe parent.", true),
    TF("Les classes JavaScript introduisent un système de typage totalement différent du système basé sur les prototypes.", false),
    M("Quelles affirmations sur les classes JavaScript sont correctes ?", [0, 1, 2], [
      "Les classes sont en réalité du sucre syntaxique au-dessus des prototypes",
      "On peut définir des méthodes statiques avec le mot-clé static",
      "super() permet d'appeler le constructeur de la classe parente",
      "Les classes JavaScript ne supportent pas l'héritage multiple ni simple",
    ]),
    S("Que fait le mot-clé `static` devant une méthode de classe ?", 0, [
      "La méthode est appelée sur la classe elle-même, pas sur les instances",
      "La méthode devient privée",
      "La méthode ne peut plus être surchargée",
      "La méthode s'exécute une seule fois au chargement",
    ]),
    S("Comment appeler une méthode de la classe parente depuis une méthode surchargée dans la classe enfant ?", 0, ["super.methode()", "parent.methode()", "this.parent.methode()", "Class.super.methode()"]),
  ]
);

quiz(
  "Prototypes et chaîne de prototypes",
  "Le mécanisme d'héritage prototypal sous-jacent aux objets JavaScript.",
  [
    S("Quelle propriété interne relie un objet à son prototype en JavaScript ?", 1, ["__proto.type", "[[Prototype]] (accessible via __proto__ ou Object.getPrototypeOf)", "this.parent", "Object.parent"]),
    S("Quelle méthode permet de récupérer le prototype d'un objet de façon standard ?", 0, ["Object.getPrototypeOf(obj)", "obj.getPrototype()", "Prototype.of(obj)", "obj.parent()"]),
    S("Que se passe-t-il lorsqu'on accède à une propriété absente d'un objet mais présente dans son prototype ?", 1, [
      "Une erreur est levée immédiatement",
      "JavaScript la cherche en remontant la chaîne de prototypes et la retourne si trouvée",
      "undefined est retourné systématiquement sans recherche",
      "La propriété est automatiquement créée sur l'objet",
    ]),
    TF("Toutes les fonctions JavaScript classiques possèdent une propriété `prototype` utilisée lors de l'instanciation avec `new`.", true),
    TF("La chaîne de prototypes est infinie et ne se termine jamais par `null`.", false),
    M("Quelles affirmations sur les prototypes JavaScript sont correctes ?", [0, 1, 2], [
      "Les classes ES6 utilisent les prototypes en interne pour partager les méthodes entre instances",
      "Object.create(proto) crée un nouvel objet avec le prototype spécifié",
      "La chaîne de prototypes permet la réutilisation de méthodes sans dupliquer le code sur chaque instance",
      "Chaque objet possède sa propre copie indépendante de chaque méthode du prototype",
    ]),
    S("Que retourne `Object.getPrototypeOf({}) === Object.prototype` ?", 0, ["true", "false", "undefined", "Une erreur"]),
    S("Quelle méthode vérifie si un objet possède une propriété directement (sans remonter la chaîne de prototypes) ?", 0, ["Object.prototype.hasOwnProperty()", "in (l'opérateur seul)", "Object.contains()", "obj.hasProperty()"]),
  ]
);

quiz(
  "Gestion des erreurs : try/catch/finally",
  "Intercepter, traiter et propager les erreurs en JavaScript.",
  [
    S("Quel bloc permet de capturer une exception levée dans un bloc try ?", 1, ["finally", "catch", "throw", "error"]),
    S("Quel bloc s'exécute toujours, qu'une erreur ait été levée ou non ?", 2, ["try", "catch", "finally", "error"]),
    S("Quel mot-clé permet de déclencher manuellement une exception ?", 1, ["catch", "throw", "raise", "error"]),
    TF("On peut lancer (throw) n'importe quelle valeur en JavaScript, pas uniquement des instances d'Error.", true),
    TF("Si une erreur est levée dans le bloc finally, elle écrase silencieusement toute erreur précédente du bloc try.", false),
    M("Quelles affirmations sur la gestion d'erreurs en JavaScript sont correctes ?", [0, 1, 2], [
      "new Error('message') crée un objet Error avec une propriété message",
      "On peut créer des classes d'erreurs personnalisées en étendant Error",
      "Le bloc catch peut capturer une variable représentant l'erreur, ex: catch (e)",
      "Un bloc try doit obligatoirement être suivi d'un catch ET d'un finally ensemble",
    ]),
    S("Que retourne `error.message` pour `const error = new Error('Oups');` ?", 0, ["'Oups'", "'Error: Oups'", "undefined", "null"]),
    S("Quel est l'intérêt de créer une classe d'erreur personnalisée comme `class ValidationError extends Error {}` ?", 0, [
      "Permettre de distinguer différents types d'erreurs avec instanceof lors du traitement",
      "Accélérer l'exécution du programme",
      "Empêcher toute erreur de se propager",
      "Remplacer complètement try/catch",
    ]),
  ]
);

quiz(
  "Modules JavaScript : import/export",
  "Organiser le code en modules avec la syntaxe ES Modules.",
  [
    S("Quelle syntaxe exporte une fonction nommée depuis un module ES ?", 0, ["export function f() {}", "module.exports = f;", "exports.f = f;", "public function f() {}"]),
    S("Quelle syntaxe importe l'export par défaut d'un module ?", 1, ["import { defaut } from './module.js';", "import defaut from './module.js';", "import * from './module.js';", "require('./module.js').default;"]),
    S("Combien d'exports par défaut (`export default`) un module ES peut-il avoir au maximum ?", 0, ["1", "2", "Autant qu'on veut", "0, c'est interdit"]),
    TF("CommonJS (utilisé par Node.js historiquement) utilise `require()` et `module.exports`, tandis que ES Modules utilise `import`/`export`.", true),
    TF("Un module ES Modules est exécuté en mode non-strict par défaut.", false),
    M("Quelles syntaxes d'export sont valides en ES Modules ?", [0, 1, 2], [
      "export const x = 1;",
      "export default function() {}",
      "export { a, b };",
      "export.default = x;",
    ]),
    S("Quelle syntaxe permet d'importer toutes les exportations nommées d'un module sous un seul objet ?", 0, ["import * as monModule from './module.js';", "import all from './module.js';", "import { * } from './module.js';", "import monModule.* from './module.js';"]),
    S("Quel attribut HTML doit-on ajouter à une balise `<script>` pour utiliser la syntaxe ES Modules dans le navigateur ?", 0, ["type=\"module\"", "type=\"esm\"", "async", "defer-module"]),
  ]
);

quiz(
  "Fonctions d'ordre supérieur et callbacks",
  "Passer des fonctions en argument ou les retourner pour composer des comportements.",
  [
    S("Qu'est-ce qu'une fonction d'ordre supérieur (higher-order function) ?", 0, [
      "Une fonction qui prend une ou plusieurs fonctions en argument, ou qui retourne une fonction",
      "Une fonction qui s'exécute plus vite que les autres",
      "Une fonction définie au niveau global uniquement",
      "Une fonction qui ne peut être appelée qu'une fois",
    ]),
    S("Qu'est-ce qu'un callback en JavaScript ?", 1, [
      "Une fonction qui s'auto-exécute immédiatement",
      "Une fonction passée en argument à une autre fonction, pour être appelée plus tard",
      "Une méthode réservée aux tableaux",
      "Un type de boucle spécifique",
    ]),
    S("Laquelle de ces méthodes de tableau accepte un callback comme argument ?", 3, ["length", "push", "Array.isArray", "map"]),
    TF("setTimeout(callback, délai) utilise un callback pour exécuter du code après un délai donné.", true),
    TF("Un callback ne peut jamais recevoir de paramètres lorsqu'il est invoqué.", false),
    M("Quels sont des exemples typiques d'usage de fonctions d'ordre supérieur en JavaScript ?", [0, 1, 2], [
      "array.map(callback)",
      "array.sort(comparateur)",
      "Une fonction factory qui retourne une fonction configurée",
      "console.log('texte')",
    ]),
    S("Quel terme désigne le problème de callbacks imbriqués les uns dans les autres rendant le code difficile à lire ?", 0, ["Callback hell (l'enfer des callbacks)", "Callback loop", "Stack overflow", "Promise chaining"]),
    S("Quelle alternative moderne remplace souvent les callbacks pour gérer l'asynchrone de façon plus lisible ?", 0, ["Les Promises et async/await", "Les boucles for...of", "Les classes", "Le mot-clé var"]),
  ]
);
