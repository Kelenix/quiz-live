import { S, M, TF, Quiz } from "./helpers.mjs";

export const quizzes = [
  Quiz(
    "JS — Tableaux : agrégation avancée avec reduce",
    "Utiliser reduce() pour des transformations plus complexes que la simple somme.",
    [
      S(
        "Que retourne ['a','b','c'].reduce((acc, val) => acc + val, '') ?",
        "'abc'",
        ["['a','b','c']", "'a,b,c'", "undefined"]
      ),
      TF("reduce() peut être utilisé pour transformer un tableau d'objets en un objet indexé par une clé (regroupement).", true),
      S(
        "Avec quelle méthode peut-on trouver la valeur maximale d'un tableau de nombres en utilisant reduce ?",
        "tableau.reduce((max, val) => val > max ? val : max)",
        ["tableau.reduce(Math.max)", "tableau.max()", "tableau.reduce.max()"]
      ),
      M(
        "Quels résultats peut produire un reduce() selon la logique du callback ?",
        ["Un nombre (somme, produit...)", "Un objet (regroupement de données)", "Un tableau (reconstruction filtrée)"],
        ["Toujours uniquement un booléen"]
      ),
      TF("reduceRight() applique la même logique que reduce() mais en parcourant le tableau de droite à gauche.", true),
      S(
        "Pourquoi fournir une valeur initiale à reduce() est-il considéré comme une bonne pratique ?",
        "Pour éviter les erreurs sur les tableaux vides et garantir un comportement prévisible",
        ["Parce que c'est obligatoire syntaxiquement dans tous les cas", "Parce que cela rend le code plus lent intentionnellement", "Cela n'a aucun effet sur le comportement"]
      ),
    ]
  ),

  Quiz(
    "JS — Programmation fonctionnelle : composition",
    "Combiner plusieurs fonctions pures pour construire des comportements complexes.",
    [
      S(
        "Qu'est-ce qu'une fonction pure en programmation fonctionnelle ?",
        "Une fonction qui retourne toujours le même résultat pour les mêmes arguments et n'a pas d'effets de bord",
        ["Une fonction qui modifie des variables globales", "Une fonction qui dépend de l'heure système", "Une fonction qui affiche toujours un message dans la console"]
      ),
      TF("La composition de fonctions consiste à combiner plusieurs fonctions simples pour en créer une plus complexe.", true),
      S(
        "Quel terme désigne le fait d'éviter de modifier les données existantes et de toujours en créer de nouvelles ?",
        "L'immuabilité (immutability)",
        ["Le hoisting", "Le polymorphisme", "Le garbage collecting"]
      ),
      M(
        "Quels avantages procure la programmation avec des fonctions pures ?",
        ["Un code plus facile à tester unitairement", "Une meilleure prévisibilité du comportement"],
        ["Une élimination totale du besoin de boucles", "Une garantie de vitesse d'exécution supérieure dans tous les cas"]
      ),
      TF("Un effet de bord est une modification observable hors de la fonction, comme modifier une variable globale ou écrire dans la console.", true),
      S(
        "Pourquoi les méthodes map/filter/reduce sont-elles souvent associées à un style fonctionnel ?",
        "Parce qu'elles encouragent à utiliser des callbacks sans muter les données d'origine",
        ["Parce qu'elles sont les seules méthodes disponibles sur les tableaux", "Parce qu'elles interdisent l'usage de variables", "Parce qu'elles remplacent obligatoirement les classes"]
      ),
    ]
  ),

  Quiz(
    "JS — Gestion avancée des erreurs asynchrones",
    "Capturer les erreurs dans les Promises et les fonctions async.",
    [
      S(
        "Comment capturer une erreur survenue dans une Promise rejetée sans async/await ?",
        "Avec un .catch() chaîné à la Promise",
        ["Avec un simple if après l'appel", "Les erreurs de Promise ne peuvent pas être capturées", "Avec un bloc finally uniquement"]
      ),
      TF("Une erreur non capturée dans une Promise peut déclencher l'événement unhandledrejection.", true),
      S(
        "Dans une fonction async, comment capturer une erreur levée par un await ?",
        "En entourant le await d'un bloc try/catch",
        ["Ce n'est pas possible avec async/await", "En utilisant uniquement .catch() sur la fonction elle-même sans try/catch", "En ajoutant un paramètre error à la fonction"]
      ),
      M(
        "Quelles bonnes pratiques aident à éviter les erreurs silencieuses en code asynchrone ?",
        ["Toujours ajouter un .catch() ou un try/catch", "Vérifier les erreurs HTTP via response.ok avec fetch"],
        ["Ignorer les erreurs pour simplifier le code", "Éviter complètement async/await"]
      ),
      TF("On peut combiner try/catch avec Promise.all() pour capturer la première erreur parmi plusieurs promesses parallèles.", true),
      S(
        "Que se passe-t-il si une fonction async lève une exception non interceptée ?",
        "La Promise retournée par la fonction async est rejetée avec cette erreur",
        ["Le programme s'arrête immédiatement sans Promise", "L'erreur est ignorée silencieusement", "Une nouvelle fonction est créée automatiquement"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux de tableaux et structures imbriquées",
    "Manipuler des structures de données imbriquées (matrices, listes de listes).",
    [
      S(
        "Comment accéder à l'élément en deuxième ligne, première colonne d'une matrice représentée par un tableau de tableaux nommé matrice ?",
        "matrice[1][0]",
        ["matrice[2][1]", "matrice(1,0)", "matrice.get(1,0)"]
      ),
      TF("flat(Infinity) aplatit un tableau imbriqué à n'importe quelle profondeur.", true),
      S(
        "Quelle méthode permet à la fois de transformer puis d'aplatir un niveau d'un tableau ?",
        "flatMap()",
        ["mapFlat()", "reduceFlat()", "flattenMap()"]
      ),
      M(
        "Quels usages typiques nécessitent de manipuler des tableaux imbriqués ?",
        ["Représenter une grille ou matrice 2D", "Représenter une arborescence de catégories"],
        ["Stocker un seul nombre", "Remplacer les objets dans tous les cas"]
      ),
      TF("Un tableau peut contenir des éléments de types différents, y compris d'autres tableaux ou objets.", true),
      S(
        "Que retourne [[1,2],[3,4]].flat() ?",
        "[1, 2, 3, 4]",
        ["[[1,2],[3,4]]", "[1,2,3,4,[3,4]]", "Une erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Conditions et structures de contrôle",
    "if/else, switch et l'opérateur ternaire pour le contrôle de flux.",
    [
      S(
        "Quelle syntaxe représente un opérateur ternaire correct ?",
        "condition ? valeurSiVrai : valeurSiFaux",
        ["condition => valeurSiVrai : valeurSiFaux", "if condition then valeurSiVrai else valeurSiFaux", "condition ?? valeurSiVrai !! valeurSiFaux"]
      ),
      TF("Une instruction switch utilise généralement break pour éviter l'exécution en cascade (fall-through) des cas suivants.", true),
      S(
        "Que se passe-t-il si on omet le mot-clé break dans un cas d'un switch (et que le cas correspond) ?",
        "L'exécution continue dans le cas suivant (fall-through) jusqu'au prochain break ou la fin du switch",
        ["Une erreur de syntaxe est levée", "Le switch s'arrête immédiatement de toute façon", "Le cas suivant est ignoré automatiquement"]
      ),
      M(
        "Quelles structures permettent de contrôler le flux conditionnel en JavaScript ?",
        ["if / else if / else", "switch / case", "L'opérateur ternaire ?:"],
        ["for...of comme structure conditionnelle"]
      ),
      TF("Le cas 'default' d'un switch s'exécute si aucun autre cas ne correspond.", true),
      S(
        "Quelle structure est généralement préférée pour une condition simple retournant une valeur, plutôt qu'un if/else complet ?",
        "L'opérateur ternaire",
        ["Le mot-clé goto", "Une boucle while", "Le mot-clé case isolé"]
      ),
    ]
  ),

  Quiz(
    "JS — Object.assign et fusion d'objets",
    "Fusionner plusieurs objets avec Object.assign() ou le spread.",
    [
      S(
        "Que fait Object.assign(cible, source) ?",
        "Elle copie les propriétés énumérables de source vers cible et retourne cible modifié",
        ["Elle crée une copie profonde indépendante de source", "Elle supprime les propriétés de cible non présentes dans source", "Elle compare cible et source"]
      ),
      TF("Object.assign({}, obj1, obj2) fusionne obj1 et obj2 dans un nouvel objet, les propriétés de obj2 écrasant celles de obj1 en cas de conflit.", true),
      S(
        "Quelle syntaxe avec spread est équivalente à Object.assign({}, obj1, obj2) ?",
        "{ ...obj1, ...obj2 }",
        ["[...obj1, ...obj2]", "obj1 + obj2", "Object.merge(obj1, obj2)"]
      ),
      M(
        "Quelles affirmations sur Object.assign() sont vraies ?",
        ["Elle ne copie que les propriétés énumérables propres (pas héritées)", "Elle effectue une copie superficielle, pas profonde"],
        ["Elle clone aussi les méthodes du prototype", "Elle fonctionne uniquement sur les tableaux"]
      ),
      TF("Si deux objets fusionnés ont une même clé, la valeur du dernier objet source l'emporte.", true),
      S(
        "Pourquoi utiliser le spread { ...obj } plutôt que Object.assign({}, obj) aujourd'hui ?",
        "Pour une syntaxe plus concise, le résultat final étant équivalent pour une copie superficielle simple",
        ["Parce que Object.assign() est obsolète et supprimé des moteurs", "Parce que le spread fait une copie profonde contrairement à Object.assign", "Il n'y a aucune raison, ils sont incompatibles"]
      ),
    ]
  ),

  Quiz(
    "JS — Fonctions génératrices avancées",
    "Déléguer entre générateurs et transmettre des valeurs avec yield.",
    [
      S(
        "Que fait yield* à l'intérieur d'un générateur ?",
        "Il délègue l'itération à un autre objet itérable ou générateur",
        ["Il met fin immédiatement au générateur", "Il multiplie la valeur courante", "Il convertit le générateur en Promise"]
      ),
      TF("On peut transmettre une valeur à un générateur en passant un argument à next(valeur), qui devient le résultat de l'expression yield en pause.", true),
      S(
        "Quelle méthode permet d'arrêter prématurément un générateur en lui injectant une valeur de retour ?",
        "return(valeur)",
        ["stop(valeur)", "end(valeur)", "halt(valeur)"]
      ),
      M(
        "Quels cas d'usage concrets exploitent les générateurs ?",
        ["Créer des séquences infinies paresseuses (lazy)", "Implémenter des itérateurs personnalisés complexes"],
        ["Remplacer obligatoirement toutes les boucles for", "Convertir un objet en JSON"]
      ),
      TF("Un générateur asynchrone se déclare avec async function* et utilise for await...of pour être consommé.", true),
      S(
        "Quelle méthode permet de signaler une erreur à l'intérieur d'un générateur depuis l'extérieur ?",
        "throw(erreur)",
        ["error(erreur)", "fail(erreur)", "reject(erreur)"]
      ),
    ]
  ),

  Quiz(
    "JS — Patterns de classes : méthodes statiques et privées",
    "Champs et méthodes statiques, privées dans les classes modernes.",
    [
      S(
        "Comment appelle-t-on une méthode statique depuis l'extérieur de la classe ?",
        "NomDeLaClasse.methode()",
        ["instance.methode()", "this.methode()", "new NomDeLaClasse().methode()"]
      ),
      TF("Un champ privé (#champ) n'est accessible que depuis l'intérieur de la classe qui le définit.", true),
      S(
        "Quelle syntaxe déclare un champ de classe privé nommé compteur ?",
        "#compteur;",
        ["private compteur;", "_compteur_;", "static #compteur uniquement"]
      ),
      M(
        "Quelles affirmations sur les champs statiques sont vraies ?",
        ["Ils sont partagés entre toutes les instances car associés à la classe elle-même", "Ils peuvent être combinés avec le préfixe # pour être privés et statiques"],
        ["Ils sont recréés pour chaque nouvelle instance", "Ils ne peuvent jamais être accédés depuis une méthode statique"]
      ),
      TF("Tenter d'accéder à un champ privé depuis l'extérieur de la classe lève une erreur de syntaxe ou d'exécution.", true),
      S(
        "Quel est l'avantage principal des champs privés par rapport à la convention historique du préfixe underscore (_champ) ?",
        "Une réelle encapsulation imposée par le moteur JavaScript, pas seulement une convention de nommage",
        ["Aucun avantage, c'est purement esthétique", "Les champs privés sont plus rapides à exécuter", "Le préfixe underscore est en fait plus sécurisé"]
      ),
    ]
  ),

  Quiz(
    "JS — Polymorphisme et redéfinition de méthodes",
    "Le polymorphisme via l'héritage de classes et la redéfinition de méthodes.",
    [
      S(
        "Qu'est-ce que le polymorphisme en programmation orientée objet ?",
        "La capacité d'objets de classes différentes à répondre différemment à un même appel de méthode",
        ["La capacité d'une classe à ne jamais être héritée", "Un synonyme strict d'encapsulation", "Une technique de compression de code"]
      ),
      TF("Une classe enfant peut redéfinir (override) une méthode héritée de sa classe parente avec sa propre implémentation.", true),
      S(
        "Comment une méthode redéfinie dans une classe enfant peut-elle quand même appeler la version du parent ?",
        "En utilisant super.nomMethode()",
        ["En utilisant parent.nomMethode()", "Ce n'est pas possible une fois redéfinie", "En utilisant this.parent.nomMethode()"]
      ),
      M(
        "Quels bénéfices apporte le polymorphisme dans une architecture orientée objet ?",
        ["Un code plus flexible face à de nouveaux types", "Une réduction des conditions explicites de type (if/else selon le type)"],
        ["Une garantie de performance supérieure dans tous les cas", "L'élimination totale du besoin de classes"]
      ),
      TF("instanceof permet de vérifier si un objet hérite, directement ou indirectement, d'une classe donnée.", true),
      S(
        "Si plusieurs classes héritent d'une même classe parente et redéfinissent une méthode commune, comment appelle-t-on ce mécanisme ?",
        "Le polymorphisme par héritage",
        ["La composition de fonctions", "Le currying", "Le hoisting de classes"]
      ),
    ]
  ),

  Quiz(
    "JS — Tableaux : Array.isArray et vérification de type",
    "Distinguer un tableau d'un objet ou d'autres structures similaires.",
    [
      S(
        "Quelle méthode fiable permet de vérifier si une valeur est un tableau ?",
        "Array.isArray(valeur)",
        ["typeof valeur === 'array'", "valeur instanceof Object uniquement", "valeur.constructor === 'array'"]
      ),
      TF("typeof appliqué à un tableau retourne 'object', pas 'array'.", true),
      S(
        "Pourquoi typeof ne suffit-il pas pour distinguer un tableau d'un objet classique ?",
        "Parce que les deux retournent 'object' avec typeof",
        ["Parce que typeof ne fonctionne pas sur les objets", "Parce que les tableaux ne sont pas des objets en JavaScript", "Parce que typeof est réservé aux primitives uniquement"]
      ),
      M(
        "Quelles méthodes permettent de vérifier des relations de type en JavaScript ?",
        ["Array.isArray()", "instanceof", "typeof"],
        ["Array.equals()"]
      ),
      TF("Un objet ressemblant à un tableau (array-like, comme arguments) n'est pas un vrai tableau et Array.isArray() retourne false pour lui.", true),
      S(
        "Que retourne Array.isArray('texte') ?",
        "false",
        ["true", "undefined", "Une erreur"]
      ),
    ]
  ),

  Quiz(
    "JS — Conditions complexes et raccourcis booléens",
    "Combiner plusieurs conditions et utiliser des raccourcis booléens dans le code.",
    [
      S(
        "Quelle expression vérifie qu'une variable utilisateur est définie ET que sa propriété actif est vraie, de façon sûre ?",
        "utilisateur?.actif === true",
        ["utilisateur.actif === true (sans protection)", "utilisateur && actif === true", "actif?.utilisateur === true"]
      ),
      TF("On utilise souvent && pour exécuter conditionnellement une instruction sans bloc if explicite : condition && faireQuelqueChose();", true),
      S(
        "Quel risque présente l'utilisation de && pour exécuter conditionnellement une fonction si la condition est un nombre potentiellement 0 ?",
        "Si la condition vaut 0 (falsy), la fonction ne sera jamais appelée même si ce n'était pas l'intention",
        ["Aucun risque, cela fonctionne toujours comme prévu", "Cela provoque systématiquement une erreur de syntaxe", "0 est toujours traité comme truthy dans ce contexte"]
      ),
      M(
        "Quelles bonnes pratiques aident à écrire des conditions complexes lisibles ?",
        ["Extraire les sous-conditions dans des variables nommées", "Utiliser des parenthèses pour clarifier la précédence des opérateurs"],
        ["Toujours imbriquer le plus de conditions possible sur une seule ligne", "Éviter complètement les opérateurs logiques"]
      ),
      TF("La précédence de && est supérieure à celle de || en JavaScript, comme en mathématiques avec * et +.", true),
      S(
        "Que retourne true || false && false ?",
        "true",
        ["false", "undefined", "Une erreur de syntaxe"]
      ),
    ]
  ),
];
