import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Introduction aux Promises",
    "Le concept de Promise pour gérer les opérations asynchrones.",
    [
      S(
        "Qu'est-ce qu'une Promise en JavaScript ?",
        "Un objet représentant l'issue future (succès ou échec) d'une opération asynchrone",
        ["Une fonction qui s'exécute toujours de façon synchrone", "Un type de tableau spécial", "Une boucle d'attente bloquante"]
      ),
      M(
        "Quels sont les trois états possibles d'une Promise ?",
        ["pending", "fulfilled", "rejected"],
        ["paused", "cancelled"]
      ),
      TF("Une fois qu'une Promise est résolue ou rejetée, son état ne peut plus changer.", true),
      S(
        "Quelle méthode permet de réagir à la résolution réussie d'une Promise ?",
        ".then()",
        [".resolve()", ".success()", ".done()"]
      ),
      S(
        "Quelle méthode permet de réagir à un rejet (erreur) d'une Promise ?",
        ".catch()",
        [".error()", ".fail()", ".reject()"]
      ),
      TF(".finally() s'exécute que la Promise soit résolue ou rejetée.", true),
    ]
  ),

  Quiz(
    "JS — Créer et chaîner des Promises",
    "Construire une Promise et enchaîner plusieurs opérations asynchrones.",
    [
      S(
        "Quelle syntaxe crée une nouvelle Promise ?",
        "new Promise((resolve, reject) => { })",
        ["Promise.create(() => {})", "new Promise.start()", "async Promise(() => {})"]
      ),
      TF("On peut chaîner plusieurs .then() successifs pour traiter des étapes asynchrones en séquence.", true),
      S(
        "Que se passe-t-il si on retourne une valeur simple (non-Promise) dans un .then() ?",
        "Elle est automatiquement enveloppée dans une Promise résolue pour le .then() suivant",
        ["Une erreur est levée immédiatement", "La chaîne de promesses s'arrête silencieusement", "La valeur est ignorée"]
      ),
      M(
        "Quelles méthodes statiques de Promise permettent de gérer plusieurs promesses en parallèle ?",
        ["Promise.all()", "Promise.race()", "Promise.allSettled()"],
        ["Promise.sequence()"]
      ),
      TF("Promise.all() rejette dès qu'une des promesses passées échoue, même si les autres réussissent.", true),
      S(
        "Quelle différence existe entre Promise.all() et Promise.allSettled() ?",
        "allSettled() attend toutes les promesses et retourne leur statut individuel, même en cas d'échec de certaines",
        ["Aucune différence", "all() ignore les erreurs", "allSettled() s'arrête à la première erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — async/await",
    "La syntaxe async/await pour écrire du code asynchrone de façon plus lisible.",
    [
      S(
        "Que retourne toujours une fonction déclarée avec async ?",
        "Une Promise",
        ["Un tableau", "undefined systématiquement", "Une valeur synchrone brute"]
      ),
      S(
        "Où peut-on utiliser le mot-clé await ?",
        "Uniquement à l'intérieur d'une fonction async (ou au niveau module dans certains contextes)",
        ["N'importe où dans le code, sans restriction", "Uniquement dans les boucles for", "Uniquement dans les callbacks classiques"]
      ),
      TF("await met en pause l'exécution de la fonction async jusqu'à ce que la Promise soit résolue ou rejetée.", true),
      M(
        "Comment gérer une erreur levée par un await qui échoue ?",
        ["Avec un bloc try/catch autour du await", "En chaînant un .catch() sur la Promise retournée par la fonction async"],
        ["C'est impossible à gérer", "En utilisant uniquement des callbacks"]
      ),
      TF("async/await est construit au-dessus des Promises, ce n'est pas un mécanisme totalement différent.", true),
      S(
        "Quel est l'avantage principal d'async/await par rapport aux chaînes de .then() ?",
        "Un code asynchrone plus lisible, qui ressemble à du code synchrone séquentiel",
        ["Une exécution garantie plus rapide", "La suppression totale du besoin de gestion d'erreurs", "Il remplace complètement le besoin de Promises en interne"]
      ),
    ]
  ),

  Quiz(
    "JS — Boucle d'événements (event loop)",
    "Comprendre comment JavaScript gère l'asynchrone avec un seul thread.",
    [
      S(
        "JavaScript est-il un langage mono-thread ou multi-thread par défaut ?",
        "Mono-thread (un seul thread d'exécution principal)",
        ["Multi-thread natif sans aucune limitation", "Cela dépend du navigateur uniquement", "Aucun thread, exécution purement événementielle sans pile"]
      ),
      S(
        "Quel est le rôle de la boucle d'événements (event loop) ?",
        "Elle gère l'exécution des tâches en attente (callbacks, promesses) en les plaçant dans la pile d'appels quand celle-ci est libre",
        ["Elle crée de nouveaux threads pour chaque opération asynchrone", "Elle exécute le code en parallèle réel", "Elle remplace la pile d'appels"]
      ),
      TF("Les microtasks (comme les callbacks de Promise) sont traitées avant les macrotasks (comme setTimeout) à chaque cycle de la boucle d'événements.", true),
      M(
        "Lesquels de ces éléments sont considérés comme des macrotasks ?",
        ["setTimeout", "setInterval"],
        ["Les callbacks .then() des Promises", "Les microtasks queue elle-même"]
      ),
      TF("La pile d'appels (call stack) doit être vide avant que l'event loop ne traite la tâche suivante de la file.", true),
      S(
        "Que se passe-t-il si le thread principal est bloqué par un calcul long et synchrone ?",
        "L'interface utilisateur se bloque et les callbacks en attente ne peuvent pas s'exécuter",
        ["Rien, un autre thread prend automatiquement le relais", "Les microtasks s'exécutent malgré tout en parallèle", "Le navigateur crée un nouveau processus instantanément"]
      ),
    ]
  ),

  Quiz(
    "JS — Microtasks et macrotasks",
    "L'ordre d'exécution précis entre tâches synchrones, microtasks et macrotasks.",
    [
      S(
        "Quel est l'ordre d'exécution typique entre code synchrone, microtasks et macrotasks ?",
        "Code synchrone, puis toutes les microtasks en attente, puis une macrotask",
        ["Macrotask, puis microtasks, puis code synchrone", "Microtasks puis code synchrone puis macrotasks", "Il n'y a aucun ordre garanti"]
      ),
      M(
        "Lesquels sont des exemples de microtasks ?",
        [".then() d'une Promise résolue", "queueMicrotask()"],
        ["setTimeout(fn, 0)", "setInterval"]
      ),
      TF("Si plusieurs microtasks sont mises en attente, elles sont toutes exécutées avant la prochaine macrotask.", true),
      S(
        "Entre console.log('A'); setTimeout(() => console.log('B'), 0); Promise.resolve().then(() => console.log('C')); console.log('D');, quel est l'ordre d'affichage ?",
        "A, D, C, B",
        ["A, B, C, D", "A, D, B, C", "D, A, C, B"]
      ),
      TF("setTimeout(fn, 0) n'exécute pas fn immédiatement, elle attend que la pile d'appels soit vide et passe après les microtasks.", true),
      S(
        "Pourquoi peut-on observer des délais plus longs que prévu avec setTimeout dans une application chargée ?",
        "Parce que le délai est un minimum, et le callback doit attendre que le thread principal et les microtasks soient libres",
        ["Parce que setTimeout est cassé par défaut", "Parce que le délai est toujours multiplié par 10", "Parce que JavaScript ignore les setTimeout après le premier appel"]
      ),
    ]
  ),

  Quiz(
    "JS — Gestion d'erreurs avec try/catch/finally",
    "Capturer et traiter les exceptions en JavaScript.",
    [
      S(
        "Quel bloc permet de capturer une erreur levée dans un bloc try ?",
        "catch",
        ["finally", "except", "rescue"]
      ),
      TF("Le bloc finally s'exécute toujours, qu'une erreur ait été levée ou non.", true),
      S(
        "Quel mot-clé permet de déclencher manuellement une exception ?",
        "throw",
        ["raise", "error", "fail"]
      ),
      M(
        "Quelles informations contient généralement un objet Error ?",
        ["Une propriété message", "Une propriété name (type d'erreur)"],
        ["Une propriété correctAnswer", "Une propriété timeout obligatoire"]
      ),
      TF("On peut créer un type d'erreur personnalisé en étendant la classe Error avec extends.", true),
      S(
        "Que se passe-t-il si une erreur est levée dans un bloc try sans bloc catch correspondant ni finally ?",
        "L'erreur se propage normalement (non interceptée) vers l'appelant",
        ["Elle est automatiquement ignorée silencieusement", "Le programme s'arrête sans message", "Elle est convertie en avertissement"]
      ),
    ]
  ),

  Quiz(
    "JS — Fetch API",
    "Effectuer des requêtes réseau côté navigateur avec fetch().",
    [
      S(
        "Que retourne un appel à fetch() ?",
        "Une Promise qui se résout avec un objet Response",
        ["Directement les données JSON", "Une chaîne de caractères brute", "Un objet XMLHttpRequest"]
      ),
      S(
        "Quelle méthode de l'objet Response permet d'extraire le corps en JSON ?",
        "response.json()",
        ["response.toJSON()", "response.parse()", "response.data()"]
      ),
      TF("fetch() ne rejette pas automatiquement la Promise pour les codes de statut HTTP d'erreur comme 404 ou 500.", true),
      M(
        "Quelles options peut-on configurer dans le second argument de fetch() ?",
        ["La méthode HTTP (method)", "Les en-têtes (headers)", "Le corps de la requête (body)"],
        ["Le nom de domaine cible obligatoire séparé"]
      ),
      TF("On utilise généralement async/await ou .then() pour traiter la réponse de fetch() car elle est asynchrone.", true),
      S(
        "Comment vérifier qu'une requête fetch a réussi côté HTTP avant de parser le JSON ?",
        "En testant la propriété response.ok",
        ["En testant response.success", "fetch() lève toujours une exception automatiquement en cas d'erreur HTTP", "Ce n'est pas possible"]
      ),
    ]
  ),

  Quiz(
    "JS — JSON.parse et JSON.stringify",
    "Convertir entre objets JavaScript et chaînes JSON.",
    [
      S(
        "Que fait JSON.stringify() ?",
        "Elle convertit une valeur JavaScript en chaîne de caractères au format JSON",
        ["Elle convertit une chaîne JSON en objet JavaScript", "Elle valide la syntaxe d'un objet", "Elle compresse un fichier JSON"]
      ),
      S(
        "Que fait JSON.parse() ?",
        "Elle convertit une chaîne JSON en valeur JavaScript (objet, tableau, etc.)",
        ["Elle convertit un objet JavaScript en chaîne JSON", "Elle valide un fichier JSON sans le convertir", "Elle supprime les espaces d'une chaîne"]
      ),
      TF("JSON.stringify() ignore les propriétés dont la valeur est une fonction ou undefined.", true),
      M(
        "Quels types de données ne sont PAS correctement supportés nativement par JSON (sérialisation directe) ?",
        ["undefined", "Les fonctions", "Symbol"],
        ["Les chaînes de caractères", "Les nombres"]
      ),
      TF("JSON.parse() lève une exception si la chaîne fournie n'est pas un JSON valide.", true),
      S(
        "Quel est le troisième argument optionnel de JSON.stringify() qui sert à l'indentation ?",
        "Un nombre d'espaces ou une chaîne d'indentation",
        ["Un booléen indiquant la compression", "Une fonction de tri obligatoire", "Le type d'encodage"]
      ),
    ]
  ),

  Quiz(
    "JS — Générateurs (function* et yield)",
    "Les fonctions génératrices qui produisent des valeurs à la demande.",
    [
      S(
        "Comment déclare-t-on une fonction génératrice ?",
        "function* nomFonction() { }",
        ["function nomFonction*() { }", "generator nomFonction() { }", "async function* uniquement"]
      ),
      S(
        "Quel mot-clé met en pause l'exécution d'un générateur et retourne une valeur ?",
        "yield",
        ["return", "pause", "await"]
      ),
      TF("Un générateur retourne un objet itérateur qui produit des valeurs via la méthode next().", true),
      M(
        "Quelles affirmations sur les générateurs sont correctes ?",
        ["Ils permettent de créer des séquences potentiellement infinies sans tout stocker en mémoire", "On peut les parcourir avec for...of"],
        ["Ils s'exécutent toujours entièrement dès leur appel", "Ils ne peuvent jamais recevoir de valeur via next(valeur)"]
      ),
      TF("L'appel d'une fonction génératrice ne lance pas immédiatement son code, elle retourne un itérateur en pause.", true),
      S(
        "Quelle méthode de l'itérateur permet de reprendre l'exécution d'un générateur jusqu'au prochain yield ?",
        "next()",
        ["resume()", "continue()", "run()"]
      ),
    ]
  ),

  Quiz(
    "JS — Map et Set",
    "Les structures de données Map et Set introduites par ES6.",
    [
      S(
        "Quelle est la principale différence entre un objet classique et un Map ?",
        "Un Map peut utiliser n'importe quel type de valeur comme clé, pas seulement des chaînes",
        ["Un Map ne peut contenir que des nombres", "Un objet classique est plus rapide dans tous les cas", "Aucune différence"]
      ),
      S(
        "Quelle structure stocke uniquement des valeurs uniques, sans clé associée ?",
        "Set",
        ["Map", "WeakMap", "Array"]
      ),
      TF("Un Set ignore automatiquement les doublons lors de l'ajout d'une valeur déjà présente.", true),
      M(
        "Quelles méthodes sont disponibles sur un objet Map ?",
        ["set()", "get()", "has()"],
        ["push()"]
      ),
      TF("On peut convertir un Set en tableau avec Array.from(monSet) ou [...monSet].", true),
      S(
        "Quelle propriété donne le nombre d'éléments d'un Map ou d'un Set ?",
        "size",
        ["length", "count", "total"]
      ),
    ]
  ),

  Quiz(
    "JS — WeakMap et WeakSet (notions)",
    "Les collections faibles qui n'empêchent pas le garbage collector d'agir.",
    [
      S(
        "Quelle est la particularité principale d'un WeakMap par rapport à un Map classique ?",
        "Les clés doivent être des objets et ne sont pas retenues fortement, permettant leur collecte par le garbage collector",
        ["Il fonctionne exactement comme un Map mais plus lentement", "Il ne peut contenir aucune valeur", "Il est itérable comme un tableau classique"]
      ),
      TF("On ne peut pas itérer directement sur les entrées d'un WeakMap (pas de méthode forEach ou keys()).", true),
      S(
        "Pourquoi utiliser un WeakMap plutôt qu'un Map pour associer des métadonnées à des objets DOM ?",
        "Pour éviter les fuites de mémoire si l'élément DOM est supprimé ailleurs dans le code",
        ["Pour accélérer toutes les opérations de lecture", "Parce que Map ne peut pas avoir d'objets comme clés", "Parce que WeakMap est plus simple à parcourir"]
      ),
      M(
        "Quelles restrictions s'appliquent à WeakSet ?",
        ["Il ne peut contenir que des objets, pas de primitives", "Il n'est pas itérable"],
        ["Il peut contenir des nombres et chaînes librement", "Il fonctionne uniquement avec des tableaux"]
      ),
      TF("WeakMap et WeakSet n'ont pas de propriété size accessible directement.", true),
      S(
        "Quel est le principal avantage des collections faibles (Weak) pour la gestion mémoire ?",
        "Elles permettent au garbage collector de libérer la mémoire des objets qui ne sont plus référencés ailleurs",
        ["Elles consomment deux fois plus de mémoire pour plus de sécurité", "Elles empêchent toute suppression d'objet", "Elles dupliquent automatiquement les données"]
      ),
    ]
  ),

  Quiz(
    "JS — Symbol (notions)",
    "Le type primitif Symbol pour créer des identifiants uniques.",
    [
      S(
        "Que produit chaque appel à Symbol() ?",
        "Une valeur unique et immuable, différente de toute autre valeur même avec la même description",
        ["Toujours la même valeur pour la même description", "Une chaîne de caractères classique", "Un nombre aléatoire"]
      ),
      TF("Deux appels Symbol('id') produisent deux symboles différents et non égaux entre eux.", true),
      S(
        "Pourquoi les symboles sont-ils utiles comme clés de propriété d'objet ?",
        "Pour créer des propriétés qui n'entrent pas en collision avec d'autres clés et sont peu visibles dans les boucles classiques",
        ["Pour rendre les objets plus rapides à itérer", "Pour remplacer entièrement les chaînes en JSON", "Pour forcer la sérialisation JSON"]
      ),
      M(
        "Quelles affirmations sur les symboles sont vraies ?",
        ["Ils ne sont pas énumérés par for...in ni Object.keys()", "Symbol.iterator est utilisé pour définir le comportement itérable d'un objet"],
        ["Ils sont automatiquement convertis en chaînes lors de la concaténation avec +", "Ils peuvent être créés avec l'opérateur new Symbol()"]
      ),
      TF("Symbol.for(cle) permet de récupérer un symbole partagé globalement à partir d'une clé donnée.", true),
      S(
        "new Symbol() est-il une syntaxe valide en JavaScript ?",
        "Non, cela lève une TypeError car Symbol n'est pas un constructeur utilisable avec new",
        ["Oui, c'est la façon recommandée de créer un symbole", "Oui mais uniquement en mode strict", "Oui, et cela retourne toujours le même symbole"]
      ),
    ]
  ),
];
