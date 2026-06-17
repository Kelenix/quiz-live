import { quiz, S, M, TF } from "./gen-js.mjs";

quiz(
  "Variables : pièges courants avec const et les objets",
  "Comprendre les limites réelles de l'immutabilité apportée par const.",
  [
    S("Que retourne ce code ? `const arr = [1, 2]; arr.push(3); console.log(arr.length);`", 2, ["2", "1", "3", "Une erreur car arr est const"]),
    S("Pourquoi `const obj = {}; obj.x = 1;` fonctionne-t-il sans erreur ?", 0, [
      "Parce que const empêche seulement la réaffectation de l'identifiant, pas la mutation du contenu",
      "Parce que obj n'est pas vraiment constant et peut être réassigné aussi",
      "Parce que JavaScript ignore le mot-clé const pour les objets",
      "Ce n'est pas vrai, ce code lève une TypeError",
    ]),
    S("Quelle méthode permet de réellement empêcher l'ajout, la suppression ou la modification de propriétés d'un objet ?", 1, ["const sur l'objet seul", "Object.freeze(obj)", "Object.lock(obj)", "obj.immutable = true"]),
    TF("`Object.freeze` empêche la modification des propriétés de premier niveau, mais pas nécessairement celles des objets imbriqués (freeze superficiel).", true),
    TF("On peut réaffecter complètement un tableau déclaré avec const, comme `const arr = []; arr = [1];`.", false),
    M("Quelles opérations sont possibles sur un tableau déclaré avec const ?", [0, 1, 2], [
      "arr.push(valeur)",
      "arr.pop()",
      "arr[0] = nouvelleValeur",
      "arr = nouveauTableau (réaffectation complète)",
    ]),
    S("Que retourne `Object.isFrozen(Object.freeze({}))` ?", 0, ["true", "false", "undefined", "Une erreur"]),
    S("En mode non strict, que se passe-t-il si on tente de modifier une propriété d'un objet gelé avec freeze ?", 0, [
      "La modification est silencieusement ignorée",
      "Une erreur est toujours levée",
      "La propriété est dupliquée",
      "L'objet entier est supprimé",
    ]),
  ]
);

quiz(
  "Portée et fonctions imbriquées",
  "Approfondir les interactions entre portée de bloc, de fonction et fonctions imbriquées.",
  [
    S(
      "Que retourne ce code ? `function externe() { let x = 'externe'; function interne() { return x; } return interne(); } externe();`",
      0,
      ["'externe'", "undefined", "ReferenceError", "null"]
    ),
    S("Une fonction interne peut-elle modifier une variable déclarée avec let dans la fonction externe qui l'englobe ?", 0, [
      "Oui, car elle a accès à cette variable par portée lexicale et peut la réassigner",
      "Non, jamais",
      "Seulement si la variable est déclarée avec var",
      "Seulement avec une fonction fléchée",
    ]),
    S("Que se passe-t-il si deux blocs `{ let x = 1; }` et `{ let x = 2; }` distincts définissent chacun leur propre `x` ?", 0, [
      "Aucun conflit, chaque bloc a sa propre portée indépendante",
      "Une erreur de redéclaration est levée",
      "Les deux valeurs sont fusionnées",
      "Seule la première déclaration est prise en compte",
    ]),
    TF("Une variable déclarée dans le bloc d'une boucle for avec let est recréée à chaque itération avec sa propre portée.", true),
    TF("Le 'shadowing' désigne le fait qu'une variable locale porte le même nom qu'une variable d'une portée englobante et la masque localement.", true),
    M("Quelles affirmations sur le shadowing de variables sont correctes ?", [0, 1], [
      "Une variable locale du même nom masque temporairement la variable englobante dans sa portée",
      "Le shadowing n'empêche pas la variable externe d'exister, elle est seulement inaccessible localement",
      "Le shadowing provoque toujours une erreur de syntaxe",
      "Le shadowing n'est possible qu'avec des fonctions fléchées",
    ]),
    S(
      "Que retourne ce code ? `let x = 'global'; function f() { let x = 'local'; return x; } f();`",
      1,
      ["'global'", "'local'", "undefined", "ReferenceError"]
    ),
    S("Quel terme désigne l'environnement mémoire associé à l'exécution d'une fonction, contenant ses variables locales ?", 0, ["Le contexte d'exécution (execution context)", "Le tas (heap) global", "Le registre processeur", "Le DOM virtuel"]),
  ]
);

