import { S, M, TF, Quiz } from "./helpers.mjs";

export const part4 = [
Quiz(
  "Threads : créer un fil d'exécution",
  "Démarrer un thread en Java via Thread et Runnable.",
  [
    S("Quelle méthode démarre réellement l'exécution d'un nouveau thread Java ?", "start()", ["run()", "execute()", "launch()"]),
    S("Que se passe-t-il si on appelle directement run() sur un objet Thread au lieu de start() ?", "Le code s'exécute dans le thread courant, sans création d'un nouveau thread", ["Un nouveau thread est créé normalement", "Une exception est levée immédiatement", "Le programme se bloque"]),
    S("Quelle interface fonctionnelle représente une tâche exécutable sans valeur de retour, utilisée avec Thread ?", "Runnable", ["Callable", "Supplier", "Future"]),
    M("Lesquelles de ces affirmations sur les threads Java sont correctes ?", ["On peut créer un thread en implémentant Runnable et en le passant à un Thread", "start() crée un nouveau thread d'exécution"], ["run() démarre toujours un nouveau thread distinct"]),
    M("Quelles façons existent de créer un thread exécutable en Java ?", ["Étendre la classe Thread et redéfinir run()", "Implémenter Runnable et le passer au constructeur de Thread"], ["Implémenter Serializable"]),
    TF("Appeler run() directement sur un objet Runnable n'exécute pas le code dans un nouveau thread.", true),
  ]
),
Quiz(
  "Synchronisation et mot-clé synchronized",
  "Comprendre comment éviter les accès concurrents incohérents avec synchronized.",
  [
    S("Quel mot-clé permet de restreindre l'accès à une méthode ou un bloc à un seul thread à la fois ?", "synchronized", ["volatile", "atomic", "locked"]),
    S("Que protège un bloc synchronized(objet) { ... } ?", "L'accès concurrent à la section critique, via le verrou associé à l'objet", ["La mémoire allouée à l'objet", "La sérialisation de l'objet", "La visibilité réseau de l'objet"]),
    S("Quel problème la synchronisation vise-t-elle principalement à éviter entre plusieurs threads partageant un état ?", "Les conditions de concurrence (race conditions) corrompant les données partagées", ["Les fuites mémoire", "Les erreurs de syntaxe", "Les erreurs de compilation"]),
    M("Lesquelles de ces affirmations sur synchronized sont correctes ?", ["Une méthode synchronized ne peut être exécutée que par un seul thread à la fois pour un même objet verrou", "synchronized peut s'appliquer à une méthode entière ou à un bloc spécifique"], ["synchronized empêche toute exception dans le bloc concerné"]),
    M("Quels problèmes de concurrence la synchronisation correcte permet-elle de limiter ?", ["Les conditions de concurrence (race conditions)", "Les incohérences de visibilité mémoire entre threads"], ["Les erreurs de syntaxe du compilateur"]),
    TF("Le mot-clé synchronized peut être appliqué à une méthode entière pour la rendre thread-safe au niveau de l'instance.", true),
  ]
),
Quiz(
  "Cycle de vie d'un thread",
  "Identifier les états successifs d'un thread Java.",
  [
    S("Dans quel état se trouve un thread juste après l'appel à start(), avant d'obtenir réellement le processeur ?", "RUNNABLE", ["NEW", "TERMINATED", "BLOCKED"]),
    S("Dans quel état se trouve un thread qui attend qu'un verrou soit libéré par un autre thread ?", "BLOCKED", ["RUNNABLE", "NEW", "TERMINATED"]),
    S("Quelle méthode permet à un thread d'attendre la fin de l'exécution d'un autre thread ?", "join()", ["wait()", "sleep()", "stop()"]),
    M("Lesquels de ces états font partie du cycle de vie d'un thread Java (énumération Thread.State) ?", ["NEW", "RUNNABLE", "TERMINATED"], ["PAUSED"]),
    M("Quelles méthodes permettent d'influencer ou d'observer le déroulement d'un thread ?", ["sleep(long)", "join()", "isAlive()"], ["compile()"]),
    TF("Une fois dans l'état TERMINATED, un thread ne peut pas être redémarré avec start().", true),
  ]
),
Quiz(
  "Expressions lambda (Java 8+)",
  "Comprendre la syntaxe et l'usage des expressions lambda.",
  [
    S("Quelle syntaxe représente une expression lambda Java prenant un paramètre x et retournant x * 2 ?", "x -> x * 2", ["function(x) { return x * 2; }", "lambda x: x * 2", "x => { x * 2 }"]),
    S("Une expression lambda en Java permet d'implémenter de manière concise :", "Une interface fonctionnelle (avec une seule méthode abstraite)", ["N'importe quelle classe abstraite", "Une interface avec plusieurs méthodes abstraites", "Une classe finale"]),
    S("Quelle annotation marque une interface comme interface fonctionnelle, utilisable avec une lambda ?", "@FunctionalInterface", ["@Lambda", "@Functional", "@SingleMethod"]),
    M("Lesquelles de ces affirmations sur les expressions lambda sont correctes ?", ["Elles permettent d'écrire du code plus concis qu'une classe anonyme", "Elles peuvent capturer des variables locales effectivement finales"], ["Elles peuvent implémenter une interface avec plusieurs méthodes abstraites"]),
    M("Quelles interfaces fonctionnelles standard de java.util.function existent en Java ?", ["Function<T, R>", "Predicate<T>", "Supplier<T>"], ["Iterator<T>"]),
    TF("Une expression lambda en Java ne peut implémenter qu'une interface possédant exactement une seule méthode abstraite.", true),
  ]
),
Quiz(
  "Stream API : opérations de base",
  "Manipuler des collections de manière déclarative avec l'API Stream.",
  [
    S("Quelle méthode permet d'obtenir un Stream à partir d'une collection comme une List ?", "stream()", ["toStream()", "asStream()", "getStream()"]),
    S("Quelle opération de Stream permet de transformer chaque élément selon une fonction donnée ?", "map(Function)", ["filter(Predicate)", "reduce(BinaryOperator)", "sorted()"]),
    S("Quelle opération de Stream permet de ne conserver que les éléments respectant une condition ?", "filter(Predicate)", ["map(Function)", "collect(Collector)", "peek(Consumer)"]),
    M("Lesquelles de ces affirmations sur les Stream Java sont correctes ?", ["Un Stream ne modifie pas la collection source", "Les opérations comme map et filter sont des opérations intermédiaires (lazy)"], ["Un Stream peut être réutilisé plusieurs fois après une opération terminale"]),
    M("Quelles méthodes sont des opérations terminales sur un Stream (déclenchant réellement le calcul) ?", ["collect(Collector)", "forEach(Consumer)", "count()"], ["map(Function)"]),
    TF("Un Stream Java ne peut être consommé qu'une seule fois ; il faut en recréer un nouveau pour relancer un traitement.", true),
  ]
),
Quiz(
  "Stream API : collect et Collectors",
  "Convertir un Stream en collection ou en valeur agrégée avec Collectors.",
  [
    S("Quelle méthode statique de Collectors permet de regrouper les éléments d'un Stream dans une List ?", "Collectors.toList()", ["Collectors.toArray()", "Collectors.toSet()", "Collectors.group()"]),
    S("Quelle méthode de Collectors permet de regrouper des éléments selon une clé, produisant une Map<clé, List<élément>> ?", "Collectors.groupingBy(Function)", ["Collectors.partitioningBy(Predicate)", "Collectors.toMap(Function, Function)", "Collectors.joining()"]),
    S("Quelle méthode de Collectors permet de concaténer des chaînes issues d'un Stream<String> avec un séparateur ?", "Collectors.joining(String)", ["Collectors.toList()", "Collectors.merge()", "Collectors.concat()"]),
    M("Lesquelles de ces affirmations sur collect() et Collectors sont correctes ?", ["collect() est une opération terminale d'un Stream", "Collectors.groupingBy() permet de produire une Map regroupant les éléments"], ["collect() est une opération intermédiaire paresseuse"]),
    M("Quelles collections un Stream peut-il produire via collect() avec les bons Collectors ?", ["Une List", "Un Set", "Une Map"], ["Un tableau primitif sans passer par toArray()"]),
    TF("Collectors.groupingBy() permet de regrouper les éléments d'un Stream en fonction d'une clé calculée.", true),
  ]
),
Quiz(
  "Stream API : réduction et agrégation",
  "Utiliser reduce(), count(), min/max et les Stream numériques.",
  [
    S("Quelle méthode de Stream permet de combiner tous les éléments en une seule valeur via un opérateur binaire ?", "reduce(BinaryOperator)", ["map(Function)", "filter(Predicate)", "sorted()"]),
    S("Quelle méthode de Stream retourne le nombre d'éléments qu'il contient ?", "count()", ["size()", "length()", "total()"]),
    S("Quel type de Stream spécialisé est utilisé pour additionner efficacement des entiers sans autoboxing ?", "IntStream", ["Stream<Integer>", "NumberStream", "LongStream uniquement"]),
    M("Lesquelles de ces affirmations sur reduce() sont correctes ?", ["reduce() peut accepter une valeur initiale (identité)", "reduce() retourne un Optional si aucune valeur initiale n'est fournie et que le Stream est vide"], ["reduce() modifie la collection source en place"]),
    M("Quelles méthodes terminales permettent d'obtenir une valeur agrégée à partir d'un Stream ?", ["count()", "reduce(BinaryOperator)", "max(Comparator)"], ["map(Function)"]),
    TF("La méthode IntStream.range(0, 5) génère les entiers de 0 à 4 inclus.", true),
  ]
),
Quiz(
  "Interfaces fonctionnelles courantes (Function, Predicate, Consumer, Supplier)",
  "Reconnaître les interfaces fonctionnelles standard de java.util.function.",
  [
    S("Quelle interface fonctionnelle représente une fonction prenant un argument de type T et retournant un résultat de type R ?", "Function<T, R>", ["Predicate<T>", "Consumer<T>", "Supplier<T>"]),
    S("Quelle interface fonctionnelle représente un test booléen sur un argument de type T ?", "Predicate<T>", ["Function<T, R>", "Consumer<T>", "Supplier<T>"]),
    S("Quelle interface fonctionnelle représente une opération consommant un argument sans retourner de valeur ?", "Consumer<T>", ["Function<T, R>", "Predicate<T>", "Supplier<T>"]),
    M("Lesquelles de ces interfaces font partie du package java.util.function ?", ["Function<T, R>", "Predicate<T>", "Supplier<T>"], ["Comparable<T>"]),
    M("Quelles méthodes abstraites sont associées à ces interfaces fonctionnelles ?", ["apply(T) pour Function", "test(T) pour Predicate"], ["compareTo(T) pour Supplier"]),
    TF("Supplier<T> représente une interface fonctionnelle qui ne prend aucun argument et retourne une valeur de type T.", true),
  ]
),
Quiz(
  "Entrées/sorties de base : Scanner",
  "Lire les entrées utilisateur depuis la console avec la classe Scanner.",
  [
    S("Quelle classe permet de lire facilement les entrées clavier depuis la console en Java ?", "Scanner", ["Reader", "InputStream", "BufferedWriter"]),
    S("Quelle méthode de Scanner lit une ligne entière saisie par l'utilisateur ?", "nextLine()", ["readLine()", "getLine()", "scanLine()"]),
    S("Quelle méthode de Scanner permet de lire un entier saisi au clavier ?", "nextInt()", ["readInt()", "getInt()", "parseInt()"]),
    M("Lesquelles de ces affirmations sur Scanner sont correctes ?", ["Scanner peut lire depuis System.in", "Scanner propose des méthodes typées comme nextInt() et nextDouble()"], ["Scanner ne peut lire que des chaînes de caractères"]),
    M("Quelles méthodes existent sur la classe Scanner pour lire différents types de données ?", ["nextInt()", "nextDouble()", "nextBoolean()"], ["nextArray()"]),
    TF("Mélanger nextInt() et nextLine() sur un même Scanner peut provoquer des comportements inattendus à cause du saut de ligne restant dans le buffer.", true),
  ]
),
Quiz(
  "Entrées/sorties de base : lecture et écriture de fichiers",
  "Manipuler des fichiers texte avec les classes standard de java.io et java.nio.",
  [
    S("Quelle classe de java.io permet de lire un fichier texte ligne par ligne de façon efficace ?", "BufferedReader", ["Scanner uniquement", "PrintWriter", "FileOutputStream"]),
    S("Quelle classe permet d'écrire facilement du texte formaté dans un fichier ?", "PrintWriter", ["FileInputStream", "BufferedReader", "ObjectInputStream"]),
    S("Quelle méthode de la classe Files (java.nio.file) permet de lire toutes les lignes d'un fichier en une seule fois ?", "Files.readAllLines(Path)", ["Files.read(Path)", "Files.open(Path)", "Files.scan(Path)"]),
    M("Lesquelles de ces affirmations sur les flux d'entrée/sortie en Java sont correctes ?", ["Il est recommandé de fermer les flux après usage, notamment via try-with-resources", "BufferedReader peut envelopper un FileReader pour améliorer la performance de lecture"], ["FileInputStream lit directement des caractères Unicode sans encodage"]),
    M("Quelles classes permettent de manipuler des fichiers en Java ?", ["File", "Path", "Files"], ["Scanner uniquement"]),
    TF("Utiliser try-with-resources pour ouvrir un fichier garantit sa fermeture automatique même en cas d'exception.", true),
  ]
),
Quiz(
  "JVM, JRE et JDK : les fondations de l'écosystème Java",
  "Distinguer les trois sigles essentiels de l'écosystème Java.",
  [
    S("Que signifie l'acronyme JVM ?", "Java Virtual Machine", ["Java Runtime Machine", "Java Verified Module", "Java Virtual Memory"]),
    S("Quel composant est responsable de l'exécution du bytecode Java, indépendamment du système d'exploitation ?", "La JVM", ["Le JDK", "Le compilateur javac uniquement", "L'IDE"]),
    S("Quelle relation décrit le mieux JDK, JRE et JVM ?", "Le JDK contient le JRE, qui contient la JVM", ["La JVM contient le JRE, qui contient le JDK", "Les trois sont totalement indépendants", "Le JRE contient le JDK"]),
    M("Lesquelles de ces affirmations sur la JVM sont correctes ?", ["Elle exécute le bytecode produit par le compilateur javac", "Elle permet la portabilité du code Java entre systèmes d'exploitation"], ["Elle compile directement le code source .java en exécutable natif sans bytecode"]),
    M("Quels éléments sont typiquement inclus dans un JDK (Java Development Kit) ?", ["Le compilateur javac", "Le JRE (incluant la JVM)"], ["Un éditeur de texte obligatoire"]),
    TF("Le JRE (Java Runtime Environment) permet d'exécuter des applications Java mais ne fournit pas les outils de développement comme javac.", true),
  ]
),
Quiz(
  "Compilation et exécution d'un programme Java",
  "Comprendre les étapes de transformation du code source en programme exécutable.",
  [
    S("Quelle commande permet de compiler un fichier source Monoprogramme.java ?", "javac Monoprogramme.java", ["java Monoprogramme.java", "compile Monoprogramme.java", "run Monoprogramme.java"]),
    S("Quelle extension de fichier porte le bytecode généré par le compilateur Java ?", ".class", [".java", ".jar", ".exe"]),
    S("Quelle commande permet de lancer l'exécution d'une classe Java compilée nommée Main ?", "java Main", ["javac Main", "run Main", "exec Main"]),
    M("Lesquelles de ces étapes font partie du cycle de vie d'un programme Java typique ?", ["Compilation en bytecode .class par javac", "Exécution du bytecode par la JVM via java"], ["Transpilation automatique vers un autre langage"]),
    M("Quelles affirmations sur le bytecode Java sont correctes ?", ["Il est indépendant de la plateforme d'exécution", "Il est interprété ou compilé à la volée (JIT) par la JVM"], ["Il s'agit de code source lisible directement comme du Java"]),
    TF("Le bytecode Java (.class) peut s'exécuter sur n'importe quelle plateforme disposant d'une JVM compatible, sans recompilation.", true),
  ]
),
Quiz(
  "Garbage collector : notions de base",
  "Comprendre le rôle du ramasse-miettes dans la gestion automatique de la mémoire.",
  [
    S("Quel est le rôle principal du garbage collector (GC) en Java ?", "Libérer automatiquement la mémoire des objets qui ne sont plus référencés", ["Compiler le code source en bytecode", "Optimiser la vitesse du CPU", "Gérer les threads concurrents"]),
    S("Un objet devient éligible au garbage collector lorsque :", "Il n'est plus accessible depuis aucune référence active du programme", ["Il a été créé il y a plus d'une seconde", "Sa méthode toString() a été appelée", "Il est déclaré final"]),
    S("Quelle méthode peut suggérer (sans garantir) au GC de s'exécuter, mais dont l'usage est généralement déconseillé ?", "System.gc()", ["System.clean()", "Runtime.free()", "Object.collect()"]),
    M("Lesquelles de ces affirmations sur le garbage collector sont correctes ?", ["Il s'exécute automatiquement sans intervention explicite du développeur", "Il évite au développeur de libérer manuellement la mémoire comme en C"], ["Il garantit la libération immédiate de la mémoire dès qu'un objet devient inaccessible"]),
    M("Lesquelles de ces affirmations sur la zone mémoire gérée par le garbage collector sont correctes ?", ["Le tas (heap) contient les objets créés avec new", "Les objets devenus inaccessibles y sont automatiquement libérés"], ["La pile d'appels (call stack) est gérée par le garbage collector"]),
    TF("En Java, le développeur n'a pas besoin d'appeler explicitement une fonction pour libérer la mémoire d'un objet inutilisé.", true),
  ]
),
Quiz(
  "Pile (stack) et tas (heap) en mémoire",
  "Distinguer les deux zones mémoire principales utilisées par une application Java.",
  [
    S("Où sont typiquement stockées les variables locales de type primitif lors de l'exécution d'une méthode ?", "Sur la pile (stack)", ["Sur le tas (heap)", "Dans le registre du processeur uniquement", "Sur le disque dur"]),
    S("Où sont stockés les objets créés avec new en Java ?", "Sur le tas (heap)", ["Sur la pile (stack)", "Dans le bytecode", "Dans le cache du compilateur"]),
    S("Que se passe-t-il si la pile d'appels dépasse sa capacité, par exemple via une récursion infinie ?", "Une StackOverflowError est levée", ["Une OutOfMemoryError du tas est levée", "Le programme continue normalement", "Le garbage collector libère automatiquement de l'espace"]),
    M("Lesquelles de ces affirmations sur la pile et le tas sont correctes ?", ["Chaque thread possède sa propre pile d'appels", "Le tas est une zone mémoire partagée entre tous les threads"], ["La pile contient tous les objets créés par le programme"]),
    M("Quelles informations trouve-t-on typiquement sur la pile d'appels en Java ?", ["Les variables locales primitives", "Les références vers des objets sur le tas"], ["Le contenu complet des objets eux-mêmes"]),
    TF("Une récursion infinie ou trop profonde peut provoquer une StackOverflowError en Java.", true),
  ]
),
Quiz(
  "Méthode main et arguments de ligne de commande",
  "Comprendre la signature exacte de la méthode main, point d'entrée d'un programme Java.",
  [
    S("Quelle est la signature standard de la méthode main, point d'entrée d'un programme Java ?", "public static void main(String[] args)", ["public void main(String[] args)", "static int main(String[] args)", "public static main(String[] args)"]),
    S("Pourquoi la méthode main doit-elle être déclarée static ?", "Pour pouvoir être appelée par la JVM sans créer d'instance de la classe au préalable", ["Pour pouvoir être redéfinie dans une sous-classe", "Pour la rendre accessible uniquement depuis le même package", "Pour permettre le polymorphisme"]),
    S("Que représente le paramètre args de la méthode main ?", "Les arguments passés en ligne de commande lors du lancement du programme", ["La liste des classes du projet", "Le chemin du fichier source", "Les variables d'environnement système"]),
    M("Lesquelles de ces affirmations sur la méthode main sont correctes ?", ["Elle doit être public pour être accessible par la JVM", "Son type de retour est void"], ["Elle peut avoir n'importe quel nom à la place de main"]),
    M("Quelles variations de la déclaration des arguments de main sont valides en Java ?", ["String[] args", "String... args"], ["String args[5]"]),
    TF("Si aucun argument n'est passé en ligne de commande, le tableau args de main a une longueur de 0 (et n'est pas null).", true),
  ]
),
Quiz(
  "Surcharge de méthodes et résolution de signature",
  "Approfondir les règles de résolution des méthodes surchargées par le compilateur.",
  [
    S("Qu'est-ce qui distingue deux méthodes surchargées portant le même nom dans une classe ?", "Le nombre ou le type de leurs paramètres", ["Leur type de retour uniquement", "Leur modificateur d'accès uniquement", "Leur ordre de déclaration dans le fichier"]),
    S("Si une classe définit additionner(int, int) et additionner(double, double), quelle méthode est appelée pour additionner(3, 4) ?", "additionner(int, int)", ["additionner(double, double)", "Une erreur de compilation se produit", "Les deux méthodes sont appelées"]),
    S("Le compilateur Java détermine quelle méthode surchargée appeler à quel moment ?", "À la compilation, selon les types des arguments fournis", ["À l'exécution, selon le type réel de l'objet", "Aléatoirement à chaque appel", "Jamais, cela provoque toujours une ambiguïté"]),
    M("Lesquelles de ces signatures constituent une surcharge valide de méthode afficher(String s) dans la même classe ?", ["afficher(int n)", "afficher(String s, int n)"], ["afficher(String texte) avec un type de retour différent uniquement"]),
    M("Quelles règles s'appliquent à la résolution de la surcharge de méthodes en Java ?", ["Elle est résolue à la compilation (liaison statique)", "Le type de retour seul ne permet pas de différencier deux signatures"], ["Elle dépend du type réel de l'objet à l'exécution comme l'overriding"]),
    TF("Deux méthodes ne différant que par leur type de retour, avec les mêmes noms et paramètres, ne constituent pas une surcharge valide en Java.", true),
  ]
),
Quiz(
  "Visibilité et héritage : protected en pratique",
  "Approfondir les subtilités du modificateur protected lors de l'héritage entre packages.",
  [
    S("Un membre protected d'une classe est accessible depuis :", "Le même package, ainsi que les sous-classes même dans un autre package", ["Uniquement la classe elle-même", "N'importe quelle classe de l'application", "Uniquement les sous-classes du même package"]),
    S("Une sous-classe dans un package différent peut-elle accéder à un champ protected de sa super-classe via une référence à un objet de cette super-classe (et non d'elle-même) ?", "Non, l'accès protected inter-package est restreint à l'instance de la sous-classe elle-même", ["Oui, sans restriction", "Cela dépend du type du champ", "Oui, uniquement si le champ est aussi static"]),
    S("Pourquoi choisit-on protected plutôt que private pour un champ destiné à être réutilisé par des sous-classes ?", "Pour permettre aux sous-classes d'y accéder directement tout en le masquant du reste de l'application", ["Pour le rendre accessible à toute l'application", "Pour empêcher complètement l'héritage", "Pour le rendre statique automatiquement"]),
    M("Lesquelles de ces affirmations sur protected sont correctes ?", ["protected est plus permissif que private", "protected est moins permissif que public"], ["protected équivaut exactement à private en termes d'accès"]),
    M("Quels contextes peuvent accéder à un membre protected d'une classe ?", ["Les classes du même package", "Les sous-classes, même dans un autre package"], ["Strictement aucune classe externe"]),
    TF("Le modificateur protected offre un accès plus large que le modificateur par défaut (package-private) car il inclut aussi les sous-classes externes au package.", true),
  ]
),
Quiz(
  "Méthodes par défaut et statiques dans les interfaces (Java 8+)",
  "Comprendre l'évolution des interfaces avec les méthodes default et static.",
  [
    S("Quel mot-clé permet de fournir une implémentation par défaut d'une méthode dans une interface depuis Java 8 ?", "default", ["abstract", "final", "virtual"]),
    S("Une classe qui implémente une interface avec une méthode default doit-elle obligatoirement la redéfinir ?", "Non, elle peut utiliser l'implémentation par défaut telle quelle", ["Oui, c'est toujours obligatoire", "Seulement si la classe est abstraite", "Seulement si la méthode est aussi static"]),
    S("Une méthode static définie dans une interface peut-elle être appelée par une instance qui l'implémente, via cette instance ?", "Non, elle doit être appelée via le nom de l'interface", ["Oui, normalement comme une méthode d'instance", "Oui, mais seulement si elle est aussi default", "Cela dépend de la JVM utilisée"]),
    M("Lesquelles de ces affirmations sur les méthodes default des interfaces sont correctes ?", ["Elles permettent d'ajouter des comportements à une interface sans casser les implémentations existantes", "Une classe implémentant l'interface peut redéfinir la méthode default si besoin"], ["Elles rendent obligatoire l'implémentation par toutes les classes"]),
    M("Quelles évolutions des interfaces ont été introduites par Java 8 ?", ["Les méthodes default avec corps", "Les méthodes static"], ["Les constructeurs d'interface"]),
    TF("Les méthodes default d'une interface permettent d'ajouter une nouvelle fonctionnalité sans casser la compatibilité des classes qui l'implémentaient déjà.", true),
  ]
),
Quiz(
  "Optional : éviter les NullPointerException",
  "Utiliser la classe Optional introduite en Java 8 pour représenter une valeur potentiellement absente.",
  [
    S("Quel est l'objectif principal de la classe Optional<T> introduite en Java 8 ?", "Représenter explicitement l'absence possible d'une valeur, pour limiter les NullPointerException", ["Remplacer totalement les exceptions en Java", "Accélérer les calculs numériques", "Remplacer les tableaux"]),
    S("Quelle méthode statique permet de créer un Optional ne contenant aucune valeur ?", "Optional.empty()", ["Optional.null()", "Optional.none()", "new Optional()"]),
    S("Quelle méthode d'Optional permet de récupérer la valeur si présente, ou une valeur de remplacement sinon ?", "orElse(valeurParDefaut)", ["get()", "getOrNull()", "fallback()"]),
    M("Lesquelles de ces affirmations sur Optional sont correctes ?", ["isPresent() indique si une valeur est contenue dans l'Optional", "Optional.of(valeur) lève une exception si la valeur passée est null"], ["Optional remplace obligatoirement tous les usages de null en Java"]),
    M("Quelles méthodes utiles sont disponibles sur Optional<T> ?", ["map(Function)", "ifPresent(Consumer)", "orElseThrow()"], ["push(T)"]),
    TF("Appeler get() sur un Optional vide lève une exception (NoSuchElementException).", true),
  ]
),
];
