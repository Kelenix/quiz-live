import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Comparaison entre Array et objet array-like",
    "Différencier un vrai tableau d'un objet ressemblant à un tableau.",
    [
      S(
        "Qu'est-ce qu'un objet array-like (similaire à un tableau) ?",
        "Un objet possédant une propriété length et des index numériques, sans être un vrai Array",
        ["Un synonyme strict de Array", "Un tableau trié automatiquement", "Un objet qui ne peut contenir que des chaînes"]
      ),
      S(
        "Quel est un exemple typique d'objet array-like en JavaScript ?",
        "L'objet arguments dans une fonction classique",
        ["Un Map", "Un Set", "Une chaîne de caractères convertie en nombre"]
      ),
      TF("On peut convertir un objet array-like en vrai tableau avec Array.from().", true),
      M(
        "Quelles limitations présente un objet array-like par rapport à un vrai Array ?",
        ["Il ne possède pas les méthodes comme map() ou filter() nativement", "Array.isArray() retourne false pour lui"],
        ["Il ne peut jamais être parcouru", "Il n'a pas de propriété length"]
      ),
      TF("NodeList, retourné par querySelectorAll(), est un exemple d'objet proche d'un tableau qui peut nécessiter une conversion pour utiliser certaines méthodes de tableau.", true),
      S(
        "Quelle syntaxe moderne avec spread permet aussi de convertir un itérable array-like en tableau ?",
        "[...objetArrayLike] si l'objet est itérable",
        ["objetArrayLike.toArray()", "Array.parse(objetArrayLike)", "new Array(objetArrayLike)"]
      ),
    ]
  ),

  Quiz(
    "JS — Gestion des dates et calculs de durée",
    "Calculer des différences entre dates et formater des durées.",
    [
      S(
        "Comment calculer la différence en millisecondes entre deux objets Date dateA et dateB ?",
        "dateA - dateB ou dateA.getTime() - dateB.getTime()",
        ["dateA.diff(dateB)", "Date.compare(dateA, dateB)", "dateA.minus(dateB)"]
      ),
      TF("Soustraire deux objets Date retourne un nombre représentant la différence en millisecondes, grâce à la conversion implicite en timestamp.", true),
      S(
        "Quelle méthode permet de définir une nouvelle valeur pour le jour du mois d'un objet Date existant ?",
        "setDate()",
        ["setDay()", "changeDate()", "updateDate()"]
      ),
      M(
        "Quelles limitations classiques de l'objet Date natif poussent parfois à utiliser des bibliothèques externes ?",
        ["Une API parfois peu intuitive pour le formatage", "Une gestion complexe des fuseaux horaires"],
        ["L'impossibilité totale de comparer deux dates", "L'absence de toute méthode pour obtenir l'année"]
      ),
      TF("Intl.DateTimeFormat permet de formater une date selon une locale spécifique sans bibliothèque externe.", true),
      S(
        "Que retourne typeof new Date() ?",
        "'object'",
        ["'date'", "'string'", "'number'"]
      ),
    ]
  ),

  Quiz(
    "JS — Symbol.iterator personnalisé",
    "Implémenter un itérateur personnalisé sur un objet avec Symbol.iterator.",
    [
      S(
        "Pour rendre un objet personnalisé compatible avec for...of, quelle méthode doit-on lui ajouter ?",
        "Une méthode nommée [Symbol.iterator] qui retourne un itérateur",
        ["Une méthode nommée iterate()", "Une propriété nommée length uniquement", "Une méthode nommée loop()"]
      ),
      TF("L'itérateur retourné par [Symbol.iterator] doit posséder une méthode next() retournant { value, done }.", true),
      S(
        "Quel avantage offre l'implémentation de Symbol.iterator sur une classe personnalisée représentant une collection ?",
        "Elle permet d'utiliser for...of, le spread et la déstructuration directement sur les instances",
        ["Elle accélère automatiquement tous les calculs internes", "Elle transforme la classe en tableau natif", "Elle empêche toute modification de la collection"]
      ),
      M(
        "Quelles syntaxes deviennent utilisables sur un objet une fois Symbol.iterator implémenté ?",
        ["for (const item of monObjet) { }", "[...monObjet]"],
        ["monObjet.map() automatiquement sans l'ajouter explicitement", "JSON.stringify(monObjet) avec un format spécial automatique"]
      ),
      TF("Les générateurs (function*) sont un moyen pratique d'implémenter facilement [Symbol.iterator] sans gérer manuellement l'état de l'itérateur.", true),
      S(
        "Que se passe-t-il si on utilise for...of sur un objet qui n'implémente pas le protocole itérable ?",
        "Une erreur TypeError est levée car l'objet n'est pas itérable",
        ["La boucle s'exécute sans rien faire silencieusement", "L'objet est automatiquement converti en tableau", "Cela retourne toujours undefined sans erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Pièges courants avec les boucles et les closures",
    "Le problème classique de var dans une boucle avec des callbacks asynchrones.",
    [
      S(
        "Dans une boucle for utilisant var et un setTimeout à chaque itération, quel problème classique survient souvent ?",
        "Tous les callbacks capturent la même variable partagée, qui a déjà atteint sa valeur finale au moment de l'exécution",
        ["Chaque callback affiche correctement la valeur attendue de son itération", "Une erreur de syntaxe est levée systématiquement", "Les callbacks ne s'exécutent jamais"]
      ),
      TF("Remplacer var par let dans la boucle résout ce problème car let crée une nouvelle liaison de variable à chaque itération.", true),
      S(
        "Quelle technique plus ancienne (avant let) permettait de corriger ce piège avec var ?",
        "Envelopper le corps de la boucle dans une IIFE pour capturer la valeur courante à chaque itération",
        ["Utiliser uniquement des boucles while", "Ce n'était pas corrigeable avant ES6", "Utiliser des fonctions fléchées uniquement, peu importe var/let"]
      ),
      M(
        "Quelles affirmations expliquent pourquoi let résout ce piège alors que var ne le fait pas ?",
        ["let a une portée de bloc, une nouvelle variable est créée à chaque itération de boucle", "var a une portée de fonction, partagée par toutes les itérations"],
        ["let est juste un alias de var sans différence réelle", "var crée une nouvelle portée à chaque itération comme let"]
      ),
      TF("Ce piège illustre bien l'importance de comprendre quand une closure capture une référence partagée plutôt qu'une copie figée.", true),
      S(
        "Avec for (let i = 0; i < 3; i++) { setTimeout(() => console.log(i), 100); }, que sera affiché ?",
        "0, 1, 2 (chaque itération capture sa propre variable i)",
        ["3, 3, 3", "0, 0, 0", "Une erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Strings : recherche et correspondance avancée",
    "Les méthodes search(), startsWith(), endsWith() pour analyser des chaînes.",
    [
      S(
        "Quelle méthode vérifie si une chaîne commence par une sous-chaîne donnée ?",
        "startsWith()",
        ["beginsWith()", "firstMatch()", "headIs()"]
      ),
      S(
        "Quelle méthode vérifie si une chaîne se termine par une sous-chaîne donnée ?",
        "endsWith()",
        ["lastMatch()", "tailIs()", "finishWith()"]
      ),
      TF("startsWith() et endsWith() acceptent un second paramètre optionnel pour spécifier une position de départ ou de fin.", true),
      M(
        "Quelles méthodes de chaîne retournent un booléen ?",
        ["includes()", "startsWith()", "endsWith()"],
        ["indexOf() retourne un booléen", "slice() retourne un booléen"]
      ),
      TF("'Bonjour'.startsWith('Bon') retourne true.", true),
      S(
        "Quelle méthode retourne l'index de la première correspondance d'une expression régulière dans une chaîne ?",
        "search()",
        ["find()", "locate()", "test()"]
      ),
    ]
  ),
];