quiz(
  "Coercition dans les structures conditionnelles",
  "Comment les valeurs sont converties implicitement dans if, while et les boucles.",
  [
    S("Que produit `if ('0') { console.log('vrai'); } else { console.log('faux'); }` ?", 0, ["'vrai' (car '0' est une chaîne non vide, donc truthy)", "'faux'", "Une erreur", "Rien ne s'affiche"]),
    S("Que produit `while (0) { console.log('boucle'); }` ?", 1, ["'boucle' une fois", "Rien, la boucle ne s'exécute jamais", "Boucle infinie", "Une erreur"]),
    S("Que retourne `Boolean(' ')` (chaîne contenant un espace) ?", 0, ["true", "false", "undefined", "NaN"]),
    TF("`if (document.querySelector('.absent')) {}` n'entre jamais dans le bloc if si l'élément n'existe pas, car querySelector retourne null (falsy).", true),
    TF("Un tableau vide `[]` utilisé dans une condition if est considéré comme falsy.", false),
    M("Quelles valeurs provoquent l'exécution du bloc 'else' (donc sont falsy) dans une condition if/else ?", [0, 1, 2], [
      "''",
      "0",
      "NaN",
      "'  ' (chaîne avec des espaces, non vide)",
    ]),
    S("Que produit ce code ? `for (let i = 3; i; i--) { console.log(i); }` (que représente la condition `i` seule) ?", 0, ["Affiche 3, 2, 1 puis s'arrête car i devient 0 (falsy)", "Boucle infinie", "N'affiche rien", "Erreur de syntaxe"]),
    S("Que retourne `Boolean(document.all)` dans un très vieux navigateur où ce comportement particulier existait (objet existant mais falsy par exception historique) ?", 1, [
      "true toujours, comme tout objet",
      "false, cas particulier historique du DOM (exotic falsy object)",
      "undefined",
      "Une erreur systématique",
    ]),
  ]
);

quiz(
  "Méthodes de tableau : pièges et subtilités",
  "Cas particuliers de mutation, de comparateurs et de valeurs retournées par les méthodes de tableau.",
  [
    S("Que retourne `[10, 1, 21].sort()` SANS fonction de comparaison ?", 1, ["[1, 10, 21]", "[1, 10, 21] n'est pas garanti, l'ordre lexicographique donne [1, 10, 21] ici mais peut surprendre pour d'autres valeurs", "[21, 10, 1]", "Une erreur"]),
    S("Comment trier un tableau de nombres `[10, 1, 21]` correctement par ordre numérique croissant ?", 0, ["arr.sort((a, b) => a - b)", "arr.sort()", "arr.sort((a, b) => a > b)", "arr.order()"]),
    S("Que retourne `[1, 2, 3].map(parseInt)` (piège classique avec parseInt et l'index) ?", 1, [
      "[1, 2, 3]",
      "[1, NaN, NaN] car parseInt reçoit aussi l'index comme base de conversion",
      "['1', '2', '3']",
      "Une erreur",
    ]),
    TF("`Array.isArray([])` retourne `true`.", true),
    TF("`[1, 2, 3].forEach()` retourne le tableau transformé après le passage du callback sur chaque élément.", false),
    M("Quelles méthodes de tableau retournent un NOUVEAU tableau sans muter l'original ?", [0, 1, 2], [
      "map()",
      "filter()",
      "concat()",
      "sort()",
    ]),
    S("Que retourne `Array.from({length: 3}, (_, i) => i * 2)` ?", 0, ["[0, 2, 4]", "[1, 2, 3]", "[0, 1, 2]", "undefined"]),
    S("Pourquoi `[1, 2, 3].map(parseInt)` ne donne pas le résultat attendu intuitivement ?", 0, [
      "Parce que map appelle le callback avec (élément, index, tableau) et parseInt interprète l'index comme une base de numération",
      "Parce que parseInt n'existe pas",
      "Parce que map ne peut pas recevoir de fonctions natives",
      "Ce n'est pas un piège réel, le résultat est toujours [1,2,3]",
    ]),
  ]
);

