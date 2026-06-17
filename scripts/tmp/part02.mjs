import { quiz, S, M, TF } from "./gen-js.mjs";

quiz(
  "Tableaux : méthode map et filter",
  "Transformer et filtrer des tableaux sans mutation grâce à map et filter.",
  [
    S("Que retourne `[1, 2, 3].map(x => x * 2)` ?", 0, ["[2, 4, 6]", "[1, 2, 3]", "6", "[1, 4, 9]"]),
    S("Que retourne `[1, 2, 3, 4].filter(x => x % 2 === 0)` ?", 1, ["[1, 3]", "[2, 4]", "[1, 2, 3, 4]", "2"]),
    S("La méthode `map` modifie-t-elle le tableau original ?", 1, [
      "Oui, elle le modifie directement",
      "Non, elle retourne un nouveau tableau",
      "Oui, mais seulement les nombres",
      "Cela dépend du navigateur",
    ]),
    TF("`filter` retourne toujours un tableau de la même longueur que le tableau d'origine.", false),
    TF("`[5, 10, 15].map(x => x > 7)` retourne `[false, true, true]`.", true),
    M("Quelles affirmations sur `map` et `filter` sont correctes ?", [0, 1, 2], [
      "map applique une fonction à chaque élément et retourne un nouveau tableau de même longueur",
      "filter retourne un nouveau tableau contenant uniquement les éléments qui satisfont une condition",
      "Ni map ni filter ne mutent le tableau original",
      "map et filter trient automatiquement le tableau résultant",
    ]),
    S("Que retourne `['a', 'bb', 'ccc'].map(s => s.length)` ?", 0, ["[1, 2, 3]", "['a', 'bb', 'ccc']", "3", "[3, 2, 1]"]),
    S("Que retourne `[].filter(x => x > 0)` sur un tableau vide ?", 0, ["[] (tableau vide)", "undefined", "null", "Une erreur"]),
  ]
);

quiz(
  "Tableaux : reduce, forEach et find",
  "Agréger, parcourir et rechercher des éléments dans un tableau.",
  [
    S("Que retourne `[1, 2, 3, 4].reduce((acc, val) => acc + val, 0)` ?", 1, ["24", "10", "[1,2,3,4]", "0"]),
    S("Quel est le rôle du second argument de `reduce` (ici `0`) ?", 0, [
      "La valeur initiale de l'accumulateur",
      "L'index de départ du parcours",
      "La valeur finale attendue",
      "Le nombre d'itérations à effectuer",
    ]),
    S("Que retourne `forEach` après avoir parcouru un tableau ?", 2, ["Le tableau transformé", "Un booléen", "undefined", "Le dernier élément traité"]),
    TF("`forEach` permet d'arrêter la boucle prématurément avec une instruction `break` comme dans une boucle for classique.", false),
    TF("`find` retourne le premier élément du tableau qui satisfait la fonction de test, ou undefined si aucun ne correspond.", true),
    M("Quelles affirmations sur `reduce` sont correctes ?", [0, 1], [
      "reduce peut servir à additionner, concaténer ou construire un objet à partir d'un tableau",
      "Si aucune valeur initiale n'est fournie, le premier élément du tableau est utilisé comme accumulateur de départ",
      "reduce mute toujours le tableau original",
      "reduce ne peut être utilisé qu'avec des nombres",
    ]),
    S("Que retourne `[5, 12, 8, 130, 44].find(x => x > 10)` ?", 1, ["5", "12", "130", "undefined"]),
    S("Que retourne `[5, 12, 8].findIndex(x => x > 10)` ?", 0, ["1", "12", "0", "-1"]),
  ]
);

