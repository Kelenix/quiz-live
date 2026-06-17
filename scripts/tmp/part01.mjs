import { quiz, S, M, TF } from "./gen-js.mjs";

quiz(
  "Variables : var, let et const",
  "Différences fondamentales entre les trois façons de déclarer une variable en JavaScript.",
  [
    S("Quel mot-clé permet de déclarer une variable dont la valeur ne peut pas être réaffectée ?", 2, ["var", "let", "const", "static"]),
    S("Quelle est la portée (scope) d'une variable déclarée avec `let` à l'intérieur d'un bloc `{ }` ?", 0, ["Le bloc dans lequel elle est déclarée", "La fonction englobante entière", "Le fichier entier (portée globale)", "Le module entier"]),
    S("Que se passe-t-il si on tente de réassigner une variable déclarée avec `const` ?", 1, ["Rien, la valeur change normalement", "Une erreur TypeError est levée", "La variable devient undefined", "JavaScript ignore silencieusement l'instruction"]),
    TF("Une variable déclarée avec `var` a une portée de fonction (function scope) et non de bloc.", true),
    TF("Il est possible de redéclarer une variable avec `var` plusieurs fois dans la même portée sans erreur.", true),
    M("Parmi les affirmations suivantes sur `const`, lesquelles sont correctes ?", [0, 2], [
      "On ne peut pas réaffecter l'identifiant après déclaration",
      "Un objet déclaré avec const ne peut jamais voir ses propriétés modifiées",
      "On peut modifier les propriétés d'un objet déclaré avec const",
      "const empêche toute mutation de tableau déclaré avec ce mot-clé",
    ]),
    S("Quelle déclaration est correcte concernant `var` par rapport à `let` et `const` ?", 1, ["var respecte la portée de bloc", "var est attachée à la portée de la fonction englobante ou au scope global", "var ne peut pas être utilisée dans une boucle for", "var empêche le hoisting"]),
    M("Lesquelles de ces déclarations sont valides en JavaScript ?", [0, 1, 2], [
      "let x = 10;",
      "const y = 5;",
      "var z = 1;",
      "constant w = 2;",
    ]),
  ]
);

quiz(
  "Hoisting en JavaScript",
  "Comprendre le mécanisme de remontée des déclarations (hoisting) et ses pièges.",
  [
    S("Que signifie le terme 'hoisting' en JavaScript ?", 1, [
      "La suppression automatique des variables inutilisées",
      "Le déplacement conceptuel des déclarations vers le haut de leur portée avant l'exécution",
      "La conversion automatique de var en let",
      "Le tri alphabétique des déclarations de fonctions",
    ]),
    S("Que retourne `console.log(a); var a = 5;` ?", 0, ["undefined", "5", "ReferenceError", "null"]),
    S("Que se passe-t-il si on exécute `console.log(b); let b = 5;` ?", 2, [
      "undefined est affiché",
      "5 est affiché",
      "Une ReferenceError est levée (zone morte temporelle)",
      "null est affiché",
    ]),
    TF("Les déclarations de fonctions classiques (`function foo() {}`) sont hoistées avec leur corps complet, contrairement aux expressions de fonction.", true),
    TF("Les variables déclarées avec `let` et `const` ne sont pas du tout affectées par le hoisting.", false),
    M("Quels éléments sont concernés par le hoisting en JavaScript ?", [0, 1, 2], [
      "Les déclarations var",
      "Les déclarations de fonctions (function declarations)",
      "Les déclarations let et const (mises dans la zone morte temporelle)",
      "Les commentaires de code",
    ]),
    S("Comment appelle-t-on la zone où une variable `let` existe mais n'est pas encore accessible avant son initialisation ?", 0, [
      "La zone morte temporelle (temporal dead zone)",
      "La zone d'exclusion",
      "Le scope flottant",
      "La portée fantôme",
    ]),
    S("Quel est le résultat de `typeof maVar; var maVar = 1;` exécuté en haut d'un script ?", 1, ["'number'", "'undefined'", "ReferenceError", "'string'"]),
  ]
);

