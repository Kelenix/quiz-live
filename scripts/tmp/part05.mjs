import { quiz, S, M, TF } from "./gen-js.mjs";

quiz(
  "Opérateurs logiques court-circuit (&&, ||)",
  "Comprendre l'évaluation court-circuit des opérateurs logiques ET et OU.",
  [
    S("Que retourne `0 && 'texte'` ?", 0, ["0", "'texte'", "true", "false"]),
    S("Que retourne `'a' || 'b'` ?", 0, ["'a'", "'b'", "true", "false"]),
    S("Pourquoi appelle-t-on `&&` et `||` des opérateurs 'court-circuit' ?", 1, [
      "Ils provoquent toujours une erreur si une condition est fausse",
      "Ils arrêtent l'évaluation dès que le résultat final est déterminé, sans évaluer le reste",
      "Ils ne fonctionnent qu'avec des booléens stricts",
      "Ils inversent automatiquement la valeur évaluée",
    ]),
    TF("`null && console.log('jamais affiché')` n'affiche rien car `null` est falsy et court-circuite l'évaluation.", true),
    TF("`obj && obj.propriete` est un pattern courant pour éviter une erreur si `obj` est null ou undefined.", true),
    M("Quelles expressions utilisent correctement le court-circuit logique ?", [0, 1, 2], [
      "utilisateur && utilisateur.nom",
      "valeur || 'valeur par défaut'",
      "estConnecte && afficherProfil()",
      "x ?? y ?? z && w (combinaison invalide sans parenthèses entre ?? et &&)",
    ]),
    S("Que retourne `true && false || true` ?", 0, ["true", "false", "undefined", "Une erreur de syntaxe"]),
    S("Que retourne `null || undefined || 0 || 'dernier'` ?", 0, ["'dernier'", "null", "undefined", "0"]),
  ]
);

quiz(
  "Comparaison d'objets et de primitives",
  "Comprendre la différence entre comparaison par valeur et par référence.",
  [
    S("Que retourne `{a: 1} === {a: 1}` ?", 1, ["true", "false", "undefined", "Une erreur"]),
    S("Pourquoi deux objets ayant le même contenu ne sont-ils pas égaux avec `===` ?", 0, [
      "Parce que les objets sont comparés par référence (adresse mémoire), pas par valeur",
      "Parce que === ne fonctionne jamais avec des objets",
      "Parce que JavaScript compare uniquement les types",
      "Parce qu'il faut toujours utiliser Object.equals()",
    ]),
    S("Que retourne `const a = {x: 1}; const b = a; a === b;` ?", 0, ["true", "false", "undefined", "NaN"]),
    TF("Deux primitives (nombres, chaînes, booléens) de même valeur sont toujours égales avec ===.", true),
    TF("Modifier l'objet référencé par `b` dans `const a = {}; const b = a;` modifie également ce que `a` référence, car les deux pointent vers le même objet.", true),
    M("Quelles affirmations sur la comparaison d'objets sont correctes ?", [0, 1], [
      "Pour comparer le contenu de deux objets, il faut une comparaison profonde (deep equal) manuelle ou via une librairie",
      "Deux variables référençant le même objet sont égales avec === car elles partagent la même référence",
      "Object.is() effectue toujours une comparaison de contenu profonde des objets",
      "Les tableaux sont comparés élément par élément automatiquement avec ===",
    ]),
    S("Que retourne `[1, 2] === [1, 2]` ?", 1, ["true", "false", "undefined", "NaN"]),
    S("Quelle méthode JSON peut servir (avec ses limites) à comparer le contenu de deux objets simples ?", 0, [
      "JSON.stringify(a) === JSON.stringify(b)",
      "a.toString() === b",
      "a == b avec coercition",
      "Object.same(a, b)",
    ]),
  ]
);

