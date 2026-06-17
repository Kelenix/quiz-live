import { quiz, S, M, TF } from "./gen-js.mjs";

quiz(
  "Valeurs truthy et falsy",
  "Identifier quelles valeurs sont évaluées comme vraies ou fausses dans un contexte booléen.",
  [
    S("Laquelle de ces valeurs est falsy en JavaScript ?", 1, ["'0' (chaîne contenant le caractère 0)", "0 (le nombre zéro)", "[] (tableau vide)", "{} (objet vide)"]),
    S("Que retourne `Boolean([])` (tableau vide) ?", 0, ["true", "false", "undefined", "NaN"]),
    S("Combien existe-t-il de valeurs falsy primitives bien connues en JavaScript (false, 0, '', null, undefined, NaN) ?", 2, ["4", "5", "6", "7"]),
    TF("`Boolean('0')` (chaîne contenant le caractère zéro) retourne `true` car c'est une chaîne non vide.", true),
    TF("Les objets et tableaux, même vides, sont toujours truthy en JavaScript.", true),
    M("Lesquelles de ces valeurs sont falsy en JavaScript ?", [0, 1, 2], [
      "NaN",
      "''",
      "null",
      "'false' (chaîne de caractères)",
    ]),
    S("Que produit `if (undefined) { console.log('A'); } else { console.log('B'); }` ?", 1, ["A", "B", "Une erreur", "Rien ne s'affiche"]),
    S("Que retourne `!!'texte'` (double négation) ?", 0, ["true", "false", "'texte'", "undefined"]),
  ]
);

quiz(
  "Méthodes des chaînes de caractères",
  "Manipuler, transformer et rechercher dans des chaînes de caractères.",
  [
    S("Quelle méthode retourne une nouvelle chaîne en majuscules ?", 1, ["toLower()", "toUpperCase()", "capitalize()", "upper()"]),
    S("Que retourne `'  bonjour  '.trim()` ?", 0, ["'bonjour'", "'  bonjour  '", "'bonjour  '", "undefined"]),
    S("Quelle méthode découpe une chaîne en tableau selon un séparateur ?", 2, ["join()", "concat()", "split()", "slice()"]),
    TF("`'JavaScript'.includes('Script')` retourne `true`.", true),
    TF("Les chaînes de caractères en JavaScript sont mutables : on peut modifier un caractère via son index comme `str[0] = 'X'`.", false),
    M("Quelles méthodes permettent de rechercher une sous-chaîne dans une chaîne ?", [0, 1, 2], [
      "includes()",
      "indexOf()",
      "startsWith()",
      "toArray()",
    ]),
    S("Que retourne `'Bonjour'.slice(0, 3)` ?", 0, ["'Bon'", "'jour'", "'Bonjour'", "'B'"]),
    S("Que retourne `'a,b,c'.split(',').join('-')` ?", 0, ["'a-b-c'", "'a,b,c'", "['a','b','c']", "'abc'"]),
  ]
);

quiz(
  "L'objet Math",
  "Utiliser les fonctions et constantes mathématiques natives de JavaScript.",
  [
    S("Quelle méthode retourne un nombre aléatoire entre 0 (inclus) et 1 (exclu) ?", 1, ["Math.rand()", "Math.random()", "Math.aleatoire()", "Random.next()"]),
    S("Quelle méthode arrondit un nombre à l'entier le plus proche ?", 0, ["Math.round()", "Math.ceil()", "Math.floor()", "Math.trunc()"]),
    S("Que retourne `Math.floor(4.9)` ?", 1, ["5", "4", "4.9", "0"]),
    TF("`Math.ceil(4.1)` retourne `5`.", true),
    TF("`Math.abs(-7)` retourne `-7`.", false),
    M("Quelles méthodes de l'objet Math existent réellement en JavaScript ?", [0, 1, 2], [
      "Math.max()",
      "Math.min()",
      "Math.pow()",
      "Math.average()",
    ]),
    S("Que retourne `Math.pow(2, 3)` ?", 1, ["6", "8", "9", "5"]),
    S("Comment générer un entier aléatoire entre 0 et 9 inclus avec Math ?", 0, [
      "Math.floor(Math.random() * 10)",
      "Math.random(10)",
      "Math.round(Math.random())",
      "Math.floor(10)",
    ]),
  ]
);

