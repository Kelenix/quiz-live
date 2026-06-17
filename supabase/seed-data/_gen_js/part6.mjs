import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Itérateurs et protocole d'itération",
    "Le protocole itérable et la méthode Symbol.iterator.",
    [
      S(
        "Qu'est-ce qu'un itérateur en JavaScript ?",
        "Un objet possédant une méthode next() qui retourne { value, done }",
        ["Un type de boucle spécifique au langage", "Un objet qui ne peut être utilisé qu'avec les tableaux", "Une fonction qui trie automatiquement les données"]
      ),
      TF("Un objet est dit itérable s'il implémente la méthode Symbol.iterator.", true),
      S(
        "Que retourne la méthode next() d'un itérateur lorsqu'il n'y a plus de valeurs à produire ?",
        "Un objet { value: undefined, done: true }",
        ["Une exception automatique", "null directement", "Un tableau vide"]
      ),
      M(
        "Quelles structures natives implémentent le protocole itérable ?",
        ["Array", "Map", "Set"],
        ["Object littéral simple sans configuration"]
      ),
      TF("On peut rendre un objet personnalisé itérable en lui ajoutant une méthode [Symbol.iterator].", true),
      S(
        "Quelle instruction permet de parcourir directement un objet itérable sans appeler next() manuellement ?",
        "for...of",
        ["for...in", "while(true)", "forEach() sur tout objet"]
      ),
    ]
  ),

  Quiz(
    "JS — Copie superficielle vs profonde",
    "Différencier shallow copy et deep copy d'objets et tableaux.",
    [
      S(
        "Qu'est-ce qu'une copie superficielle (shallow copy) d'un objet ?",
        "Une copie qui duplique le premier niveau de propriétés, mais partage les références des objets imbriqués",
        ["Une copie qui duplique absolument tout, à tous les niveaux", "Une copie qui ne fonctionne que sur les tableaux", "Une copie qui transforme l'objet en chaîne JSON"]
      ),
      TF("L'opérateur spread { ...objet } effectue une copie superficielle, pas une copie profonde.", true),
      S(
        "Quelle méthode native (plus récente) permet d'effectuer une copie profonde d'un objet sérialisable ?",
        "structuredClone()",
        ["Object.deepCopy()", "Array.clone()", "JSON.deepClone()"]
      ),
      M(
        "Quelles techniques sont couramment utilisées pour copier un objet (avec leurs limites) ?",
        ["Object.assign({}, objet) — copie superficielle", "JSON.parse(JSON.stringify(objet)) — copie profonde mais perd fonctions et certains types"],
        ["objet.toString() — copie complète garantie", "delete objet — copie l'objet avant suppression"]
      ),
      TF("Modifier un objet imbriqué obtenu par copie superficielle modifie aussi l'objet original correspondant.", true),
      S(
        "Pourquoi JSON.parse(JSON.stringify(objet)) n'est-il pas une solution universelle de copie profonde ?",
        "Parce qu'il perd les fonctions, undefined, Symbol, Date (converties en chaînes), et ne gère pas les références circulaires",
        ["Parce qu'il est plus lent que toutes les autres méthodes", "Parce qu'il ne fonctionne que sur les tableaux", "Parce qu'il duplique les fonctions correctement contrairement aux croyances"]
      ),
    ]
  ),

  Quiz(
    "JS — Égalité et comparaison d'objets",
    "Comprendre pourquoi deux objets similaires ne sont pas toujours égaux.",
    [
      S(
        "Pourquoi { a: 1 } === { a: 1 } retourne false en JavaScript ?",
        "Parce que les objets sont comparés par référence et non par valeur de leur contenu",
        ["Parce que les deux objets ont des clés différentes", "Parce que === ne fonctionne pas sur les objets", "C'est une erreur du moteur JavaScript"]
      ),
      TF("Deux variables référençant le même objet en mémoire sont égales avec ===.", true),
      S(
        "Comment comparer le contenu de deux objets en profondeur en JavaScript natif (sans bibliothèque) ?",
        "En comparant manuellement leurs propriétés (ou via JSON.stringify avec ses limites)",
        ["Avec l'opérateur === directement", "Avec l'opérateur == qui compare le contenu", "Ce n'est jamais possible en JavaScript"]
      ),
      M(
        "Quelles affirmations sur la comparaison de tableaux sont vraies ?",
        ["[1,2] === [1,2] retourne false car ce sont deux références différentes", "Comparer deux tableaux nécessite souvent de comparer élément par élément"],
        ["[1,2] == [1,2] retourne toujours true", "Les tableaux sont comparés par valeur nativement"]
      ),
      TF("const a = {}; const b = a; a === b retourne true car b référence le même objet que a.", true),
      S(
        "Quelle méthode permet de comparer deux valeurs avec une sémantique légèrement différente de === (utile pour NaN et -0/+0) ?",
        "Object.is()",
        ["Object.equals()", "Object.compare()", "Array.is()"]
      ),
    ]
  ),

  Quiz(
    "JS — Immutabilité avec Object.freeze",
    "Empêcher la modification d'un objet avec Object.freeze().",
    [
      S(
        "Que fait Object.freeze() sur un objet ?",
        "Il empêche l'ajout, la suppression et la modification de ses propriétés existantes",
        ["Il supprime toutes les propriétés de l'objet", "Il convertit l'objet en chaîne JSON figée", "Il clone l'objet en lecture seule sur le serveur"]
      ),
      TF("Object.isFrozen() permet de vérifier si un objet a été figé avec Object.freeze().", true),
      S(
        "Object.freeze() effectue-t-il un gel profond (deep freeze) par défaut ?",
        "Non, seul le premier niveau de propriétés est figé ; les objets imbriqués restent modifiables",
        ["Oui, tous les niveaux sont figés automatiquement", "Cela dépend du navigateur utilisé", "Cela dépend du type de données contenu"]
      ),
      M(
        "Quelles méthodes permettent de restreindre la modification d'un objet ?",
        ["Object.freeze()", "Object.seal()"],
        ["Object.lock()", "Object.protect()"]
      ),
      TF("En mode strict, tenter de modifier une propriété d'un objet figé lève une erreur TypeError.", true),
      S(
        "Quelle est la différence entre Object.seal() et Object.freeze() ?",
        "seal() empêche d'ajouter/supprimer des propriétés mais permet de modifier les valeurs existantes, freeze() empêche aussi la modification",
        ["Ce sont des synonymes stricts", "seal() est plus restrictif que freeze()", "freeze() ne fonctionne que sur les tableaux"]
      ),
    ]
  ),

  Quiz(
    "JS — Conversion d'objets en primitives",
    "Les méthodes toString() et valueOf() lors des conversions implicites.",
    [
      S(
        "Quelle méthode un objet utilise-t-il par défaut pour se convertir en chaîne de caractères ?",
        "toString()",
        ["valueOf() en priorité absolue", "stringify()", "toPrimitive() uniquement"]
      ),
      TF("Pour un objet personnalisé, on peut redéfinir toString() afin de contrôler sa représentation textuelle.", true),
      S(
        "Que retourne par défaut ({}).toString() pour un objet littéral simple ?",
        "'[object Object]'",
        ["'{}'", "undefined", "'null'"]
      ),
      M(
        "Quelles méthodes interviennent dans la conversion implicite d'un objet en primitive ?",
        ["toString()", "valueOf()"],
        ["parseInt()"]
      ),
      TF("On peut personnaliser totalement la conversion d'un objet avec la méthode Symbol.toPrimitive.", true),
      S(
        "Dans un contexte numérique (comme une soustraction), quelle méthode est généralement privilégiée pour convertir un objet ?",
        "valueOf()",
        ["toString() en priorité absolue", "JSON.stringify()", "Aucune conversion n'est tentée"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux : recherche et tests",
    "Les méthodes indexOf, includes, lastIndexOf pour rechercher dans un tableau.",
    [
      S(
        "Quelle méthode retourne l'index de la première occurrence d'une valeur dans un tableau, ou -1 si absente ?",
        "indexOf()",
        ["includes()", "find()", "search()"]
      ),
      S(
        "Quelle méthode retourne un booléen indiquant si une valeur est présente dans un tableau ?",
        "includes()",
        ["indexOf() retourne déjà un booléen", "contains()", "hasValue()"]
      ),
      TF("includes() utilise une comparaison stricte pour déterminer si une valeur est présente.", true),
      M(
        "Quelles méthodes permettent de localiser un élément dans un tableau selon des critères différents ?",
        ["indexOf() pour une valeur exacte", "findIndex() pour une condition via callback"],
        ["sort() pour localiser un élément", "join() pour rechercher un élément"]
      ),
      TF("indexOf() ne fonctionne pas avec NaN car NaN n'est égal à rien, même lui-même ; includes() gère ce cas correctement.", true),
      S(
        "Quelle méthode retourne l'index de la dernière occurrence d'une valeur dans un tableau ?",
        "lastIndexOf()",
        ["indexOf() en partant de la fin automatiquement", "findLast()", "reverse().indexOf()"]
      ),
    ]
  ),

  Quiz(
    "JS — Conversion entre tableaux et chaînes",
    "join(), split() et Array.from() pour convertir entre tableaux et chaînes.",
    [
      S(
        "Quelle méthode convertit un tableau en chaîne de caractères avec un séparateur donné ?",
        "join()",
        ["split()", "toString() avec un argument séparateur", "concat()"]
      ),
      S(
        "Quelle méthode découpe une chaîne en tableau selon un séparateur ?",
        "split()",
        ["join()", "slice()", "divide()"]
      ),
      TF("'a,b,c'.split(',') retourne ['a', 'b', 'c'].", true),
      M(
        "Quelles façons permettent de créer un tableau à partir d'un objet itérable ou similaire à un tableau ?",
        ["Array.from()", "L'opérateur spread [...iterable]"],
        ["JSON.parse() directement sur n'importe quelle valeur", "Array.toArray()"]
      ),
      TF("['a', 'b', 'c'].join('-') retourne 'a-b-c'.", true),
      S(
        "Que retourne Array.from({length: 3}, (_, i) => i * 2) ?",
        "[0, 2, 4]",
        ["[1, 2, 3]", "[0, 1, 2]", "Une erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Opérateurs d'affectation composés",
    "Les raccourcis +=, -=, *=, /=, &&=, ||=, ??=.",
    [
      S(
        "Que fait l'opérateur += dans x += 5 ?",
        "Il équivaut à x = x + 5",
        ["Il équivaut à x = 5", "Il équivaut à x = x * 5", "Il déclare une nouvelle variable x"]
      ),
      TF("L'opérateur ||= assigne la valeur de droite seulement si la variable de gauche est falsy.", true),
      TF("L'opérateur &&= assigne la valeur de droite seulement si la variable de gauche est truthy.", true),
      M(
        "Quels opérateurs d'affectation composés existent en JavaScript moderne ?",
        ["??=", "||=", "&&="],
        ["**=  n'existe pas du tout (affirmation fausse à exclure)"]
      ),
      S(
        "Que vaut x après let x = 0; x ||= 10; ?",
        "10",
        ["0", "undefined", "NaN"]
      ),
      S(
        "Que vaut x après let x = 0; x ??= 10; ?",
        "0",
        ["10", "undefined", "NaN"]
      ),
    ]
  ),

  Quiz(
    "JS — Comparaison de chaînes et méthodes string utiles",
    "Les méthodes courantes pour manipuler des chaînes de caractères.",
    [
      S(
        "Quelle méthode retourne une portion d'une chaîne entre deux index ?",
        "slice()",
        ["splice()", "cut()", "part()"]
      ),
      S(
        "Quelle méthode retire les espaces en début et fin de chaîne ?",
        "trim()",
        ["clean()", "strip()", "removeSpaces()"]
      ),
      TF("includes() sur une chaîne vérifie si une sous-chaîne est présente, comme pour les tableaux.", true),
      M(
        "Quelles méthodes de chaîne modifient la casse du texte ?",
        ["toUpperCase()", "toLowerCase()"],
        ["trim()", "padStart()"]
      ),
      TF("padStart() permet de compléter une chaîne avec des caractères jusqu'à atteindre une longueur donnée, au début.", true),
      S(
        "Quelle méthode remplace toutes les occurrences d'une sous-chaîne (sans regex globale) en une seule fois ?",
        "replaceAll()",
        ["replace() remplace toujours toutes les occurrences", "removeAll()", "substituteAll()"]
      ),
    ]
  ),

  Quiz(
    "JS — Optional chaining et fonctions",
    "Combiner ?. avec des appels de fonction et l'opérateur ??.",
    [
      S(
        "Quelle syntaxe permet d'appeler une méthode seulement si elle existe, sans lever d'erreur si elle est absente ?",
        "objet.methode?.()",
        ["objet?.methode()", "objet.methode!()", "objet??methode()"]
      ),
      TF("Si une variable intermédiaire dans une chaîne est null, ?. court-circuite toute la chaîne et retourne undefined.", true),
      S(
        "Que retourne const config = null; config?.options?.theme ?? 'clair'; ?",
        "'clair'",
        ["null", "undefined", "Une erreur"]
      ),
      M(
        "Pourquoi combine-t-on souvent ?. et ?? ensemble ?",
        ["Pour accéder en sécurité à une propriété profondément imbriquée", "Pour fournir une valeur de repli si le résultat est null/undefined"],
        ["Pour remplacer try/catch dans tous les cas", "Pour transformer un objet en tableau"]
      ),
      TF("a?.b.c lève une erreur si a est défini mais a.b est null, car seul le premier accès est protégé.", true),
      S(
        "Le chaînage optionnel a-t-il été introduit nativement avant ou après les Promises en JavaScript ?",
        "Après (ES2020, alors que les Promises datent d'ES2015)",
        ["Avant (ES5)", "En même temps qu'ES5", "Le chaînage optionnel n'existe pas nativement"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux : copie et mutation",
    "Distinguer les méthodes de tableau qui mutent de celles qui ne mutent pas.",
    [
      S(
        "Parmi push(), pop(), map(), laquelle ne modifie PAS le tableau d'origine ?",
        "map()",
        ["push()", "pop()", "Toutes le modifient"]
      ),
      TF("reverse() inverse l'ordre des éléments du tableau d'origine directement (mutation).", true),
      M(
        "Quelles méthodes provoquent une mutation du tableau d'origine ?",
        ["sort()", "splice()", "reverse()"],
        ["map()", "filter()"]
      ),
      TF("Depuis ES2023, toSorted(), toReversed() et toSpliced() offrent des versions non-mutantes de sort(), reverse() et splice().", true),
      S(
        "Pourquoi est-il parfois risqué d'utiliser sort() directement sur un tableau partagé entre plusieurs parties du code ?",
        "Parce qu'il mute le tableau original, ce qui peut affecter d'autres références à ce même tableau",
        ["Parce que sort() ne fonctionne jamais correctement", "Parce qu'il supprime des éléments aléatoirement", "Parce qu'il convertit le tableau en chaîne définitivement"]
      ),
      S(
        "Comment créer une copie indépendante d'un tableau avant de le trier sans affecter l'original ?",
        "[...tableau].sort(...) ou tableau.slice().sort(...)",
        ["tableau.sort() suffit déjà à préserver l'original", "tableau.copy().sort()", "Ce n'est pas possible"]
      ),
    ]
  ),

  Quiz(
    "JS — Portée lexicale et fonctions imbriquées",
    "Comment les fonctions imbriquées accèdent aux variables des portées parentes.",
    [
      S(
        "Qu'est-ce que la portée lexicale (lexical scoping) ?",
        "La portée déterminée par l'emplacement du code source au moment de l'écriture, pas par l'endroit où la fonction est appelée",
        ["Une portée définie dynamiquement à l'exécution selon l'appelant", "Un synonyme strict de portée globale", "Une portée qui change selon le navigateur"]
      ),
      TF("Une fonction imbriquée a accès aux variables de toutes ses fonctions parentes grâce à la portée lexicale.", true),
      S(
        "Si une fonction interne déclare une variable avec le même nom qu'une variable externe, laquelle est utilisée à l'intérieur de la fonction interne ?",
        "La variable locale interne (elle masque/shadow la variable externe)",
        ["La variable externe systématiquement", "Une erreur est levée", "Les deux fusionnent en une seule valeur"]
      ),
      M(
        "Quelles affirmations sur le masquage de variables (shadowing) sont vraies ?",
        ["Une variable locale peut masquer une variable de portée supérieure avec le même nom", "Le masquage peut rendre le code plus difficile à déboguer si mal utilisé"],
        ["Le masquage supprime définitivement la variable externe", "Le masquage n'existe qu'avec var"]
      ),
      TF("La portée lexicale est déterminée à l'écriture du code, pas à son exécution, contrairement à this qui dépend du contexte d'appel.", true),
      S(
        "Pourquoi la portée lexicale est-elle essentielle au fonctionnement des closures ?",
        "Parce qu'une closure capture les variables visibles dans sa portée lexicale au moment de sa création",
        ["Parce qu'elle empêche toute closure de se former", "Parce qu'elle est sans rapport avec les closures", "Parce qu'elle redéfinit this automatiquement"]
      ),
    ]
  ),
];
