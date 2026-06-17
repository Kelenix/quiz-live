import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Méthode map()",
    "Transformer chaque élément d'un tableau avec Array.prototype.map().",
    [
      S(
        "Que fait la méthode map() sur un tableau ?",
        "Elle crée un nouveau tableau en appliquant une fonction à chaque élément",
        ["Elle modifie le tableau original en place sans rien retourner", "Elle filtre les éléments selon une condition", "Elle trie les éléments du tableau"]
      ),
      TF("map() retourne un nouveau tableau de la même longueur que le tableau original.", true),
      S(
        "Que retourne [1, 2, 3].map(x => x * 2) ?",
        "[2, 4, 6]",
        ["[1, 2, 3]", "6", "[1, 4, 9]"]
      ),
      M(
        "Quels paramètres la fonction de callback de map() peut-elle recevoir ?",
        ["L'élément courant", "L'index courant", "Le tableau original"],
        ["La longueur totale du tableau précédent"]
      ),
      TF("map() modifie le tableau d'origine (mutation).", false),
      S(
        "Quelle méthode utiliser si on veut transformer un tableau sans en créer un nouveau, en modifiant chaque élément en place ?",
        "Une boucle for ou forEach avec affectation par index, car map() ne mute pas",
        ["map() avec un second argument", "filter() avec callback de mutation", "reduce() seul"]
      ),
    ]
  ),

  Quiz(
    "JS — Méthode filter()",
    "Sélectionner des éléments d'un tableau selon une condition avec filter().",
    [
      S(
        "Que fait la méthode filter() ?",
        "Elle crée un nouveau tableau contenant uniquement les éléments qui satisfont une condition",
        ["Elle trie le tableau par ordre croissant", "Elle transforme chaque élément du tableau", "Elle supprime le tableau original"]
      ),
      S(
        "Que retourne [1, 2, 3, 4].filter(x => x % 2 === 0) ?",
        "[2, 4]",
        ["[1, 3]", "[1, 2, 3, 4]", "2"]
      ),
      TF("filter() retourne toujours un tableau, même vide si aucun élément ne correspond.", true),
      M(
        "Quelles affirmations sur filter() sont correctes ?",
        ["Le callback doit retourner un booléen (ou une valeur truthy/falsy)", "filter() ne modifie pas le tableau d'origine"],
        ["filter() retourne le premier élément trouvé uniquement", "filter() trie automatiquement le résultat"]
      ),
      TF("On peut chaîner filter() avec map() : tableau.filter(...).map(...)", true),
      S(
        "Quelle est la principale différence entre filter() et find() ?",
        "filter() retourne tous les éléments correspondants dans un tableau, find() retourne le premier élément trouvé seul",
        ["filter() retourne un booléen, find() retourne un tableau", "Aucune différence", "find() modifie le tableau, filter() non"]
      ),
    ]
  ),

  Quiz(
    "JS — Méthode reduce()",
    "Accumuler les valeurs d'un tableau en une seule valeur avec reduce().",
    [
      S(
        "Que fait la méthode reduce() ?",
        "Elle réduit un tableau à une seule valeur en appliquant une fonction accumulatrice",
        ["Elle réduit la taille du tableau de moitié", "Elle retourne uniquement le dernier élément", "Elle filtre les doublons"]
      ),
      S(
        "Que retourne [1, 2, 3, 4].reduce((acc, val) => acc + val, 0) ?",
        "10",
        ["[1, 2, 3, 4]", "24", "0"]
      ),
      TF("Le deuxième argument de reduce() définit la valeur initiale de l'accumulateur.", true),
      M(
        "Quels cas d'usage peuvent être implémentés avec reduce() ?",
        ["Calculer une somme ou un produit", "Transformer un tableau en objet"],
        ["Trier un tableau de façon stable obligatoirement", "Ajouter un élément en tête sans logique"]
      ),
      TF("Si aucune valeur initiale n'est fournie à reduce() et que le tableau est vide, une erreur est levée.", true),
      S(
        "Quels sont les paramètres reçus par le callback de reduce() dans l'ordre ?",
        "accumulateur, élément courant, index, tableau",
        ["élément courant, accumulateur, index, tableau", "index, élément courant, accumulateur", "tableau, accumulateur, index"]
      ),
    ]
  ),

  Quiz(
    "JS — forEach, find, some, every",
    "Parcourir et tester les éléments d'un tableau avec ces méthodes complémentaires.",
    [
      S(
        "Que retourne la méthode forEach() ?",
        "undefined, elle ne retourne pas de nouveau tableau",
        ["Un nouveau tableau transformé", "Un booléen", "Le premier élément du tableau"]
      ),
      S(
        "Que fait la méthode find() ?",
        "Elle retourne le premier élément du tableau qui satisfait une condition, ou undefined sinon",
        ["Elle retourne tous les éléments correspondants", "Elle retourne l'index du premier élément trouvé", "Elle modifie le tableau d'origine"]
      ),
      TF("La méthode some() retourne true si au moins un élément du tableau satisfait la condition donnée.", true),
      TF("La méthode every() retourne true uniquement si tous les éléments satisfont la condition donnée.", true),
      M(
        "Quelles méthodes parmi celles-ci retournent un booléen ?",
        ["some()", "every()"],
        ["find()", "forEach()"]
      ),
      S(
        "Que retourne [1, 2, 3].every(x => x > 0) ?",
        "true",
        ["false", "[1, 2, 3]", "undefined"]
      ),
    ]
  ),

  Quiz(
    "JS — Méthode sort()",
    "Trier les éléments d'un tableau avec sort() et ses pièges.",
    [
      S(
        "Que fait sort() par défaut sans fonction de comparaison sur un tableau de nombres ?",
        "Elle convertit les éléments en chaînes et trie selon l'ordre lexicographique, ce qui peut donner un résultat inattendu",
        ["Elle trie toujours numériquement de façon correcte", "Elle ne trie rien", "Elle lève systématiquement une erreur"]
      ),
      TF("sort() modifie le tableau original (mutation) et retourne aussi une référence à ce tableau.", true),
      S(
        "Comment trier un tableau de nombres par ordre croissant de façon fiable ?",
        "tableau.sort((a, b) => a - b)",
        ["tableau.sort()", "tableau.sort(true)", "tableau.order('asc')"]
      ),
      M(
        "Quelles affirmations sur la fonction de comparaison de sort() sont vraies ?",
        ["Un retour négatif place a avant b", "Un retour positif place a après b"],
        ["Elle doit toujours retourner un booléen", "Elle est ignorée pour les tableaux de nombres"]
      ),
      TF("[10, 1, 2].sort() sans callback donne [1, 10, 2] car le tri se fait sur la représentation en chaîne.", true),
      S(
        "Comment obtenir un tableau trié sans modifier l'original (depuis ES2023) ?",
        "Utiliser toSorted()",
        ["Utiliser sort() directement", "Utiliser reverse()", "Ce n'est pas possible nativement"]
      ),
    ]
  ),

  Quiz(
    "JS — Autres méthodes de tableaux",
    "push, pop, shift, unshift, slice, splice, includes, concat, flat.",
    [
      S(
        "Quelle méthode ajoute un ou plusieurs éléments à la fin d'un tableau ?",
        "push()",
        ["pop()", "shift()", "unshift()"]
      ),
      S(
        "Quelle méthode supprime le premier élément d'un tableau et le retourne ?",
        "shift()",
        ["pop()", "push()", "slice()"]
      ),
      TF("slice() ne modifie pas le tableau d'origine, elle retourne une copie partielle.", true),
      TF("splice() modifie le tableau d'origine en ajoutant et/ou supprimant des éléments.", true),
      M(
        "Quelles méthodes ne mutent PAS le tableau d'origine ?",
        ["slice()", "concat()", "map()"],
        ["splice()", "push()"]
      ),
      S(
        "Quelle méthode permet d'aplatir un tableau de tableaux imbriqués ?",
        "flat()",
        ["flatten()", "merge()", "concat() seul sans argument"]
      ),
    ]
  ),

  Quiz(
    "JS — Objets et propriétés",
    "Créer, lire et modifier des propriétés d'objets en JavaScript.",
    [
      S(
        "Quelle syntaxe crée un objet littéral avec une propriété nom valant 'Alice' ?",
        "{ nom: 'Alice' }",
        ["[nom: 'Alice']", "(nom: 'Alice')", "<nom: 'Alice'>"]
      ),
      M(
        "Quelles syntaxes permettent d'accéder à une propriété d'un objet ?",
        ["objet.propriete", "objet['propriete']"],
        ["objet->propriete", "objet::propriete"]
      ),
      TF("On peut utiliser une variable comme nom de propriété avec la notation crochets : objet[variable].", true),
      S(
        "Quelle méthode retourne un tableau des clés énumérables d'un objet ?",
        "Object.keys()",
        ["Object.values()", "Object.entries()", "Object.assign()"]
      ),
      S(
        "Que retourne Object.entries({a: 1, b: 2}) ?",
        "[['a', 1], ['b', 2]]",
        ["['a', 'b']", "[1, 2]", "{a: 1, b: 2}"]
      ),
      TF("delete objet.propriete supprime la propriété de l'objet.", true),
    ]
  ),

  Quiz(
    "JS — Prototypes et héritage prototypal",
    "Le mécanisme de prototype qui sous-tend l'héritage en JavaScript.",
    [
      S(
        "Qu'est-ce que le prototype d'un objet en JavaScript ?",
        "Un objet dont héritent les propriétés et méthodes lorsque celles-ci ne sont pas trouvées directement sur l'objet",
        ["Une copie figée de l'objet au moment de sa création", "Un type de donnée primitif", "Une fonction de validation des données"]
      ),
      TF("Tous les objets JavaScript (sauf ceux créés avec Object.create(null)) ont un prototype.", true),
      S(
        "Quelle propriété permet d'accéder explicitement au prototype d'un objet ?",
        "Object.getPrototypeOf(objet)",
        ["objet.prototype directement sur une instance", "objet.parent", "objet.base"]
      ),
      M(
        "Quelles affirmations sur la chaîne de prototypes sont vraies ?",
        ["La recherche d'une propriété remonte la chaîne jusqu'à Object.prototype", "On peut créer un objet sans prototype avec Object.create(null)"],
        ["Chaque objet a plusieurs prototypes simultanément", "La chaîne de prototypes est limitée à un seul niveau"]
      ),
      TF("Les classes ES6 (class) utilisent le prototype en interne pour l'héritage.", true),
      S(
        "Quel opérateur vérifie si un objet est une instance d'une classe/constructeur donné ?",
        "instanceof",
        ["typeof", "in", "hasOwnProperty"]
      ),
    ]
  ),

  Quiz(
    "JS — Destructuring",
    "Extraire des valeurs de tableaux et d'objets via la déstructuration.",
    [
      S(
        "Quelle syntaxe extrait correctement la propriété nom d'un objet personne dans une variable nom ?",
        "const { nom } = personne;",
        ["const nom = { personne };", "const [nom] = personne;", "const nom -> personne;"]
      ),
      S(
        "Quelle syntaxe extrait le premier élément d'un tableau coordonnees dans une variable x ?",
        "const [x] = coordonnees;",
        ["const { x } = coordonnees;", "const x = coordonnees{0};", "const x := coordonnees[0];"]
      ),
      TF("On peut renommer une propriété lors de la déstructuration d'objet : const { nom: prenomUtilisateur } = personne;", true),
      M(
        "Quelles fonctionnalités sont possibles avec le destructuring ?",
        ["Définir une valeur par défaut : const { age = 18 } = personne;", "Déstructurer des paramètres de fonction directement"],
        ["Déstructurer uniquement les tableaux, jamais les objets", "Modifier l'objet source automatiquement"]
      ),
      TF("La déstructuration imbriquée est possible : const { adresse: { ville } } = personne;", true),
      S(
        "Comment ignorer le deuxième élément d'un tableau lors de la déstructuration ?",
        "const [premier, , troisieme] = tableau;",
        ["const [premier, _skip_, troisieme] = tableau;", "const [premier, troisieme] = tableau.skip(1);", "Ce n'est pas possible"]
      ),
    ]
  ),

  Quiz(
    "JS — Spread et rest",
    "Les opérateurs ... pour étaler ou regrouper des valeurs.",
    [
      S(
        "Que fait l'opérateur spread (...) appliqué à un tableau dans un nouvel tableau littéral ?",
        "Il étale les éléments du tableau source dans le nouveau tableau",
        ["Il copie une référence au tableau source uniquement", "Il fusionne les clés en supprimant les doublons obligatoirement", "Il convertit le tableau en chaîne"]
      ),
      S(
        "Que retourne [...[1, 2], ...[3, 4]] ?",
        "[1, 2, 3, 4]",
        ["[[1, 2], [3, 4]]", "[1, 2]", "Une erreur"]
      ),
      TF("L'opérateur rest (...) regroupe les arguments restants d'une fonction dans un tableau.", true),
      M(
        "Quels usages sont possibles avec l'opérateur spread/rest ?",
        ["Copier superficiellement un objet : { ...obj }", "Capturer les arguments restants : function f(a, ...reste) {}"],
        ["Créer une boucle infinie", "Remplacer obligatoirement JSON.stringify"]
      ),
      TF("function somme(...nombres) accepte un nombre variable d'arguments regroupés dans un tableau nombres.", true),
      S(
        "Quelle est la différence entre spread et rest bien qu'ils utilisent la même syntaxe ... ?",
        "Spread étale des éléments, rest regroupe des éléments restants en un tableau/objet",
        ["Aucune différence, ce sont des synonymes stricts", "Rest ne fonctionne que sur les objets", "Spread ne fonctionne que dans les fonctions"]
      ),
    ]
  ),

  Quiz(
    "JS — Classes ES6",
    "La syntaxe de classe introduite par ES6 pour structurer du code orienté objet.",
    [
      S(
        "Quel mot-clé permet de définir une classe en JavaScript moderne ?",
        "class",
        ["struct", "object", "type"]
      ),
      S(
        "Quelle méthode spéciale est appelée automatiquement lors de la création d'une instance ?",
        "constructor()",
        ["init()", "create()", "new()"]
      ),
      TF("Les classes ES6 sont en réalité du sucre syntaxique au-dessus du système de prototypes existant.", true),
      M(
        "Quels éléments peuvent être définis à l'intérieur d'une classe ES6 ?",
        ["Des méthodes d'instance", "Des méthodes et propriétés statiques (static)"],
        ["Des balises HTML", "Des feuilles de style CSS"]
      ),
      TF("Le code à l'intérieur du corps d'une classe est exécuté en mode strict automatiquement.", true),
      S(
        "Comment définir une méthode statique appelée directement sur la classe et non sur une instance ?",
        "static nomMethode() { }",
        ["this.static.nomMethode() { }", "global nomMethode() { }", "const nomMethode = static() { }"]
      ),
    ]
  ),

  Quiz(
    "JS — Héritage avec extends et super",
    "L'héritage entre classes via extends et l'appel au parent avec super.",
    [
      S(
        "Quel mot-clé permet à une classe d'hériter d'une autre classe ?",
        "extends",
        ["inherits", "implements", "uses"]
      ),
      S(
        "À quoi sert l'appel super() dans le constructeur d'une classe enfant ?",
        "Il appelle le constructeur de la classe parente pour initialiser l'état hérité",
        ["Il supprime les propriétés héritées", "Il crée une nouvelle instance de la classe parente séparée", "Il est purement optionnel et sans effet"]
      ),
      TF("Dans une classe enfant avec un constructeur personnalisé, super() doit être appelé avant d'utiliser this.", true),
      M(
        "Quelles affirmations sur l'héritage de classes sont correctes ?",
        ["Une classe enfant peut redéfinir (override) une méthode du parent", "super.methode() permet d'appeler la version du parent depuis l'enfant"],
        ["Une classe ne peut hériter que de deux classes parentes simultanément", "extends interdit toute redéfinition de méthode"]
      ),
      TF("instanceof retourne true pour une instance d'une classe enfant testée contre la classe parente.", true),
      S(
        "Que se passe-t-il si une classe enfant n'a pas de constructeur explicite ?",
        "Un constructeur implicite appelant super(...args) est utilisé",
        ["Une erreur de compilation est levée systématiquement", "this devient automatiquement null", "L'héritage est annulé"]
      ),
    ]
  ),

  Quiz(
    "JS — Getters, setters et propriétés calculées",
    "Définir des accesseurs personnalisés et des noms de propriétés dynamiques.",
    [
      S(
        "Quel mot-clé permet de définir un accesseur en lecture personnalisé dans une classe ou un objet ?",
        "get",
        ["read", "fetch", "access"]
      ),
      S(
        "Quel mot-clé permet de définir un accesseur en écriture personnalisé ?",
        "set",
        ["write", "assign", "put"]
      ),
      TF("Un getter permet d'exposer une propriété calculée comme si elle était une propriété simple, sans parenthèses lors de l'accès.", true),
      M(
        "Quels usages sont pertinents pour les getters/setters ?",
        ["Valider une valeur avant de l'assigner via un setter", "Calculer une valeur dérivée à la volée via un getter"],
        ["Remplacer obligatoirement tous les attributs publics", "Empêcher totalement l'accès à une propriété"]
      ),
      TF("On peut utiliser une expression entre crochets comme nom de propriété calculée dans un objet littéral : { [cle]: valeur }.", true),
      S(
        "Dans une classe, comment déclare-t-on une propriété privée (syntaxe moderne) ?",
        "Avec un préfixe # : #proprietePrivee",
        ["Avec le mot-clé private devant le nom", "Avec un underscore obligatoire uniquement", "Ce n'est pas possible nativement"]
      ),
    ]
  ),
];