quiz(
  "Tableaux : sort, slice et splice",
  "Trier et extraire des portions de tableaux, avec ou sans mutation.",
  [
    S("Quelle méthode trie un tableau en le modifiant directement (mutation) ?", 1, ["slice", "sort", "map", "filter"]),
    S("Quelle méthode extrait une portion d'un tableau SANS modifier l'original ?", 0, ["slice", "splice", "sort", "push"]),
    S("Quelle méthode permet d'ajouter ou de retirer des éléments à une position donnée, en mutant le tableau ?", 2, ["slice", "concat", "splice", "join"]),
    TF("`[3, 1, 2].sort()` sans fonction de comparaison trie les nombres en les convertissant en chaînes, ce qui peut donner des résultats inattendus pour de grands nombres.", true),
    TF("`splice` retourne un nouveau tableau et laisse le tableau original intact.", false),
    M("Quelles méthodes de tableau mutent (modifient) le tableau original ?", [0, 1, 2], [
      "sort()",
      "splice()",
      "reverse()",
      "slice()",
    ]),
    S("Que retourne `[1, 2, 3, 4, 5].slice(1, 3)` ?", 1, ["[1, 2, 3]", "[2, 3]", "[2, 3, 4]", "[1, 2]"]),
    S("Que fait `arr.splice(2, 1, 'x')` sur `arr = ['a','b','c','d']` ?", 0, [
      "Supprime 1 élément à l'index 2 et insère 'x' à sa place",
      "Ajoute 'x' à la fin du tableau",
      "Supprime tous les éléments après l'index 2",
      "Ne modifie rien, retourne juste une copie",
    ]),
  ]
);

quiz(
  "Objets et destructuring",
  "Extraire des valeurs d'objets et de tableaux avec la syntaxe de déstructuration.",
  [
    S("Quelle syntaxe extrait correctement la propriété `nom` d'un objet `personne` ?", 0, [
      "const { nom } = personne;",
      "const [nom] = personne;",
      "const nom = personne.[nom];",
      "const nom := personne.nom;",
    ]),
    S("Que vaut `b` après `const { a, b = 10 } = { a: 1 };` ?", 1, ["undefined", "10", "1", "null"]),
    S("Quelle syntaxe permet de renommer une propriété lors de la déstructuration ?", 2, [
      "const { nom -> n } = obj;",
      "const { nom = n } = obj;",
      "const { nom: n } = obj;",
      "const { n = nom } = obj;",
    ]),
    TF("On peut déstructurer un tableau avec la syntaxe `const [premier, second] = [1, 2, 3];`.", true),
    TF("La déstructuration d'objet dépend de l'ordre des propriétés dans l'objet source.", false),
    M("Quelles syntaxes de déstructuration sont valides ?", [0, 1, 2], [
      "const { x, y } = { x: 1, y: 2 };",
      "const [a, , c] = [1, 2, 3];",
      "const { a: { b } } = { a: { b: 1 } };",
      "const { x, y } := obj;",
    ]),
    S("Que vaut `reste` après `const { a, ...reste } = { a: 1, b: 2, c: 3 };` ?", 0, ["{ b: 2, c: 3 }", "{ a: 1 }", "[2, 3]", "undefined"]),
    S("Comment échanger les valeurs de deux variables `x` et `y` en une seule ligne grâce à la déstructuration ?", 0, [
      "[x, y] = [y, x];",
      "x, y = y, x;",
      "swap(x, y);",
      "{x, y} = {y, x};",
    ]),
  ]
);

quiz(
  "Opérateurs spread et rest",
  "Étaler ou regrouper des éléments d'itérables grâce à la syntaxe ...",
  [
    S("Que retourne `[...[1, 2], ...[3, 4]]` ?", 0, ["[1, 2, 3, 4]", "[[1,2],[3,4]]", "[1, 2]", "10"]),
    S("Que retourne `{...{a: 1}, ...{b: 2}}` ?", 1, ["{a: 1}", "{a: 1, b: 2}", "{b: 2}", "undefined"]),
    S("Dans `function f(...args) {}`, que représente `args` à l'intérieur de la fonction ?", 0, [
      "Un tableau contenant tous les arguments passés",
      "Le premier argument uniquement",
      "Un objet avec des clés numériques non itérable",
      "undefined si plus d'un argument est passé",
    ]),
    TF("L'opérateur spread permet de copier superficiellement (shallow copy) un tableau : `const copie = [...original];`.", true),
    TF("Le spread operator et le rest operator utilisent une syntaxe différente (l'un utilise `...` et l'autre `..`).", false),
    M("Dans quels contextes peut-on utiliser l'opérateur `...` (spread/rest) ?", [0, 1, 2], [
      "Pour copier les éléments d'un tableau dans un nouveau tableau",
      "Pour fusionner les propriétés de plusieurs objets",
      "Pour capturer les paramètres restants d'une fonction",
      "Pour déclarer une variable globale",
    ]),
    S("Que retourne `Math.max(...[3, 7, 2])` ?", 1, ["[3, 7, 2]", "7", "3", "NaN"]),
    S("Que vaut `b` après `const [a, ...b] = [1, 2, 3, 4];` ?", 0, ["[2, 3, 4]", "[1, 2, 3, 4]", "4", "undefined"]),
  ]
);