quiz(
  "L'objet Date",
  "Créer, lire et manipuler des dates en JavaScript.",
  [
    S("Comment créer un objet représentant la date et l'heure actuelles ?", 0, ["new Date()", "Date.now() retourne un objet Date", "new Date.create()", "Date.today()"]),
    S("Quelle méthode retourne le timestamp actuel en millisecondes depuis le 1er janvier 1970 ?", 1, ["new Date()", "Date.now()", "Date.getTime()", "Date.timestamp()"]),
    S("Quelle méthode d'une instance Date retourne le numéro du mois (0 pour janvier) ?", 2, ["getDay()", "getYear()", "getMonth()", "getDate()"]),
    TF("`getMonth()` retourne une valeur entre 0 et 11, où 0 représente janvier.", true),
    TF("`getDay()` retourne le numéro du jour dans le mois (1 à 31).", false),
    M("Quelles méthodes existent sur une instance de Date ?", [0, 1, 2], [
      "getFullYear()",
      "getHours()",
      "getDay()",
      "getWeek()",
    ]),
    S("Que retourne `new Date(2024, 0, 15).getFullYear()` ?", 0, ["2024", "0", "15", "2025"]),
    S("Quelle méthode statique permet d'obtenir le timestamp actuel sans créer d'instance Date ?", 0, ["Date.now()", "Date.getTime()", "Date.current()", "new Date.now()"]),
  ]
);

quiz(
  "Expressions régulières en JavaScript",
  "Les bases de la syntaxe et de l'utilisation des regex pour valider ou extraire du texte.",
  [
    S("Quelle syntaxe crée une expression régulière littérale en JavaScript ?", 1, ["new RegExp.create('abc')", "/abc/", "'abc'.regex()", "Regex('abc')"]),
    S("Quelle méthode d'une chaîne teste si elle correspond globalement à un pattern et retourne un booléen via la regex ?", 2, ["str.match(regex)", "str.search(regex)", "regex.test(str)", "regex.match(str)"]),
    S("Que signifie le flag `g` ajouté à une regex comme `/abc/g` ?", 0, [
      "Recherche globale : trouve toutes les occurrences, pas seulement la première",
      "Ignore la casse (majuscules/minuscules)",
      "Active le mode multi-lignes",
      "Rend la regex gourmande (greedy) uniquement",
    ]),
    TF("Le flag `i` dans une regex comme `/abc/i` rend la recherche insensible à la casse.", true),
    TF("`/^\\d+$/.test('12345')` retourne `false` car la chaîne contient des chiffres.", false),
    M("Quelles méthodes JavaScript permettent d'utiliser des expressions régulières ?", [0, 1, 2], [
      "String.prototype.replace()",
      "String.prototype.match()",
      "RegExp.prototype.test()",
      "Array.prototype.regex()",
    ]),
    S("Que retourne `'2024-01-15'.match(/\\d{4}/)[0]` ?", 0, ["'2024'", "'01'", "'15'", "null"]),
    S("Quel symbole regex représente 'un ou plusieurs' du caractère précédent ?", 0, ["+", "*", "?", "."]),
  ]
);

quiz(
  "Map et Set",
  "Les structures de données Map (clé-valeur) et Set (valeurs uniques) introduites en ES6.",
  [
    S("Quelle structure permet de stocker des paires clé-valeur où les clés peuvent être de n'importe quel type ?", 0, ["Map", "Object uniquement", "Array", "Set"]),
    S("Quelle structure garantit que chaque valeur qu'elle contient est unique (pas de doublons) ?", 2, ["Map", "Array", "Set", "Object"]),
    S("Quelle méthode ajoute une paire clé-valeur à une Map ?", 0, ["map.set(cle, valeur)", "map.add(cle, valeur)", "map.put(cle, valeur)", "map.push(cle, valeur)"]),
    TF("Contrairement aux clés d'objet classique qui sont converties en chaînes, les clés d'une Map peuvent être des objets, des fonctions ou tout autre type sans conversion.", true),
    TF("Un Set peut contenir des doublons si on les ajoute avec `.add()` plusieurs fois.", false),
    M("Quelles méthodes existent sur une instance de Set ?", [0, 1, 2], [
      "add()",
      "has()",
      "delete()",
      "push()",
    ]),
    S("Que retourne `new Set([1, 2, 2, 3, 3, 3]).size` ?", 0, ["3", "6", "1", "undefined"]),
    S("Quelle propriété (et non méthode) retourne le nombre d'éléments d'une Map ou d'un Set ?", 0, ["size", "length", "count", "total"]),
  ]
);

quiz(
  "Générateurs et itérateurs",
  "Créer des séquences paresseuses avec function* et le mot-clé yield.",
  [
    S("Quel symbole indique qu'une fonction est un générateur ?", 1, ["function& nom() {}", "function* nom() {}", "function! nom() {}", "generator function nom() {}"]),
    S("Quel mot-clé met en pause l'exécution d'un générateur et retourne une valeur ?", 0, ["yield", "return", "pause", "await"]),
    S("Que retourne l'appel d'une fonction génératrice (sans encore itérer) ?", 1, [
      "La première valeur générée directement",
      "Un objet itérateur (Generator)",
      "undefined",
      "Un tableau de toutes les valeurs",
    ]),
    TF("On peut parcourir un générateur avec une boucle for...of car il implémente le protocole itérable.", true),
    TF("Un générateur, une fois entièrement consommé (terminé), peut être réinitialisé et relancé depuis le début avec la même instance.", false),
    M("Quelles affirmations sur les générateurs sont correctes ?", [0, 1, 2], [
      "Chaque appel à .next() reprend l'exécution jusqu'au prochain yield",
      "Les générateurs permettent de créer des séquences potentiellement infinies de façon paresseuse",
      "L'objet retourné par .next() a la forme { value, done }",
      "Un générateur exécute tout son code immédiatement lors de son appel, sans pause possible",
    ]),
    S("Que vaut `done` dans l'objet retourné par `.next()` quand le générateur a fini de produire toutes ses valeurs ?", 0, ["true", "false", "undefined", "null"]),
    S("Quel protocole un objet doit-il implémenter (méthode Symbol.iterator) pour être utilisable dans une boucle for...of ?", 0, ["Le protocole itérable", "Le protocole comparable", "Le protocole sérialisable", "Le protocole observable"]),
  ]
);

