import { S, M, TF, Quiz } from "./helpers.mjs";

export const part5 = [
Quiz(
  "Méthode toString() et représentation textuelle",
  "Redéfinir toString() pour afficher une représentation lisible d'un objet.",
  [
    S("Quelle méthode héritée de Object est implicitement appelée lors d'un System.out.println(objet) ?", "toString()", ["equals()", "hashCode()", "getClass()"]),
    S("Que retourne par défaut toString() si elle n'est pas redéfinie dans une classe ?", "Le nom de la classe suivi d'un identifiant de hachage (ex: Personne@1a2b3c)", ["Une chaîne vide", "null", "Une exception est levée"]),
    S("Pourquoi redéfinit-on souvent toString() dans une classe métier ?", "Pour obtenir un affichage lisible et utile pour le débogage", ["Pour rendre la classe sérialisable", "Pour permettre l'héritage multiple", "Pour activer l'autoboxing"]),
    M("Lesquelles de ces affirmations sur toString() sont correctes ?", ["Elle est héritée de la classe Object par toute classe Java", "Elle peut être redéfinie pour personnaliser l'affichage d'un objet"], ["Elle doit obligatoirement retourner un nombre entier"]),
    M("Dans quels contextes Java appelle-t-il implicitement toString() sur un objet ?", ["Lors d'une concaténation avec l'opérateur +", "Lors d'un System.out.println(objet)"], ["Lors d'une comparaison avec =="]),
    TF("La méthode toString() est héritée de la classe Object par défaut dans toutes les classes Java.", true),
  ]
),
Quiz(
  "Classe Object : méthodes héritées universelles",
  "Connaître les méthodes fondamentales héritées par toute classe Java.",
  [
    S("Quelle méthode de la classe Object permet d'obtenir la classe réelle (Class<?>) d'un objet à l'exécution ?", "getClass()", ["toString()", "hashCode()", "clone()"]),
    S("Quelle classe est l'ancêtre commun de toutes les classes Java, implicitement ou explicitement ?", "Object", ["Class", "Root", "Base"]),
    S("Quelle méthode de Object permet de créer une copie superficielle d'un objet, sous certaines conditions ?", "clone()", ["copy()", "duplicate()", "fork()"]),
    M("Lesquelles de ces méthodes sont héritées de la classe Object par toute classe Java ?", ["toString()", "equals(Object)", "hashCode()"], ["compareTo(Object)"]),
    M("Quelles affirmations sur la classe Object sont correctes ?", ["Toute classe Java hérite implicitement de Object si elle n'étend rien explicitement", "Object fournit une implémentation par défaut de equals() basée sur la référence"], ["Object est une interface, pas une classe"]),
    TF("En Java, toute classe hérite directement ou indirectement de la classe Object.", true),
  ]
),
Quiz(
  "Enums avancés : champs, constructeurs et méthodes",
  "Concevoir des enums riches avec état et comportement associés à chaque constante.",
  [
    S("Peut-on définir un constructeur dans un type enum en Java ?", "Oui, mais il est implicitement privé", ["Non, jamais", "Oui, et il peut être public", "Seulement si l'enum n'a qu'une seule constante"]),
    S("Comment associe-t-on une donnée (comme un prix) à chaque constante d'un enum Forfait ?", "En déclarant un champ et en l'initialisant via le constructeur de l'enum pour chaque constante", ["En créant une sous-classe pour chaque constante uniquement", "Ce n'est pas possible en Java", "En utilisant une HashMap statique externe obligatoirement"]),
    S("Un enum Java peut-il implémenter une interface ?", "Oui, un enum peut implémenter une ou plusieurs interfaces", ["Non, jamais", "Oui, mais une seule interface maximum", "Seulement les interfaces marquées @FunctionalInterface"]),
    M("Lesquelles de ces affirmations sur les enums avancés sont correctes ?", ["Chaque constante d'un enum peut avoir un corps spécifique redéfinissant une méthode abstraite", "Un enum peut avoir des champs d'instance comme une classe normale"], ["Un enum peut être étendu (extends) par une autre classe"]),
    M("Quelles capacités similaires aux classes normales possèdent les enums Java ?", ["Définir des méthodes", "Implémenter des interfaces", "Avoir des champs privés"], ["Être instanciés avec new depuis l'extérieur"]),
    TF("Un enum Java ne peut pas étendre une autre classe car il hérite déjà implicitement de java.lang.Enum.", true),
  ]
),
Quiz(
  "Varargs : nombre variable d'arguments",
  "Utiliser la syntaxe des arguments variables (varargs) dans une méthode.",
  [
    S("Quelle syntaxe permet de déclarer une méthode acceptant un nombre variable d'arguments entiers ?", "void somme(int... nombres)", ["void somme(int[] nombres)", "void somme(int *nombres)", "void somme(int nombres...)"]),
    S("Combien de paramètres varargs au maximum une méthode Java peut-elle déclarer ?", "Un seul, et il doit être le dernier paramètre", ["Aucune limite, à n'importe quelle position", "Deux maximum", "Cela dépend du type"]),
    S("À l'intérieur du corps de la méthode, comment se comporte un paramètre varargs comme int... nombres ?", "Comme un tableau classique int[]", ["Comme une ArrayList", "Comme une chaîne de caractères", "Comme un objet Iterator"]),
    M("Lesquelles de ces affirmations sur les varargs sont correctes ?", ["Un paramètre varargs doit être le dernier de la liste des paramètres", "On peut appeler une méthode varargs sans lui passer aucun argument pour ce paramètre"], ["Une méthode peut avoir plusieurs paramètres varargs différents"]),
    M("Quelles méthodes de l'API standard Java utilisent des varargs ?", ["String.format(String, Object...)", "List.of(E...)"], ["String.length()"]),
    TF("Un paramètre varargs comme String... mots est traité comme un tableau String[] à l'intérieur de la méthode.", true),
  ]
),
Quiz(
  "Opérateurs bit à bit",
  "Manipuler des entiers au niveau binaire avec les opérateurs bit à bit Java.",
  [
    S("Quel opérateur effectue un ET au niveau du bit entre deux entiers en Java ?", "&", ["&&", "|", "^"]),
    S("Quel opérateur effectue un OU exclusif (XOR) au niveau du bit en Java ?", "^", ["|", "&", "~"]),
    S("Que fait l'opérateur de décalage à gauche << appliqué à un entier ?", "Il décale les bits vers la gauche, ce qui multiplie généralement par une puissance de 2", ["Il inverse tous les bits", "Il effectue une division", "Il convertit l'entier en chaîne binaire"]),
    M("Lesquels de ces opérateurs sont des opérateurs bit à bit en Java ?", ["&", "|", "^", "~"], ["&&"]),
    M("Quelles affirmations sur les opérateurs de décalage en Java sont correctes ?", ["<< décale les bits vers la gauche", ">> est un décalage arithmétique à droite qui préserve le signe"], [">>> n'existe pas en Java"]),
    TF("L'opérateur >>> effectue un décalage à droite non signé, en remplissant de zéros par la gauche.", true),
  ]
),
Quiz(
  "Méthodes statiques d'utilitaires : Math et Objects",
  "Utiliser les classes utilitaires standard Math et Objects.",
  [
    S("Quelle méthode statique de la classe Math retourne la valeur absolue d'un nombre ?", "Math.abs(x)", ["Math.absolute(x)", "Math.positive(x)", "Math.norm(x)"]),
    S("Quelle méthode statique de la classe Math retourne la racine carrée d'un nombre ?", "Math.sqrt(x)", ["Math.root(x)", "Math.pow(x, 0.5)", "Math.square(x)"]),
    S("Quelle méthode utilitaire de la classe Objects permet de comparer deux références en gérant proprement le cas null ?", "Objects.equals(a, b)", ["Objects.compare(a, b)", "Objects.same(a, b)", "a.equals(b) uniquement"]),
    M("Lesquelles de ces méthodes appartiennent à la classe Math en Java ?", ["Math.max(a, b)", "Math.pow(a, b)", "Math.random()"], ["Math.concat(a, b)"]),
    M("Quelles méthodes utilitaires fournit la classe Objects pour simplifier le code défensif ?", ["Objects.requireNonNull(obj)", "Objects.equals(a, b)"], ["Objects.clone(obj)"]),
    TF("Math.random() retourne un double compris dans l'intervalle [0.0, 1.0) en Java.", true),
  ]
),
Quiz(
  "Initialisation des champs et blocs d'initialisation",
  "Comprendre l'ordre d'initialisation des champs, blocs et constructeurs.",
  [
    S("Dans quel ordre s'exécutent, à la création d'un objet, les blocs d'initialisation d'instance et le constructeur ?", "Les blocs d'initialisation d'instance s'exécutent avant le corps du constructeur", ["Le constructeur s'exécute toujours avant les blocs d'initialisation", "L'ordre est aléatoire", "Les blocs d'initialisation ne s'exécutent jamais automatiquement"]),
    S("Quand un bloc d'initialisation statique (static { ... }) s'exécute-t-il ?", "Une seule fois, lors du chargement de la classe par la JVM", ["À chaque création d'instance", "Jamais automatiquement", "Uniquement si la méthode main l'appelle explicitement"]),
    S("Si un champ d'instance est initialisé à la fois lors de sa déclaration et dans le constructeur, quelle valeur prévaut finalement ?", "La valeur affectée dans le constructeur, exécuté en dernier", ["La valeur de déclaration, qui prévaut toujours", "Une erreur de compilation se produit", "La valeur par défaut du type"]),
    M("Lesquelles de ces affirmations sur l'ordre d'initialisation en Java sont correctes ?", ["Les champs statiques sont initialisés avant toute instance de la classe", "Les blocs d'initialisation d'instance s'exécutent dans l'ordre où ils apparaissent dans le code"], ["Le constructeur s'exécute systématiquement avant les champs d'instance"]),
    M("Quels éléments participent à l'initialisation d'un objet Java à sa création ?", ["Les initialiseurs de champs d'instance", "Les blocs d'initialisation d'instance", "Le corps du constructeur"], ["Le garbage collector"]),
    TF("Un bloc d'initialisation statique ne s'exécute qu'une seule fois par classe, indépendamment du nombre d'instances créées.", true),
  ]
),
Quiz(
  "Héritage et constructeurs : ordre d'appel",
  "Comprendre la chaîne d'appel des constructeurs lors de l'instanciation d'une sous-classe.",
  [
    S("Lorsqu'on instancie un objet d'une sous-classe, quel constructeur est exécuté en premier ?", "Le constructeur de la super-classe (implicitement ou via super())", ["Le constructeur de la sous-classe uniquement", "Aucun, seuls les champs sont initialisés", "Les deux constructeurs s'exécutent simultanément"]),
    S("Si une sous-classe ne fait pas d'appel explicite à super(...) dans son constructeur, que fait le compilateur ?", "Il insère implicitement un appel à super() sans argument en première instruction", ["Il provoque une erreur de compilation systématique", "Il ignore totalement le constructeur parent", "Il appelle this() par défaut"]),
    S("Que se passe-t-il si la super-classe ne possède pas de constructeur sans argument et que la sous-classe n'appelle pas explicitement super(...) avec les bons arguments ?", "Une erreur de compilation se produit", ["Le programme compile mais lève une exception à l'exécution", "Java crée automatiquement un constructeur compatible", "Rien, l'appel est ignoré"]),
    M("Lesquelles de ces affirmations sur l'ordre d'appel des constructeurs sont correctes ?", ["Le constructeur de la super-classe s'exécute avant celui de la sous-classe", "super(...) doit être la première instruction du constructeur si utilisé explicitement"], ["this() et super() peuvent être appelés tous les deux dans le même constructeur"]),
    M("Quelles conséquences a l'absence de constructeur sans argument dans une super-classe ?", ["La sous-classe doit appeler explicitement un super(...) avec les bons arguments", "Ne pas le faire provoque une erreur de compilation"], ["Cela rend la super-classe abstraite automatiquement"]),
    TF("this() et super() ne peuvent pas être utilisés tous les deux dans le même constructeur, car chacun doit être la première instruction.", true),
  ]
),
Quiz(
  "Classes scellées et modélisation des types (notions modernes)",
  "Découvrir les évolutions récentes de Java pour mieux modéliser des hiérarchies fermées.",
  [
    S("Quel est l'objectif principal d'une classe ou interface sealed (scellée), introduite en Java 17 ?", "Restreindre explicitement la liste des sous-types autorisés", ["Empêcher toute instanciation de la classe", "Rendre la classe automatiquement thread-safe", "Remplacer les interfaces classiques"]),
    S("Quel mot-clé doit accompagner la déclaration d'une classe sealed pour lister ses sous-classes autorisées ?", "permits", ["extends", "allows", "implements"]),
    S("Une sous-classe directe d'une classe sealed doit obligatoirement être déclarée comme :", "final, sealed ou non-sealed", ["abstract uniquement", "static uniquement", "private"]),
    M("Lesquelles de ces affirmations sur les classes sealed sont correctes ?", ["Elles permettent un contrôle plus strict de la hiérarchie de classes", "Elles facilitent l'exhaustivité d'un pattern matching sur les sous-types"], ["Elles autorisent n'importe quelle classe externe à les étendre librement"]),
    M("Quels mots-clés interviennent dans la déclaration d'une hiérarchie sealed en Java ?", ["sealed", "permits", "non-sealed"], ["volatile"]),
    TF("Une classe sealed limite explicitement, via la liste permits, quelles classes peuvent en hériter.", true),
  ]
),
Quiz(
  "Records : classes de données concises (Java 16+)",
  "Découvrir les records comme moyen concis de modéliser des objets immuables porteurs de données.",
  [
    S("Quel mot-clé introduit en Java 16 permet de définir une classe de données immuable de façon concise ?", "record", ["data", "struct", "value"]),
    S("Que génère automatiquement le compilateur pour un record Point(int x, int y) ?", "Un constructeur, des accesseurs, equals(), hashCode() et toString()", ["Uniquement un constructeur vide", "Rien, il faut tout écrire manuellement", "Uniquement la méthode toString()"]),
    S("Les champs d'un record sont-ils modifiables après construction ?", "Non, ils sont implicitement final", ["Oui, via des setters générés automatiquement", "Oui, directement par accès au champ", "Cela dépend du type du champ"]),
    M("Lesquelles de ces affirmations sur les records Java sont correctes ?", ["Un record est implicitement final", "Un record peut implémenter des interfaces"], ["Un record peut étendre une autre classe"]),
    M("Quels éléments un record génère-t-il automatiquement à partir de ses composants ?", ["Des méthodes d'accès portant le nom du composant", "Une méthode equals() basée sur les composants"], ["Des setters pour chaque composant"]),
    TF("Un record en Java est implicitement final et ne peut donc pas être étendu par une autre classe.", true),
  ]
),
Quiz(
  "Encapsulation : getters, setters et validation",
  "Concevoir des accesseurs robustes qui valident les données avant modification.",
  [
    S("Quel est l'intérêt principal d'utiliser un setter plutôt qu'un champ public direct pour modifier un attribut ?", "Pouvoir valider ou contrôler la valeur avant de l'assigner réellement", ["Rendre le champ accessible à tout le monde", "Accélérer l'exécution du programme", "Rendre la classe abstraite"]),
    S("Que devrait faire un setter setAge(int age) si la valeur reçue est négative, dans une conception robuste ?", "Lever une exception ou refuser l'affectation", ["Accepter silencieusement la valeur négative", "Mettre l'âge à 100 automatiquement", "Arrêter le programme immédiatement avec System.exit"]),
    S("Quel principe de conception orientée objet est directement renforcé par l'utilisation cohérente de getters et setters validés ?", "L'encapsulation", ["L'héritage multiple", "La généricité", "Le polymorphisme statique"]),
    M("Lesquelles de ces pratiques favorisent une bonne encapsulation en Java ?", ["Déclarer les champs private", "Exposer des méthodes publiques contrôlées pour lire ou modifier l'état"], ["Déclarer tous les champs public pour simplifier l'accès"]),
    M("Quels avantages apporte une encapsulation correcte des champs d'une classe ?", ["Elle permet de changer l'implémentation interne sans casser le code appelant", "Elle permet de valider les données avant modification"], ["Elle interdit toute lecture des données depuis l'extérieur"]),
    TF("Une bonne encapsulation consiste à déclarer les champs private et à exposer un accès contrôlé via des méthodes publiques.", true),
  ]
),
Quiz(
  "Méthodes génériques et bornes de types",
  "Définir des méthodes génériques et utiliser des bornes avec extends.",
  [
    S("Quelle syntaxe déclare une méthode générique statique acceptant un type T quelconque ?", "static <T> void afficher(T element)", ["static void afficher<T>(T element)", "static void afficher(T<element>)", "static T afficher(element)"]),
    S("Que signifie la borne <T extends Number> dans une déclaration générique ?", "T doit être Number ou une sous-classe de Number", ["T doit être différent de Number", "T ne peut être que la classe Number exacte", "T doit implémenter Comparable"]),
    S("Quel symbole générique représente un type inconnu utilisé pour la flexibilité en lecture, comme List<?> ?", "Le wildcard ?", ["Le symbole T", "Le symbole *", "Le symbole _"]),
    M("Lesquelles de ces déclarations génériques sont valides en Java ?", ["<T> T premierElement(List<T> liste)", "<T extends Comparable<T>> T max(List<T> liste)"], ["<T> sans aucun usage dans la signature de la méthode"]),
    M("Quelles affirmations sur les bornes génériques (extends) sont correctes ?", ["Elles permettent de restreindre les types acceptés par un paramètre générique", "Elles permettent d'appeler les méthodes de la borne sur le paramètre générique"], ["Elles permettent d'utiliser des types primitifs directement comme int"]),
    TF("La borne <T extends Number> permet d'appeler des méthodes de Number, comme doubleValue(), sur une variable de type T.", true),
  ]
),
Quiz(
  "Comparaison approfondie ArrayList vs Vector vs Stack",
  "Distinguer ArrayList des anciennes classes historiques Vector et Stack.",
  [
    S("Quelle différence majeure existe entre ArrayList et Vector concernant la concurrence ?", "Vector est synchronisée par défaut, contrairement à ArrayList", ["ArrayList est synchronisée, contrairement à Vector", "Les deux sont identiques en tout point", "Vector ne peut pas contenir d'objets"]),
    S("Quelle classe historique de Java implémente une structure de pile (LIFO) en étendant Vector ?", "Stack", ["Queue", "Deque", "ArrayList"]),
    S("Pourquoi recommande-t-on souvent ArrayDeque plutôt que la classe historique Stack pour implémenter une pile aujourd'hui ?", "ArrayDeque est plus performante et n'hérite pas du surcoût de synchronisation de Vector", ["Stack ne peut contenir que des entiers", "ArrayDeque est synchronisée alors que Stack ne l'est pas", "Stack n'existe plus dans les versions récentes de Java"]),
    M("Lesquelles de ces affirmations sur Vector sont correctes ?", ["Vector est une classe historique présente depuis les débuts de Java", "Ses méthodes sont synchronisées, ce qui peut nuire à la performance en environnement mono-thread"], ["Vector a été totalement supprimée des versions récentes de Java"]),
    M("Quelles classes peuvent être utilisées pour représenter une pile (LIFO) en Java moderne ?", ["ArrayDeque", "Stack (historique)"], ["HashSet"]),
    TF("La synchronisation systématique des méthodes de Vector entraîne un coût de performance inutile dans un contexte mono-thread.", true),
  ]
),
Quiz(
  "Map avancée : merge, computeIfAbsent et getOrDefault",
  "Utiliser les méthodes par défaut modernes de l'interface Map introduites en Java 8.",
  [
    S("Quelle méthode de Map permet de récupérer la valeur d'une clé, ou une valeur de remplacement si la clé est absente, sans modifier la map ?", "getOrDefault(clé, valeurParDefaut)", ["get(clé)", "computeIfAbsent(clé, fonction)", "putIfAbsent(clé, valeur)"]),
    S("Quelle méthode de Map permet d'ajouter une valeur calculée uniquement si la clé n'est pas déjà présente ?", "computeIfAbsent(clé, fonction)", ["getOrDefault(clé, valeur)", "remove(clé)", "replace(clé, valeur)"]),
    S("Quelle méthode de Map permet de combiner une nouvelle valeur avec une valeur existante via une fonction, utile pour des compteurs ?", "merge(clé, valeur, fonction)", ["get(clé)", "containsKey(clé)", "keySet()"]),
    M("Lesquelles de ces méthodes par défaut de l'interface Map ont été introduites en Java 8 ?", ["getOrDefault(K, V)", "computeIfAbsent(K, Function)", "merge(K, V, BiFunction)"], ["put(K, V)"]),
    M("Quels usages typiques se prêtent bien à la méthode merge() d'une Map ?", ["Compter les occurrences d'un mot dans un texte", "Cumuler des montants associés à une même clé"], ["Trier les clés d'une map par ordre alphabétique"]),
    TF("La méthode getOrDefault() ne modifie pas la map, contrairement à computeIfAbsent() qui peut y insérer une nouvelle entrée.", true),
  ]
),
Quiz(
  "Classes utilitaires : Arrays et manipulation de tableaux",
  "Exploiter les méthodes statiques de la classe Arrays pour trier, copier et comparer des tableaux.",
  [
    S("Quelle méthode statique de la classe Arrays permet de trier un tableau d'entiers en place ?", "Arrays.sort(tableau)", ["Arrays.order(tableau)", "tableau.sort()", "Collections.sort(tableau)"]),
    S("Quelle méthode statique de Arrays permet de convertir un tableau en une chaîne lisible pour le débogage ?", "Arrays.toString(tableau)", ["tableau.toString()", "Arrays.print(tableau)", "String.valueOf(tableau) uniquement"]),
    S("Quelle méthode statique de Arrays permet de copier une portion d'un tableau dans un nouveau tableau ?", "Arrays.copyOfRange(tableau, debut, fin)", ["Arrays.slice(tableau, debut, fin)", "tableau.copy(debut, fin)", "Arrays.extract(tableau, debut, fin)"]),
    M("Lesquelles de ces méthodes appartiennent à la classe utilitaire Arrays ?", ["Arrays.sort(T[])", "Arrays.equals(T[], T[])", "Arrays.fill(T[], T)"], ["Arrays.add(T[], T)"]),
    M("Quelles affirmations sur la classe Arrays sont correctes ?", ["Arrays.equals() compare le contenu de deux tableaux élément par élément", "tableau.toString() sur un tableau natif n'affiche pas son contenu de façon lisible"], ["Les tableaux disposent nativement d'une méthode toString() lisible sans passer par Arrays"]),
    TF("Appeler directement toString() sur un tableau Java (sans passer par Arrays.toString()) n'affiche pas son contenu de façon lisible.", true),
  ]
),
Quiz(
  "Annotations courantes : @Override, @Deprecated, @SuppressWarnings",
  "Reconnaître l'usage des annotations standard les plus fréquentes en Java.",
  [
    S("Quelle annotation indique au compilateur qu'une méthode est censée redéfinir une méthode héritée ?", "@Override", ["@Inherited", "@FunctionalInterface", "@SuppressWarnings"]),
    S("Quelle annotation signale qu'un élément (méthode, classe) est obsolète et ne devrait plus être utilisé ?", "@Deprecated", ["@Override", "@Retired", "@Legacy"]),
    S("Quelle annotation permet de désactiver certains avertissements du compilateur pour une portion de code ?", "@SuppressWarnings", ["@IgnoreWarnings", "@NoWarnings", "@Silent"]),
    M("Lesquelles de ces annotations existent nativement en Java ?", ["@Override", "@Deprecated", "@SuppressWarnings"], ["@Synchronized"]),
    M("Quel intérêt apporte l'utilisation de @Override sur une méthode redéfinie ?", ["Le compilateur signale une erreur si la méthode ne redéfinit en réalité rien", "Cela améliore la lisibilité du code pour les autres développeurs"], ["Cela rend la méthode automatiquement plus rapide à l'exécution"]),
    TF("@Override permet au compilateur de détecter une erreur si la méthode annotée ne correspond en réalité à aucune méthode de la super-classe ou de l'interface.", true),
  ]
),
Quiz(
  "Conditions de course et bonnes pratiques de concurrence",
  "Identifier les pièges courants de la programmation concurrente en Java.",
  [
    S("Qu'est-ce qu'une condition de course (race condition) en programmation concurrente ?", "Une situation où le résultat dépend de l'ordre d'exécution imprévisible de plusieurs threads", ["Une erreur de compilation liée aux threads", "Un type particulier d'exception Java", "Une boucle infinie dans un thread"]),
    S("Pourquoi un compteur partagé incrémenté par plusieurs threads sans synchronisation peut-il donner un résultat incorrect ?", "Parce que l'opération d'incrémentation n'est pas atomique et peut être interrompue entre threads", ["Parce que Java interdit les variables partagées", "Parce que les threads s'exécutent toujours dans le désordre total", "Parce que le compilateur refuse ce genre de code"]),
    S("Quelle classe de java.util.concurrent.atomic permet d'incrémenter un compteur de manière thread-safe sans synchronized explicite ?", "AtomicInteger", ["Integer", "volatile int", "SafeCounter"]),
    M("Lesquelles de ces pratiques permettent de réduire les risques de conditions de course en Java ?", ["Utiliser le mot-clé synchronized sur les sections critiques", "Utiliser des classes atomiques comme AtomicInteger"], ["Ignorer la synchronisation si le programme semble fonctionner sur sa machine"]),
    M("Quelles affirmations sur les conditions de course sont correctes ?", ["Elles sont souvent difficiles à reproduire car dépendantes du timing d'exécution", "Elles peuvent corrompre des données partagées entre threads"], ["Elles ne peuvent jamais se produire en Java grâce à la JVM"]),
    TF("Une condition de course peut se produire lorsque plusieurs threads accèdent et modifient une même variable partagée sans synchronisation appropriée.", true),
  ]
),
Quiz(
  "Méthodes d'égalité spécifiques : tableaux et collections imbriquées",
  "Comprendre les pièges de comparaison entre tableaux et collections.",
  [
    S("Pourquoi deux tableaux contenant les mêmes éléments ne sont-ils pas égaux avec == ou même equals() par défaut ?", "Parce que equals() d'un tableau n'est pas redéfini et compare les références comme ==", ["Parce que les tableaux ne peuvent jamais être comparés", "Parce que Java compare automatiquement le contenu mais affiche une erreur", "Parce que les tableaux sont toujours triés différemment"]),
    S("Quelle méthode statique permet de comparer correctement le contenu de deux tableaux simples ?", "Arrays.equals(tab1, tab2)", ["tab1.equals(tab2)", "tab1 == tab2", "Objects.same(tab1, tab2)"]),
    S("Quelle méthode statique permet de comparer le contenu de deux tableaux multidimensionnels (tableaux de tableaux) ?", "Arrays.deepEquals(tab1, tab2)", ["Arrays.equals(tab1, tab2)", "tab1.deepEquals(tab2)", "Arrays.compare(tab1, tab2)"]),
    M("Lesquelles de ces affirmations sur l'égalité des tableaux en Java sont correctes ?", ["tab1.equals(tab2) revient à comparer les références comme ==", "Arrays.equals() compare le contenu élément par élément pour un tableau simple"], ["Les tableaux Java redéfinissent equals() pour comparer leur contenu automatiquement"]),
    M("Quelles collections standard redéfinissent correctement equals() pour comparer leur contenu (et non leur référence) ?", ["ArrayList", "HashMap"], ["Les tableaux natifs comme int[]"]),
    TF("Par défaut, comparer deux tableaux avec equals() revient à comparer leurs références, comme avec l'opérateur ==.", true),
  ]
),
Quiz(
  "Conception orientée objet : composition vs héritage",
  "Choisir entre composition et héritage selon le contexte de conception.",
  [
    S("Quel principe de conception orientée objet privilégie l'assemblage d'objets plutôt qu'une hiérarchie de classes rigide ?", "La composition", ["L'héritage multiple", "Le polymorphisme statique", "L'encapsulation stricte"]),
    S("Quel problème classique l'héritage profond et mal conçu peut-il provoquer dans une application ?", "Un fort couplage entre classes et une fragilité face aux changements de la super-classe", ["Une amélioration automatique des performances", "Une réduction du nombre de classes nécessaires", "Aucun problème particulier"]),
    S("Dans une relation de composition, comment une classe Voiture utilise-t-elle typiquement une classe Moteur ?", "En détenant une référence vers un objet Moteur comme champ d'instance", ["En héritant directement de Moteur via extends", "En implémentant Moteur comme une interface", "En dupliquant le code de Moteur"]),
    M("Lesquelles de ces affirmations sur composition et héritage sont correctes ?", ["La composition favorise un couplage plus faible entre les classes", "L'héritage convient bien à une relation \"est-un\" claire et stable"], ["La composition oblige obligatoirement à utiliser des interfaces"]),
    M("Dans quelles situations la composition est-elle généralement préférée à l'héritage ?", ["Quand la relation entre les classes est de type \"a-un\" plutôt que \"est-un\"", "Quand on veut pouvoir changer le comportement à l'exécution en changeant l'objet composé"], ["Quand on veut absolument maximiser le nombre de niveaux d'héritage"]),
    TF("La phrase souvent citée en conception orientée objet est de préférer la composition à l'héritage lorsque c'est possible, pour limiter le couplage.", true),
  ]
),
];