quiz(
  "Template literals (littéraux de gabarit)",
  "Utiliser les chaînes de caractères avec interpolation et lignes multiples.",
  [
    S("Quel caractère délimite un template literal en JavaScript ?", 2, ["Guillemets doubles \"", "Guillemets simples '", "Backticks `", "Crochets []"]),
    S("Comment insère-t-on une variable `nom` dans un template literal ?", 1, ["'Bonjour ' + nom", "`Bonjour ${nom}`", "\"Bonjour {nom}\"", "'Bonjour %nom%'"]),
    S("Que retourne `` `Total: ${2 + 3}` `` ?", 0, ["'Total: 5'", "'Total: 2 + 3'", "'Total: ${2+3}'", "Une erreur de syntaxe"]),
    TF("Les template literals permettent d'écrire des chaînes de caractères sur plusieurs lignes sans caractère d'échappement spécial.", true),
    TF("Les expressions à l'intérieur de `${}` ne peuvent contenir que des variables simples, pas des appels de fonction.", false),
    M("Quels avantages offrent les template literals par rapport à la concaténation classique ?", [0, 1, 2], [
      "Interpolation directe de variables et d'expressions",
      "Support natif des chaînes multi-lignes",
      "Possibilité de créer des tagged templates (fonctions de transformation)",
      "Conversion automatique en nombre de toute la chaîne",
    ]),
    S("Que retourne `` `${1 === 1 ? 'oui' : 'non'}` `` ?", 0, ["'oui'", "'non'", "true", "undefined"]),
    S("Que représente une 'tagged template' comme `` tag`Bonjour ${nom}` `` ?", 1, [
      "Une erreur de syntaxe car tag n'existe pas",
      "Un appel à la fonction tag avec les parties statiques et les valeurs interpolées séparément",
      "Une simple concaténation de chaînes",
      "Un commentaire spécial JavaScript",
    ]),
  ]
);

quiz(
  "Promises : les bases",
  "Comprendre le fonctionnement d'une Promise et ses états.",
  [
    S("Quels sont les trois états possibles d'une Promise ?", 0, [
      "pending, fulfilled, rejected",
      "waiting, success, error",
      "open, closed, pending",
      "start, running, done",
    ]),
    S("Quelle méthode permet de réagir au succès d'une Promise ?", 1, [".catch()", ".then()", ".resolve()", ".success()"]),
    S("Quelle méthode permet de gérer une erreur survenue dans une chaîne de Promises ?", 2, [".then()", ".finally()", ".catch()", ".error()"]),
    TF("Une Promise, une fois résolue (fulfilled) ou rejetée (rejected), ne peut plus changer d'état.", true),
    TF(".finally() s'exécute uniquement si la Promise est résolue avec succès.", false),
    M("Quelles affirmations sur les Promises sont correctes ?", [0, 1, 2], [
      "Une Promise représente le résultat éventuel (futur) d'une opération asynchrone",
      "On peut chaîner plusieurs .then() à la suite",
      "Promise.resolve(valeur) crée une Promise déjà résolue avec cette valeur",
      "Une Promise s'exécute toujours de manière synchrone et bloquante",
    ]),
    S("Que retourne `Promise.resolve(5).then(v => v * 2)` une fois résolu ?", 0, ["Une Promise résolue avec la valeur 10", "5", "10 directement (pas de Promise)", "undefined"]),
    S("Quelle méthode statique attend que TOUTES les Promises d'un tableau soient résolues (ou qu'une échoue) ?", 0, ["Promise.all()", "Promise.race()", "Promise.any()", "Promise.first()"]),
  ]
);