quiz(
  "Portée des variables (scope)",
  "Notions de portée globale, de fonction et de bloc en JavaScript.",
  [
    S("Comment appelle-t-on la portée accessible depuis n'importe quel endroit du programme ?", 0, ["La portée globale", "La portée locale", "La portée de bloc", "La portée lexicale fermée"]),
    S("Dans quelle portée une variable déclarée à l'intérieur d'une fonction avec `var` est-elle visible ?", 1, ["Uniquement dans le bloc if/for englobant", "Dans toute la fonction où elle est déclarée", "Dans le fichier entier", "Nulle part hors de la ligne de déclaration"]),
    S("Que produit ce code ? `if (true) { let x = 1; } console.log(x);`", 2, ["1", "undefined", "ReferenceError : x n'est pas défini", "0"]),
    TF("Une fonction imbriquée (fonction interne) peut accéder aux variables de la fonction qui l'englobe.", true),
    TF("La portée de bloc s'applique également aux variables déclarées avec `var`.", false),
    M("Quels facteurs déterminent la portée lexicale d'une variable en JavaScript ?", [0, 1], [
      "L'endroit où la fonction ou le bloc est écrit dans le code source",
      "La structure d'imbrication des fonctions et des blocs au moment de l'écriture",
      "L'endroit depuis lequel la fonction est appelée à l'exécution",
      "La taille de la pile d'appels au moment de l'exécution",
    ]),
    S("Quel terme désigne une variable accessible uniquement à l'intérieur de la fonction où elle est déclarée ?", 0, ["Variable locale", "Variable globale", "Variable statique", "Variable constante"]),
    S("Que vaut `x` après l'exécution de : `let x = 1; function f() { let x = 2; } f(); console.log(x);` ?", 0, ["1", "2", "undefined", "ReferenceError"]),
  ]
);

quiz(
  "Coercition de types en JavaScript",
  "Comment JavaScript convertit implicitement les types lors des opérations.",
  [
    S("Que retourne l'expression `'5' + 3` ?", 2, ["8", "'53' converti en nombre", "'53' (chaîne de caractères)", "NaN"]),
    S("Que retourne l'expression `'5' - 3` ?", 0, ["2", "'53'", "NaN", "'2'"]),
    S("Que retourne `Number('123abc')` ?", 1, ["123", "NaN", "'123abc'", "0"]),
    TF("L'opérateur `+` entre une chaîne et un nombre provoque toujours une conversion du nombre en chaîne suivie d'une concaténation.", true),
    TF("`Boolean('')` retourne `true`.", false),
    M("Quelles expressions retournent `true` à cause de la coercition de type ?", [0, 1, 3], [
      "'5' == 5",
      "0 == false",
      "null == undefined",
      "[] == false",
    ]),
    S("Que retourne `+'42'` (avec l'opérateur unaire plus) ?", 0, ["42 (nombre)", "'42' (chaîne)", "NaN", "undefined"]),
    S("Que retourne `String(null)` ?", 1, ["'undefined'", "'null'", "null", "TypeError"]),
  ]
);

quiz(
  "Opérateurs == et === : égalité stricte vs souple",
  "Distinguer la comparaison avec et sans conversion de type implicite.",
  [
    S("Que retourne `1 === '1'` ?", 1, ["true", "false", "NaN", "undefined"]),
    S("Que retourne `1 == '1'` ?", 0, ["true", "false", "NaN", "undefined"]),
    S("Quel opérateur faut-il privilégier pour éviter les conversions de type implicites surprenantes ?", 1, ["==", "===", "=", "<=>"]),
    TF("`null === undefined` retourne `true`.", false),
    TF("`null == undefined` retourne `true`.", true),
    M("Quelles comparaisons retournent `true` ?", [0, 2], [
      "NaN !== NaN",
      "NaN === NaN",
      "'0' == 0",
      "'0' === 0",
    ]),
    S("Que retourne `0 === -0` ?", 0, ["true", "false", "NaN", "undefined"]),
    S("Que retourne `[] == ''`?", 0, ["true (les deux sont convertis en chaîne vide)", "false", "TypeError", "undefined"]),
  ]
);

quiz(
  "Opérateur ternaire et nullish coalescing (??)",
  "Manipuler les expressions conditionnelles compactes en JavaScript moderne.",
  [
    S("Quelle syntaxe représente l'opérateur ternaire en JavaScript ?", 1, ["condition ? a : b ? c", "condition ? valeurSiVrai : valeurSiFaux", "if (condition) valeur", "condition => valeur"]),
    S("Que retourne `0 ?? 'défaut'` ?", 1, ["'défaut'", "0", "undefined", "NaN"]),
    S("Que retourne `null ?? 'défaut'` ?", 0, ["'défaut'", "null", "undefined", "0"]),
    TF("L'opérateur `??` retourne l'opérande de droite uniquement si la valeur de gauche est `null` ou `undefined`.", true),
    TF("`0 || 'défaut'` et `0 ?? 'défaut'` retournent toujours le même résultat.", false),
    M("Pour quelles valeurs de gauche l'opérateur `??` renvoie-t-il l'opérande de droite ?", [1, 2], [
      "0",
      "null",
      "undefined",
      "'' (chaîne vide)",
    ]),
    S("Que retourne `true ? 'A' : false ? 'B' : 'C'` ?", 0, ["'A'", "'B'", "'C'", "undefined"]),
    S("Quel est l'intérêt principal de l'opérateur `??` par rapport à `||` ?", 1, [
      "Il est plus rapide à l'exécution",
      "Il ne considère que null/undefined comme valeurs manquantes, pas les autres valeurs falsy comme 0 ou ''",
      "Il fonctionne uniquement avec des booléens",
      "Il remplace complètement l'opérateur ternaire",
    ]),
  ]
);

