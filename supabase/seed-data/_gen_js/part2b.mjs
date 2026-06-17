import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Déclarations de fonctions",
    "Function declaration, function expression et leur hoisting.",
    [
      S(
        "Comment appelle-t-on une fonction définie avec le mot-clé function et un nom, au niveau supérieur d'un bloc ?",
        "Une déclaration de fonction (function declaration)",
        ["Une expression de fonction", "Une fonction fléchée", "Une fonction anonyme"]
      ),
      TF("Une déclaration de fonction est hissée (hoisted) avec son corps complet, on peut l'appeler avant sa définition dans le code.", true),
      S(
        "Qu'est-ce qu'une expression de fonction (function expression) ?",
        "Une fonction assignée à une variable, évaluée à l'endroit où elle apparaît",
        ["Une fonction qui retourne toujours une expression mathématique", "Un synonyme de fonction fléchée", "Une fonction qui ne peut pas avoir de nom"]
      ),
      M(
        "Quelles affirmations sur les fonctions anonymes sont vraies ?",
        ["Elles n'ont pas de nom propre", "Elles sont souvent utilisées comme callbacks"],
        ["Elles sont toujours hissées comme les déclarations", "Elles ne peuvent jamais être assignées à une variable"]
      ),
      S(
        "Que se passe-t-il si on appelle une fonction définie par une expression de fonction avant sa ligne de définition ?",
        "Une erreur (TypeError ou ReferenceError selon le cas)",
        ["La fonction s'exécute normalement", "undefined est retourné silencieusement", "La fonction est automatiquement hissée"]
      ),
      TF("Une fonction peut être passée en argument à une autre fonction en JavaScript.", true),
    ]
  ),

  Quiz(
    "JS — Fonctions fléchées (arrow functions)",
    "Syntaxe et particularités des fonctions fléchées introduites par ES6.",
    [
      S(
        "Quelle syntaxe définit une fonction fléchée simple prenant un paramètre x et retournant x * 2 ?",
        "x => x * 2",
        ["function x => x * 2", "=> x { x * 2 }", "x -> x * 2"]
      ),
      TF("Une fonction fléchée ne possède pas son propre this, elle hérite de celui du contexte englobant.", true),
      S(
        "Quel mot-clé/objet n'est PAS disponible dans une fonction fléchée ?",
        "arguments",
        ["this (hérité)", "des paramètres", "une valeur de retour"]
      ),
      M(
        "Quelles affirmations sur les fonctions fléchées sont correctes ?",
        ["Elles ne peuvent pas être utilisées comme constructeurs avec new", "Elles n'ont pas leur propre objet arguments"],
        ["Elles ont toujours leur propre this", "Elles sont hissées comme les déclarations de fonction"]
      ),
      TF("On peut omettre les parenthèses autour d'un seul paramètre dans une fonction fléchée : x => x + 1.", true),
      S(
        "Pourquoi évite-t-on les fonctions fléchées pour définir des méthodes d'objet qui utilisent this ?",
        "Parce que this ne référencera pas l'objet mais le contexte englobant",
        ["Parce que c'est une erreur de syntaxe", "Parce que les fonctions fléchées sont plus lentes", "Parce que cela empêche le hoisting"]
      ),
    ]
  ),

  Quiz(
    "JS — Hoisting",
    "Le mécanisme de hissage des déclarations en JavaScript.",
    [
      S(
        "Qu'est-ce que le hoisting en JavaScript ?",
        "Le déplacement conceptuel des déclarations vers le haut de leur portée avant l'exécution",
        ["Une optimisation qui supprime le code mort", "Un mécanisme de compilation à la volée", "Une fonctionnalité réservée aux classes"]
      ),
      TF("Les variables déclarées avec var sont hissées et initialisées à undefined.", true),
      TF("Les variables déclarées avec let et const sont hissées mais restent inaccessibles avant leur déclaration (zone morte temporelle).", true),
      S(
        "Comment appelle-t-on la zone où let/const existent mais ne sont pas encore accessibles ?",
        "La zone morte temporelle (temporal dead zone)",
        ["La zone d'exclusion", "Le scope fantôme", "La zone non définie"]
      ),
      M(
        "Quels éléments sont concernés par le hoisting ?",
        ["Les déclarations de fonctions (function declaration)", "Les déclarations var"],
        ["Les expressions de fonctions fléchées", "Les imports de modules sans hoisting"]
      ),
      S(
        "Que retourne console.log(x); var x = 5; (exécuté dans cet ordre) ?",
        "undefined",
        ["5", "Une erreur ReferenceError", "null"]
      ),
    ]
  ),

  Quiz(
    "JS — Closures",
    "Le concept de fermeture (closure) et ses cas d'usage.",
    [
      S(
        "Qu'est-ce qu'une closure en JavaScript ?",
        "Une fonction qui conserve l'accès aux variables de sa portée lexicale même après que la fonction englobante a terminé son exécution",
        ["Une fonction qui ne prend aucun paramètre", "Un objet qui empêche la modification de ses propriétés", "Une boucle infinie volontaire"]
      ),
      TF("Une closure permet de créer des variables privées en encapsulant l'état dans une fonction englobante.", true),
      S(
        "Dans l'exemple d'un compteur créé par une fonction qui retourne une fonction interne incrémentant une variable, comment appelle-t-on ce mécanisme ?",
        "Une closure",
        ["Un callback", "Une promesse", "Un générateur"]
      ),
      M(
        "Quels cas d'usage typiques exploitent les closures ?",
        ["Créer des fonctions factory paramétrées", "Implémenter l'encapsulation de données privées"],
        ["Convertir une chaîne en nombre", "Trier un tableau par ordre alphabétique"]
      ),
      TF("Une closure peut provoquer des fuites de mémoire si elle retient des références inutiles trop longtemps.", true),
      S(
        "Que retient une closure exactement ?",
        "Une référence vers les variables de la portée englobante, pas une copie",
        ["Une copie figée des variables au moment de la création", "Uniquement les variables globales", "Rien, le terme est un abus de langage"]
      ),
    ]
  ),

  Quiz(
    "JS — Le mot-clé this",
    "Comprendre comment la valeur de this est déterminée selon le contexte d'appel.",
    [
      S(
        "Dans une méthode d'objet classique (function), à quoi this fait-il référence ?",
        "À l'objet qui appelle la méthode",
        ["Toujours à l'objet global", "Toujours à undefined", "À la fonction elle-même"]
      ),
      TF("Dans une fonction fléchée définie au niveau global, this correspond au this du contexte englobant (souvent l'objet global ou undefined en module).", true),
      S(
        "Que vaut this dans une fonction normale appelée seule, sans objet, en mode strict ?",
        "undefined",
        ["L'objet global (window)", "null", "La fonction elle-même"]
      ),
      M(
        "Quelles méthodes permettent de modifier explicitement la valeur de this lors d'un appel de fonction ?",
        ["call()", "apply()", "bind()"],
        ["toString()"]
      ),
      TF("bind() crée une nouvelle fonction avec un this fixé, sans l'exécuter immédiatement.", true),
      S(
        "Quelle est la différence entre call() et apply() ?",
        "call() prend les arguments séparés par des virgules, apply() prend un tableau d'arguments",
        ["Aucune différence", "apply() ne fonctionne que sur les tableaux", "call() ne permet pas de définir this"]
      ),
    ]
  ),

  Quiz(
    "JS — IIFE (fonctions immédiatement invoquées)",
    "Le pattern IIFE pour créer une portée isolée et exécuter du code immédiatement.",
    [
      S(
        "Que signifie l'acronyme IIFE ?",
        "Immediately Invoked Function Expression",
        ["Internal Inline Function Execution", "Iterative Init Function Element", "Indexed Immutable Function Expression"]
      ),
      S(
        "Quelle syntaxe représente une IIFE correcte ?",
        "(function() { /* code */ })();",
        ["function() { /* code */ }();", "function { /* code */ }();", "(function() { /* code */ });()"]
      ),
      TF("Une IIFE permet de créer une portée isolée et d'éviter de polluer l'espace de noms global.", true),
      M(
        "Pourquoi utilisait-on des IIFE avant l'arrivée des modules ES et du bloc-scope ?",
        ["Pour encapsuler des variables sans les exposer globalement", "Pour exécuter du code d'initialisation une seule fois"],
        ["Pour créer des boucles infinies", "Pour remplacer les Promises"]
      ),
      TF("Une IIFE peut être écrite avec une fonction fléchée : (() => { /* code */ })();", true),
      S(
        "Quel est l'avantage principal d'une IIFE par rapport à une simple déclaration de fonction suivie d'un appel ?",
        "Elle ne crée pas de nom de fonction visible dans la portée englobante",
        ["Elle est plus rapide à l'exécution", "Elle empêche tout accès aux closures", "Elle permet d'utiliser this de façon globale"]
      ),
    ]
  ),

  Quiz(
    "JS — Mode strict ('use strict')",
    "Le mode strict et ses effets sur l'exécution du code.",
    [
      S(
        "Comment active-t-on le mode strict dans un script ?",
        "En ajoutant la directive 'use strict'; en haut du fichier ou de la fonction",
        ["En ajoutant #!strict en haut du fichier", "En utilisant l'attribut HTML strict=true", "En renommant le fichier en .strict.js"]
      ),
      TF("En mode strict, assigner une valeur à une variable non déclarée lève une erreur.", true),
      M(
        "Quels comportements changent en mode strict ?",
        ["this est undefined dans une fonction appelée sans contexte", "Les variables globales accidentelles sont interdites"],
        ["Les boucles for deviennent obligatoires", "Les template literals sont désactivés"]
      ),
      TF("Les modules ES (import/export) sont automatiquement en mode strict.", true),
      S(
        "Quel est l'objectif principal du mode strict ?",
        "Détecter des erreurs silencieuses et imposer des règles plus sûres",
        ["Accélérer l'exécution du code de 50%", "Désactiver les fonctions fléchées", "Permettre l'utilisation de var uniquement"]
      ),
      S(
        "Peut-on désactiver le mode strict une fois activé dans un fichier ?",
        "Non, une fois activé en haut du fichier il s'applique à tout le fichier",
        ["Oui avec 'use loose';", "Oui en redéfinissant les variables", "Oui avec un commentaire spécial"]
      ),
    ]
  ),

  Quiz(
    "JS — Fonctions d'ordre supérieur",
    "Les fonctions qui prennent ou retournent d'autres fonctions.",
    [
      S(
        "Qu'est-ce qu'une fonction d'ordre supérieur (higher-order function) ?",
        "Une fonction qui prend une ou plusieurs fonctions en paramètre, et/ou qui retourne une fonction",
        ["Une fonction qui s'exécute plus vite que les autres", "Une fonction définie avec class", "Une fonction qui ne retourne jamais de valeur"]
      ),
      M(
        "Lesquelles de ces méthodes de tableau sont des fonctions d'ordre supérieur ?",
        ["map()", "filter()", "reduce()"],
        ["length", "push() seul sans callback"]
      ),
      TF("Une fonction qui retourne une autre fonction (comme une factory de fonctions) est aussi une fonction d'ordre supérieur.", true),
      S(
        "Pourquoi les fonctions d'ordre supérieur favorisent-elles un style de programmation fonctionnelle ?",
        "Parce qu'elles permettent de composer et réutiliser des comportements sans dupliquer de code",
        ["Parce qu'elles interdisent l'utilisation de boucles", "Parce qu'elles ne peuvent pas avoir d'effets de bord", "Parce qu'elles remplacent les classes"]
      ),
      TF("setTimeout est un exemple de fonction d'ordre supérieur car elle accepte une fonction callback en argument.", true),
      S(
        "Quel terme désigne une fonction retournée par une autre fonction, qui se souvient de l'environnement où elle a été créée ?",
        "Une closure",
        ["Un singleton", "Un proxy", "Un mixin"]
      ),
    ]
  ),

  Quiz(
    "JS — Currying",
    "Transformer une fonction à plusieurs arguments en une séquence de fonctions à un argument.",
    [
      S(
        "Qu'est-ce que le currying en programmation fonctionnelle ?",
        "Transformer une fonction prenant plusieurs arguments en une suite de fonctions prenant chacune un seul argument",
        ["Une technique d'optimisation mémoire", "Une méthode de tri de tableaux", "Un type de boucle spécial"]
      ),
      S(
        "Quelle expression illustre une fonction curryfiée pour additionner deux nombres ?",
        "const add = a => b => a + b;",
        ["const add = (a, b) => a + b;", "const add = function(a, b) { return a + b; }", "const add = a, b => a + b;"]
      ),
      TF("Le currying permet de créer facilement des fonctions partiellement appliquées et réutilisables.", true),
      M(
        "Quels avantages apporte le currying ?",
        ["Faciliter la réutilisation de fonctions spécialisées", "Permettre une composition de fonctions plus claire"],
        ["Réduire automatiquement la complexité algorithmique", "Remplacer entièrement les Promises"]
      ),
      S(
        "Avec add = a => b => a + b, que retourne add(2)(3) ?",
        "5",
        ["23", "undefined", "Une erreur de syntaxe"]
      ),
      TF("Une fonction curryfiée appelée avec un seul argument retourne généralement une nouvelle fonction en attente du ou des arguments suivants.", true),
    ]
  ),

  Quiz(
    "JS — Paramètres par défaut et arguments",
    "Les valeurs par défaut des paramètres et l'objet arguments.",
    [
      S(
        "Comment définir une valeur par défaut pour un paramètre de fonction ?",
        "function f(x = 10) { }",
        ["function f(x ?? 10) { }", "function f(x default 10) { }", "function f(x : 10) { }"]
      ),
      TF("L'objet arguments contient tous les arguments passés à une fonction classique, même ceux sans paramètre nommé correspondant.", true),
      S(
        "Une fonction fléchée a-t-elle accès à l'objet arguments ?",
        "Non, elle doit utiliser les paramètres rest pour un comportement équivalent",
        ["Oui, comme une fonction classique", "Seulement si elle est nommée", "Seulement en mode strict"]
      ),
      M(
        "Quelles affirmations sur les paramètres par défaut sont vraies ?",
        ["Ils peuvent référencer des paramètres précédents dans la liste", "Ils ne s'appliquent que si l'argument est undefined"],
        ["Ils s'appliquent même si l'argument vaut null", "Ils sont obligatoires pour tous les paramètres"]
      ),
      TF("function f(a, b = a + 1) est une syntaxe valide en JavaScript.", true),
      S(
        "Que retourne f(undefined) si f est définie par function f(x = 5) { return x; } ?",
        "5",
        ["undefined", "NaN", "Une erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Callbacks et callback hell",
    "Les fonctions de rappel et le problème d'imbrication excessive.",
    [
      S(
        "Qu'est-ce qu'un callback en JavaScript ?",
        "Une fonction passée en argument à une autre fonction, exécutée plus tard",
        ["Une fonction qui s'auto-exécute en boucle", "Un type de variable globale", "Une méthode réservée aux tableaux"]
      ),
      TF("Le 'callback hell' désigne un code difficile à lire dû à de multiples callbacks imbriqués.", true),
      M(
        "Quelles solutions modernes permettent d'éviter le callback hell ?",
        ["Les Promises", "async/await"],
        ["Augmenter le nombre de callbacks imbriqués", "Utiliser uniquement des boucles for"]
      ),
      S(
        "Quel est un inconvénient majeur du callback hell ?",
        "Un code difficile à lire, déboguer et maintenir à cause de l'imbrication",
        ["Une exécution plus rapide du programme", "Une réduction automatique de la mémoire utilisée", "Aucun inconvénient, c'est juste un style"]
      ),
      TF("setTimeout(callback, 1000) exécute le callback après au moins 1000 millisecondes.", true),
      S(
        "Dans une fonction asynchrone basée sur callback, comment gère-t-on classiquement les erreurs ?",
        "En passant l'erreur comme premier argument du callback (convention error-first)",
        ["En utilisant uniquement try/catch autour du callback", "Les erreurs ne peuvent pas être gérées avec des callbacks", "En relançant automatiquement la fonction"]
      ),
    ]
  ),

  Quiz(
    "JS — Debounce et throttle (notions)",
    "Les techniques de limitation de fréquence d'exécution de fonctions.",
    [
      S(
        "Que fait une fonction de debounce ?",
        "Elle retarde l'exécution d'une fonction jusqu'à ce qu'un délai sans nouvel appel soit passé",
        ["Elle exécute la fonction immédiatement à chaque appel", "Elle bloque définitivement les appels suivants", "Elle dédouble chaque appel de fonction"]
      ),
      S(
        "Que fait une fonction de throttle ?",
        "Elle limite l'exécution d'une fonction à une fois maximum par intervalle de temps donné",
        ["Elle empêche toute exécution de la fonction", "Elle exécute la fonction un nombre infini de fois", "Elle convertit la fonction en Promise"]
      ),
      TF("Le debounce est souvent utilisé pour limiter les appels lors de la saisie dans un champ de recherche.", true),
      M(
        "Dans quels cas d'usage le throttle est-il pertinent ?",
        ["Limiter la fréquence de gestion d'un événement de scroll", "Limiter les appels lors d'un redimensionnement de fenêtre (resize)"],
        ["Empêcher complètement un événement de se déclencher", "Remplacer toutes les Promises d'une application"]
      ),
      TF("Debounce et throttle utilisent généralement setTimeout ou des horodatages pour gérer le délai.", true),
      S(
        "Quelle est la différence clé entre debounce et throttle ?",
        "Le debounce attend une pause dans les appels, le throttle exécute à intervalles réguliers même si les appels continuent",
        ["Ils sont strictement identiques", "Le throttle attend une pause, le debounce exécute à intervalles réguliers", "Le debounce ne fonctionne que sur les clics"]
      ),
    ]
  ),
];
