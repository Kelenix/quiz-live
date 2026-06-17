import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Async/await et boucles",
    "Utiliser await à l'intérieur de boucles for...of versus forEach.",
    [
      S(
        "Pourquoi await ne fonctionne-t-il pas comme attendu à l'intérieur d'un forEach() classique ?",
        "Parce que forEach() ne gère pas les Promises retournées par son callback et n'attend pas leur résolution",
        ["Parce que forEach() n'accepte aucune fonction asynchrone en argument", "Parce qu'await est interdit dans tous les callbacks", "Parce que forEach() est plus rapide que for...of"]
      ),
      TF("Une boucle for...of avec await à l'intérieur traite les itérations de façon séquentielle, en attendant chaque Promise avant de continuer.", true),
      S(
        "Comment exécuter plusieurs appels asynchrones en parallèle à partir d'un tableau d'identifiants ?",
        "En mappant chaque identifiant vers une Promise puis en utilisant Promise.all() sur le tableau de promesses",
        ["En utilisant uniquement une boucle for...of avec await à chaque itération", "Ce n'est pas possible en JavaScript", "En utilisant forEach() avec async directement, cela suffit"]
      ),
      M(
        "Quelles affirmations sur l'exécution séquentielle vs parallèle en async sont vraies ?",
        ["for...of avec await exécute les opérations l'une après l'autre", "Promise.all() permet de lancer plusieurs opérations en parallèle"],
        ["forEach() attend automatiquement chaque Promise", "Le parallélisme est impossible en JavaScript"]
      ),
      TF("Du code asynchrone séquentiel (un await après l'autre sans nécessité) peut être plus lent qu'une exécution parallèle équivalente.", true),
      S(
        "Quelle structure choisir pour traiter des éléments un par un, en respectant un ordre strict avec des dépendances entre eux ?",
        "Une boucle for...of avec await",
        ["Promise.all() systématiquement", "Promise.race()", "Un tableau de callbacks sans await"]
      ),
    ]
  ),

  Quiz(
    "JS — Méthodes statiques de Promise",
    "Promise.resolve, Promise.reject, Promise.race et Promise.any.",
    [
      S(
        "Que fait Promise.resolve(valeur) ?",
        "Elle retourne une Promise déjà résolue avec la valeur donnée",
        ["Elle attend une valeur indéfiniment", "Elle rejette toujours la Promise", "Elle convertit la valeur en chaîne"]
      ),
      S(
        "Que fait Promise.race(promesses) ?",
        "Elle se résout ou se rejette dès que la première Promise du tableau se termine, quel que soit son statut",
        ["Elle attend que toutes les promesses soient terminées", "Elle ignore les rejets et attend uniquement les succès", "Elle exécute les promesses dans l'ordre, une par une"]
      ),
      TF("Promise.any() se résout dès qu'une des promesses réussit, et ne rejette que si toutes échouent.", true),
      M(
        "Quelles méthodes statiques font partie de l'API Promise ?",
        ["Promise.all()", "Promise.race()", "Promise.any()"],
        ["Promise.merge()"]
      ),
      TF("Promise.reject(erreur) crée directement une Promise déjà rejetée avec l'erreur fournie.", true),
      S(
        "Dans quel cas privilégier Promise.any() plutôt que Promise.all() ?",
        "Quand on veut le premier résultat réussi parmi plusieurs sources, en tolérant que certaines échouent",
        ["Quand on veut absolument que toutes les promesses réussissent", "Quand on veut exécuter les promesses en séquence stricte", "Promise.any() et Promise.all() sont strictement interchangeables"]
      ),
    ]
  ),

  Quiz(
    "JS — Création d'objets : littéral, constructeur, Object.create",
    "Les différentes façons de créer des objets en JavaScript.",
    [
      S(
        "Quelle est la façon la plus simple de créer un objet en JavaScript ?",
        "Avec un objet littéral : { cle: valeur }",
        ["Avec uniquement new Object()", "Avec uniquement Object.create(null)", "Avec une classe obligatoirement"]
      ),
      S(
        "Que fait Object.create(prototypeParent) ?",
        "Elle crée un nouvel objet dont le prototype est l'objet passé en argument",
        ["Elle clone un objet existant en copie profonde", "Elle convertit un objet en JSON", "Elle crée une classe à partir d'un objet"]
      ),
      TF("On peut créer un objet sans aucun prototype avec Object.create(null), ce qui le prive même des méthodes héritées d'Object.prototype.", true),
      M(
        "Quelles façons de créer un objet existent en JavaScript ?",
        ["Objet littéral { }", "new MaClasse()", "Object.create()"],
        ["Array.create()"]
      ),
      TF("new MaFonction() crée un nouvel objet et exécute MaFonction avec this pointant sur ce nouvel objet, si MaFonction est utilisée comme constructeur classique.", true),
      S(
        "Avant les classes ES6, comment simulait-on l'héritage entre 'constructeurs' de fonction ?",
        "En manipulant directement les prototypes (Object.create, Function.prototype)",
        ["Avec le mot-clé extends qui existait déjà", "Ce n'était pas possible avant ES6", "Avec async/await"]
      ),
    ]
  ),

  Quiz(
    "JS — Méthodes d'objets et raccourcis ES6",
    "Les raccourcis de syntaxe pour les méthodes et propriétés d'objets.",
    [
      S(
        "Quelle syntaxe raccourcie permet de définir une propriété avec le nom d'une variable existante portant la même valeur ?",
        "{ nom } équivaut à { nom: nom }",
        ["{ nom: }", "{ :nom }", "{ nom == nom }"]
      ),
      TF("ES6 permet de définir une méthode d'objet sans le mot-clé function : { saluer() { } }.", true),
      S(
        "Quelle syntaxe permet de calculer dynamiquement le nom d'une propriété dans un objet littéral ?",
        "{ [expression]: valeur }",
        ["{ expression: valeur }", "{ (expression): valeur }", "{ #expression: valeur }"]
      ),
      M(
        "Quels raccourcis ES6 simplifient l'écriture d'objets littéraux ?",
        ["Les noms de propriétés abrégés", "Les méthodes sans mot-clé function", "Les noms de propriétés calculés entre crochets"],
        ["Les classes sans mot-clé class"]
      ),
      TF("Ces raccourcis ES6 ne changent pas le comportement de l'objet, ils simplifient uniquement la syntaxe d'écriture.", true),
      S(
        "Avec const x = 1, y = 2; quelle expression crée un objet { x: 1, y: 2 } via le raccourci de propriété ?",
        "{ x, y }",
        ["{ x: , y: }", "{ x = 1, y = 2 }", "{ x -> 1, y -> 2 }"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux : Array.of et Array constructeur",
    "Créer des tableaux avec Array(), Array.of() et leurs différences.",
    [
      S(
        "Que retourne new Array(3) ?",
        "Un tableau vide de longueur 3 (avec des emplacements non assignés)",
        ["[3]", "Un tableau [0, 1, 2]", "Une erreur systématique"]
      ),
      S(
        "Que retourne Array.of(3) ?",
        "[3]",
        ["Un tableau vide de longueur 3", "[0, 1, 2]", "Une erreur"]
      ),
      TF("Array.of() a été créé pour éviter l'ambiguïté du constructeur Array() avec un seul argument numérique.", true),
      M(
        "Quelles méthodes permettent de générer un tableau pré-rempli de valeurs identiques ?",
        ["new Array(n).fill(valeur)", "Array.from({length: n}, () => valeur)"],
        ["Array.of(n).fill omis volontairement sans argument", "JSON.parse('[]')"]
      ),
      TF("fill() remplace tous les éléments d'un tableau (ou une portion) par une valeur donnée, en mutant le tableau.", true),
      S(
        "Pourquoi new Array(1, 2, 3) et Array.of(1, 2, 3) donnent-ils le même résultat ?",
        "Parce qu'avec plusieurs arguments, le comportement du constructeur Array() n'est pas ambigu",
        ["Ils ne donnent jamais le même résultat", "Parce qu'Array.of() est un alias strict de new Array() dans tous les cas", "Parce que les deux ignorent les arguments fournis"]
      ),
    ]
  ),

  Quiz(
    "JS — Contexte this dans les callbacks",
    "Les pièges de this lorsqu'une méthode est utilisée comme callback.",
    [
      S(
        "Que se passe-t-il si on passe objet.methode comme callback à setTimeout sans le lier explicitement ?",
        "this perd la référence à objet lors de l'exécution du callback (souvent undefined ou l'objet global)",
        ["this reste automatiquement lié à objet", "Une erreur de syntaxe est levée immédiatement", "this devient automatiquement la fonction setTimeout"]
      ),
      TF("Utiliser une fonction fléchée pour définir un callback à l'intérieur d'une méthode permet souvent de conserver le this attendu.", true),
      S(
        "Quelle méthode permet de créer une version d'une fonction avec un this définitivement fixé, utilisable plus tard comme callback ?",
        "bind()",
        ["call()", "apply()", "fix()"]
      ),
      M(
        "Quelles solutions corrigent un problème de this perdu dans un callback ?",
        ["Utiliser .bind(objet) avant de passer la méthode", "Utiliser une fonction fléchée qui capture le this englobant"],
        ["Ignorer le problème, il se résout automatiquement", "Renommer la méthode"]
      ),
      TF("Dans les gestionnaires d'événements DOM définis avec une fonction classique, this référence généralement l'élément qui a déclenché l'événement.", true),
      S(
        "Pourquoi ce piège de this est-il fréquent avec les méthodes de classe utilisées comme callbacks (ex: bouton.addEventListener('click', this.gerer)) ?",
        "Parce que la méthode est détachée de l'instance lors du passage en callback, perdant son this d'origine",
        ["Parce que addEventListener n'accepte pas les méthodes de classe", "Parce que this est toujours undefined en JavaScript", "Parce que les classes ne supportent pas les méthodes"]
      ),
    ]
  ),

  Quiz(
    "JS — Conversion booléenne et opérateurs unaires",
    "Les opérateurs unaires +, -, ! et leur effet de conversion.",
    [
      S(
        "Que fait l'opérateur unaire + appliqué à une chaîne comme +'42' ?",
        "Il convertit la chaîne en nombre, équivalent à Number('42')",
        ["Il concatène un signe positif sans conversion", "Il lève toujours une erreur", "Il convertit en booléen"]
      ),
      S(
        "Que retourne !!valeur (double négation logique) ?",
        "L'équivalent booléen (truthy/falsy) de valeur",
        ["Toujours false", "Toujours la valeur d'origine inchangée", "Une erreur de syntaxe"]
      ),
      TF("L'opérateur unaire - peut aussi convertir une chaîne numérique en nombre négatif, comme -'5' qui vaut -5.", true),
      M(
        "Quelles expressions retournent un nombre valide (pas NaN) ?",
        ["+'10'", "-'3'"],
        ["+'dix'", "-'abc'"]
      ),
      TF("Le résultat de +'' (chaîne vide convertie en nombre) est 0.", true),
      S(
        "Que retourne +true ?",
        "1",
        ["0", "NaN", "'true'"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux : entries(), keys(), values()",
    "Itérer sur les index et valeurs d'un tableau avec les méthodes d'itération dédiées.",
    [
      S(
        "Que retourne tableau.entries() ?",
        "Un itérateur produisant des paires [index, valeur]",
        ["Un tableau simple des valeurs", "Un objet avec les clés uniquement", "Une chaîne formatée"]
      ),
      S(
        "Que retourne tableau.keys() pour un tableau de 3 éléments ?",
        "Un itérateur produisant les index 0, 1, 2",
        ["Un tableau des valeurs", "Le nombre 3 uniquement", "Un objet vide"]
      ),
      TF("On peut utiliser for...of directement sur le résultat de entries(), keys() ou values() car ce sont des itérateurs.", true),
      M(
        "Quelles méthodes d'itération sont disponibles directement sur les tableaux ?",
        ["entries()", "keys()", "values()"],
        ["fields()"]
      ),
      TF("for (const [index, valeur] of tableau.entries()) { } permet d'obtenir à la fois l'index et la valeur via destructuring.", true),
      S(
        "Quelle est l'utilité principale de entries() par rapport à une simple boucle for classique ?",
        "Elle permet une syntaxe plus déclarative avec for...of et le destructuring, sans gérer manuellement un compteur",
        ["Elle est la seule façon d'accéder aux index d'un tableau", "Elle trie automatiquement le tableau", "Elle est plus rapide dans tous les cas"]
      ),
    ]
  ),

  Quiz(
    "JS — Stratégies de validation et garde de type",
    "Vérifier le type et la validité des données avant de les utiliser.",
    [
      S(
        "Pourquoi vérifier typeof valeur === 'number' && !Number.isNaN(valeur) avant un calcul ?",
        "Pour s'assurer que la valeur est bien un nombre valide et éviter des résultats NaN inattendus",
        ["Parce que typeof seul suffit toujours à garantir un nombre valide", "Parce que NaN n'est jamais de type number", "Cette vérification n'a aucune utilité pratique"]
      ),
      TF("Vérifier Array.isArray(valeur) avant d'appeler .map() évite une erreur si valeur n'est pas un tableau.", true),
      S(
        "Quelle expression vérifie qu'un objet possède une propriété donnée, y compris héritée ?",
        "'propriete' in objet",
        ["objet.hasOwnProperty('propriete') uniquement", "typeof objet.propriete", "objet.propriete !== undefined uniquement"]
      ),
      M(
        "Quelles techniques aident à valider la forme des données reçues (ex: depuis une API) ?",
        ["Vérifier la présence et le type des propriétés attendues", "Utiliser des valeurs par défaut avec destructuring ou ??"],
        ["Faire confiance aveuglément aux données sans vérification", "Toujours utiliser eval() pour analyser les données"]
      ),
      TF("hasOwnProperty() vérifie qu'une propriété appartient directement à l'objet, sans remonter la chaîne de prototypes.", true),
      S(
        "Pourquoi privilégier Object.hasOwn(objet, 'propriete') (ES2022) à objet.hasOwnProperty('propriete') ?",
        "Parce qu'elle fonctionne même si l'objet n'a pas hérité de Object.prototype (ex: Object.create(null))",
        ["Parce qu'elles ont des comportements totalement opposés", "Parce que hasOwnProperty() est supprimée des moteurs modernes", "Il n'y a aucune raison valable"]
      ),
    ]
  ),

  Quiz(
    "JS — Récursivité",
    "Les fonctions récursives et leurs cas d'usage typiques.",
    [
      S(
        "Qu'est-ce qu'une fonction récursive ?",
        "Une fonction qui s'appelle elle-même, directement ou indirectement, pour résoudre un problème",
        ["Une fonction qui ne peut jamais se terminer", "Une fonction qui retourne toujours undefined", "Une fonction qui modifie son propre code à l'exécution"]
      ),
      TF("Une fonction récursive doit avoir une condition d'arrêt (cas de base) pour éviter une récursion infinie.", true),
      S(
        "Que se passe-t-il si une fonction récursive n'a pas de cas de base correctement défini ?",
        "Une erreur de dépassement de pile (stack overflow) se produit généralement",
        ["Le programme s'exécute indéfiniment sans aucun problème", "JavaScript détecte et corrige automatiquement l'erreur", "La fonction retourne automatiquement 0"]
      ),
      M(
        "Quels problèmes sont classiquement résolus avec une approche récursive ?",
        ["Le parcours d'une arborescence (ex: structure de fichiers)", "Le calcul de la factorielle ou de Fibonacci"],
        ["L'addition simple de deux nombres", "La lecture d'un seul caractère"]
      ),
      TF("Chaque appel récursif ajoute un nouveau cadre (frame) à la pile d'appels, consommant de la mémoire.", true),
      S(
        "Quel terme désigne une fonction récursive structurée pour permettre certaines optimisations de la pile d'appels par le moteur ?",
        "La récursivité terminale (tail recursion)",
        ["La récursivité croisée", "La récursivité globale", "La récursivité asynchrone"]
      ),
    ]
  ),

  Quiz(
    "JS — Comparaison entre fonctions classiques et méthodes de classe",
    "Différences de comportement entre une fonction classique et une méthode définie dans une classe.",
    [
      S(
        "Une méthode définie dans une classe ES6 est-elle hissée (hoisted) comme une déclaration de fonction classique ?",
        "Non, les classes ne sont pas hissées avec leur définition complète comme les fonctions déclarées",
        ["Oui, exactement comme les déclarations de fonction", "Cela dépend du nombre de méthodes", "Les classes n'existent pas réellement à l'exécution"]
      ),
      TF("Une classe déclarée est elle aussi soumise à une zone morte temporelle, comme let et const.", true),
      S(
        "Le corps d'une classe (et donc ses méthodes) s'exécute-t-il en mode strict automatiquement ?",
        "Oui, peu importe que le mode strict soit activé ailleurs dans le fichier",
        ["Non, jamais", "Seulement si 'use strict' est ajouté explicitement dans la classe", "Seulement pour les méthodes statiques"]
      ),
      M(
        "Quelles différences existent entre une fonction constructeur classique (pre-ES6) et une classe ES6 ?",
        ["Une classe ne peut pas être appelée sans new (erreur si on essaie)", "Le corps de la classe est en mode strict automatiquement"],
        ["Une fonction constructeur classique ne peut jamais être appelée avec new", "Les classes ES6 n'utilisent pas du tout les prototypes en interne"]
      ),
      TF("Appeler une classe sans le mot-clé new lève une erreur TypeError.", true),
      S(
        "Quel est l'objectif principal des classes ES6 par rapport aux fonctions constructeurs ?",
        "Offrir une syntaxe plus claire et structurée pour l'héritage et l'encapsulation, basée sur les prototypes en interne",
        ["Remplacer entièrement le système de prototypes par un autre mécanisme", "Supprimer la possibilité d'héritage", "Accélérer l'exécution du code de façon garantie"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux et égalité référentielle dans les structures de données",
    "Pourquoi la mutabilité des tableaux peut provoquer des bugs subtils.",
    [
      S(
        "Que se passe-t-il si on passe un tableau en argument à une fonction qui utilise push() sur ce tableau ?",
        "Le tableau original est modifié car les tableaux sont passés par référence",
        ["Une copie est automatiquement créée, l'original reste intact", "Une erreur est levée car les tableaux sont immuables", "Le tableau original est convertu en chaîne"]
      ),
      TF("En JavaScript, les objets et tableaux sont assignés et passés par référence, contrairement aux primitives qui sont copiées par valeur.", true),
      S(
        "Comment éviter qu'une fonction modifie accidentellement un tableau reçu en paramètre ?",
        "En travaillant sur une copie du tableau (par exemple avec slice() ou le spread) avant de le modifier",
        ["Ce n'est pas possible, les tableaux sont toujours modifiés", "En utilisant typeof avant chaque appel", "En renommant le paramètre"]
      ),
      M(
        "Quelles situations illustrent le passage par référence des tableaux/objets ?",
        ["Deux variables pointant vers le même tableau, modifier l'une affecte l'autre", "Modifier un tableau reçu en paramètre de fonction affecte l'appelant"],
        ["Assigner un nombre à une nouvelle variable copie une référence partagée", "Les tableaux sont toujours clonés automatiquement lors d'une assignation"]
      ),
      TF("const tableau = [1, 2]; const copie = tableau; copie.push(3); affecte aussi la variable tableau car copie référence le même tableau.", true),
      S(
        "Pourquoi préfère-t-on souvent des opérations non-mutantes (comme le spread ou map/filter) dans les applications modernes (ex: React) ?",
        "Pour éviter les effets de bord inattendus et faciliter la détection des changements d'état",
        ["Parce que les mutations sont interdites par le langage", "Parce que cela rend le code plus difficile à comprendre intentionnellement", "Cela n'a aucun rapport avec la détection de changements"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux : Array.prototype.at() et accès négatif",
    "Accéder aux éléments d'un tableau ou d'une chaîne avec des index négatifs.",
    [
      S(
        "Que fait la méthode at() sur un tableau, introduite récemment en JavaScript ?",
        "Elle permet d'accéder à un élément par index, y compris avec un index négatif pour compter depuis la fin",
        ["Elle ajoute un élément à une position donnée", "Elle retourne toujours le premier élément", "Elle est un synonyme strict de indexOf()"]
      ),
      S(
        "Que retourne [10, 20, 30].at(-1) ?",
        "30",
        ["10", "undefined", "Une erreur"]
      ),
      TF("Avant l'introduction de at(), accéder au dernier élément nécessitait souvent tableau[tableau.length - 1].", true),
      M(
        "Quelles structures supportent la méthode at() en JavaScript moderne ?",
        ["Array", "String"],
        ["Object littéral simple"]
      ),
      TF("tableau[-1] (avec la notation crochets classique) ne retourne PAS le dernier élément d'un tableau, contrairement à at(-1).", true),
      S(
        "Pourquoi tableau[-1] ne fonctionne-t-il pas comme un index négatif sur un tableau JavaScript classique ?",
        "Parce que la notation crochets traite -1 comme un nom de propriété littéral, pas comme un index relatif à la fin",
        ["Parce que les tableaux ne supportent aucun accès par crochets", "Parce que -1 est toujours converti en 0", "Parce que c'est une erreur de syntaxe systématique"]
      ),
    ]
  ),

  Quiz(
    "JS — Variables globales et objet global",
    "L'objet global (window, globalThis) et la pollution de l'espace de noms.",
    [
      S(
        "Quel objet global permet d'accéder à l'environnement global de façon uniforme, quel que soit l'environnement d'exécution (navigateur, Node.js) ?",
        "globalThis",
        ["window uniquement", "self uniquement", "root"]
      ),
      TF("Dans un navigateur, window représente l'objet global, alors qu'en Node.js c'est généralement global ou globalThis.", true),
      S(
        "Pourquoi est-il déconseillé de créer trop de variables globales dans une application ?",
        "Parce que cela augmente le risque de collisions de noms et complique la maintenance du code",
        ["Parce que JavaScript limite strictement à 10 variables globales", "Parce que cela ralentit le démarrage du navigateur de façon mesurable systématiquement", "Il n'y a aucune raison valable, c'est une légende"]
      ),
      M(
        "Quelles pratiques aident à limiter la pollution de l'espace de noms global ?",
        ["Utiliser des modules ES avec import/export", "Encapsuler le code dans des IIFE ou des fonctions"],
        ["Déclarer systématiquement toutes les variables avec var au niveau racine", "Éviter complètement les fonctions"]
      ),
      TF("Les modules ES créent leur propre portée de module, ce qui évite que leurs variables top-level polluent l'objet global.", true),
      S(
        "Quel est le risque principal d'assigner une valeur à une variable sans la déclarer (sans var/let/const) en mode non strict ?",
        "Une variable globale est créée implicitement, ce qui peut provoquer des bugs difficiles à tracer",
        ["Aucun risque, c'est la pratique recommandée", "Une erreur de syntaxe est levée immédiatement dans tous les modes", "La variable devient automatiquement constante"]
      ),
    ]
  ),
];