quiz(
  "Fonctions : déclarations, expressions et fonctions fléchées",
  "Les différentes façons de définir une fonction en JavaScript.",
  [
    S("Quelle syntaxe correspond à une déclaration de fonction (function declaration) ?", 0, [
      "function saluer() { return 'bonjour'; }",
      "const saluer = function() { return 'bonjour'; };",
      "const saluer = () => 'bonjour';",
      "let saluer = new Function();",
    ]),
    S("Quelle syntaxe représente une fonction fléchée (arrow function) ?", 2, [
      "function() {}",
      "function nommee() {}",
      "() => {}",
      "new Function()",
    ]),
    S("Quelle est une caractéristique propre aux fonctions fléchées par rapport aux fonctions classiques ?", 1, [
      "Elles possèdent leur propre objet `arguments`",
      "Elles n'ont pas leur propre `this` et héritent de celui du contexte englobant",
      "Elles ne peuvent jamais recevoir de paramètres",
      "Elles sont hoistées comme les déclarations de fonction",
    ]),
    TF("Les expressions de fonction (function expressions) ne sont pas hoistées avec leur corps, contrairement aux déclarations de fonction.", true),
    TF("Une fonction fléchée peut être utilisée comme constructeur avec le mot-clé `new`.", false),
    M("Lesquelles de ces syntaxes définissent correctement une fonction qui additionne deux nombres ?", [0, 1, 2], [
      "function add(a, b) { return a + b; }",
      "const add = (a, b) => a + b;",
      "const add = function(a, b) { return a + b; };",
      "const add = (a, b) -> a + b;",
    ]),
    S("Que retourne une fonction fléchée sans instruction `return` explicite, écrite en une seule expression comme `(x) => x * 2` ?", 0, [
      "Le résultat de l'expression, retourné implicitement",
      "undefined toujours",
      "Une erreur de syntaxe",
      "null",
    ]),
    S("Quel mot-clé est nécessaire pour créer une fonction anonyme assignée à une variable ?", 1, ["def", "function (ou une fonction fléchée)", "lambda", "func"]),
  ]
);

quiz(
  "Paramètres par défaut et fonctions variadiques",
  "Définir des valeurs par défaut et gérer un nombre variable d'arguments.",
  [
    S("Comment définir une valeur par défaut pour un paramètre de fonction ?", 0, [
      "function f(x = 10) {}",
      "function f(x default 10) {}",
      "function f(x ?? 10) {}",
      "function f(x: 10) {}",
    ]),
    S("Que retourne `function f(x = 5) { return x; } f();` ?", 1, ["undefined", "5", "null", "NaN"]),
    S("Que retourne `function f(x = 5) { return x; } f(undefined);` ?", 1, ["undefined", "5", "0", "NaN"]),
    TF("Si on appelle `f(null)` avec `function f(x = 5) {}`, la valeur par défaut 5 est utilisée.", false),
    TF("L'opérateur rest (`...args`) permet de regrouper un nombre indéfini d'arguments dans un tableau.", true),
    M("Quelles syntaxes de fonction sont valides pour capturer un nombre variable d'arguments ?", [0, 1], [
      "function f(...args) {}",
      "function f(a, b, ...reste) {}",
      "function f(...args, last) {}",
      "function f(, ...args) {}",
    ]),
    S("Que retourne `function somme(...nombres) { return nombres.reduce((a,b) => a+b, 0); } somme(1,2,3);` ?", 1, ["0", "6", "[1,2,3]", "NaN"]),
    S("Pourquoi l'opérateur rest doit-il être le dernier paramètre d'une fonction ?", 0, [
      "Parce qu'il capture tous les arguments restants, il n'y a donc rien après lui",
      "Par convention stylistique uniquement, ce n'est pas obligatoire",
      "Parce que JavaScript trie les paramètres alphabétiquement",
      "Ce n'est pas une vraie règle du langage",
    ]),
  ]
);