quiz(
  "Closures avancées et gestion de la mémoire",
  "Approfondir l'usage des closures et leur impact sur le cycle de vie mémoire.",
  [
    S("Pourquoi une closure peut-elle empêcher le garbage collector de libérer une variable ?", 0, [
      "Parce que la fonction interne conserve une référence active à cette variable tant qu'elle existe",
      "Parce que les closures dupliquent la mémoire automatiquement",
      "Parce que JavaScript ne possède pas de garbage collector",
      "Les closures n'ont aucun impact sur la mémoire",
    ]),
    S("Quel pattern utilise une closure pour exposer uniquement certaines méthodes publiques tout en gardant un état privé ?", 0, [
      "Le pattern module (module pattern)",
      "Le pattern singleton uniquement",
      "Le pattern observer obligatoirement",
      "L'héritage de classe",
    ]),
    S(
      "Que retourne ce code ? `function creerCompteurs() { let total = 0; return { inc: () => ++total, get: () => total }; } const c = creerCompteurs(); c.inc(); c.inc(); c.get();`",
      1,
      ["0", "2", "1", "undefined"]
    ),
    TF("Plusieurs fonctions retournées par la même fonction englobante peuvent partager la même variable capturée par closure.", true),
    TF("Une closure copie la valeur des variables externes au moment où la fonction interne est définie, et ne reflète plus les changements ultérieurs.", false),
    M("Quelles utilisations pratiques des closures sont courantes ?", [0, 1, 2], [
      "Créer des fonctions de type 'curry' (application partielle d'arguments)",
      "Implémenter un debounce ou un throttle avec état interne",
      "Créer des variables privées encapsulées dans une factory function",
      "Remplacer entièrement les boucles for",
    ]),
    S("Que fait une fonction 'curry' typique illustrant les closures, comme `const add = a => b => a + b;` appelée `add(2)(3)` ?", 0, ["Retourne 5", "Retourne une fonction sans l'exécuter", "Lève une erreur", "Retourne undefined"]),
    S("Pourquoi peut-on dire qu'un long historique de closures non libérées dans une application web peut entraîner une fuite mémoire ?", 0, [
      "Parce que les références conservées empêchent le garbage collector de récupérer la mémoire associée tant qu'elles existent",
      "Parce que les closures sont stockées sur le disque",
      "Parce que chaque closure crée un nouveau thread",
      "Ce n'est jamais un problème en JavaScript",
    ]),
  ]
);

quiz(
  "Coercition avancée et pièges courants",
  "Cas particuliers et pièges fréquents liés à la conversion implicite de types.",
  [
    S("Que retourne `[] + []` ?", 1, ["[]", "'' (chaîne vide)", "0", "NaN"]),
    S("Que retourne `[] + {}` ?", 0, ["'[object Object]'", "0", "NaN", "undefined"]),
    S("Que retourne `1 + '1' + 1` ?", 1, ["3", "'111'", "12", "'21'"]),
    TF("`typeof NaN` retourne `'number'`, même si NaN signifie 'Not a Number'.", true),
    TF("`NaN === NaN` retourne `true`.", false),
    M("Quelles expressions retournent `NaN` ?", [0, 1, 2], [
      "Number('abc')",
      "0 / 0",
      "undefined + 1",
      "'5' - '3'",
    ]),
    S("Quelle fonction permet de vérifier de façon fiable si une valeur est NaN ?", 0, ["Number.isNaN()", "valeur === NaN", "typeof valeur === 'NaN'", "valeur.isNaN()"]),
    S("Que retourne `Boolean(NaN)` ?", 1, ["true", "false", "undefined", "NaN"]),
  ]
);

quiz(
  "Tableaux : includes, some, every et flat",
  "Méthodes complémentaires de test et d'aplatissement de tableaux.",
  [
    S("Quelle méthode retourne `true` si AU MOINS un élément du tableau satisfait une condition ?", 1, ["every()", "some()", "includes()", "filter()"]),
    S("Quelle méthode retourne `true` uniquement si TOUS les éléments satisfont une condition ?", 0, ["every()", "some()", "find()", "map()"]),
    S("Que retourne `[1, [2, 3], [4, [5]]].flat()` (profondeur 1) ?", 1, ["[1, 2, 3, 4, 5]", "[1, 2, 3, 4, [5]]", "[1, [2, 3], [4, [5]]]", "5"]),
    TF("`[1, 2, 3].includes(2)` retourne `true`.", true),
    TF("`[].every(x => x > 0)` sur un tableau vide retourne `false`.", false),
    M("Quelles affirmations sont correctes concernant some/every ?", [0, 1], [
      "some() s'arrête dès qu'il trouve un élément qui satisfait la condition (court-circuit)",
      "every() s'arrête dès qu'il trouve un élément qui NE satisfait PAS la condition",
      "some() et every() mutent toujours le tableau d'origine",
      "every() retourne toujours un tableau, jamais un booléen",
    ]),
    S("Que retourne `[2, 4, 6].every(x => x % 2 === 0)` ?", 0, ["true", "false", "[2,4,6]", "undefined"]),
    S("Quelle méthode permet d'aplatir un tableau ET de le transformer en une seule passe (équivalent map + flat) ?", 0, ["flatMap()", "mapFlat()", "reduceFlat()", "flatten()"]),
  ]
);

