import { S, M, TF, Quiz } from "./helpers.mjs";

export const part1 = [
Quiz(
  "Types primitifs : panorama complet",
  "Identifier les huit types primitifs de Java et leurs usages.",
  [
    S("Combien existe-t-il de types primitifs en Java ?", "8", ["6", "7", "9"]),
    S("Quel type primitif permet de stocker un seul caractère Unicode ?", "char", ["String", "byte", "int"]),
    S("Quel type primitif est utilisé pour représenter une valeur booléenne en Java ?", "boolean", ["bool", "bit", "flag"]),
    M("Lesquels des éléments suivants sont des types primitifs Java ?", ["int", "double", "boolean", "char"], ["String"]),
    M("Lesquels de ces types sont des types numériques entiers en Java ?", ["byte", "short", "long"], ["float", "boolean"]),
    TF("Le type String est un type primitif en Java.", false),
  ]
),
Quiz(
  "Déclaration et initialisation de variables",
  "Comprendre la syntaxe de déclaration de variables et les règles de nommage.",
  [
    S("Quelle déclaration de variable est syntaxiquement correcte en Java ?", "int age = 25;", ["int 25 = age;", "age int = 25", "25 = int age;"]),
    S("Quel mot réservé permet de déclarer une variable dont la valeur ne peut plus changer après son initialisation ?", "final", ["const", "static", "fixed"]),
    S("Parmi ces identifiants, lequel est un nom de variable valide en Java ?", "_total2", ["2total", "total-2", "class"]),
    M("Lesquels de ces identifiants de variable sont valides en Java ?", ["nom1", "_valeur", "$prix"], ["1nom", "for"]),
    M("Lesquelles de ces affirmations sur les variables locales en Java sont correctes ?", ["Elles doivent être initialisées avant leur première utilisation", "Leur portée est limitée au bloc dans lequel elles sont déclarées"], ["Elles ont toujours une valeur par défaut comme les champs d'instance"]),
    TF("En Java, les noms de variables sont sensibles à la casse (age et Age sont différents).", true),
  ]
),
Quiz(
  "Opérateurs arithmétiques et incrémentation",
  "Maîtriser les opérateurs arithmétiques de base et les opérateurs d'incrémentation/décrémentation.",
  [
    S("Quel est le résultat de l'expression entière 7 / 2 en Java ?", "3", ["3.5", "4", "3.0"]),
    S("Quel est le résultat de l'opération modulo 17 % 5 en Java ?", "2", ["3", "5", "0"]),
    S("Soit int x = 5; le résultat de x++ + ++x vaut :", "12", ["11", "10", "13"]),
    M("Lesquels de ces opérateurs sont des opérateurs arithmétiques en Java ?", ["+", "%", "*"], ["&&", "=="]),
    M("Quelles affirmations sur l'opérateur ++ en Java sont correctes ?", ["x++ retourne la valeur de x avant incrémentation", "++x incrémente x avant de retourner sa valeur"], ["x++ ne modifie jamais la variable x"]),
    TF("L'expression 7 / 2.0 en Java donne 3.5.", true),
  ]
),
Quiz(
  "Opérateurs de comparaison et logiques",
  "Distinguer les opérateurs relationnels et booléens, et leur évaluation court-circuit.",
  [
    S("Quel opérateur teste l'égalité de deux valeurs primitives en Java ?", "==", ["=", "equals", "==="]),
    S("Quel opérateur logique réalise un ET avec évaluation court-circuit ?", "&&", ["&", "||", "AND"]),
    S("Quelle est la valeur de l'expression (5 > 3) && (2 > 4) ?", "false", ["true", "5", "erreur de compilation"]),
    M("Lesquels de ces opérateurs retournent un résultat de type boolean ?", [">=", "!=", "instanceof"], ["+="]),
    M("Quelles affirmations sur l'opérateur || (OU logique court-circuit) sont vraies ?", ["Si l'opérande gauche est true, l'opérande droit n'est pas évalué", "Il retourne un boolean"], ["Il évalue toujours les deux opérandes"]),
    TF("L'opérateur & peut être utilisé comme opérateur logique ET sans court-circuit en Java.", true),
  ]
),
Quiz(
  "Structure conditionnelle if / else",
  "Construire des branchements conditionnels avec if, else if et else.",
  [
    S("Quelle structure permet d'exécuter un bloc de code uniquement si une condition est vraie ?", "if", ["switch", "for", "while"]),
    S("Dans une chaîne if / else if / else, combien de blocs peuvent être exécutés au maximum ?", "1", ["2", "Tous les blocs", "0"]),
    S("Quel est l'affichage produit par : int n = 10; if (n > 5) System.out.print(\"A\"); else System.out.print(\"B\");", "A", ["B", "AB", "Erreur de compilation"]),
    M("Lesquelles de ces affirmations sur le if en Java sont correctes ?", ["La condition entre parenthèses doit être de type boolean", "Le bloc else est optionnel"], ["Un if doit obligatoirement avoir un else"]),
    M("Quels types d'expressions peuvent être utilisés comme condition d'un if ?", ["Une variable boolean", "Le résultat d'une comparaison comme x > 0"], ["Un entier comme 5 directement"]),
    TF("En Java, on peut omettre les accolades autour d'un if si le bloc ne contient qu'une seule instruction.", true),
  ]
),
Quiz(
  "Structure switch et switch expressions",
  "Utiliser switch pour remplacer des chaînes de if / else if, y compris le fall-through.",
  [
    S("Quel mot-clé permet de sortir d'un bloc switch classique pour éviter le fall-through ?", "break", ["exit", "stop", "return;"]),
    S("Que se passe-t-il si on oublie un break dans un case d'un switch classique en Java ?", "L'exécution continue dans le case suivant (fall-through)", ["Une exception est levée", "Le programme ne compile pas", "Le switch s'arrête silencieusement"]),
    S("Quel type ne peut PAS être utilisé comme expression de sélection d'un switch classique en Java ?", "double", ["int", "String", "enum"]),
    M("Quelles affirmations sur le switch en Java sont correctes ?", ["Le bloc default est optionnel", "Plusieurs case peuvent partager le même bloc d'instructions"], ["Un switch ne peut comporter qu'un seul case"]),
    M("Quels types peuvent être utilisés dans l'expression d'un switch classique en Java ?", ["int", "String", "enum"], ["double", "boolean"]),
    TF("Dans un switch, le bloc default doit obligatoirement être placé en dernière position.", false),
  ]
),
Quiz(
  "Boucle for et parcours indexé",
  "Construire et analyser des boucles for classiques avec compteur.",
  [
    S("Quelle est la syntaxe correcte d'une boucle for affichant les nombres de 0 à 4 ?", "for (int i = 0; i < 5; i++) { System.out.println(i); }", ["for (int i = 0; i < 5; i--)", "for (i = 0; i < 5)", "for int i = 0 to 5"]),
    S("Combien de fois le bloc s'exécute-t-il dans : for (int i = 0; i < 3; i++) { }", "3", ["2", "4", "Une infinité de fois"]),
    S("Que produit ce code : for (int i = 5; i > 0; i--) { System.out.print(i); } ?", "54321", ["12345", "543210", "Erreur de compilation"]),
    M("Lesquels de ces éléments font partie de l'en-tête d'une boucle for classique ?", ["L'initialisation", "La condition d'arrêt", "L'instruction de mise à jour"], ["Le bloc finally"]),
    M("Quelles affirmations sur la boucle for sont correctes en Java ?", ["On peut déclarer plusieurs variables dans l'initialisation séparées par des virgules", "La condition est évaluée avant chaque itération"], ["La boucle for ne peut pas être imbriquée dans une autre boucle for"]),
    TF("Dans une boucle for, les trois parties de l'en-tête (initialisation, condition, mise à jour) sont toutes obligatoires.", false),
  ]
),
Quiz(
  "Boucles while et do-while",
  "Différencier les boucles à condition d'entrée et à condition de sortie.",
  [
    S("Quelle boucle garantit l'exécution du bloc au moins une fois, même si la condition est fausse dès le départ ?", "do-while", ["while", "for", "for-each"]),
    S("Que produit ce code : int i = 0; while (i < 3) { System.out.print(i); i++; } ?", "012", ["0123", "123", "Boucle infinie"]),
    S("Quel mot-clé permet d'interrompre immédiatement l'exécution d'une boucle while ?", "break", ["continue", "exit", "stop"]),
    M("Lesquelles de ces affirmations sur do-while sont correctes ?", ["La condition est testée après l'exécution du bloc", "Le bloc s'exécute au moins une fois"], ["La condition est testée avant chaque itération comme pour while"]),
    M("Quels mots-clés permettent de contrôler le flux à l'intérieur d'une boucle while ?", ["break", "continue"], ["case", "default"]),
    TF("Une boucle while dont la condition est toujours vraie crée une boucle infinie si rien ne l'interrompt.", true),
  ]
),
Quiz(
  "Mot-clé continue et contrôle de flux",
  "Comprendre l'effet de continue dans les boucles for et while.",
  [
    S("Quel est l'effet du mot-clé continue dans une boucle for ?", "Il passe directement à l'itération suivante", ["Il arrête définitivement la boucle", "Il relance le programme", "Il provoque une exception"]),
    S("Que produit ce code : for (int i = 0; i < 5; i++) { if (i == 2) continue; System.out.print(i); } ?", "0134", ["01234", "01", "012"]),
    S("Dans une boucle for, à quel moment continue déclenche-t-il l'instruction de mise à jour (i++) ?", "Immédiatement après l'appel à continue", ["Jamais", "Avant l'appel à continue", "Seulement si break est aussi présent"]),
    M("Lesquelles de ces affirmations sur continue sont correctes ?", ["continue peut être utilisé dans une boucle while", "continue ne termine pas la boucle entière"], ["continue est identique à break"]),
    M("Quels mots-clés peuvent être étiquetés (avec un label) pour cibler une boucle externe en Java ?", ["break", "continue"], ["return", "throw"]),
    TF("Le mot-clé continue, utilisé dans une boucle for, saute le reste du corps de la boucle pour l'itération en cours.", true),
  ]
),
Quiz(
  "Tableaux unidimensionnels en Java",
  "Déclarer, initialiser et parcourir un tableau simple.",
  [
    S("Quelle est la syntaxe correcte pour déclarer un tableau d'entiers en Java ?", "int[] tab = new int[5];", ["int tab[5];", "array<int> tab = new array(5);", "int tab = new int[5];"]),
    S("Quel est l'indice du premier élément d'un tableau en Java ?", "0", ["1", "-1", "Cela dépend du tableau"]),
    S("Quelle propriété permet de connaître la taille d'un tableau nommé tab en Java ?", "tab.length", ["tab.size()", "tab.count", "tab.length()"]),
    M("Lesquelles de ces déclarations de tableau sont valides en Java ?", ["int[] a = new int[3];", "int[] a = {1, 2, 3};"], ["int[] a = new int[]; "]),
    M("Quelles affirmations sur les tableaux Java sont correctes ?", ["La taille d'un tableau est fixée à sa création", "Les éléments d'un tableau d'int sont initialisés à 0 par défaut"], ["Un tableau Java peut changer de taille dynamiquement comme une ArrayList"]),
    TF("En Java, accéder à un indice hors limites d'un tableau provoque une ArrayIndexOutOfBoundsException.", true),
  ]
),
Quiz(
  "Tableaux multidimensionnels",
  "Manipuler des tableaux à deux dimensions et comprendre leur représentation interne.",
  [
    S("Comment déclare-t-on un tableau à deux dimensions de type int en Java ?", "int[][] grille = new int[3][4];", ["int[3][4] grille;", "int grille[][] = new int(3,4);", "int[2] grille = new int[3,4];"]),
    S("Comment accède-t-on à l'élément situé ligne 1, colonne 2 d'un tableau 2D nommé grille ?", "grille[1][2]", ["grille[1,2]", "grille(1)(2)", "grille.get(1,2)"]),
    S("En Java, un tableau à deux dimensions est en réalité implémenté comme :", "Un tableau de tableaux", ["Une matrice native du langage", "Une simple liste linéaire", "Un objet Matrix intégré"]),
    M("Lesquelles de ces affirmations sur les tableaux 2D Java sont correctes ?", ["Chaque ligne peut avoir une longueur différente (tableau irrégulier)", "grille.length donne le nombre de lignes"], ["Un tableau 2D doit obligatoirement être carré"]),
    M("Quelles expressions permettent de connaître les dimensions d'un tableau 2D nommé m ?", ["m.length", "m[0].length"], ["m.size()", "m.rows()"]),
    TF("En Java, il est possible de créer un tableau 2D dont les lignes ont des longueurs différentes.", true),
  ]
),
Quiz(
  "Parcours de tableaux avec for-each",
  "Utiliser la boucle for-each pour itérer sur des collections et tableaux.",
  [
    S("Quelle syntaxe correspond à une boucle for-each parcourant un tableau tab d'entiers ?", "for (int x : tab) { }", ["for (int x in tab) { }", "for (x : tab) { }", "foreach (x in tab) { }"]),
    S("Dans une boucle for-each, peut-on modifier la valeur d'un élément primitif du tableau via la variable de boucle ?", "Non, la variable est une copie locale", ["Oui, cela modifie directement le tableau", "Cela dépend du type du tableau", "Seulement avec un cast"]),
    S("Que produit ce code : int[] t = {1,2,3}; int s = 0; for (int x : t) { s += x; } System.out.print(s); ?", "6", ["3", "123", "0"]),
    M("Lesquelles de ces affirmations sur for-each sont correctes ?", ["for-each fonctionne sur les tableaux et les collections implémentant Iterable", "On ne peut pas connaître facilement l'indice courant dans un for-each simple"], ["for-each permet de modifier la taille du tableau pendant le parcours"]),
    M("Sur quels types de structures peut-on utiliser une boucle for-each en Java ?", ["Un tableau", "Une ArrayList", "Un HashSet"], ["Un entier simple"]),
    TF("La boucle for-each est aussi appelée boucle for étendue (enhanced for) en Java.", true),
  ]
),
Quiz(
  "Conversions de types : casting explicite",
  "Distinguer conversions implicites (widening) et explicites (narrowing) entre types primitifs.",
  [
    S("Quelle conversion nécessite un cast explicite car elle peut entraîner une perte de données ?", "double vers int", ["int vers double", "int vers long", "byte vers int"]),
    S("Quel est le résultat de l'expression : int x = (int) 3.99; ?", "3", ["4", "3.99", "Erreur de compilation"]),
    S("Quelle syntaxe permet de convertir explicitement un double d en int ?", "(int) d", ["int(d)", "d.toInt()", "cast<int>(d)"]),
    M("Lesquelles de ces conversions sont implicites (élargissantes) et ne nécessitent pas de cast en Java ?", ["int vers long", "int vers double", "float vers double"], ["double vers float"]),
    M("Lesquelles de ces affectations provoquent une erreur de compilation sans cast explicite ?", ["int i = 3.5;", "byte b = 300;"], ["long l = 100;", "double d = 5;"]),
    TF("La conversion d'un int vers un double en Java se fait automatiquement sans cast explicite.", true),
  ]
),
Quiz(
  "Dépassement de capacité et constantes numériques",
  "Comprendre l'overflow des entiers et les constantes limites des types numériques.",
  [
    S("Que se passe-t-il lorsqu'on ajoute 1 à un int valant Integer.MAX_VALUE en Java ?", "Il devient Integer.MIN_VALUE (dépassement par retour)", ["Une exception est levée", "Il reste à Integer.MAX_VALUE", "Il devient 0"]),
    S("Que vaut Integer.MAX_VALUE en Java ?", "2147483647", ["2147483648", "65535", "4294967295"]),
    S("Quelle classe utilitaire fournit la constante MAX_VALUE pour le type int ?", "Integer", ["Int", "Number", "Math"]),
    M("Lesquelles de ces affirmations sur le dépassement de capacité (overflow) des entiers en Java sont correctes ?", ["Il ne lève aucune exception par défaut", "La valeur boucle de manière circulaire", "Math.addExact peut le détecter en levant une exception"], ["Il provoque toujours un arrêt du programme"]),
    M("Quelles classes wrapper exposent des constantes MIN_VALUE et MAX_VALUE en Java ?", ["Integer", "Long", "Double"], ["Math"]),
    TF("En Java, le modulo d'un nombre négatif comme -7 % 3 donne -1.", true),
  ]
),
Quiz(
  "Précédence et associativité des opérateurs",
  "Évaluer correctement des expressions combinant plusieurs opérateurs.",
  [
    S("Quel est le résultat de l'expression 2 + 3 * 4 en Java ?", "14", ["20", "9", "24"]),
    S("Quel est le résultat de l'expression (2 + 3) * 4 en Java ?", "20", ["14", "9", "11"]),
    S("Dans l'expression a = b = 5, quel est l'ordre d'évaluation de l'opérateur d'affectation = ?", "De droite à gauche", ["De gauche à droite", "Cela dépend du compilateur", "Indéfini"]),
    M("Lesquelles de ces affirmations sur la précédence des opérateurs Java sont correctes ?", ["La multiplication a une priorité plus élevée que l'addition", "Les parenthèses permettent de forcer un ordre d'évaluation"], ["Tous les opérateurs ont la même priorité"]),
    M("Parmi ces opérateurs, lesquels ont une priorité plus élevée que l'opérateur + (addition) ?", ["*", "/", "%"], ["=", "||"]),
    TF("L'opérateur ternaire ?: a une priorité plus faible que les opérateurs de comparaison comme >.", true),
  ]
),
Quiz(
  "Opérateur ternaire et instanceof",
  "Utiliser l'opérateur conditionnel ternaire et l'opérateur instanceof.",
  [
    S("Quelle est la syntaxe de l'opérateur ternaire en Java ?", "condition ? valeurSiVrai : valeurSiFaux", ["condition then a else b", "if condition a else b", "condition => a : b"]),
    S("Que renvoie l'expression : int max = (5 > 3) ? 5 : 3; ?", "5", ["3", "true", "Erreur de compilation"]),
    S("Quel opérateur permet de tester si un objet est une instance d'une classe donnée ?", "instanceof", ["typeof", "isInstanceOf", "is"]),
    M("Lesquelles de ces affirmations sur l'opérateur ternaire sont correctes ?", ["Il peut remplacer un if/else simple retournant une valeur", "Il peut être imbriqué dans une autre expression ternaire"], ["Il ne peut être utilisé qu'avec des booléens comme résultat"]),
    M("Quelles affirmations sur instanceof sont correctes en Java ?", ["Il retourne un boolean", "Il peut être utilisé pour vérifier qu'un objet appartient à une sous-classe"], ["Il ne fonctionne qu'avec les types primitifs"]),
    TF("L'expression null instanceof String retourne false en Java.", true),
  ]
),
Quiz(
  "Chaînes de caractères : bases et concatenation",
  "Manipuler la classe String et comprendre la concatenation.",
  [
    S("Quel opérateur permet de concaténer deux chaînes en Java ?", "+", ["&", ".", "++"]),
    S("Quelle méthode de la classe String retourne le nombre de caractères d'une chaîne ?", "length()", ["size()", "count()", "len()"]),
    S("Que produit ce code : String s = \"Bonjour\" + \" \" + \"monde\"; System.out.print(s); ?", "Bonjour monde", ["BonjourMonde", "Bonjour+monde", "Erreur de compilation"]),
    M("Lesquelles de ces méthodes existent sur la classe String en Java ?", ["length()", "toUpperCase()", "substring(int)"], ["push()"]),
    M("Quelles affirmations sur la concatenation de chaînes en Java sont correctes ?", ["L'opérateur + peut concaténer une String et un int", "La concaténation répétée avec + dans une boucle est moins performante que StringBuilder"], ["La concaténation modifie la chaîne d'origine en place"]),
    TF("En Java, la méthode String.length() retourne un int.", true),
  ]
),
Quiz(
  "Immuabilité de la classe String",
  "Comprendre pourquoi les objets String sont immuables et leurs conséquences.",
  [
    S("Qu'est-ce qui caractérise l'immuabilité des objets String en Java ?", "Une fois créé, le contenu d'un objet String ne peut plus être modifié", ["On ne peut créer qu'une seule chaîne par programme", "Les String ne peuvent pas être comparées", "Les String sont stockées uniquement sur la pile"]),
    S("Que se passe-t-il en mémoire quand on exécute : String s = \"a\"; s = s + \"b\"; ?", "Un nouvel objet String est créé, l'ancien reste inchangé", ["L'objet original \"a\" est modifié pour devenir \"ab\"", "Une erreur de compilation se produit", "Rien, l'opération est ignorée"]),
    S("Quelle structure mémoire spéciale permet de réutiliser les littéraux String identiques en Java ?", "Le String pool", ["Le tas (heap) classique uniquement", "Le garbage collector", "Le cache CPU"]),
    M("Lesquelles de ces affirmations sur l'immuabilité de String sont correctes ?", ["Elle rend les String naturellement thread-safe", "Elle permet la réutilisation sécurisée via le String pool"], ["Elle empêche toute concaténation de chaînes"]),
    M("Quelles classes mutables permettent de construire des chaînes efficacement sans créer de nombreux objets intermédiaires ?", ["StringBuilder", "StringBuffer"], ["String"]),
    TF("Les objets String en Java sont immuables : leur contenu ne peut pas être modifié après création.", true),
  ]
),
Quiz(
  "Méthodes courantes de String",
  "Explorer les méthodes essentielles de manipulation de chaînes.",
  [
    S("Quelle méthode permet d'extraire une sous-chaîne entre deux indices ?", "substring(int, int)", ["extract(int, int)", "slice(int, int)", "part(int, int)"]),
    S("Quelle méthode compare deux chaînes en ignorant la casse ?", "equalsIgnoreCase(String)", ["equals(String)", "compareTo(String)", "matches(String)"]),
    S("Que retourne \"Bonjour\".indexOf(\"jour\") ?", "3", ["4", "-1", "0"]),
    M("Lesquelles de ces méthodes de String renvoient un boolean ?", ["isEmpty()", "startsWith(String)", "contains(CharSequence)"], ["length()"]),
    M("Quelles méthodes permettent de transformer la casse d'une chaîne en Java ?", ["toUpperCase()", "toLowerCase()"], ["trim()"]),
    TF("La méthode trim() d'une String retourne une nouvelle chaîne sans espaces de début et de fin.", true),
  ]
),
Quiz(
  "StringBuilder et performance",
  "Comprendre l'intérêt de StringBuilder pour la construction efficace de chaînes.",
  [
    S("Pourquoi préfère-t-on StringBuilder à la concatenation par + dans une boucle avec de nombreuses itérations ?", "Parce que StringBuilder évite de créer de multiples objets String intermédiaires", ["Parce que + ne fonctionne pas dans les boucles", "Parce que StringBuilder est immuable", "Parce que + ne peut concaténer que des nombres"]),
    S("Quelle méthode de StringBuilder permet d'ajouter du texte à la fin ?", "append(String)", ["add(String)", "concat(String)", "push(String)"]),
    S("Quelle méthode convertit un StringBuilder en objet String ?", "toString()", ["build()", "toStr()", "convert()"]),
    M("Lesquelles de ces affirmations sur StringBuilder sont correctes ?", ["StringBuilder est mutable", "append() retourne le StringBuilder lui-même pour permettre le chaînage"], ["StringBuilder est immuable comme String"]),
    M("Quelles méthodes sont disponibles sur StringBuilder en Java ?", ["append(String)", "reverse()", "insert(int, String)"], ["concatAll()"]),
    TF("StringBuilder n'est pas synchronisé pour la concurrence, contrairement à StringBuffer.", true),
  ]
),
];