quiz(
  "Destructuring avancé et valeurs par défaut imbriquées",
  "Cas plus complexes de déstructuration avec objets imbriqués et paramètres de fonction.",
  [
    S(
      "Que vaut `ville` après `const { adresse: { ville } = {} } = {};` ?",
      0,
      ["undefined", "'' (chaîne vide)", "null", "Une erreur car adresse n'existe pas"]
    ),
    S("Quelle syntaxe permet de déstructurer directement un objet passé en paramètre de fonction ?", 0, [
      "function f({ nom, age }) { /* ... */ }",
      "function f(obj.nom, obj.age) { /* ... */ }",
      "function f(nom, age) = obj { /* ... */ }",
      "function f(destructure obj) { /* ... */ }",
    ]),
    S(
      "Que retourne `function f({ x = 10 } = {}) { return x; } f();` ?",
      1,
      ["undefined", "10", "0", "Une erreur car aucun argument n'est passé"]
    ),
    TF("On peut combiner déstructuration de tableau et d'objet, comme `const [{ nom }] = [{ nom: 'Ana' }];`.", true),
    TF("La déstructuration avec valeur par défaut ne s'applique que si la propriété est strictement absente, pas si elle vaut explicitement `null`.", true),
    M("Quelles syntaxes de déstructuration imbriquée sont valides ?", [0, 1, 2], [
      "const { a: { b: { c } } } = obj;",
      "const [[a, b], [c, d]] = [[1, 2], [3, 4]];",
      "const { liste: [premier] } = { liste: [1, 2, 3] };",
      "const { a, } := obj;",
    ]),
    S(
      "Que vaut `premier` après `const { liste: [premier] = [] } = {};` ?",
      0,
      ["undefined", "[] (tableau vide)", "0", "Erreur"]
    ),
    S("Pourquoi écrit-on souvent `function f({ options } = {})` avec une valeur par défaut sur le paramètre entier ?", 0, [
      "Pour éviter une erreur si la fonction est appelée sans aucun argument (déstructurer undefined lèverait une erreur)",
      "Pour rendre la fonction asynchrone",
      "C'est purement stylistique sans aucun effet",
      "Pour forcer options à être un tableau",
    ]),
  ]
);

quiz(
  "Spread et copies superficielles (shallow copy)",
  "Les limites du spread operator face aux structures de données imbriquées.",
  [
    S(
      "Que se passe-t-il si on fait `const copie = {...original}; copie.nested.x = 99;` alors que `original.nested` est un objet imbriqué ?",
      0,
      ["original.nested.x vaut aussi 99 car nested est partagé par référence (copie superficielle)", "original n'est jamais affecté", "Une erreur est levée", "copie devient identique à original par valeur profonde"]
    ),
    S("Comment qualifie-t-on une copie réalisée avec `{...obj}` qui ne duplique pas les objets imbriqués ?", 0, ["Une copie superficielle (shallow copy)", "Une copie profonde (deep copy)", "Une copie par référence totale", "Un clonage complet"]),
    S("Quelle fonction native (disponible dans les environnements récents) permet de réaliser une copie profonde simple d'un objet sans fonctions ni références circulaires ?", 0, ["structuredClone()", "Object.deepCopy()", "JSON.clone()", "Array.deepClone()"]),
    TF("`JSON.parse(JSON.stringify(obj))` est une technique courante (avec des limites) pour cloner profondément un objet simple.", true),
    TF("Le spread operator clone toujours profondément tous les niveaux d'un objet, peu importe son imbrication.", false),
    M("Quelles techniques permettent d'obtenir une copie d'un objet ou tableau en JavaScript ?", [0, 1, 2], [
      "Le spread operator {...obj} (copie superficielle)",
      "Object.assign({}, obj) (copie superficielle)",
      "structuredClone(obj) (copie profonde)",
      "obj.copy() (méthode native universelle)",
    ]),
    S("Que retourne `[...[1, [2, 3]]][1] === [1, [2, 3]][1]` (même référence pour le sous-tableau imbriqué) ?", 0, ["true", "false", "undefined", "Erreur"]),
    S("Pourquoi privilégier structuredClone ou une librairie dédiée plutôt que JSON.stringify/parse pour cloner un objet complexe ?", 0, [
      "Parce que JSON.stringify/parse perd les fonctions, les dates deviennent des chaînes, et échoue sur les références circulaires",
      "Parce que JSON.stringify est plus lent dans tous les cas",
      "Il n'y a aucune différence pratique",
      "Parce que JSON ne supporte pas les nombres",
    ]),
  ]
);