quiz(
  "Objets : Object.keys, values, entries et assign",
  "Manipuler les objets via les méthodes statiques de la classe Object.",
  [
    S("Quelle méthode retourne un tableau des clés (propriétés) propres d'un objet ?", 0, ["Object.keys()", "Object.values()", "Object.entries()", "Object.props()"]),
    S("Quelle méthode retourne un tableau des valeurs d'un objet ?", 1, ["Object.keys()", "Object.values()", "Object.entries()", "Object.list()"]),
    S("Que retourne `Object.entries({a: 1, b: 2})` ?", 0, ["[['a', 1], ['b', 2]]", "{a: 1, b: 2}", "['a', 'b']", "[1, 2]"]),
    TF("`Object.assign({}, {a: 1}, {b: 2})` retourne `{a: 1, b: 2}` en fusionnant les objets sources dans la cible.", true),
    TF("Object.keys() inclut les propriétés héritées via la chaîne de prototypes.", false),
    M("Quelles méthodes statiques de Object permettent de parcourir ou transformer un objet ?", [0, 1, 2], [
      "Object.keys()",
      "Object.values()",
      "Object.entries()",
      "Object.map()",
    ]),
    S("Quelle syntaxe moderne crée une copie superficielle d'un objet, alternative à Object.assign ?", 0, ["{...obj}", "obj.copy()", "new Object(obj)", "Object.duplicate(obj)"]),
    S("Que retourne `Object.fromEntries([['a', 1], ['b', 2]])` ?", 0, ["{a: 1, b: 2}", "[['a',1],['b',2]]", "['a','b']", "undefined"]),
  ]
);

quiz(
  "Promise.all, Promise.race et Promise.allSettled",
  "Combiner plusieurs Promises selon différentes stratégies d'attente.",
  [
    S("Que retourne `Promise.race([p1, p2])` ?", 0, [
      "Une Promise résolue ou rejetée dès que la première parmi p1 et p2 se termine",
      "Un tableau contenant les résultats des deux Promises",
      "Toujours la Promise p1 en priorité",
      "Une erreur si plus d'une Promise est passée",
    ]),
    S("Que se passe-t-il avec `Promise.all([p1, p2])` si UNE des deux Promises est rejetée ?", 1, [
      "Promise.all attend que toutes les autres se terminent avant de se rejeter",
      "Promise.all se rejette immédiatement avec la raison du premier rejet rencontré",
      "Promise.all ignore l'erreur et continue",
      "Cela provoque une boucle infinie",
    ]),
    S("Quelle méthode attend que TOUTES les Promises se terminent (résolues ou rejetées), sans jamais rejeter elle-même ?", 2, ["Promise.all()", "Promise.race()", "Promise.allSettled()", "Promise.any()"]),
    TF("Promise.any() se résout dès qu'UNE des Promises est résolue avec succès, et ne se rejette que si TOUTES échouent.", true),
    TF("Promise.all() exécute les Promises les unes après les autres de façon séquentielle (pas en parallèle).", false),
    M("Quelles méthodes statiques existent réellement sur l'objet Promise ?", [0, 1, 2], [
      "Promise.all()",
      "Promise.race()",
      "Promise.allSettled()",
      "Promise.sequence()",
    ]),
    S("Quel est le format d'un élément du tableau retourné par `Promise.allSettled()` ?", 0, [
      "{ status: 'fulfilled' | 'rejected', value ou reason }",
      "Juste la valeur résolue, sans statut",
      "Un booléen indiquant succès ou échec",
      "Une nouvelle Promise imbriquée",
    ]),
    S("Pourquoi privilégier `Promise.allSettled()` plutôt que `Promise.all()` dans certains cas ?", 0, [
      "Pour obtenir le résultat de chaque Promise même si certaines échouent, sans interrompre les autres",
      "Parce que Promise.all() est dépréciée",
      "Parce que allSettled() est plus rapide dans tous les cas",
      "Il n'y a aucune différence pratique",
    ]),
  ]
);