quiz(
  "Closures et portée lexicale",
  "Comprendre comment une fonction capture son environnement lexical.",
  [
    S("Qu'est-ce qu'une closure (fermeture) en JavaScript ?", 1, [
      "Une fonction qui ne peut pas être appelée deux fois",
      "Une fonction qui conserve l'accès aux variables de sa portée lexicale même après que la fonction englobante a terminé son exécution",
      "Une méthode pour fermer une connexion réseau",
      "Une fonction qui retourne toujours undefined",
    ]),
    S(
      "Que retourne ce code ? `function compteur() { let n = 0; return function() { n++; return n; }; } const c = compteur(); c(); c();`",
      1,
      ["1", "2", "0", "undefined"]
    ),
    S("Quel est l'avantage principal des closures pour créer des variables privées ?", 0, [
      "Elles permettent d'encapsuler un état sans l'exposer directement dans la portée globale",
      "Elles suppriment automatiquement la mémoire utilisée",
      "Elles empêchent toute fonction d'être appelée plus d'une fois",
      "Elles rendent le code plus rapide à l'exécution",
    ]),
    TF("Une closure conserve une référence vivante à la variable de la portée englobante, pas une copie figée de sa valeur au moment de la création.", true),
    TF("Les closures ne peuvent être créées qu'avec des fonctions fléchées.", false),
    M("Quelles affirmations sur les closures sont correctes ?", [0, 1], [
      "Une closure se forme chaque fois qu'une fonction est définie à l'intérieur d'une autre fonction et utilise une variable externe",
      "Les closures permettent de créer des fonctions usine (factory functions) avec un état encapsulé",
      "Les closures empêchent toute fonction interne d'accéder aux variables externes",
      "Une closure copie immédiatement la valeur des variables externes au moment de l'appel, sans référence",
    ]),
    S(
      "Dans une boucle `for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 0); }`, que va-t-on afficher ?",
      2,
      ["0, 1, 2", "0, 0, 0", "3, 3, 3", "undefined trois fois"]
    ),
    S(
      "Dans une boucle `for (let i = 0; i < 3; i++) { setTimeout(() => console.log(i), 0); }`, que va-t-on afficher ?",
      0,
      ["0, 1, 2", "3, 3, 3", "0, 0, 0", "Une erreur de syntaxe"]
    ),
  ]
);

quiz(
  "Le mot-clé this en JavaScript",
  "Déterminer la valeur de this selon le contexte d'appel d'une fonction.",
  [
    S("Dans une méthode d'objet classique `obj.methode()`, à quoi `this` fait-il référence à l'intérieur de `methode` ?", 0, [
      "À l'objet `obj` lui-même",
      "À l'objet global (window ou globalThis)",
      "À undefined systématiquement",
      "À la fonction methode elle-même",
    ]),
    S("Que vaut `this` à l'intérieur d'une fonction fléchée définie dans une méthode d'objet ?", 1, [
      "L'objet sur lequel la méthode est appelée",
      "La même valeur que `this` dans la portée englobante (héritage lexical)",
      "undefined toujours, sans exception",
      "L'objet global",
    ]),
    S("Quelle méthode permet de fixer explicitement la valeur de `this` pour un appel de fonction ponctuel ?", 2, ["bind", "apply", "call", "this.set"]),
    TF("La méthode `.bind()` retourne une nouvelle fonction avec `this` lié de façon permanente, sans l'exécuter immédiatement.", true),
    TF("En mode strict, `this` vaut `undefined` dans une fonction simple appelée sans contexte (et non l'objet global).", true),
    M("Quelles méthodes permettent de contrôler explicitement la valeur de `this` lors de l'appel d'une fonction ?", [0, 1, 2], [
      "call()",
      "apply()",
      "bind()",
      "this()",
    ]),
    S("Quelle est la différence principale entre `call()` et `apply()` ?", 1, [
      "call() ne fonctionne pas avec des objets",
      "apply() prend les arguments sous forme de tableau, call() les prend séparément",
      "Elles sont strictement identiques sans aucune différence",
      "call() est dépréciée en JavaScript moderne",
    ]),
    S("Dans un gestionnaire d'événement DOM classique (`element.addEventListener('click', function(){...})`), à quoi correspond `this` ?", 0, [
      "L'élément DOM sur lequel l'événement est écouté",
      "L'objet window toujours",
      "undefined",
      "L'objet event",
    ]),
  ]
);
