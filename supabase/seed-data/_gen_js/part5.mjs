import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Sélection d'éléments du DOM",
    "Les méthodes pour récupérer des éléments dans le document HTML.",
    [
      S(
        "Quelle méthode sélectionne le premier élément correspondant à un sélecteur CSS donné ?",
        "document.querySelector()",
        ["document.getElementByClass()", "document.selectFirst()", "document.findElement()"]
      ),
      S(
        "Quelle méthode sélectionne un élément par son identifiant unique (id) ?",
        "document.getElementById()",
        ["document.getElementByName()", "document.querySelectorId()", "document.getById()"]
      ),
      TF("document.querySelectorAll() retourne une NodeList contenant tous les éléments correspondant au sélecteur.", true),
      M(
        "Quelles méthodes permettent de sélectionner plusieurs éléments à la fois ?",
        ["document.querySelectorAll()", "document.getElementsByClassName()"],
        ["document.getElementById()", "document.querySelector()"]
      ),
      TF("Une NodeList retournée par querySelectorAll() n'est pas un tableau mais peut être convertie avec Array.from().", true),
      S(
        "Quelle méthode permet de sélectionner des éléments par leur nom de balise (tag) ?",
        "document.getElementsByTagName()",
        ["document.getElementsByTag()", "document.selectByTag()", "document.queryTag()"]
      ),
    ]
  ),

  Quiz(
    "JS — Manipulation du DOM",
    "Modifier le contenu, les attributs et la structure du document.",
    [
      S(
        "Quelle propriété modifie le contenu HTML interne d'un élément ?",
        "innerHTML",
        ["outerText", "value uniquement", "src"]
      ),
      S(
        "Quelle méthode crée un nouvel élément HTML en mémoire ?",
        "document.createElement()",
        ["document.newElement()", "document.makeElement()", "document.buildElement()"]
      ),
      TF("appendChild() ajoute un nœud comme dernier enfant d'un élément parent.", true),
      M(
        "Quelles méthodes permettent de modifier la structure du DOM ?",
        ["appendChild()", "removeChild()", "insertBefore()"],
        ["getComputedStyle()"]
      ),
      TF("textContent insère du texte brut sans interpréter le HTML, contrairement à innerHTML.", true),
      S(
        "Quelle méthode moderne permet de supprimer un élément directement sans passer par son parent ?",
        "element.remove()",
        ["element.delete()", "element.destroy()", "element.clear()"]
      ),
    ]
  ),

  Quiz(
    "JS — Attributs et classes CSS via le DOM",
    "Lire et modifier les attributs HTML et les classes CSS en JavaScript.",
    [
      S(
        "Quelle méthode permet de lire la valeur d'un attribut HTML quelconque ?",
        "element.getAttribute('nom')",
        ["element.attr('nom')", "element.readAttribute('nom')", "element.value('nom')"]
      ),
      S(
        "Quelle propriété donne accès à un objet permettant d'ajouter/retirer des classes CSS facilement ?",
        "element.classList",
        ["element.className uniquement", "element.styleList", "element.cssClasses"]
      ),
      TF("classList.toggle('actif') ajoute la classe 'actif' si elle est absente, et la retire si elle est présente.", true),
      M(
        "Quelles méthodes sont disponibles sur classList ?",
        ["add()", "remove()", "contains()"],
        ["delete()"]
      ),
      TF("setAttribute() permet de définir ou modifier la valeur d'un attribut HTML.", true),
      S(
        "Comment vérifier si un élément possède une classe CSS donnée ?",
        "element.classList.contains('nomClasse')",
        ["element.hasClass('nomClasse')", "element.className.includes()", "element.css('nomClasse')"]
      ),
    ]
  ),

  Quiz(
    "JS — Gestion des événements",
    "Écouter et réagir aux événements utilisateurs avec addEventListener.",
    [
      S(
        "Quelle méthode permet d'attacher un gestionnaire d'événement à un élément ?",
        "element.addEventListener('click', callback)",
        ["element.onEvent('click', callback)", "element.bind('click', callback)", "element.listen('click', callback)"]
      ),
      S(
        "Quelle méthode permet de retirer un gestionnaire d'événement précédemment attaché ?",
        "element.removeEventListener()",
        ["element.detachEvent()", "element.unbind()", "element.stopListening()"]
      ),
      TF("Plusieurs gestionnaires peuvent être attachés au même événement sur le même élément avec addEventListener.", true),
      M(
        "Quelles méthodes de l'objet event permettent de contrôler la propagation ?",
        ["stopPropagation()", "preventDefault()"],
        ["stopElement()", "cancelBubble() comme méthode standard moderne"]
      ),
      TF("preventDefault() empêche le comportement par défaut du navigateur associé à un événement (par exemple suivre un lien).", true),
      S(
        "Quelle propriété de l'objet event identifie l'élément qui a déclenché l'événement ?",
        "event.target",
        ["event.source", "event.origin", "event.element"]
      ),
    ]
  ),

  Quiz(
    "JS — Propagation et délégation d'événements",
    "Comprendre le bubbling, le capturing et la délégation d'événements.",
    [
      S(
        "Qu'est-ce que la délégation d'événements ?",
        "Attacher un seul gestionnaire sur un élément parent pour gérer les événements de ses enfants via la propagation",
        ["Créer un événement personnalisé pour chaque enfant", "Désactiver tous les événements d'un parent", "Une technique obsolète sans usage actuel"]
      ),
      TF("Par défaut, les événements DOM se propagent de l'élément cible vers ses parents (bubbling).", true),
      S(
        "Quel avantage offre la délégation d'événements sur une longue liste d'éléments générés dynamiquement ?",
        "Elle évite d'attacher un écouteur à chaque élément et fonctionne aussi pour les éléments ajoutés plus tard",
        ["Elle empêche tout événement de se déclencher", "Elle ralentit systématiquement l'application", "Elle nécessite de réattacher les écouteurs à chaque ajout d'élément"]
      ),
      M(
        "Quelles affirmations sur la phase de capture (capturing) sont vraies ?",
        ["Elle se produit avant la phase de bubbling, du document vers la cible", "On peut l'activer en passant true (ou {capture: true}) comme troisième argument à addEventListener"],
        ["Elle remplace totalement le bubbling", "Elle n'existe pas en JavaScript"]
      ),
      TF("event.currentTarget référence l'élément sur lequel le gestionnaire est attaché, alors que event.target référence l'élément réellement cliqué.", true),
      S(
        "Dans un cas de délégation, comment identifier précisément quel enfant a déclenché le clic depuis le gestionnaire posé sur le parent ?",
        "En inspectant event.target (et souvent closest() pour remonter au bon élément)",
        ["En utilisant uniquement event.currentTarget", "C'est impossible à déterminer", "En comptant les enfants manuellement à chaque clic"]
      ),
    ]
  ),

  Quiz(
    "JS — Modules ES (import/export)",
    "Organiser le code en modules réutilisables avec la syntaxe ES6.",
    [
      S(
        "Quel mot-clé permet d'exposer une variable ou fonction depuis un module pour qu'elle soit utilisable ailleurs ?",
        "export",
        ["expose", "public", "share"]
      ),
      S(
        "Quel mot-clé permet d'utiliser dans un fichier une valeur exportée par un autre module ?",
        "import",
        ["require uniquement en ESM", "include", "use"]
      ),
      TF("Un module peut avoir un export par défaut (export default) en plus de plusieurs exports nommés.", true),
      M(
        "Quelles syntaxes d'import sont valides avec les modules ES ?",
        ["import { fonction } from './module.js';", "import fonctionParDefaut from './module.js';"],
        ["import './module.js' as fonction;", "require('./module.js').fonction;"]
      ),
      TF("Les modules ES sont exécutés en mode strict automatiquement.", true),
      S(
        "Quelle syntaxe importe toutes les exportations nommées d'un module sous un seul objet ?",
        "import * as module from './module.js';",
        ["import all from './module.js';", "import { * } from './module.js';", "import module.* from './module.js';"]
      ),
    ]
  ),

  Quiz(
    "JS — Expressions régulières",
    "Créer et utiliser des regex pour rechercher et valider des motifs dans des chaînes.",
    [
      S(
        "Quelle syntaxe crée une expression régulière littérale en JavaScript ?",
        "/motif/flags",
        ["regex(motif, flags)", "\"motif\"/g", "Pattern(motif)"]
      ),
      S(
        "Quelle méthode de chaîne teste si une regex correspond et retourne un booléen ?",
        "regex.test(chaine)",
        ["chaine.test(regex)", "regex.match(chaine) retournant un booléen", "chaine.regex(motif)"]
      ),
      TF("Le flag 'g' (global) permet de trouver toutes les correspondances dans une chaîne, pas seulement la première.", true),
      M(
        "Quelles méthodes permettent d'utiliser une regex avec une chaîne ?",
        ["chaine.match(regex)", "chaine.replace(regex, remplacement)"],
        ["chaine.regexTest()", "regex.parse(chaine)"]
      ),
      TF("Le flag 'i' rend la recherche insensible à la casse.", true),
      S(
        "Quelle méthode retourne un tableau de toutes les correspondances avec leurs groupes capturés, sous forme d'itérateur ?",
        "chaine.matchAll(regex)",
        ["chaine.findAll(regex)", "regex.allMatches(chaine)", "chaine.search(regex, all=true)"]
      ),
    ]
  ),

  Quiz(
    "JS — localStorage et sessionStorage",
    "Stocker des données côté client dans le navigateur.",
    [
      S(
        "Quelle est la différence principale entre localStorage et sessionStorage ?",
        "localStorage persiste après la fermeture du navigateur, sessionStorage est effacé à la fermeture de l'onglet/session",
        ["Aucune différence fonctionnelle", "sessionStorage est plus grand en capacité", "localStorage est envoyé automatiquement au serveur"]
      ),
      S(
        "Quel type de données peut-on stocker directement dans localStorage ?",
        "Des chaînes de caractères uniquement (il faut sérialiser les objets avec JSON.stringify)",
        ["N'importe quel objet JavaScript directement sans conversion", "Uniquement des nombres", "Des fonctions exécutables"]
      ),
      TF("localStorage.setItem('cle', 'valeur') stocke une paire clé-valeur de façon persistante.", true),
      M(
        "Quelles méthodes sont disponibles sur l'API localStorage ?",
        ["setItem()", "getItem()", "removeItem()"],
        ["push()"]
      ),
      TF("Les données stockées dans localStorage sont accessibles uniquement par des pages de la même origine (même protocole, domaine et port).", true),
      S(
        "Comment stocker un objet JavaScript complexe dans localStorage ?",
        "En le convertissant en chaîne avec JSON.stringify() avant stockage, puis JSON.parse() à la lecture",
        ["En le stockant directement sans conversion", "Ce n'est pas possible du tout", "En utilisant Object.toStorage()"]
      ),
    ]
  ),

  Quiz(
    "JS — Boucles for, for...of, for...in",
    "Les différentes formes de boucles disponibles pour parcourir des structures.",
    [
      S(
        "Quelle boucle est conçue pour parcourir les valeurs d'un objet itérable comme un tableau ?",
        "for...of",
        ["for...in", "while uniquement", "do...of"]
      ),
      S(
        "Quelle boucle est conçue pour parcourir les clés énumérables d'un objet ?",
        "for...in",
        ["for...of", "forEach uniquement", "repeat...in"]
      ),
      TF("for...in peut aussi parcourir les indices d'un tableau, mais ce n'est généralement pas recommandé pour les tableaux.", true),
      M(
        "Quelles structures sont directement itérables avec for...of ?",
        ["Les tableaux (Array)", "Les chaînes de caractères (String)", "Les Map et Set"],
        ["Les objets littéraux classiques sans Symbol.iterator"]
      ),
      TF("La boucle classique for (let i = 0; i < n; i++) permet un contrôle précis de l'index et du pas d'itération.", true),
      S(
        "Pourquoi préfère-t-on souvent for...of à for...in pour parcourir un tableau ?",
        "Parce que for...of itère sur les valeurs directement et ignore les propriétés héritées/énumérables non désirées",
        ["Parce que for...in est plus rapide dans tous les cas", "Parce que for...of ne fonctionne pas sur les tableaux", "Il n'y a aucune raison, ils sont identiques"]
      ),
    ]
  ),

  Quiz(
    "JS — Boucle while et do...while",
    "Les boucles conditionnelles while et do...while.",
    [
      S(
        "Quelle est la différence entre while et do...while ?",
        "do...while exécute le bloc au moins une fois avant de vérifier la condition, while vérifie la condition avant",
        ["Aucune différence", "while exécute toujours deux fois", "do...while ne vérifie jamais de condition"]
      ),
      TF("Une boucle while(true) sans instruction break crée une boucle infinie.", true),
      S(
        "Quel mot-clé permet de sortir immédiatement d'une boucle ?",
        "break",
        ["exit", "stop", "return uniquement"]
      ),
      M(
        "Quels mots-clés permettent de contrôler le flux à l'intérieur d'une boucle ?",
        ["break", "continue"],
        ["pause", "skip"]
      ),
      TF("continue passe directement à l'itération suivante sans exécuter le reste du code de l'itération courante.", true),
      S(
        "Quelle syntaxe correspond à une boucle do...while correcte ?",
        "do { /* code */ } while (condition);",
        ["do (condition) { /* code */ }", "while { /* code */ } do (condition);", "do { /* code */ } until (condition);"]
      ),
    ]
  ),

  Quiz(
    "JS — Objet Date (notions de base)",
    "Manipuler les dates et heures avec l'objet Date natif.",
    [
      S(
        "Quelle expression crée un objet Date représentant le moment actuel ?",
        "new Date()",
        ["Date.now() (qui retourne un objet Date)", "Date.current()", "new Date.today()"]
      ),
      S(
        "Que retourne Date.now() ?",
        "Le nombre de millisecondes écoulées depuis le 1er janvier 1970 (timestamp Unix en ms)",
        ["Un objet Date complet", "Une chaîne de date formatée", "Le nombre de secondes depuis 1970"]
      ),
      TF("Les mois dans l'objet Date sont indexés à partir de 0 (janvier = 0, décembre = 11).", true),
      M(
        "Quelles méthodes permettent d'extraire des informations d'un objet Date ?",
        ["getFullYear()", "getMonth()", "getDate()"],
        ["getCentury()"]
      ),
      TF("On peut comparer deux dates avec les opérateurs <, > car elles sont converties en timestamp numérique.", true),
      S(
        "Quelle méthode convertit un objet Date en chaîne au format ISO 8601 ?",
        "toISOString()",
        ["toLocalString() uniquement", "toJSONDate()", "format('ISO')"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux typés (notions de base)",
    "Les TypedArray pour manipuler des données binaires de façon performante.",
    [
      S(
        "Qu'est-ce qu'un tableau typé (TypedArray) comme Int32Array ou Float64Array ?",
        "Un tableau dont tous les éléments sont d'un type numérique fixe et de taille fixe en mémoire",
        ["Un tableau classique avec des annotations de type TypeScript", "Un tableau qui ne peut contenir que des chaînes", "Un synonyme d'Array classique"]
      ),
      TF("Les tableaux typés sont construits au-dessus d'un ArrayBuffer représentant un bloc de mémoire brut.", true),
      S(
        "Pourquoi utiliser des tableaux typés plutôt que des tableaux classiques pour du traitement de données binaires ?",
        "Pour de meilleures performances et un contrôle précis de la taille mémoire utilisée",
        ["Parce que les tableaux classiques ne supportent pas les nombres", "Parce que c'est obligatoire pour utiliser des boucles for", "Parce qu'ils sont plus simples à écrire"]
      ),
      M(
        "Quels exemples sont des types de TypedArray valides en JavaScript ?",
        ["Uint8Array", "Float32Array", "Int16Array"],
        ["StringArray"]
      ),
      TF("La taille d'un tableau typé est fixe après sa création, contrairement à un Array classique.", true),
      S(
        "Quel objet bas niveau représente le bloc de mémoire brut sur lequel s'appuient les tableaux typés ?",
        "ArrayBuffer",
        ["MemoryBlock", "RawData", "BufferArray"]
      ),
    ]
  ),
];
