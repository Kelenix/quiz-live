import { S, M, TF, Quiz } from "./helpers.mjs";

export const part6 = [
Quiz(
  "API Date et Heure : LocalDate et LocalDateTime",
  "Manipuler les dates et heures modernes avec java.time (Java 8+).",
  [
    S("Quelle classe de java.time représente une date sans heure (jour, mois, année) ?", "LocalDate", ["Date", "Calendar", "LocalTime"]),
    S("Quelle méthode statique permet d'obtenir la date du jour avec LocalDate ?", "LocalDate.now()", ["LocalDate.today()", "new LocalDate()", "LocalDate.current()"]),
    S("Quelle classe représente à la fois une date et une heure, sans fuseau horaire ?", "LocalDateTime", ["LocalDate", "LocalTime", "Instant"]),
    M("Lesquelles de ces affirmations sur l'API java.time sont correctes ?", ["Les objets LocalDate sont immuables", "plusDays(n) retourne une nouvelle instance sans modifier l'originale"], ["LocalDate permet de stocker une heure précise avec fuseau"]),
    M("Quelles classes font partie de l'API java.time moderne introduite en Java 8 ?", ["LocalDate", "LocalDateTime", "Duration"], ["java.util.Date comme remplacement recommandé"]),
    TF("Les classes de l'API java.time comme LocalDate sont immuables : chaque modification retourne une nouvelle instance.", true),
  ]
),
Quiz(
  "Références de méthodes (method references)",
  "Utiliser la syntaxe :: pour référencer des méthodes existantes comme lambdas.",
  [
    S("Quel opérateur permet d'écrire une référence de méthode en Java, par exemple System.out::println ?", "::", ["->", "::=", "=>"]),
    S("Quelle référence de méthode équivaut à la lambda (s) -> s.length() ?", "String::length", ["String::new", "this::length", "length::String"]),
    S("Que représente la référence de méthode MaClasse::new ?", "Une référence vers un constructeur de MaClasse", ["Un appel direct à une méthode statique new", "Une erreur de compilation systématique", "Une référence vers une méthode d'instance nommée new"]),
    M("Lesquelles de ces formes de références de méthodes existent en Java ?", ["Référence à une méthode statique (Classe::methodeStatique)", "Référence à un constructeur (Classe::new)"], ["Référence directe à une variable locale (variable::valeur)"]),
    M("Quelles affirmations sur les références de méthodes sont correctes ?", ["Elles peuvent remplacer une lambda qui se contente d'appeler une méthode existante", "Elles sont compatibles avec les interfaces fonctionnelles comme Function ou Consumer"], ["Elles nécessitent toujours une lambda explicite en complément"]),
    TF("Une référence de méthode comme Integer::parseInt peut être utilisée partout où une Function<String, Integer> est attendue.", true),
  ]
),
Quiz(
  "Texte formaté : String.format() et printf",
  "Construire des chaînes formatées avec des spécificateurs de conversion.",
  [
    S("Quel spécificateur de format affiche un entier décimal avec String.format() ?", "%d", ["%s", "%f", "%c"]),
    S("Quel spécificateur de format affiche un nombre à virgule flottante avec String.format() ?", "%f", ["%d", "%s", "%b"]),
    S("Quelle méthode de PrintStream (comme System.out) permet d'afficher directement une chaîne formatée sans la stocker ?", "printf(String, Object...)", ["format(String, Object...) uniquement sur String", "print(String, Object...)", "write(String, Object...)"]),
    M("Lesquelles de ces affirmations sur String.format() sont correctes ?", ["Elle retourne une nouvelle chaîne sans l'afficher", "Elle accepte un nombre variable d'arguments à substituer"], ["Elle modifie directement la chaîne de format passée en argument"]),
    M("Quels spécificateurs de conversion sont valides avec String.format() ?", ["%d pour un entier", "%s pour une chaîne", "%.2f pour un flottant avec 2 décimales"], ["%j sans signification définie"]),
    TF("String.format(\"%05d\", 42) produit la chaîne \"00042\" en complétant avec des zéros.", true),
  ]
),
Quiz(
  "BigDecimal et précision numérique",
  "Comprendre pourquoi et comment utiliser BigDecimal pour des calculs précis.",
  [
    S("Pourquoi privilégier BigDecimal plutôt que double pour des calculs monétaires précis ?", "Parce que double souffre d'imprécisions liées à la représentation binaire des flottants", ["Parce que double est plus lent que BigDecimal", "Parce que double ne peut pas stocker de grands nombres", "Parce que BigDecimal est un type primitif optimisé"]),
    S("Quelle méthode de BigDecimal permet d'additionner deux valeurs sans modifier les objets d'origine ?", "add(BigDecimal)", ["plus(BigDecimal)", "sum(BigDecimal)", "increment(BigDecimal)"]),
    S("Pourquoi est-il déconseillé de construire un BigDecimal directement à partir d'un double littéral comme new BigDecimal(0.1) ?", "Parce que cela peut reproduire l'imprécision binaire du double sous-jacent", ["Parce que cela lève toujours une exception", "Parce que BigDecimal ne supporte pas les doubles", "Parce que cela arrondit automatiquement à l'entier"]),
    M("Lesquelles de ces affirmations sur BigDecimal sont correctes ?", ["BigDecimal est immuable : chaque opération retourne une nouvelle instance", "Construire un BigDecimal à partir d'une chaîne comme \"0.1\" est plus sûr qu'à partir d'un double"], ["BigDecimal effectue toujours ses calculs plus rapidement que double"]),
    M("Dans quels contextes BigDecimal est-il particulièrement recommandé ?", ["Calculs monétaires nécessitant une précision exacte", "Arrondis contrôlés avec un mode d'arrondi explicite"], ["Calculs intensifs nécessitant la performance maximale du CPU"]),
    TF("BigDecimal est un type immuable : les méthodes comme add() retournent un nouvel objet plutôt que de modifier l'instance existante.", true),
  ]
),
Quiz(
  "Modules Java (notions, Java 9+)",
  "Comprendre l'objectif du système de modules introduit avec Java 9 (Jigsaw).",
  [
    S("Quel fichier déclare les dépendances et exports d'un module Java (depuis Java 9) ?", "module-info.java", ["module.xml", "package-info.java", "manifest.mf"]),
    S("Quel mot-clé, dans module-info.java, permet de rendre un package accessible aux autres modules ?", "exports", ["imports", "public", "uses"]),
    S("Quel est l'un des objectifs principaux du système de modules introduit par Java 9 ?", "Renforcer l'encapsulation au niveau du module et clarifier les dépendances entre composants", ["Remplacer entièrement les classes par des modules", "Supprimer le besoin de compiler le code", "Accélérer uniquement le ramasse-miettes"]),
    M("Lesquelles de ces affirmations sur les modules Java (JPMS) sont correctes ?", ["Un module peut explicitement déclarer les packages qu'il exporte", "Le fichier module-info.java se trouve à la racine du module"], ["Tous les packages d'un module sont automatiquement accessibles depuis l'extérieur"]),
    M("Quels mots-clés peuvent apparaître dans un fichier module-info.java ?", ["requires", "exports"], ["extends"]),
    TF("Le système de modules (JPMS) introduit en Java 9 permet de déclarer explicitement quels packages d'un module sont exposés aux autres modules.", true),
  ]
),
];