quiz(
  "Mode strict ('use strict')",
  "Activer un comportement plus rigoureux et sécurisé de l'interpréteur JavaScript.",
  [
    S("Quelle directive active le mode strict en haut d'un fichier ou d'une fonction ?", 0, ["'use strict';", "#strict", "strict mode on;", "@strict"]),
    S("Que se passe-t-il en mode strict si on assigne une valeur à une variable non déclarée ?", 1, [
      "La variable est créée silencieusement en global comme en mode normal",
      "Une ReferenceError est levée",
      "Rien, l'instruction est ignorée",
      "Un avertissement console est affiché, sans erreur",
    ]),
    S("Les modules ES (import/export) sont-ils automatiquement en mode strict ?", 0, ["Oui, toujours", "Non, jamais", "Seulement si on l'active explicitement", "Seulement côté serveur Node.js"]),
    TF("En mode strict, `this` vaut `undefined` dans une fonction normale appelée sans contexte d'objet, au lieu de référencer l'objet global.", true),
    TF("Le mode strict autorise la duplication de noms de paramètres dans une fonction, contrairement au mode normal.", false),
    M("Quels comportements changent en mode strict par rapport au mode non strict ?", [0, 1, 2], [
      "Les affectations à des variables non déclarées lèvent une erreur",
      "this vaut undefined dans une fonction simple appelée sans contexte",
      "Certains mots réservés futurs deviennent interdits comme identifiants",
      "Les boucles for s'exécutent deux fois plus vite",
    ]),
    S("Les classes JavaScript (déclarées avec `class`) sont-elles exécutées en mode strict par défaut ?", 0, ["Oui, automatiquement", "Non, jamais", "Seulement si extends est utilisé", "Seulement en Node.js"]),
    S("Pourquoi recommande-t-on souvent le mode strict dans du code JavaScript moderne ?", 0, [
      "Il aide à détecter des erreurs silencieuses plus tôt et évite certains pièges du langage",
      "Il rend le code deux fois plus rapide à coup sûr",
      "Il est obligatoire pour utiliser les Promises",
      "Il désactive complètement les exceptions",
    ]),
  ]
);

quiz(
  "IIFE : fonctions immédiatement invoquées",
  "Encapsuler du code dans une fonction exécutée immédiatement après sa définition.",
  [
    S("Que signifie l'acronyme IIFE ?", 0, [
      "Immediately Invoked Function Expression",
      "Internal Inline Function Execution",
      "Independent Isolated Function Element",
      "Iterative Invoked Function Expression",
    ]),
    S("Quelle syntaxe représente une IIFE valide ?", 1, [
      "function () {}();",
      "(function () { /* ... */ })();",
      "function() {} ();",
      "execute function() {}",
    ]),
    S("Quel était l'un des principaux intérêts historiques des IIFE avant l'arrivée des modules ES ?", 0, [
      "Créer une portée privée pour éviter de polluer l'espace global",
      "Accélérer l'exécution du code de moitié",
      "Permettre l'héritage multiple",
      "Remplacer complètement les boucles for",
    ]),
    TF("Une IIFE s'exécute une seule fois, immédiatement après sa définition.", true),
    TF("On ne peut pas passer d'arguments à une IIFE.", false),
    M("Quelles affirmations sur les IIFE sont correctes ?", [0, 1, 2], [
      "Elles permettent d'isoler des variables dans une portée de fonction privée",
      "Elles peuvent retourner une valeur, par exemple pour le pattern module",
      "Elles s'exécutent immédiatement sans avoir besoin d'être appelées séparément",
      "Elles doivent obligatoirement être déclarées avec le mot-clé async",
    ]),
    S("Pourquoi entoure-t-on souvent la fonction d'une IIFE par des parenthèses, comme `(function(){})()` ?", 0, [
      "Pour que le moteur JavaScript interprète l'expression comme une expression de fonction et non une déclaration",
      "C'est purement décoratif et n'a aucun effet",
      "Pour rendre la fonction asynchrone automatiquement",
      "Pour permettre l'utilisation de this",
    ]),
    S("Quelle alternative moderne remplace souvent l'usage des IIFE pour l'encapsulation de portée ?", 0, ["Les modules ES (import/export)", "Les boucles while", "var en portée globale", "Les commentaires de bloc"]),
  ]
);
