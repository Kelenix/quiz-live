import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — var, let et const",
    "Différences entre var, let et const : portée et réaffectation.",
    [
      S(
        "Quel mot-clé permet de déclarer une variable dont la valeur ne peut pas être réaffectée ?",
        "const",
        ["var", "let", "static"]
      ),
      S(
        "Quelle est la portée d'une variable déclarée avec let ?",
        "La portée de bloc",
        ["La portée globale uniquement", "La portée de fonction uniquement", "Aucune portée définie"]
      ),
      TF("Une variable déclarée avec var a une portée de bloc comme let.", false),
      TF("On peut modifier les propriétés d'un objet déclaré avec const.", true),
      M(
        "Parmi ces affirmations sur var, lesquelles sont vraies ?",
        ["var a une portée de fonction", "var est sujette au hoisting avec initialisation à undefined"],
        ["var respecte la portée de bloc", "var empêche toute redéclaration dans la même fonction"]
      ),
      S(
        "Que se passe-t-il si on tente de réaffecter une variable const ?",
        "Une erreur TypeError est levée",
        ["La valeur est simplement ignorée", "La variable devient automatiquement let", "Rien, la réaffectation fonctionne"]
      ),
    ]
  ),

  Quiz(
    "JS — Portée des variables",
    "Comprendre la portée globale, de fonction et de bloc en JavaScript.",
    [
      S(
        "Comment appelle-t-on une variable accessible uniquement à l'intérieur d'une fonction ?",
        "Une variable locale",
        ["Une variable globale", "Une variable statique", "Une variable d'environnement"]
      ),
      TF("Une fonction peut accéder aux variables définies dans la portée englobante (scope parent).", true),
      M(
        "Quels blocs créent une nouvelle portée pour let et const ?",
        ["Un bloc if { }", "Un bloc de boucle for { }"],
        ["Une simple expression sans accolades", "Un commentaire"]
      ),
      S(
        "Quel terme désigne l'ensemble des portées imbriquées qu'une fonction peut consulter pour résoudre une variable ?",
        "La chaîne de portée (scope chain)",
        ["La pile d'appels (call stack)", "Le tas mémoire (heap)", "La table de hachage"]
      ),
      S(
        "Dans quel cas une variable globale est-elle créée accidentellement en mode non strict ?",
        "Quand on assigne une valeur à un identifiant non déclaré",
        ["Quand on utilise const dans une fonction", "Quand on utilise let dans un bloc", "Jamais, c'est impossible"]
      ),
      TF("Le mode strict ('use strict') empêche la création accidentelle de variables globales.", true),
    ]
  ),

  Quiz(
    "JS — Types primitifs",
    "Les types de données primitifs du langage JavaScript.",
    [
      M(
        "Lesquels des éléments suivants sont des types primitifs en JavaScript ?",
        ["string", "number", "boolean"],
        ["Array", "Object"]
      ),
      S(
        "Quel opérateur permet de connaître le type d'une valeur ?",
        "typeof",
        ["instanceof", "typecheck", "gettype"]
      ),
      TF("typeof null retourne 'object' en JavaScript.", true),
      S(
        "Que retourne typeof undefined ?",
        "'undefined'",
        ["'null'", "'object'", "'undefined value'"]
      ),
      S(
        "Quel type primitif a été ajouté pour représenter des entiers de précision arbitraire ?",
        "bigint",
        ["bignumber", "longint", "decimal"]
      ),
      TF("Les valeurs primitives (string, number, boolean) sont immuables en JavaScript.", true),
    ]
  ),

  Quiz(
    "JS — Coercion de types",
    "La conversion implicite et explicite entre types en JavaScript.",
    [
      S(
        "Que vaut l'expression '5' + 3 en JavaScript ?",
        "'53'",
        ["8", "'8'", "NaN"]
      ),
      S(
        "Que vaut l'expression '5' - 3 en JavaScript ?",
        "2",
        ["'53'", "NaN", "'2'"]
      ),
      TF("L'opérateur + concatène deux chaînes mais convertit aussi les nombres en chaînes si l'un des opérandes est une chaîne.", true),
      M(
        "Quelles expressions provoquent une conversion implicite (coercion) ?",
        ["'3' * 2", "true + 1"],
        ["Number('3') * 2", "String(true) + '1'"]
      ),
      S(
        "Quelle fonction convertit explicitement une chaîne en nombre entier ?",
        "parseInt",
        ["toString", "valueOf", "String"]
      ),
      S(
        "Que retourne Boolean('') en JavaScript ?",
        "false",
        ["true", "undefined", "Une erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Valeurs falsy et truthy",
    "Identifier les valeurs considérées comme fausses ou vraies dans un contexte booléen.",
    [
      M(
        "Lesquelles de ces valeurs sont considérées comme falsy en JavaScript ?",
        ["0", "''", "null"],
        ["'0'", "[]"]
      ),
      TF("Un tableau vide [] est une valeur truthy en JavaScript.", true),
      S(
        "Parmi ces valeurs, laquelle est falsy ?",
        "NaN",
        ["'false'", "1", "[]"]
      ),
      TF("La valeur undefined est falsy.", true),
      S(
        "Que vaut Boolean(' ') (chaîne contenant un seul espace) ?",
        "true",
        ["false", "undefined", "Une erreur de syntaxe"]
      ),
      M(
        "Quelles valeurs sont truthy ?",
        ["'0' (chaîne)", "{} (objet vide)"],
        ["0 (nombre)", "null"]
      ),
    ]
  ),

  Quiz(
    "JS — Opérateurs de comparaison",
    "Différences entre == et === et les pièges de l'égalité en JavaScript.",
    [
      S(
        "Quelle est la différence principale entre == et === ?",
        "=== compare aussi le type, == effectue une coercion de type avant comparaison",
        ["== est plus strict que ===", "=== ne fonctionne que sur les nombres", "Aucune différence, ce sont des synonymes"]
      ),
      TF("L'expression 1 == '1' retourne true en JavaScript.", true),
      TF("L'expression 1 === '1' retourne true en JavaScript.", false),
      S(
        "Que retourne null == undefined ?",
        "true",
        ["false", "NaN", "Une erreur"]
      ),
      M(
        "Quelles bonnes pratiques sont recommandées concernant les comparaisons ?",
        ["Préférer === à == pour éviter les coercions inattendues", "Utiliser Object.is() pour des cas particuliers comme NaN"],
        ["Toujours utiliser == pour plus de flexibilité", "Éviter typeof pour vérifier les types"]
      ),
      S(
        "Que retourne null === undefined ?",
        "false",
        ["true", "NaN", "undefined"]
      ),
    ]
  ),

  Quiz(
    "JS — NaN et égalité spéciale",
    "Le comportement particulier de NaN et les méthodes pour le détecter.",
    [
      TF("NaN === NaN retourne true en JavaScript.", false),
      S(
        "Quelle fonction permet de vérifier de façon fiable si une valeur est NaN ?",
        "Number.isNaN()",
        ["isNaN() uniquement", "typeof", "NaN.equals()"]
      ),
      S(
        "Que retourne typeof NaN ?",
        "'number'",
        ["'NaN'", "'undefined'", "'object'"]
      ),
      TF("Object.is(NaN, NaN) retourne true.", true),
      M(
        "Quelles opérations peuvent produire NaN ?",
        ["0 / 0", "'abc' * 2"],
        ["1 + 1", "'5' * 2"]
      ),
      S(
        "Pourquoi isNaN('abc') et Number.isNaN('abc') peuvent donner des résultats différents ?",
        "isNaN() convertit d'abord l'argument en nombre, Number.isNaN() ne convertit pas",
        ["Ce sont des alias strictement identiques", "Number.isNaN() est obsolète", "isNaN() ne fonctionne que sur les nombres"]
      ),
    ]
  ),

  Quiz(
    "JS — Opérateurs logiques",
    "Les opérateurs &&, ||, ! et leur comportement de court-circuit.",
    [
      S(
        "Que retourne l'expression true && false ?",
        "false",
        ["true", "undefined", "Une erreur"]
      ),
      S(
        "Que retourne l'expression 0 || 'valeur par défaut' ?",
        "'valeur par défaut'",
        ["0", "undefined", "false"]
      ),
      TF("L'opérateur && retourne la première valeur falsy rencontrée ou la dernière valeur si toutes sont truthy.", true),
      M(
        "Quelles affirmations sur le court-circuit (short-circuit) sont correctes ?",
        ["&& arrête l'évaluation dès qu'une valeur falsy est rencontrée", "|| arrête l'évaluation dès qu'une valeur truthy est rencontrée"],
        ["&& évalue toujours tous les opérandes", "Le court-circuit n'existe pas en JavaScript"]
      ),
      S(
        "Que retourne !!'texte' (double négation) ?",
        "true",
        ["false", "'texte'", "undefined"]
      ),
      S(
        "Quel est le résultat de null || undefined || 'fin' ?",
        "'fin'",
        ["null", "undefined", "Une erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Nullish coalescing (??)",
    "L'opérateur ?? et sa différence avec ||.",
    [
      S(
        "Que fait l'opérateur ?? (nullish coalescing) ?",
        "Il retourne l'opérande de droite seulement si la gauche est null ou undefined",
        ["Il retourne l'opérande de droite si la gauche est falsy", "Il compare strictement deux valeurs", "Il convertit les types automatiquement"]
      ),
      S(
        "Que retourne 0 ?? 'valeur par défaut' ?",
        "0",
        ["'valeur par défaut'", "undefined", "NaN"]
      ),
      TF("0 ?? 'défaut' et 0 || 'défaut' donnent le même résultat.", false),
      TF("L'opérateur ?? considère uniquement null et undefined comme déclencheurs du membre de droite.", true),
      M(
        "Pour quelles valeurs l'opérateur ?? retourne-t-il l'opérande de droite ?",
        ["null", "undefined"],
        ["0", "''"]
      ),
      S(
        "Comment écrire une affectation conditionnelle qui assigne une valeur par défaut uniquement si la variable est null/undefined ?",
        "variable ??= valeurParDefaut;",
        ["variable ||= valeurParDefaut;", "variable = valeurParDefaut;", "variable &&= valeurParDefaut;"]
      ),
    ]
  ),

  Quiz(
    "JS — Opérateur de chaînage optionnel (?.)",
    "Utiliser ?. pour accéder en toute sécurité à des propriétés potentiellement absentes.",
    [
      S(
        "Que fait l'opérateur ?. (chaînage optionnel) ?",
        "Il retourne undefined au lieu de lever une erreur si la référence est null ou undefined",
        ["Il convertit automatiquement les types", "Il déclare une propriété optionnelle dans une classe", "Il vérifie l'égalité stricte"]
      ),
      TF("obj?.prop renvoie undefined si obj est null, sans lever d'erreur.", true),
      S(
        "Que retourne (undefined)?.toUpperCase() ?",
        "undefined",
        ["Une erreur TypeError", "''", "null"]
      ),
      M(
        "Dans quels contextes peut-on utiliser le chaînage optionnel ?",
        ["Accès à une propriété : obj?.prop", "Appel de méthode : obj.method?.()"],
        ["Déclaration de variable : let?.x = 1", "Boucle for?.of"]
      ),
      S(
        "Comment accéder en toute sécurité à un élément d'un tableau qui pourrait être undefined ?",
        "tableau?.[0]",
        ["tableau.0?", "tableau??[0]", "tableau!.0"]
      ),
      TF("Le chaînage optionnel peut être combiné avec l'opérateur ?? pour fournir une valeur par défaut.", true),
    ]
  ),

  Quiz(
    "JS — Opérateurs arithmétiques",
    "Les opérateurs +, -, *, /, %, ** et leurs particularités.",
    [
      S(
        "Que retourne l'opérateur % (modulo) appliqué à 7 % 3 ?",
        "1",
        ["2", "3", "0"]
      ),
      S(
        "Quel opérateur permet de calculer une puissance en JavaScript moderne ?",
        "**",
        ["^", "pow", "%%"]
      ),
      TF("L'opérateur ++ peut être utilisé en préfixe (++x) ou en suffixe (x++) avec des comportements différents.", true),
      M(
        "Quelles expressions retournent un nombre valide (pas NaN ni Infinity) ?",
        ["10 / 2", "2 ** 3"],
        ["10 / 0", "'a' * 2"]
      ),
      S(
        "Que vaut 10 / 0 en JavaScript ?",
        "Infinity",
        ["Une erreur", "NaN", "0"]
      ),
      S(
        "Quelle est la différence entre x++ et ++x ?",
        "x++ retourne la valeur avant incrémentation, ++x retourne la valeur après",
        ["Aucune différence", "++x ne fonctionne que sur les chaînes", "x++ incrémente de 2"]
      ),
    ]
  ),

  Quiz(
    "JS — Template literals",
    "Les chaînes de caractères avec interpolation et multi-lignes via les backticks.",
    [
      S(
        "Quel symbole délimite un template literal en JavaScript ?",
        "Les backticks `",
        ["Les guillemets doubles \"", "Les apostrophes '", "Les crochets []"]
      ),
      S(
        "Comment insérer une expression dans un template literal ?",
        "Avec la syntaxe ${expression}",
        ["Avec la syntaxe #{expression}", "Avec la syntaxe %expression%", "Avec la syntaxe {{expression}}"]
      ),
      TF("Les template literals permettent d'écrire des chaînes sur plusieurs lignes sans caractère d'échappement spécial.", true),
      M(
        "Quels avantages offrent les template literals par rapport à la concaténation classique ?",
        ["Interpolation de variables plus lisible", "Support natif du multi-lignes"],
        ["Exécution plus rapide dans tous les moteurs", "Typage statique automatique"]
      ),
      S(
        "Que vaut `Total: ${2 + 3}` ?",
        "'Total: 5'",
        ["'Total: 2 + 3'", "'Total: ${2 + 3}'", "Une erreur de syntaxe"]
      ),
      TF("Les templates literals taggés (tagged templates) permettent de transformer une chaîne via une fonction.", true),
    ]
  ),

  Quiz(
    "JS — Conversion explicite de types",
    "Les méthodes pour convertir explicitement entre string, number et boolean.",
    [
      S(
        "Quelle fonction convertit explicitement une valeur en chaîne de caractères ?",
        "String()",
        ["Number()", "Boolean()", "parseFloat()"]
      ),
      S(
        "Que retourne Number('42px') ?",
        "NaN",
        ["42", "'42px'", "0"]
      ),
      S(
        "Que retourne parseInt('42px') ?",
        "42",
        ["NaN", "'42px'", "0"]
      ),
      TF("parseFloat('3.14 metres') retourne 3.14.", true),
      M(
        "Quelles méthodes permettent de convertir un nombre en chaîne ?",
        ["String(nombre)", "nombre.toString()"],
        ["Number(nombre)", "Boolean(nombre)"]
      ),
      S(
        "Quelle est la différence entre Number('') et Number(' ')  (chaîne vide vs espace) ?",
        "Les deux retournent 0",
        ["Number('') retourne NaN, Number(' ') retourne 0", "Number('') retourne 0, Number(' ') retourne NaN", "Les deux retournent NaN"]
      ),
    ]
  ),
];