quiz(
  "async/await en pratique",
  "Simplifier l'écriture de code asynchrone avec async et await.",
  [
    S("Que retourne toujours une fonction déclarée avec `async` ?", 0, ["Une Promise", "Un objet brut", "undefined systématiquement", "Un tableau"]),
    S("Où peut-on utiliser le mot-clé `await` ?", 1, [
      "N'importe où dans le code, même hors fonction async (en module top-level uniquement dans certains cas)",
      "Uniquement à l'intérieur d'une fonction déclarée async (ou en haut de module ES)",
      "Uniquement dans les boucles for",
      "Jamais à l'intérieur d'un try/catch",
    ]),
    S("Comment gérer une erreur levée par un `await` qui échoue ?", 2, [
      "Avec .then() après le await",
      "C'est impossible, il faut utiliser .catch() sur la fonction entière",
      "Avec un bloc try/catch autour du await",
      "Les erreurs async sont ignorées automatiquement",
    ]),
    TF("`await` suspend l'exécution de la fonction async jusqu'à ce que la Promise soit résolue ou rejetée, sans bloquer le thread principal.", true),
    TF("Une fonction async ne peut contenir qu'un seul `await`.", false),
    M("Quelles affirmations sur async/await sont correctes ?", [0, 1, 2], [
      "async/await est une syntaxe plus lisible construite au-dessus des Promises",
      "On peut utiliser try/catch pour intercepter les rejets de Promise avec await",
      "Plusieurs await peuvent être utilisés successivement dans une même fonction async",
      "await transforme une fonction asynchrone en fonction strictement synchrone bloquante",
    ]),
    S("Que retourne une fonction `async function f() { return 42; }` lorsqu'on l'appelle `f()` ?", 0, ["Une Promise résolue avec 42", "42 directement", "undefined", "Une erreur"]),
    S("Comment exécuter plusieurs opérations asynchrones en parallèle puis attendre toutes leurs résolutions avec async/await ?", 0, [
      "await Promise.all([promesse1, promesse2])",
      "await promesse1; await promesse2; en boucle séquentielle uniquement",
      "Ce n'est pas possible avec async/await",
      "async.parallel(promesse1, promesse2)",
    ]),
  ]
);

quiz(
  "La boucle d'événements (event loop)",
  "Comprendre l'ordre d'exécution entre code synchrone, microtâches et macrotâches.",
  [
    S("Que veut dire le fait que JavaScript soit 'mono-thread' (single-threaded) ?", 0, [
      "Il n'exécute qu'une seule instruction à la fois sur un seul fil d'exécution principal",
      "Il ne peut exécuter qu'une seule fonction dans toute sa durée de vie",
      "Il ne peut pas faire d'opérations asynchrones",
      "Il utilise plusieurs threads pour chaque fonction",
    ]),
    S("Parmi `setTimeout` et `Promise.then`, lequel est traité comme une microtâche ?", 1, ["setTimeout", "Promise.then", "Les deux sont des macrotâches", "Aucun des deux"]),
    S(
      "Quel est l'ordre d'affichage de : `console.log('A'); setTimeout(() => console.log('B'), 0); Promise.resolve().then(() => console.log('C')); console.log('D');` ?",
      0,
      ["A, D, C, B", "A, B, C, D", "A, D, B, C", "B, C, A, D"]
    ),
    TF("Les microtâches (Promises) sont toujours exécutées avant les macrotâches (setTimeout) à priorité égale dans la file d'attente.", true),
    TF("L'event loop exécute le code asynchrone sur un thread séparé du thread principal en JavaScript natif (sans Web Workers).", false),
    M("Quels éléments font partie du fonctionnement de l'event loop ?", [0, 1, 2], [
      "La pile d'appels (call stack)",
      "La file des microtâches (microtask queue)",
      "La file des macrotâches (callback/task queue)",
      "Le garbage collector qui s'exécute en tant que macrotâche prioritaire",
    ]),
    S("Pourquoi `setTimeout(fn, 0)` ne s'exécute-t-il pas immédiatement ?", 0, [
      "Parce qu'il est placé dans la file des tâches et attend que la pile d'appels soit vide",
      "Parce que 0 millisecondes est interprété comme une erreur",
      "Parce que setTimeout est toujours plus lent que 4ms au minimum, sans rapport avec la pile",
      "Ce n'est pas vrai, il s'exécute toujours en premier",
    ]),
    S("Quel terme désigne la structure de données qui garde trace des fonctions en cours d'exécution ?", 0, ["La pile d'appels (call stack)", "Le tas (heap)", "La file d'attente (queue)", "Le registre"]),
  ]
);