quiz(
  "Event loop : approfondissement microtasks/macrotasks",
  "Cas avancés d'ordonnancement entre Promises, setTimeout et code synchrone.",
  [
    S(
      "Quel est l'ordre d'affichage de : `setTimeout(() => console.log(1), 0); Promise.resolve().then(() => console.log(2)); console.log(3);` ?",
      1,
      ["1, 2, 3", "3, 2, 1", "3, 1, 2", "2, 3, 1"]
    ),
    S("Pourquoi une Promise résolue s'exécute-t-elle avant un setTimeout(fn, 0), même si les deux sont planifiés au même moment ?", 0, [
      "Parce que la file des microtâches est vidée entièrement avant de traiter la prochaine macrotâche",
      "Parce que setTimeout a toujours un délai minimum de 1000ms",
      "Parce que les Promises s'exécutent de façon synchrone",
      "Ce n'est pas vrai, l'ordre est aléatoire",
    ]),
    S(
      "Si on enchaîne `Promise.resolve().then(() => Promise.resolve()).then(() => console.log('fin'))` après un `console.log('debut')`, quel est l'ordre d'affichage ?",
      0,
      ["debut, fin", "fin, debut", "Les deux s'affichent simultanément", "Erreur"]
    ),
    TF("Une boucle synchrone très longue (bloquante) retarde l'exécution de toutes les microtâches et macrotâches en attente.", true),
    TF("requestAnimationFrame est traité comme une microtâche au même niveau de priorité que les Promises.", false),
    M("Quelles affirmations sur l'ordonnancement des tâches sont correctes ?", [0, 1, 2], [
      "Le code synchrone s'exécute toujours avant toute microtâche ou macrotâche",
      "Toutes les microtâches en attente sont traitées avant la macrotâche suivante",
      "async/await utilise les mêmes mécanismes de microtâches que les Promises classiques",
      "setTimeout(fn, 0) garantit une exécution immédiate, sans délai",
    ]),
    S("Quel type de tâche est ajouté à la file lorsqu'on utilise `queueMicrotask(fn)` ?", 0, ["Une microtâche", "Une macrotâche", "Une tâche synchrone immédiate", "Aucune, cela lève une erreur"]),
    S("Dans quel ordre s'exécutent en général : code synchrone, microtâches, macrotâches ?", 0, [
      "Synchrone, puis microtâches, puis macrotâches",
      "Macrotâches, puis microtâches, puis synchrone",
      "Microtâches, puis synchrone, puis macrotâches",
      "L'ordre est totalement aléatoire",
    ]),
  ]
);

quiz(
  "POO avancée : méthodes statiques, getters et setters",
  "Approfondir les classes avec accesseurs et membres de classe.",
  [
    S("Quel mot-clé définit un accesseur en lecture qui se comporte comme une propriété plutôt qu'une méthode appelée ?", 0, ["get", "static", "set", "readonly"]),
    S("Quel mot-clé définit une méthode qui s'exécute lors d'une affectation à une propriété, comme `obj.x = 5`?", 2, ["get", "static", "set", "assign"]),
    S("Comment appelle-t-on une propriété de classe précédée du symbole `#`, comme `#valeur` ?", 1, ["Une propriété statique", "Une propriété privée", "Une propriété protégée par convention uniquement", "Une propriété en lecture seule"]),
    TF("Les champs privés (#nom) d'une classe ne sont accessibles que depuis l'intérieur de la classe elle-même.", true),
    TF("Une méthode statique peut accéder directement à `this` représentant une instance particulière de la classe.", false),
    M("Quelles affirmations sur les getters/setters de classe sont correctes ?", [0, 1, 2], [
      "Un getter permet d'accéder à une valeur calculée comme s'il s'agissait d'une propriété simple",
      "Un setter peut valider ou transformer une valeur avant de l'assigner à un champ interne",
      "On peut combiner un champ privé avec un getter/setter public pour encapsuler l'accès",
      "Les getters doivent obligatoirement être déclarés static",
    ]),
    S("Dans `class Cercle { get aire() { return Math.PI * this.rayon ** 2; } }`, comment accède-t-on à l'aire d'une instance `c` ?", 0, ["c.aire", "c.aire()", "c.getAire()", "Cercle.aire(c)"]),
    S("Quel est l'avantage principal des champs privés (#nom) introduits récemment en JavaScript ?", 0, [
      "Garantir une réelle encapsulation, inaccessible même via du code extérieur malveillant ou accidentel",
      "Accélérer l'exécution du code de moitié",
      "Permettre l'héritage multiple",
      "Remplacer complètement les méthodes statiques",
    ]),
  ]
);
