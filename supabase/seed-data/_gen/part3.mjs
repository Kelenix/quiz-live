import { S, M, TF, Quiz } from "./helpers.mjs";

export const part3 = [
Quiz(
  "Exceptions : try, catch, finally",
  "Maîtriser la structure de base de la gestion d'exceptions en Java.",
  [
    S("Quel bloc contient le code susceptible de lever une exception ?", "try", ["catch", "finally", "throw"]),
    S("Quel bloc s'exécute systématiquement, qu'une exception soit levée ou non ?", "finally", ["try", "catch", "throws"]),
    S("Quel mot-clé permet de capturer une exception levée dans un bloc try ?", "catch", ["try", "finally", "throw"]),
    M("Lesquelles de ces affirmations sur try/catch/finally sont correctes ?", ["Un bloc try peut être suivi de plusieurs blocs catch", "Le bloc finally s'exécute même si un return est présent dans le try"], ["Le bloc finally ne s'exécute jamais si une exception est levée"]),
    M("Quels éléments peuvent suivre un bloc try en Java ?", ["Un ou plusieurs catch", "Un bloc finally"], ["Un bloc else"]),
    TF("Le bloc finally s'exécute même si le bloc try contient une instruction return.", true),
  ]
),
Quiz(
  "Lever des exceptions : throw et throws",
  "Distinguer l'instruction throw et la déclaration throws dans une signature.",
  [
    S("Quel mot-clé permet de lever explicitement une exception dans le code ?", "throw", ["throws", "catch", "raise"]),
    S("Quel mot-clé, placé dans la signature d'une méthode, indique qu'elle peut propager une exception checked ?", "throws", ["throw", "catch", "declare"]),
    S("Quelle est la syntaxe correcte pour lever une nouvelle exception personnalisée ?", "throw new IllegalArgumentException(\"message\");", ["throws new IllegalArgumentException(\"message\");", "throw IllegalArgumentException(\"message\");", "raise IllegalArgumentException(\"message\");"]),
    M("Lesquelles de ces affirmations sur throw et throws sont correctes ?", ["throw est utilisé à l'intérieur du corps d'une méthode pour déclencher une exception", "throws est utilisé dans la signature d'une méthode pour annoncer les exceptions checked possibles"], ["throw et throws sont strictement interchangeables"]),
    M("Quelles informations peut-on passer au constructeur d'une exception en Java ?", ["Un message décrivant l'erreur", "Une cause (autre exception) pour le chaînage"], ["Un type de retour"]),
    TF("Une méthode qui lève une RuntimeException n'est pas obligée de la déclarer avec throws.", true),
  ]
),
Quiz(
  "Exceptions vérifiées (checked) vs non vérifiées (unchecked)",
  "Distinguer les deux grandes familles d'exceptions Java et leurs implications.",
  [
    S("Quelle classe est la super-classe directe des exceptions checked et des RuntimeException ?", "Exception", ["Error", "Throwable", "RuntimeException"]),
    S("Une exception checked comme IOException doit obligatoirement être :", "Capturée ou déclarée avec throws", ["Ignorée par le compilateur", "Convertie en Error", "Levée uniquement dans main"]),
    S("À quelle catégorie appartient NullPointerException ?", "Une exception unchecked (RuntimeException)", ["Une exception checked", "Une Error", "Aucune des deux"]),
    M("Lesquelles de ces exceptions sont des exceptions unchecked (héritent de RuntimeException) ?", ["NullPointerException", "ArrayIndexOutOfBoundsException", "ArithmeticException"], ["IOException"]),
    M("Quelles affirmations sur les exceptions checked sont correctes ?", ["Le compilateur oblige à les capturer ou à les déclarer", "IOException et SQLException en sont des exemples typiques"], ["Elles héritent toutes de RuntimeException"]),
    TF("Toutes les exceptions unchecked héritent de la classe RuntimeException.", true),
  ]
),
Quiz(
  "Hiérarchie des exceptions Java",
  "Comprendre l'arborescence Throwable, Exception et Error.",
  [
    S("Quelle est la classe racine de toute la hiérarchie des exceptions en Java ?", "Throwable", ["Exception", "Error", "RuntimeException"]),
    S("Quelle catégorie de problème représente la classe Error, comme OutOfMemoryError ?", "Des erreurs graves généralement non récupérables par l'application", ["Des erreurs de syntaxe détectées à la compilation", "Des exceptions à toujours capturer", "Des avertissements sans conséquence"]),
    S("Quelle classe est la super-classe directe de IllegalArgumentException ?", "RuntimeException", ["Exception", "Error", "Throwable"]),
    M("Lesquelles de ces classes font partie de la hiérarchie standard des exceptions Java ?", ["Throwable", "Exception", "Error"], ["Warning"]),
    M("Quelles affirmations sur la hiérarchie Throwable sont correctes ?", ["Exception et Error héritent toutes deux de Throwable", "RuntimeException hérite de Exception"], ["Error hérite de RuntimeException"]),
    TF("La classe Error représente généralement des problèmes graves que l'application n'est pas censée tenter de capturer.", true),
  ]
),
Quiz(
  "Exceptions personnalisées",
  "Créer ses propres types d'exceptions métier en Java.",
  [
    S("Pour créer une exception personnalisée non vérifiée, quelle classe doit-on étendre ?", "RuntimeException", ["Exception", "Error", "Throwable seul sans hériter d'Exception"]),
    S("Pour créer une exception personnalisée vérifiée (checked), quelle classe doit-on étendre ?", "Exception", ["RuntimeException", "Error", "Object"]),
    S("Quel est l'intérêt principal de créer une exception métier comme SoldeInsuffisantException plutôt que d'utiliser RuntimeException directement ?", "Cela rend le code plus explicite et permet une gestion ciblée de ce cas précis", ["Cela accélère l'exécution du programme", "Cela évite d'écrire des blocs try/catch", "Cela transforme automatiquement l'exception en avertissement"]),
    M("Lesquelles de ces étapes sont nécessaires pour créer une exception personnalisée checked en Java ?", ["Étendre la classe Exception", "Définir un ou plusieurs constructeurs appelant super(message)"], ["Implémenter l'interface Runnable"]),
    M("Quelles bonnes pratiques s'appliquent à la conception d'exceptions personnalisées ?", ["Donner un nom descriptif se terminant souvent par Exception", "Fournir un constructeur acceptant un message et éventuellement une cause"], ["Toujours hériter directement de Throwable plutôt que d'Exception"]),
    TF("Une classe d'exception personnalisée qui étend RuntimeException n'a pas besoin d'être déclarée avec throws pour être propagée.", true),
  ]
),
Quiz(
  "Multi-catch et try-with-resources",
  "Utiliser les fonctionnalités modernes de gestion d'exceptions de Java 7+.",
  [
    S("Quelle syntaxe permet de capturer plusieurs types d'exceptions dans un même bloc catch ?", "catch (IOException | SQLException e)", ["catch (IOException, SQLException e)", "catch (IOException e) catch (SQLException e)", "catch [IOException, SQLException] (e)"]),
    S("Quel est l'intérêt du try-with-resources introduit en Java 7 ?", "Fermer automatiquement les ressources implémentant AutoCloseable à la fin du bloc", ["Capturer automatiquement toutes les exceptions sans catch", "Accélérer la compilation", "Remplacer totalement le mot-clé finally"]),
    S("Quelle interface une ressource doit-elle implémenter pour être utilisable dans un try-with-resources ?", "AutoCloseable", ["Serializable", "Comparable", "Iterable"]),
    M("Lesquelles de ces affirmations sur try-with-resources sont correctes ?", ["Les ressources sont fermées automatiquement même si une exception est levée", "On peut déclarer plusieurs ressources séparées par un point-virgule"], ["Il interdit l'utilisation d'un bloc catch associé"]),
    M("Quelles classes Java standard implémentent AutoCloseable et sont couramment utilisées avec try-with-resources ?", ["FileInputStream", "BufferedReader"], ["Integer"]),
    TF("Dans un multi-catch comme catch (IOException | SQLException e), la variable e a pour type effectif l'union des deux types.", true),
  ]
),
Quiz(
  "ArrayList : liste dynamique",
  "Manipuler la collection ArrayList et comprendre ses caractéristiques.",
  [
    S("Quelle interface de la bibliothèque standard ArrayList implémente-t-elle principalement ?", "List", ["Set", "Map", "Queue"]),
    S("Quelle méthode permet d'ajouter un élément à la fin d'une ArrayList ?", "add(element)", ["push(element)", "insert(element)", "append(element)"]),
    S("Quel est l'avantage principal d'une ArrayList par rapport à un tableau classique ?", "Sa taille peut s'adapter dynamiquement lors des ajouts", ["Elle consomme toujours moins de mémoire", "Elle est plus rapide pour tous les accès", "Elle ne peut contenir que des nombres"]),
    M("Lesquelles de ces affirmations sur ArrayList sont correctes ?", ["L'accès par indice get(i) est en temps constant", "ArrayList autorise les doublons"], ["ArrayList ne peut contenir que des types primitifs"]),
    M("Quelles méthodes sont disponibles sur une ArrayList en Java ?", ["add(E)", "remove(int)", "get(int)"], ["push(E)"]),
    TF("ArrayList conserve l'ordre d'insertion des éléments.", true),
  ]
),
Quiz(
  "LinkedList : liste chaînée",
  "Comparer LinkedList à ArrayList en termes de structure et de performance.",
  [
    S("Quelle structure de données interne caractérise LinkedList par opposition à ArrayList ?", "Une liste doublement chaînée de nœuds", ["Un tableau redimensionnable", "Une table de hachage", "Un arbre binaire"]),
    S("Pour quelle opération LinkedList est-elle généralement plus efficace qu'ArrayList ?", "L'insertion ou la suppression en début de liste", ["L'accès aléatoire par indice", "Le tri par défaut", "La recherche binaire"]),
    S("Quelles interfaces LinkedList implémente-t-elle, en plus de List ?", "Deque", ["Set", "Map", "Comparable"]),
    M("Lesquelles de ces affirmations comparant ArrayList et LinkedList sont correctes ?", ["ArrayList offre un accès en temps constant par indice", "LinkedList est souvent plus efficace pour des insertions fréquentes en tête de liste"], ["LinkedList offre un accès en temps constant par indice comme ArrayList"]),
    M("Quelles opérations LinkedList propose-t-elle grâce à l'interface Deque ?", ["addFirst(E)", "addLast(E)"], ["binarySearch(E)"]),
    TF("L'accès à un élément au milieu d'une LinkedList par indice est plus lent qu'avec une ArrayList.", true),
  ]
),
Quiz(
  "HashMap : structure clé-valeur",
  "Comprendre le fonctionnement de HashMap et ses garanties.",
  [
    S("Quelle interface définit le contrat clé-valeur implémenté par HashMap ?", "Map", ["List", "Set", "Collection"]),
    S("Quelle méthode permet d'ajouter ou de mettre à jour une paire clé-valeur dans une HashMap ?", "put(clé, valeur)", ["add(clé, valeur)", "insert(clé, valeur)", "set(clé, valeur)"]),
    S("HashMap garantit-elle un ordre particulier de parcours de ses éléments ?", "Non, l'ordre n'est pas garanti", ["Oui, toujours l'ordre d'insertion", "Oui, toujours l'ordre alphabétique des clés", "Oui, toujours l'ordre croissant des valeurs"]),
    M("Lesquelles de ces affirmations sur HashMap sont correctes ?", ["Une HashMap n'autorise qu'une seule clé null", "Les clés d'une HashMap doivent avoir des implémentations cohérentes de equals() et hashCode()"], ["Une HashMap conserve l'ordre d'insertion comme LinkedHashMap"]),
    M("Quelles méthodes sont disponibles sur une HashMap en Java ?", ["put(K, V)", "get(K)", "containsKey(K)"], ["push(K, V)"]),
    TF("Dans une HashMap, une même clé ne peut être associée qu'à une seule valeur à la fois.", true),
  ]
),
Quiz(
  "HashSet : ensembles sans doublons",
  "Manipuler HashSet pour stocker des éléments uniques.",
  [
    S("Quelle est la principale caractéristique d'un HashSet ?", "Il ne contient aucun élément en double", ["Il conserve l'ordre d'insertion", "Il trie automatiquement les éléments", "Il accepte les indices comme une liste"]),
    S("Que renvoie la méthode add() d'un HashSet si l'élément ajouté est déjà présent ?", "false, et l'ensemble reste inchangé", ["true, et l'élément est dupliqué", "Une exception est levée", "null"]),
    S("Sur quel mécanisme HashSet repose-t-il en interne pour stocker ses éléments efficacement ?", "Une table de hachage (via HashMap en interne)", ["Un tableau trié", "Une liste chaînée simple", "Un arbre binaire de recherche"]),
    M("Lesquelles de ces affirmations sur HashSet sont correctes ?", ["Il ne garantit aucun ordre de parcours particulier", "Il repose sur equals() et hashCode() pour détecter les doublons"], ["Il autorise plusieurs occurrences d'un même élément"]),
    M("Quelles méthodes sont disponibles sur un HashSet en Java ?", ["add(E)", "contains(E)", "remove(E)"], ["get(int)"]),
    TF("HashSet n'accepte qu'une seule occurrence de la valeur null.", true),
  ]
),
Quiz(
  "Comparer List, Set et Map",
  "Synthétiser les différences fondamentales entre les grandes familles de collections.",
  [
    S("Quelle interface de collection autorise les doublons et conserve un ordre indexé ?", "List", ["Set", "Map", "Queue uniquement"]),
    S("Quelle interface de collection garantit l'unicité de ses éléments ?", "Set", ["List", "Map", "Deque"]),
    S("Quelle interface de collection associe des clés uniques à des valeurs ?", "Map", ["List", "Set", "Collection"]),
    M("Lesquelles de ces affirmations sur List, Set et Map sont correctes ?", ["Une List autorise les doublons", "Un Set ne contient pas de doublons"], ["Map hérite directement de l'interface Collection"]),
    M("Quelles implémentations concrètes correspondent à chacune de ces interfaces en Java ?", ["ArrayList implémente List", "HashSet implémente Set"], ["HashMap implémente List"]),
    TF("L'interface Map ne fait pas partie de la hiérarchie de l'interface Collection en Java.", true),
  ]
),
Quiz(
  "Itération sur les collections : Iterator",
  "Comprendre l'interface Iterator et son usage pour parcourir une collection en toute sécurité.",
  [
    S("Quelle méthode de Iterator permet de vérifier s'il reste un élément à parcourir ?", "hasNext()", ["hasMore()", "next()", "remaining()"]),
    S("Quelle méthode de Iterator retourne l'élément courant et avance le curseur ?", "next()", ["get()", "current()", "advance()"]),
    S("Quel risque court-on en supprimant un élément d'une ArrayList directement dans une boucle for-each ?", "Une ConcurrentModificationException", ["Une StackOverflowError", "Un blocage infini du programme", "Aucun risque particulier"]),
    M("Lesquelles de ces affirmations sur Iterator sont correctes ?", ["Il permet de supprimer un élément en toute sécurité via remove() pendant le parcours", "Il est obtenu en appelant iterator() sur une collection"], ["Il garantit toujours un parcours dans l'ordre des clés triées"]),
    M("Quelles méthodes appartiennent à l'interface Iterator en Java ?", ["hasNext()", "next()", "remove()"], ["sort()"]),
    TF("Modifier la structure d'une ArrayList (ajout/suppression) pendant un parcours for-each classique peut lever une ConcurrentModificationException.", true),
  ]
),
Quiz(
  "TreeMap et TreeSet : collections triées",
  "Découvrir les implémentations triées des interfaces Map et Set.",
  [
    S("Sur quelle structure de données TreeMap repose-t-elle en interne pour garantir un ordre trié ?", "Un arbre rouge-noir (arbre binaire de recherche équilibré)", ["Une table de hachage", "Une liste chaînée", "Un tableau dynamique"]),
    S("Dans quel ordre TreeSet parcourt-il ses éléments par défaut ?", "L'ordre naturel croissant des éléments", ["L'ordre d'insertion", "Un ordre aléatoire", "L'ordre décroissant systématiquement"]),
    S("Quelle interface les éléments d'un TreeSet doivent-ils implémenter pour permettre le tri par défaut ?", "Comparable", ["Iterable", "Serializable", "Cloneable"]),
    M("Lesquelles de ces affirmations sur TreeMap et TreeSet sont correctes ?", ["Ils maintiennent leurs éléments dans un ordre trié", "On peut fournir un Comparator personnalisé pour changer l'ordre de tri"], ["Ils sont plus rapides que HashMap/HashSet pour un simple get() ou contains()"]),
    M("Quelles opérations TreeMap permet-il grâce à son tri interne ?", ["firstKey()", "lastKey()"], ["push()"]),
    TF("Contrairement à HashMap, TreeMap garantit que les clés sont parcourues dans un ordre trié.", true),
  ]
),
Quiz(
  "Queue et Deque : files et piles",
  "Comprendre les structures FIFO et LIFO en Java avec Queue et Deque.",
  [
    S("Quelle discipline de traitement caractérise typiquement une Queue (file) ?", "FIFO : premier entré, premier sorti", ["LIFO : dernier entré, premier sorti", "Un ordre totalement aléatoire", "Un ordre alphabétique"]),
    S("Quelle méthode de Queue permet d'ajouter un élément en fin de file ?", "offer(element)", ["push(element)", "insertFirst(element)", "set(element)"]),
    S("Quelle interface Java représente une structure permettant d'ajouter et retirer des éléments aux deux extrémités ?", "Deque", ["Queue uniquement", "List uniquement", "Stack uniquement"]),
    M("Lesquelles de ces affirmations sur Queue sont correctes ?", ["poll() retire et retourne l'élément en tête de file", "LinkedList peut être utilisée comme implémentation de Queue"], ["Une Queue garantit toujours un tri par ordre naturel"]),
    M("Quelles méthodes Deque permettent un comportement de pile (LIFO) ?", ["push(E)", "pop()"], ["enqueue(E)"]),
    TF("Une Deque (double-ended queue) peut être utilisée à la fois comme une pile (LIFO) et comme une file (FIFO).", true),
  ]
),
Quiz(
  "Collections immuables et utilitaires",
  "Découvrir les méthodes utilitaires de la classe Collections et les listes immuables.",
  [
    S("Quelle méthode statique de List (depuis Java 9) permet de créer une liste immuable rapidement ?", "List.of(...)", ["List.create(...)", "List.immutable(...)", "List.build(...)"]),
    S("Que se passe-t-il si on appelle add() sur une liste créée avec List.of(...) ?", "Une UnsupportedOperationException est levée", ["L'élément est ajouté normalement", "La liste double sa capacité", "Rien, l'appel est ignoré silencieusement"]),
    S("Quelle classe utilitaire fournit des méthodes statiques comme sort() et reverse() pour manipuler des List ?", "Collections", ["Collectors", "Arrays", "Objects"]),
    M("Lesquelles de ces affirmations sur les collections immuables sont correctes ?", ["Elles empêchent toute modification après création", "List.of() et Map.of() permettent d'en créer facilement depuis Java 9"], ["Une collection immuable peut toujours être modifiée via ses setters"]),
    M("Quelles méthodes statiques utiles fournit la classe Collections en Java ?", ["Collections.sort(List)", "Collections.unmodifiableList(List)"], ["Collections.parse(String)"]),
    TF("Collections.unmodifiableList() enveloppe une liste existante pour en interdire la modification via la vue retournée.", true),
  ]
),
Quiz(
  "Comparable et Comparator : tri d'objets",
  "Implémenter un ordre de tri naturel ou personnalisé pour des objets métier.",
  [
    S("Quelle interface une classe doit-elle implémenter pour définir un ordre de tri naturel ?", "Comparable<T>", ["Comparator<T>", "Serializable", "Iterable<T>"]),
    S("Quelle méthode doit-on implémenter pour respecter l'interface Comparable ?", "compareTo(T autre)", ["compare(T a, T b)", "equals(Object o)", "sort(T a, T b)"]),
    S("Quel est l'avantage principal d'utiliser un Comparator externe plutôt que Comparable ?", "Permettre plusieurs critères de tri sans modifier la classe d'origine", ["Rendre la classe immuable", "Accélérer automatiquement le tri", "Éviter d'implémenter equals()"]),
    M("Lesquelles de ces affirmations sur Comparable et Comparator sont correctes ?", ["Comparable définit un ordre naturel unique pour la classe", "Comparator permet de définir plusieurs stratégies de tri différentes"], ["Comparable et Comparator sont la même interface sous deux noms"]),
    M("Quelles valeurs peut retourner compareTo() ou compare() pour indiquer une relation d'ordre ?", ["Une valeur négative si le premier élément précède le second", "Zéro si les deux éléments sont équivalents pour l'ordre"], ["Toujours une valeur booléenne true ou false"]),
    TF("Collections.sort() peut trier une liste d'objets personnalisés si leur classe implémente Comparable.", true),
  ]
),
Quiz(
  "Tableaux vs collections : choisir la bonne structure",
  "Comparer les tableaux natifs aux collections de l'API Java.",
  [
    S("Quelle est la principale limitation d'un tableau Java par rapport à une ArrayList ?", "Sa taille est fixe une fois créé", ["Il ne peut pas contenir d'objets", "Il ne peut pas être parcouru avec for-each", "Il est toujours plus lent à l'accès"]),
    S("Quelle classe utilitaire permet de convertir facilement un tableau en List avec Arrays.asList() ?", "Arrays", ["Collections", "List", "Objects"]),
    S("Quel est l'avantage principal d'un tableau de type int[] par rapport à une ArrayList<Integer> ?", "Il évite l'autoboxing et consomme moins de mémoire", ["Il peut changer de taille dynamiquement", "Il offre plus de méthodes utilitaires", "Il garantit l'absence de doublons"]),
    M("Lesquelles de ces affirmations sur les tableaux Java sont correctes ?", ["Un tableau peut contenir des types primitifs directement", "La taille d'un tableau ne peut pas changer après sa création"], ["Un tableau est automatiquement trié à sa création"]),
    M("Dans quels cas privilégie-t-on une collection (comme ArrayList) plutôt qu'un tableau brut ?", ["Quand la taille de la structure doit varier dynamiquement", "Quand on a besoin de méthodes utilitaires riches comme contains() ou sort()"], ["Quand on veut absolument éviter tout objet en mémoire"]),
    TF("La méthode Arrays.asList() retourne une liste de taille fixe adossée au tableau d'origine.", true),
  ]
),
Quiz(
  "ConcurrentModificationException et parcours sécurisé",
  "Comprendre les pièges de la modification d'une collection pendant son parcours.",
  [
    S("Quelle exception peut être levée si on appelle list.remove() directement dans une boucle for-each sur cette même liste ?", "ConcurrentModificationException", ["NullPointerException", "IndexOutOfBoundsException", "IllegalStateException"]),
    S("Quel objet permet de supprimer un élément en toute sécurité pendant le parcours d'une collection ?", "L'Iterator de la collection, via sa méthode remove()", ["Le tableau interne de la collection", "Une nouvelle ArrayList vide", "Le mot-clé synchronized"]),
    S("Quelle classe de la bibliothèque standard permet d'éviter ce problème en travaillant sur une copie ou une vue spécialisée pour la concurrence ?", "CopyOnWriteArrayList", ["ArrayList", "LinkedList", "HashSet"]),
    M("Lesquelles de ces pratiques permettent d'éviter une ConcurrentModificationException ?", ["Utiliser iterator.remove() pendant le parcours", "Parcourir une copie de la collection pour effectuer les suppressions"], ["Modifier directement la collection dans un for-each classique"]),
    M("Quelles affirmations sur ConcurrentModificationException sont correctes ?", ["Elle est généralement liée à un compteur de modification (modCount) interne détecté incohérent", "Elle peut survenir même en environnement mono-thread"], ["Elle ne peut survenir qu'en environnement multi-thread"]),
    TF("Utiliser explicitement la méthode remove() d'un Iterator pendant un parcours évite la ConcurrentModificationException.", true),
  ]
),
Quiz(
  "Complexité algorithmique des opérations sur collections",
  "Évaluer la complexité de base des opérations courantes sur les principales collections.",
  [
    S("Quelle est la complexité moyenne de l'opération get(clé) sur une HashMap bien dimensionnée ?", "O(1) en moyenne", ["O(n) systématiquement", "O(log n) systématiquement", "O(n²)"]),
    S("Quelle est la complexité de l'accès par indice get(i) sur une ArrayList ?", "O(1)", ["O(n)", "O(log n)", "O(n log n)"]),
    S("Quelle est la complexité de l'insertion en tête d'une LinkedList ?", "O(1)", ["O(n)", "O(log n)", "Dépend de la taille de la liste"]),
    M("Lesquelles de ces affirmations sur la complexité des collections sont correctes ?", ["L'accès par indice sur une LinkedList est en O(n) dans le pire cas", "La recherche contains() sur une ArrayList non triée est en O(n)"], ["get() sur une HashMap est toujours en O(n)"]),
    M("Quelles opérations sont typiquement en O(log n) sur une TreeMap correctement équilibrée ?", ["get(clé)", "put(clé, valeur)"], ["L'itération complète qui reste en O(n)"]),
    TF("L'insertion en fin d'une ArrayList est généralement en O(1) amorti, sauf lors d'un redimensionnement interne.", true),
  ]
),
];
