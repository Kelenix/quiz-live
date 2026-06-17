import { S, M, TF, Quiz } from "./helpers.mjs";

export const part2 = [
Quiz(
  "Classes et objets : fondamentaux",
  "Découvrir la notion de classe, d'objet et leur instanciation en Java.",
  [
    S("Quel mot-clé est utilisé pour créer une nouvelle instance d'une classe en Java ?", "new", ["create", "instance", "make"]),
    S("Comment appelle-t-on une instance concrète d'une classe en Java ?", "Un objet", ["Une méthode", "Un paquet", "Une interface"]),
    S("Quel élément d'une classe sert à initialiser un objet au moment de sa création ?", "Le constructeur", ["Le destructeur", "Le getter", "Le finaliseur"]),
    M("Quels éléments peut contenir une classe Java classique ?", ["Des champs (attributs)", "Des méthodes", "Des constructeurs"], ["Des balises HTML"]),
    M("Quelles affirmations décrivent correctement la relation entre une classe et un objet ?", ["Une classe est un modèle (plan) pour créer des objets", "On peut créer plusieurs objets à partir d'une même classe"], ["Une classe est toujours une instance d'un objet"]),
    TF("En Java, on peut créer plusieurs objets indépendants à partir d'une même classe.", true),
  ]
),
Quiz(
  "Constructeurs : par défaut et surchargés",
  "Comprendre les constructeurs implicites, explicites et leur surcharge.",
  [
    S("Que fournit automatiquement le compilateur Java si aucun constructeur n'est défini dans une classe ?", "Un constructeur par défaut sans argument", ["Une erreur de compilation", "Un constructeur avec tous les champs en paramètre", "Rien du tout"]),
    S("Quel mot-clé permet d'appeler un autre constructeur de la même classe depuis un constructeur ?", "this(...)", ["super(...)", "self(...)", "new(...)"]),
    S("Que se passe-t-il si une classe définit un constructeur avec paramètres et qu'on essaie d'appeler new MaClasse() sans le redéfinir explicitement ?", "Erreur de compilation, car le constructeur par défaut n'est plus généré", ["Le constructeur par défaut est tout de même disponible", "Java crée un objet avec des valeurs nulles", "Une exception est levée à l'exécution"]),
    M("Lesquelles de ces affirmations sur les constructeurs Java sont correctes ?", ["Un constructeur porte le même nom que la classe", "Une classe peut avoir plusieurs constructeurs surchargés"], ["Un constructeur peut avoir un type de retour comme void"]),
    M("Quelles règles s'appliquent à l'appel this(...) dans un constructeur ?", ["Il doit être la première instruction du constructeur", "Il permet de réutiliser la logique d'un autre constructeur"], ["Il peut être appelé à n'importe quel endroit du constructeur"]),
    TF("En Java, un constructeur peut avoir le même nom que sa classe mais ne possède pas de type de retour, pas même void.", true),
  ]
),
Quiz(
  "Encapsulation et modificateurs d'accès",
  "Maîtriser private, protected, public et package-private.",
  [
    S("Quel modificateur d'accès rend un membre visible uniquement à l'intérieur de sa propre classe ?", "private", ["protected", "public", "default (package-private)"]),
    S("Quel modificateur d'accès permet l'accès depuis le même package ET les sous-classes, même dans un autre package ?", "protected", ["private", "public", "package-private"]),
    S("Quelle est la pratique recommandée pour exposer en lecture/écriture un champ privé d'une classe ?", "Utiliser des méthodes getter et setter publiques", ["Rendre le champ public directement", "Utiliser un champ static", "Créer une sous-classe"]),
    M("Lesquels de ces modificateurs d'accès existent en Java pour les membres d'une classe ?", ["private", "protected", "public"], ["internal"]),
    M("Quelles affirmations sur l'encapsulation en Java sont correctes ?", ["Elle consiste à cacher les détails internes d'une classe", "Elle facilite la maintenance en limitant les dépendances externes"], ["Elle interdit toute méthode publique dans une classe"]),
    TF("Un champ déclaré sans modificateur d'accès explicite a une visibilité dite package-private.", true),
  ]
),
Quiz(
  "Héritage : extends et super",
  "Comprendre les mécanismes de base de l'héritage entre classes.",
  [
    S("Quel mot-clé permet à une classe d'hériter d'une autre classe en Java ?", "extends", ["implements", "inherits", "extend"]),
    S("Quel mot-clé permet d'appeler le constructeur de la classe parente depuis une sous-classe ?", "super(...)", ["this(...)", "parent(...)", "base(...)"]),
    S("Combien de classes une classe Java peut-elle étendre directement (héritage simple) ?", "1", ["2", "Autant qu'elle veut", "0"]),
    M("Lesquelles de ces affirmations sur l'héritage en Java sont correctes ?", ["Une sous-classe hérite des membres publics et protégés de sa super-classe", "Java ne supporte pas l'héritage multiple de classes"], ["Une classe peut étendre plusieurs classes à la fois"]),
    M("Quelles affirmations sur le mot-clé super sont correctes ?", ["super() doit être la première instruction du constructeur s'il est utilisé", "super.methode() permet d'appeler la version de la méthode définie dans la classe parente"], ["super fait référence à la sous-classe courante"]),
    TF("En Java, toute classe hérite implicitement de la classe Object si elle n'étend explicitement aucune autre classe.", true),
  ]
),
Quiz(
  "Polymorphisme et liaison dynamique",
  "Comprendre comment le polymorphisme s'exprime via la redéfinition de méthodes.",
  [
    S("Qu'est-ce que le polymorphisme en programmation orientée objet ?", "La capacité d'un objet à prendre plusieurs formes selon son type réel à l'exécution", ["La capacité de dupliquer une classe", "Le fait qu'une classe ne puisse avoir qu'une seule méthode", "Le fait d'avoir plusieurs constructeurs"]),
    S("Quand une référence de type Animal pointe vers un objet Chien, quelle version de la méthode crier() est appelée si elle est redéfinie dans Chien ?", "La version définie dans Chien", ["La version définie dans Animal", "Une erreur de compilation se produit", "Aucune méthode n'est appelée"]),
    S("Quel terme désigne le mécanisme par lequel la méthode réellement exécutée est déterminée à l'exécution selon le type réel de l'objet ?", "La liaison dynamique (late binding)", ["La liaison statique", "La surcharge", "L'encapsulation"]),
    M("Lesquelles de ces affirmations sur le polymorphisme en Java sont correctes ?", ["Il permet de traiter des objets de sous-classes différentes via une référence de type parent", "Il repose souvent sur la redéfinition de méthodes (overriding)"], ["Il interdit l'utilisation de l'héritage"]),
    M("Quelles conditions favorisent le polymorphisme en Java ?", ["Une méthode redéfinie dans une sous-classe avec @Override", "Une référence typée avec la classe parente ou une interface"], ["Une méthode déclarée static dans la sous-classe"]),
    TF("Le polymorphisme permet d'appeler une méthode redéfinie sans connaître le type exact de l'objet au moment de la compilation.", true),
  ]
),
Quiz(
  "Surcharge vs redéfinition (overloading vs overriding)",
  "Distinguer clairement la surcharge de méthodes et leur redéfinition dans une sous-classe.",
  [
    S("Comment appelle-t-on le fait de définir plusieurs méthodes de même nom mais avec des paramètres différents dans une même classe ?", "La surcharge (overloading)", ["La redéfinition (overriding)", "L'encapsulation", "L'instanciation"]),
    S("Comment appelle-t-on le fait qu'une sous-classe fournisse une nouvelle implémentation d'une méthode héritée avec la même signature ?", "La redéfinition (overriding)", ["La surcharge (overloading)", "La généricité", "La sérialisation"]),
    S("Quelle annotation permet d'indiquer explicitement qu'une méthode redéfinit une méthode de la classe parente ?", "@Override", ["@Overload", "@Inherited", "@Redefine"]),
    M("Lesquelles de ces affirmations sur la surcharge (overloading) sont correctes ?", ["Les méthodes surchargées ont le même nom", "Les méthodes surchargées doivent différer par le nombre ou le type de leurs paramètres"], ["Le type de retour seul suffit à distinguer deux méthodes surchargées"]),
    M("Lesquelles de ces affirmations sur la redéfinition (overriding) sont correctes ?", ["La méthode redéfinie doit avoir la même signature que la méthode parente", "Elle est résolue à l'exécution (liaison dynamique)"], ["Elle est résolue uniquement à la compilation"]),
    TF("La surcharge de méthodes (overloading) est résolue à la compilation, contrairement à la redéfinition.", true),
  ]
),
Quiz(
  "Interfaces : contrats et implémentation",
  "Comprendre le rôle des interfaces et le mot-clé implements.",
  [
    S("Quel mot-clé permet à une classe d'implémenter une interface en Java ?", "implements", ["extends", "interface", "uses"]),
    S("Avant Java 8, quel type de méthode une interface pouvait-elle contenir ?", "Des méthodes abstraites uniquement (sans corps)", ["Des méthodes avec corps uniquement", "Des constructeurs", "Des champs d'instance mutables"]),
    S("Combien d'interfaces une classe Java peut-elle implémenter ?", "Plusieurs, sans limite", ["Une seule", "Aucune", "Deux maximum"]),
    M("Lesquelles de ces affirmations sur les interfaces Java sont correctes ?", ["Une interface peut être utilisée comme type de référence", "Une interface ne peut pas être instanciée directement"], ["Une interface peut hériter d'une classe concrète"]),
    M("Depuis Java 8, quels types de méthodes une interface peut-elle contenir ?", ["Des méthodes default avec un corps", "Des méthodes static"], ["Des constructeurs"]),
    TF("Tous les champs déclarés dans une interface Java sont implicitement public, static et final.", true),
  ]
),
Quiz(
  "Classes abstraites",
  "Comprendre le rôle des classes abstraites comme base partielle d'implémentation.",
  [
    S("Quel mot-clé permet de déclarer une classe abstraite en Java ?", "abstract", ["interface", "virtual", "sealed"]),
    S("Peut-on instancier directement une classe abstraite avec new ?", "Non, c'est interdit par le compilateur", ["Oui, sans restriction", "Oui, mais seulement si elle a un constructeur public", "Cela dépend du nombre de méthodes abstraites"]),
    S("Qu'est-ce qui distingue une méthode abstraite d'une méthode concrète dans une classe abstraite ?", "Une méthode abstraite n'a pas de corps et doit être implémentée par les sous-classes", ["Une méthode abstraite ne peut pas être publique", "Une méthode abstraite ne peut pas avoir de paramètres", "Une méthode abstraite est toujours static"]),
    M("Lesquelles de ces affirmations sur les classes abstraites sont correctes ?", ["Elles peuvent contenir des méthodes concrètes et des méthodes abstraites", "Une sous-classe concrète doit implémenter toutes les méthodes abstraites héritées"], ["Elles peuvent être instanciées directement comme une classe normale"]),
    M("Quelles différences existent entre une classe abstraite et une interface en Java ?", ["Une classe abstraite peut avoir des champs d'instance avec état", "Une classe ne peut étendre qu'une seule classe abstraite"], ["Une interface peut avoir des constructeurs"]),
    TF("Une classe abstraite peut contenir des constructeurs, même si elle ne peut pas être instanciée directement.", true),
  ]
),
Quiz(
  "Mot-clé final : variables, méthodes, classes",
  "Comprendre les trois usages du mot-clé final en Java.",
  [
    S("Quel est l'effet du mot-clé final appliqué à une variable ?", "Sa valeur ne peut plus être réassignée après initialisation", ["Elle devient automatiquement statique", "Elle ne peut plus être lue", "Elle devient privée"]),
    S("Quel est l'effet du mot-clé final appliqué à une méthode ?", "Elle ne peut plus être redéfinie par une sous-classe", ["Elle ne peut plus être appelée", "Elle devient abstraite", "Elle devient statique"]),
    S("Quel est l'effet du mot-clé final appliqué à une classe ?", "Elle ne peut plus être étendue (aucune sous-classe possible)", ["Elle devient abstraite", "Elle ne peut plus avoir de constructeur", "Elle devient une interface"]),
    M("Lesquelles de ces affirmations sur final sont correctes en Java ?", ["Une classe final ne peut pas être héritée", "Une méthode final ne peut pas être redéfinie"], ["Une variable final peut être réassignée plusieurs fois"]),
    M("Sur quels éléments le mot-clé final peut-il être appliqué en Java ?", ["Une variable locale", "Une méthode", "Une classe"], ["Un package"]),
    TF("La classe String est déclarée final en Java, ce qui empêche de l'étendre.", true),
  ]
),
Quiz(
  "Classes internes (notions)",
  "Découvrir les classes membres, locales, anonymes et statiques imbriquées.",
  [
    S("Comment appelle-t-on une classe définie à l'intérieur d'une autre classe en Java ?", "Une classe interne (nested class)", ["Une classe enfant", "Une classe jumelle", "Une classe satellite"]),
    S("Quelle différence existe entre une classe interne non-statique et une classe imbriquée statique ?", "La classe interne non-statique garde une référence implicite vers l'instance englobante", ["La classe imbriquée statique ne peut pas avoir de méthodes", "La classe interne non-statique ne peut pas avoir de champs", "Il n'y a aucune différence"]),
    S("Quel terme désigne une classe interne sans nom, souvent utilisée pour implémenter rapidement une interface ?", "Une classe anonyme", ["Une classe abstraite", "Une classe scellée", "Une classe générique"]),
    M("Lesquelles de ces affirmations sur les classes internes sont correctes ?", ["Une classe interne peut accéder aux membres privés de la classe englobante", "Une classe imbriquée statique n'a pas de référence implicite vers une instance englobante"], ["Une classe interne ne peut jamais accéder aux membres de la classe englobante"]),
    M("Quels types de classes internes existent en Java ?", ["Classe membre (non statique)", "Classe statique imbriquée", "Classe anonyme"], ["Classe globale"]),
    TF("Une classe interne statique (static nested class) ne possède pas de référence implicite vers une instance de la classe englobante.", true),
  ]
),
Quiz(
  "Le mot-clé static : champs et méthodes",
  "Comprendre la portée et l'usage des membres statiques d'une classe.",
  [
    S("Un champ déclaré static appartient à :", "La classe elle-même, partagé par toutes les instances", ["Chaque instance individuellement", "Aucune instance, il est inaccessible", "Une seule instance choisie aléatoirement"]),
    S("Peut-on appeler une méthode static directement via le nom de la classe, sans créer d'instance ?", "Oui, c'est l'usage typique d'une méthode statique", ["Non, il faut toujours une instance", "Seulement si la classe est abstraite", "Seulement dans la méthode main"]),
    S("Une méthode static peut-elle accéder directement à un champ d'instance non-statique ?", "Non, sans référence explicite à un objet", ["Oui, sans aucune restriction", "Oui, mais uniquement en lecture", "Cela dépend du modificateur d'accès"]),
    M("Lesquelles de ces affirmations sur static sont correctes en Java ?", ["Un champ static est partagé entre toutes les instances de la classe", "La méthode main est déclarée static"], ["Un membre static appartient à chaque instance séparément"]),
    M("Quels éléments peuvent être déclarés static en Java ?", ["Un champ", "Une méthode", "Un bloc d'initialisation"], ["Un constructeur"]),
    TF("Un bloc d'initialisation statique (static { ... }) s'exécute une seule fois, au chargement de la classe.", true),
  ]
),
Quiz(
  "Méthode equals() et égalité d'objets",
  "Comprendre la différence entre == et equals() pour les objets.",
  [
    S("Quel opérateur compare les références mémoire de deux objets en Java, et non leur contenu ?", "==", ["equals()", "compareTo()", "same()"]),
    S("Que retourne par défaut la méthode equals() héritée de la classe Object si elle n'est pas redéfinie ?", "Le résultat équivalent à une comparaison de références (==)", ["true systématiquement", "false systématiquement", "Une exception"]),
    S("Pourquoi redéfinit-on souvent equals() dans une classe métier comme Personne ?", "Pour comparer deux objets sur la base de leurs attributs plutôt que leur référence", ["Pour empêcher toute comparaison", "Pour rendre la classe abstraite", "Pour la rendre sérialisable"]),
    M("Lesquelles de ces affirmations sur equals() et == sont correctes en Java ?", ["== compare les références pour les types objets", "equals() peut être redéfini pour comparer le contenu logique de deux objets"], ["equals() compare toujours les références mémoire, comme =="]),
    M("Quelles bonnes pratiques s'appliquent à la redéfinition de equals() ?", ["Elle doit être cohérente avec hashCode()", "Elle doit gérer le cas où l'objet comparé est null"], ["Elle doit toujours retourner true pour simplifier le code"]),
    TF("Pour les objets de type String, equals() compare le contenu des chaînes, pas leur référence mémoire.", true),
  ]
),
Quiz(
  "Contrat hashCode() et collections basées sur le hachage",
  "Comprendre le lien entre equals() et hashCode() pour HashMap et HashSet.",
  [
    S("Que doit-on garantir si deux objets sont égaux selon equals() ?", "Ils doivent avoir le même hashCode()", ["Ils doivent avoir des hashCode() différents", "Ils doivent être de classes différentes", "Rien n'est garanti"]),
    S("Que se passe-t-il si on redéfinit equals() sans redéfinir hashCode() et qu'on utilise l'objet comme clé d'un HashMap ?", "Le comportement de la collection peut devenir incohérent (objets égaux non retrouvés)", ["Aucun problème, Java gère cela automatiquement", "Une exception de compilation est levée", "Le programme refuse de démarrer"]),
    S("Quelle méthode de la classe Object retourne un entier représentant l'objet pour les structures de hachage ?", "hashCode()", ["toString()", "equals()", "getClass()"]),
    M("Lesquelles de ces affirmations sur le contrat equals()/hashCode() sont correctes ?", ["Deux objets égaux doivent retourner le même hashCode()", "Deux objets avec le même hashCode() ne sont pas forcément égaux"], ["Deux objets différents doivent obligatoirement avoir des hashCode() différents"]),
    M("Quelles collections Java utilisent le hashCode() pour organiser efficacement leurs éléments ?", ["HashMap", "HashSet"], ["ArrayList", "LinkedList"]),
    TF("Si deux objets sont égaux selon equals(), ils doivent obligatoirement avoir le même hashCode().", true),
  ]
),
Quiz(
  "Immuabilité des objets et objets final",
  "Concevoir des classes immuables robustes en Java.",
  [
    S("Quelle est la première condition pour rendre une classe immuable en Java ?", "Déclarer tous ses champs final et ne pas fournir de setters", ["Déclarer la classe abstract", "Implémenter Serializable", "Utiliser uniquement des types primitifs"]),
    S("Pourquoi déclare-t-on souvent une classe immuable comme final elle-même ?", "Pour empêcher une sous-classe de la rendre mutable en redéfinissant son comportement", ["Pour permettre l'héritage multiple", "Pour activer l'autoboxing", "Pour réduire la taille mémoire de l'objet"]),
    S("Si une classe immuable contient un champ de type tableau, quelle précaution doit-on prendre dans le constructeur ?", "Copier le tableau (copie défensive) plutôt que de garder la référence reçue", ["Rendre le tableau public", "Le déclarer static", "Ne rien faire de spécial"]),
    M("Lesquelles de ces caractéristiques favorisent l'immuabilité d'une classe en Java ?", ["Tous les champs sont final", "Aucune méthode ne modifie l'état interne après construction"], ["La classe expose des setters publics pour chaque champ"]),
    M("Quels avantages procure l'immuabilité d'un objet en programmation concurrente ?", ["Elle élimine les problèmes de modification concurrente de l'état", "Elle simplifie le partage sûr entre threads"], ["Elle empêche toute lecture de l'objet"]),
    TF("La classe String est un exemple classique d'objet immuable en Java.", true),
  ]
),
Quiz(
  "Packages et imports",
  "Organiser le code en packages et utiliser correctement les imports.",
  [
    S("Quel mot-clé déclare le package auquel appartient une classe Java, en première ligne du fichier ?", "package", ["namespace", "module", "using"]),
    S("Quel mot-clé permet d'utiliser une classe d'un autre package sans préciser son nom complet à chaque usage ?", "import", ["include", "require", "using"]),
    S("Quel package Java est importé implicitement dans toutes les classes, sans instruction import explicite ?", "java.lang", ["java.util", "java.io", "java.net"]),
    M("Lesquelles de ces affirmations sur les packages Java sont correctes ?", ["Un package correspond généralement à une arborescence de répertoires", "On peut importer toutes les classes d'un package avec une étoile (import java.util.*;)"], ["Un fichier Java ne peut appartenir à aucun package"]),
    M("Quelles affirmations sur les imports en Java sont correctes ?", ["import static permet d'importer des membres statiques directement", "Les imports n'affectent pas la taille du bytecode généré"], ["On doit importer java.lang.String explicitement pour l'utiliser"]),
    TF("Le package java.lang, contenant des classes comme String et Math, est importé automatiquement dans tout fichier Java.", true),
  ]
),
Quiz(
  "Enums : types énumérés",
  "Définir et utiliser des constantes énumérées typées en Java.",
  [
    S("Quel mot-clé permet de définir un type énuméré en Java ?", "enum", ["enumeration", "const", "type"]),
    S("Quelle méthode implicite d'un enum retourne le tableau de toutes ses constantes ?", "values()", ["list()", "all()", "elements()"]),
    S("Quelle méthode implicite d'un enum retourne sa position (index) dans la déclaration ?", "ordinal()", ["index()", "position()", "rank()"]),
    M("Lesquelles de ces affirmations sur les enums Java sont correctes ?", ["Un enum peut avoir des champs et des méthodes comme une classe", "Un enum peut être utilisé dans un switch"], ["Un enum peut être instancié avec new depuis l'extérieur"]),
    M("Quelles méthodes sont automatiquement disponibles sur un type enum en Java ?", ["values()", "name()", "ordinal()"], ["push()"]),
    TF("Chaque constante d'un enum Java est en réalité une instance unique (singleton) de ce type.", true),
  ]
),
Quiz(
  "Génériques : classes et méthodes paramétrées",
  "Comprendre l'intérêt des génériques pour la sécurité de type.",
  [
    S("Quelle syntaxe déclare une classe générique paramétrée par un type T ?", "class Boite<T> { }", ["class Boite(T) { }", "class Boite[T] { }", "class Boite<<T>> { }"]),
    S("Quel est le principal avantage des génériques introduits en Java 5 ?", "Détecter les erreurs de type à la compilation plutôt qu'à l'exécution", ["Accélérer l'exécution du programme", "Réduire la taille du bytecode", "Permettre l'héritage multiple"]),
    S("Quel terme désigne le mécanisme par lequel le compilateur Java remplace les types génériques par Object en bytecode ?", "L'effacement de type (type erasure)", ["Le boxing", "La réflexion", "L'autoboxing"]),
    M("Lesquelles de ces déclarations utilisent correctement des génériques en Java ?", ["List<String> liste = new ArrayList<>();", "Map<String, Integer> map = new HashMap<>();"], ["List<int> liste = new ArrayList<int>();"]),
    M("Quelles affirmations sur les génériques Java sont correctes ?", ["Ils permettent d'éviter des casts explicites lors de la récupération d'éléments", "Ils ne fonctionnent qu'avec des types référence, pas des primitifs"], ["Ils permettent de créer un tableau générique avec new T[10] directement"]),
    TF("On ne peut pas utiliser un type primitif comme int directement comme paramètre générique ; il faut utiliser le type wrapper Integer.", true),
  ]
),
Quiz(
  "Autoboxing et unboxing",
  "Comprendre la conversion automatique entre types primitifs et classes wrapper.",
  [
    S("Comment appelle-t-on la conversion automatique d'un type primitif comme int vers son équivalent objet Integer ?", "L'autoboxing", ["Le casting", "L'unboxing", "La sérialisation"]),
    S("Comment appelle-t-on la conversion automatique d'un objet Integer vers le type primitif int ?", "L'unboxing", ["L'autoboxing", "Le wrapping", "Le parsing"]),
    S("Quelle classe wrapper correspond au type primitif boolean en Java ?", "Boolean", ["Bool", "Bit", "Flag"]),
    M("Lesquelles de ces affirmations sur l'autoboxing sont correctes ?", ["Integer i = 5; déclenche un autoboxing implicite", "L'autoboxing peut provoquer une légère perte de performance par rapport aux primitifs"], ["L'autoboxing empêche toute utilisation de int dans une collection générique"]),
    M("Quelles classes sont des wrappers de types primitifs en Java ?", ["Integer", "Double", "Character"], ["String"]),
    TF("Comparer deux objets Integer avec == peut donner un résultat inattendu en dehors du cache des petites valeurs (-128 à 127).", true),
  ]
),
];