quiz(
  "Template literals avancés : tagged templates",
  "Créer des fonctions de transformation personnalisées sur des template literals.",
  [
    S(
      "Dans `function tag(strings, ...values) {}` utilisée comme `` tag`a${1}b${2}c` ``, que contient `strings` ?",
      0,
      ["Un tableau des parties statiques : ['a', 'b', 'c']", "Un tableau des valeurs interpolées : [1, 2]", "La chaîne complète 'a1b2c'", "undefined"]
    ),
    S("Dans le même exemple, que contient `values` (capturé via rest) ?", 1, ["['a', 'b', 'c']", "[1, 2]", "'a1b2c'", "undefined"]),
    S("Quel cas d'usage réel utilise les tagged templates dans l'écosystème JavaScript moderne (ex: styled-components) ?", 0, [
      "Générer du CSS-in-JS à partir d'un template littéral",
      "Compiler du code vers WebAssembly",
      "Remplacer les boucles for",
      "Créer des Promises automatiquement",
    ]),
    TF("Une fonction tag reçoit toujours le tableau des chaînes statiques en premier argument, suivi des valeurs interpolées.", true),
    TF("On ne peut pas échapper de caractères spéciaux dans un template literal classique.", false),
    M("Quelles affirmations sur les tagged templates sont correctes ?", [0, 1], [
      "Elles permettent d'intercepter et transformer le résultat d'un template literal avant qu'il devienne une chaîne finale",
      "La fonction tag peut retourner n'importe quel type, pas uniquement une chaîne",
      "Les tagged templates ne peuvent contenir aucune interpolation ${}",
      "Elles sont identiques en tout point à un appel de fonction classique avec une chaîne en argument",
    ]),
    S("Que retourne une fonction tag simple qui fait juste `return strings.join('-');` appelée sur `` tag`a${1}b` `` ?", 0, ["'a-b'", "'a1b'", "1", "undefined"]),
    S("La propriété `strings.raw` dans une fonction tag permet d'accéder à quoi exactement ?", 0, [
      "La version brute des chaînes, sans interprétation des séquences d'échappement comme \\n",
      "Les valeurs interpolées brutes",
      "Le nombre total d'interpolations",
      "Un tableau vide toujours",
    ]),
  ]
);

quiz(
  "Chaînage optionnel (optional chaining ?.)",
  "Accéder en toute sécurité à des propriétés potentiellement absentes.",
  [
    S("Que retourne `const obj = {}; obj?.a?.b;` ?", 0, ["undefined", "null", "Une erreur TypeError", "0"]),
    S("Quel est l'intérêt principal de l'opérateur `?.` (optional chaining) ?", 0, [
      "Éviter une erreur lors de l'accès à une propriété d'un objet potentiellement null ou undefined",
      "Convertir automatiquement une valeur en booléen",
      "Remplacer complètement les opérateurs de comparaison",
      "Forcer la conversion en chaîne de caractères",
    ]),
    S("Que retourne `obj?.methode?.()` si `obj.methode` n'existe pas ?", 0, ["undefined, sans lever d'erreur", "Une TypeError car methode n'est pas une fonction", "null", "0"]),
    TF("`obj?.a.b` lève toujours une erreur si `obj` est null, mais pas si seulement `obj.a` est null sans le second `?.`.", true),
    TF("L'optional chaining peut être combiné avec l'opérateur nullish coalescing, comme `obj?.a ?? 'défaut'`.", true),
    M("Dans quels contextes peut-on utiliser l'opérateur `?.` ?", [0, 1, 2], [
      "Accès à une propriété d'objet : obj?.prop",
      "Appel de méthode potentiellement absente : obj?.methode?.()",
      "Accès à un élément de tableau : arr?.[0]",
      "Déclaration de variable : let?.x = 5",
    ]),
    S("Que retourne `null?.toString()` ?", 0, ["undefined", "'null'", "Une erreur TypeError", "''"]),
    S("Avant l'introduction de `?.`, quelle syntaxe plus verbeuse devait-on utiliser pour le même résultat ?", 0, [
      "obj && obj.a && obj.a.b",
      "obj || obj.a || obj.a.b",
      "try { obj.a.b } catch {}",
      "obj.a.b directement sans vérification",
    ]),
  ]
);

quiz(
  "WeakMap et WeakSet",
  "Structures de données à références faibles pour éviter les fuites mémoire.",
  [
    S("Quelle est la principale différence entre WeakMap et Map concernant les clés ?", 0, [
      "Les clés de WeakMap doivent être des objets et sont faiblement référencées (éligibles au garbage collector)",
      "WeakMap n'accepte que des chaînes comme clés",
      "WeakMap est juste un alias de Map sans différence réelle",
      "WeakMap ne peut contenir que des nombres comme valeurs",
    ]),
    S("Pourquoi ne peut-on pas itérer (forEach, for...of) sur un WeakMap comme sur un Map classique ?", 0, [
      "Parce que ses entrées peuvent disparaître à tout moment via le garbage collector, rendant l'itération non déterministe",
      "Parce que WeakMap ne supporte que 0 ou 1 entrée",
      "C'est une limitation arbitraire sans rapport avec la mémoire",
      "En réalité on peut très bien itérer un WeakMap normalement",
    ]),
    S("Quel cas d'usage typique justifie l'utilisation d'un WeakMap ?", 0, [
      "Associer des métadonnées à un objet DOM sans empêcher sa libération mémoire quand il est retiré du DOM",
      "Stocker des données qui doivent persister indéfiniment en mémoire",
      "Remplacer tous les tableaux de l'application",
      "Stocker des chaînes de caractères comme clés",
    ]),
    TF("Un WeakSet ne peut contenir que des objets, pas des primitives comme des nombres ou des chaînes.", true),
    TF("WeakMap possède une propriété `size` comme Map pour connaître le nombre d'entrées.", false),
    M("Quelles méthodes existent sur une instance de WeakMap ?", [0, 1, 2], [
      "get()",
      "set()",
      "has()",
      "keys() (itération possible comme Map)",
    ]),
    S("Que retourne `new WeakMap().size` ?", 1, ["0", "undefined (la propriété size n'existe pas sur WeakMap)", "null", "Une erreur"]),
    S("Pourquoi WeakMap/WeakSet aident-ils à éviter les fuites mémoire par rapport à Map/Set classiques ?", 0, [
      "Parce qu'ils ne maintiennent pas leurs clés (objets) en vie artificiellement, permettant leur collecte par le garbage collector",
      "Parce qu'ils stockent les données sur le disque plutôt qu'en mémoire",
      "Parce qu'ils limitent le nombre d'entrées à 100",
      "Il n'y a en réalité aucune différence sur ce point",
    ]),
  ]
);
