# -*- coding: utf-8 -*-
import json, sys, re

def Q(statement, type_, answers, time_limit=None):
    if time_limit is None:
        time_limit = {"single": 20, "truefalse": 15, "multiple": 30}[type_]
    return {
        "statement": statement,
        "type": type_,
        "time_limit": time_limit,
        "answers": answers,
    }

def A(text, correct=False):
    return {"text": text, "is_correct": correct}

def TF(statement, correct_is_true):
    return Q(statement, "truefalse", [
        A("Vrai", correct_is_true),
        A("Faux", not correct_is_true),
    ])

quizzes = []

def add(title, description, questions):
    assert len(questions) == 6, f"{title}: {len(questions)} questions"
    types = [q["type"] for q in questions]
    for t in ("single", "multiple", "truefalse"):
        assert t in types, f"{title}: missing type {t}"
    quizzes.append({"title": title, "description": description, "questions": questions})


# ===================== BLOC 1 : SYNTAXE & VARIABLES (quiz 1-10) =====================

add("Syntaxe Python : les fondamentaux", "Découvrir les bases de la syntaxe et de l'indentation en Python.", [
    Q("Comment Python délimite-t-il les blocs de code (corps d'une fonction, d'un if, etc.) ?", "single", [
        A("Avec des accolades { }"),
        A("Avec l'indentation", True),
        A("Avec des mots-clés begin/end"),
        A("Avec des points-virgules"),
    ]),
    Q("Quel symbole introduit un commentaire sur une seule ligne en Python ?", "single", [
        A("//"),
        A("#", True),
        A("--"),
        A("<!--"),
    ]),
    Q("Quelle instruction permet d'afficher du texte dans la console en Python 3 ?", "single", [
        A("echo()"),
        A("print()", True),
        A("console.log()"),
        A("printf()"),
    ]),
    Q("Parmi ces extensions de fichier, lesquelles sont valides pour un script Python ?", "multiple", [
        A(".py", True),
        A(".pyw", True),
        A(".pyc", True),
        A(".pj"),
    ]),
    TF("En Python, il est obligatoire de terminer chaque instruction par un point-virgule.", False),
    TF("Python est sensible à la casse : la variable Age et la variable age sont différentes.", True),
])

add("Variables et affectation en Python", "Comprendre comment déclarer et affecter des variables.", [
    Q("Quelle ligne crée correctement une variable nommée score avec la valeur 10 ?", "single", [
        A("score = 10", True),
        A("int score = 10"),
        A("var score = 10"),
        A("score := 10;"),
    ]),
    Q("Que fait l'instruction `a, b = b, a` si a=1 et b=2 ?", "single", [
        A("Elle provoque une erreur de syntaxe"),
        A("Elle échange les valeurs de a et b", True),
        A("Elle additionne a et b"),
        A("Elle ne fait rien"),
    ]),
    Q("Quel mot-clé est nécessaire pour déclarer le type d'une variable avant de l'utiliser en Python ?", "single", [
        A("var"),
        A("let"),
        A("Aucun, Python n'exige pas de déclaration de type", True),
        A("dim"),
    ]),
    Q("Parmi ces noms de variables, lesquels sont syntaxiquement valides en Python ?", "multiple", [
        A("_total", True),
        A("valeur2", True),
        A("2valeur"),
        A("mon-nom"),
    ]),
    TF("En Python, on peut affecter plusieurs variables en une seule ligne avec `x = y = z = 0`.", True),
    TF("Le nom de variable `class` est un identifiant valide car ce n'est pas un mot réservé.", False),
])

add("Types de données numériques", "Identifier et manipuler les types int, float et complex.", [
    Q("Quel est le type de la valeur retournée par `3 / 2` en Python 3 ?", "single", [
        A("int"),
        A("float", True),
        A("str"),
        A("complex"),
    ]),
    Q("Quel opérateur effectue une division entière (sans reste) en Python ?", "single", [
        A("/"),
        A("//", True),
        A("%"),
        A("div"),
    ]),
    Q("Que retourne `type(10)` en Python ?", "single", [
        A("<class 'int'>", True),
        A("<class 'float'>"),
        A("<class 'number'>"),
        A("int"),
    ]),
    Q("Parmi les expressions suivantes, lesquelles produisent un résultat de type float ?", "multiple", [
        A("7 / 2", True),
        A("3.0 + 1"),
        A("2 ** 0.5", True),
        A("4 // 2"),
    ]),
    TF("En Python, `10 % 3` retourne 1.", True),
    TF("Le type `int` en Python a une taille maximale fixe de 32 bits, comme en C.", False),
])

add("Chaînes de caractères : les bases", "Manipuler le type str et ses opérations élémentaires.", [
    Q("Comment définir une chaîne de caractères contenant une apostrophe, par exemple l'aujourd'hui ?", "single", [
        A('Avec des guillemets doubles : "aujourd\'hui"', True),
        A("Impossible en Python"),
        A("Avec des crochets uniquement"),
        A("En échappant systématiquement chaque lettre"),
    ]),
    Q("Quel opérateur permet de concaténer deux chaînes de caractères ?", "single", [
        A("&"),
        A("+", True),
        A(".",),
        A("++"),
    ]),
    Q("Que retourne `len('Python')` ?", "single", [
        A("5"),
        A("6", True),
        A("7"),
        A("Une erreur"),
    ]),
    Q("Parmi ces expressions, lesquelles sont des chaînes de caractères valides en Python ?", "multiple", [
        A("'bonjour'", True),
        A('"bonjour"', True),
        A("'''bonjour'''", True),
        A("(bonjour)"),
    ]),
    TF("En Python, le type str est immuable : on ne peut pas modifier un caractère d'une chaîne via son index.", True),
    TF("L'opérateur * permet de répéter une chaîne, par exemple 'ab' * 3 donne 'ababab'.", True),
])

add("Booléens et valeurs de vérité", "Comprendre le type bool et la notion de 'truthiness' en Python.", [
    Q("Quelles sont les deux seules valeurs possibles du type bool en Python ?", "single", [
        A("0 et 1"),
        A("True et False", True),
        A("vrai et faux"),
        A("yes et no"),
    ]),
    Q("Que retourne `bool(0)` ?", "single", [
        A("True"),
        A("False", True),
        A("0"),
        A("Une erreur"),
    ]),
    Q("Que retourne `bool('')` (chaîne vide) ?", "single", [
        A("True"),
        A("False", True),
        A("None"),
        A("Une erreur de type"),
    ]),
    Q("Parmi ces valeurs, lesquelles sont considérées comme \"fausses\" (falsy) en Python ?", "multiple", [
        A("0", True),
        A("[]", True),
        A("None", True),
        A("'0'"),
    ]),
    TF("En Python, le type bool est en réalité une sous-classe du type int.", True),
    TF("L'expression `True + True` provoque une erreur de type en Python.", False),
])

add("Listes : création et accès", "Apprendre à créer des listes et à accéder à leurs éléments.", [
    Q("Comment crée-t-on une liste vide en Python ?", "single", [
        A("liste = ()"),
        A("liste = []", True),
        A("liste = {}"),
        A("liste = list;"),
    ]),
    Q("Quel est l'index du premier élément d'une liste Python ?", "single", [
        A("1"),
        A("0", True),
        A("-1"),
        A("Cela dépend de la liste"),
    ]),
    Q("Soit `liste = [10, 20, 30]`. Que retourne `liste[-1]` ?", "single", [
        A("10"),
        A("20"),
        A("30", True),
        A("Une erreur"),
    ]),
    Q("Parmi ces méthodes, lesquelles permettent d'ajouter un ou plusieurs éléments à une liste ?", "multiple", [
        A("append()", True),
        A("extend()", True),
        A("insert()", True),
        A("pop()"),
    ]),
    TF("Une liste Python peut contenir des éléments de types différents, par exemple `[1, 'a', True]`.", True),
    TF("La méthode `liste.append(x)` retourne une nouvelle liste sans modifier la liste d'origine.", False),
])

add("Tuples : caractéristiques essentielles", "Comprendre le tuple, sa syntaxe et son immuabilité.", [
    Q("Comment crée-t-on un tuple contenant un seul élément, par exemple la valeur 5 ?", "single", [
        A("(5)"),
        A("(5,)", True),
        A("[5]"),
        A("tuple(5)"),
    ]),
    Q("Quelle est la principale différence entre une liste et un tuple en Python ?", "single", [
        A("Le tuple ne peut contenir que des entiers"),
        A("Le tuple est immuable, la liste est mutable", True),
        A("La liste ne peut pas être indexée"),
        A("Il n'y a aucune différence"),
    ]),
    Q("Que retourne `len((1, 2, 3))` ?", "single", [
        A("2"),
        A("3", True),
        A("1"),
        A("Une erreur"),
    ]),
    Q("Parmi ces opérations, lesquelles sont possibles sur un tuple ?", "multiple", [
        A("Accéder à un élément par son index", True),
        A("Parcourir le tuple avec une boucle for", True),
        A("Modifier un élément existant via son index"),
        A("Compter ses éléments avec len()", True),
    ]),
    TF("On peut convertir une liste en tuple avec la fonction `tuple()`.", True),
    TF("Un tuple peut être utilisé comme clé dans un dictionnaire, contrairement à une liste.", True),
])

add("Dictionnaires : structure clé-valeur", "Découvrir la création et l'accès aux dictionnaires Python.", [
    Q("Comment crée-t-on un dictionnaire associant 'nom' à 'Alice' ?", "single", [
        A("{'nom': 'Alice'}", True),
        A("['nom', 'Alice']"),
        A("('nom' = 'Alice')"),
        A("dict('nom', 'Alice')"),
    ]),
    Q("Quelle méthode permet d'accéder à une valeur d'un dictionnaire sans provoquer d'erreur si la clé est absente ?", "single", [
        A("d.get('cle')", True),
        A("d['cle']"),
        A("d.fetch('cle')"),
        A("d.find('cle')"),
    ]),
    Q("Soit `d = {'a': 1, 'b': 2}`. Que retourne `d.keys()` ?", "single", [
        A("Les valeurs du dictionnaire"),
        A("Les clés du dictionnaire", True),
        A("Le nombre de paires"),
        A("Une erreur"),
    ]),
    Q("Parmi ces méthodes, lesquelles s'appliquent à un objet dictionnaire ?", "multiple", [
        A("items()", True),
        A("values()", True),
        A("keys()", True),
        A("append()"),
    ]),
    TF("Les clés d'un dictionnaire Python doivent être des objets hashables (immuables comme str, int, tuple).", True),
    TF("Depuis Python 3.7, l'ordre d'insertion des clés dans un dictionnaire est garanti.", True),
])

add("Ensembles (sets) : éliminer les doublons", "Comprendre les particularités du type set en Python.", [
    Q("Comment crée-t-on un ensemble (set) contenant les valeurs 1, 2 et 3 ?", "single", [
        A("{1, 2, 3}", True),
        A("[1, 2, 3]"),
        A("(1, 2, 3)"),
        A("set[1, 2, 3]"),
    ]),
    Q("Que retourne `set([1, 2, 2, 3, 3, 3])` ?", "single", [
        A("{1, 2, 2, 3, 3, 3}"),
        A("{1, 2, 3}", True),
        A("[1, 2, 3]"),
        A("Une erreur, car les sets n'acceptent pas les listes"),
    ]),
    Q("Quelle affirmation décrit correctement un set en Python ?", "single", [
        A("Une collection ordonnée et indexable"),
        A("Une collection non ordonnée d'éléments uniques", True),
        A("Une collection qui autorise les doublons"),
        A("Une structure clé-valeur"),
    ]),
    Q("Parmi ces opérations, lesquelles sont définies entre deux ensembles (sets) en Python ?", "multiple", [
        A("Union avec |", True),
        A("Intersection avec &", True),
        A("Différence avec -", True),
        A("Concatenation avec +"),
    ]),
    TF("On peut accéder à un élément d'un set via un index, comme `mon_set[0]`.", False),
    TF("Un ensemble (set) ne peut contenir que des éléments hashables.", True),
])

add("Structures de contrôle : if, elif, else", "Maîtriser les conditions et leur enchaînement en Python.", [
    Q("Quel mot-clé permet de tester une condition supplémentaire après un `if` ?", "single", [
        A("elseif"),
        A("elif", True),
        A("else if"),
        A("then"),
    ]),
    Q("Que va afficher ce code : `x = 5` puis `if x > 10: print('A')` puis `else: print('B')` ?", "single", [
        A("A"),
        A("B", True),
        A("Rien"),
        A("Une erreur de syntaxe"),
    ]),
    Q("Quel symbole est obligatoire à la fin de la ligne `if x > 0` en Python ?", "single", [
        A("Une accolade ouvrante"),
        A("Les deux-points :", True),
        A("Un point-virgule"),
        A("Rien du tout"),
    ]),
    Q("Parmi ces expressions, lesquelles sont des opérateurs de comparaison valides en Python ?", "multiple", [
        A("==", True),
        A("!=", True),
        A(">=", True),
        A("=<"),
    ]),
    TF("En Python, un bloc `else` peut exister sans `if` correspondant.", False),
    TF("Il est possible d'imbriquer un `if` à l'intérieur d'un autre `if`.", True),
])

# ===================== BLOC 2 : BOUCLES, FONCTIONS, ARGS (quiz 11-20) =====================

add("La boucle for et l'itération", "Comprendre le fonctionnement de la boucle for sur des séquences.", [
    Q("Que fait `for i in range(3): print(i)` ?", "single", [
        A("Affiche 1, 2, 3"),
        A("Affiche 0, 1, 2", True),
        A("Affiche 0, 1, 2, 3"),
        A("Provoque une erreur"),
    ]),
    Q("Quelle fonction intégrée génère une séquence de nombres souvent utilisée avec for ?", "single", [
        A("sequence()"),
        A("range()", True),
        A("loop()"),
        A("series()"),
    ]),
    Q("Comment parcourt-on à la fois l'index et la valeur des éléments d'une liste avec une boucle for ?", "single", [
        A("Avec la fonction enumerate()", True),
        A("Avec la fonction index()"),
        A("C'est impossible en Python"),
        A("Avec la méthode .indexValue()"),
    ]),
    Q("Parmi ces objets, lesquels sont directement itérables avec une boucle for ?", "multiple", [
        A("Une liste", True),
        A("Une chaîne de caractères", True),
        A("Un dictionnaire", True),
        A("Un entier"),
    ]),
    TF("`range(5)` génère les nombres de 0 à 5 inclus.", False),
    TF("On peut itérer directement sur les caractères d'une chaîne avec `for c in 'abc':`.", True),
])

add("La boucle while et ses contrôles", "Étudier la boucle while ainsi que break et continue.", [
    Q("Quelle instruction permet de sortir immédiatement d'une boucle while ?", "single", [
        A("exit"),
        A("break", True),
        A("return"),
        A("stop"),
    ]),
    Q("Que fait l'instruction `continue` à l'intérieur d'une boucle ?", "single", [
        A("Elle arrête définitivement la boucle"),
        A("Elle passe directement à l'itération suivante", True),
        A("Elle relance le programme"),
        A("Elle met la boucle en pause"),
    ]),
    Q("Quel est le risque principal d'une boucle `while True:` sans condition de sortie ?", "single", [
        A("Une erreur de syntaxe immédiate"),
        A("Une boucle infinie", True),
        A("Le programme s'arrête après 1 itération"),
        A("Aucun risque, Python la limite automatiquement"),
    ]),
    Q("Parmi ces instructions, lesquelles permettent de modifier le déroulement normal d'une boucle ?", "multiple", [
        A("break", True),
        A("continue", True),
        A("pass", True),
        A("yield"),
    ]),
    TF("Une boucle while peut posséder une clause else exécutée si la boucle se termine sans break.", True),
    TF("L'instruction `pass` interrompt l'exécution de la boucle en cours.", False),
])

add("Fonctions : définition et retour", "Apprendre à définir des fonctions et à utiliser return.", [
    Q("Quel mot-clé permet de définir une fonction en Python ?", "single", [
        A("function"),
        A("def", True),
        A("func"),
        A("define"),
    ]),
    Q("Que retourne une fonction Python qui ne contient aucune instruction `return` ?", "single", [
        A("0"),
        A("None", True),
        A("Une chaîne vide"),
        A("Une erreur"),
    ]),
    Q("Comment appelle-t-on une fonction nommée `saluer` sans argument ?", "single", [
        A("saluer;"),
        A("saluer()", True),
        A("call saluer()"),
        A("saluer[]"),
    ]),
    Q("Parmi ces éléments, lesquels peuvent apparaître dans la signature d'une fonction Python ?", "multiple", [
        A("Des paramètres positionnels", True),
        A("Des paramètres avec valeur par défaut", True),
        A("Une annotation de type de retour", True),
        A("Un mot-clé return obligatoire"),
    ]),
    TF("Une fonction Python peut retourner plusieurs valeurs séparées par des virgules, sous forme de tuple.", True),
    TF("En Python, il est interdit de définir une fonction à l'intérieur d'une autre fonction.", False),
])

add("Arguments par défaut et nommés", "Comprendre les paramètres par défaut et les appels avec mots-clés.", [
    Q("Que fait `def saluer(nom='Monde'): print('Bonjour', nom)` lorsqu'on appelle `saluer()` sans argument ?", "single", [
        A("Provoque une erreur"),
        A("Affiche 'Bonjour Monde'", True),
        A("Affiche 'Bonjour None'"),
        A("N'affiche rien"),
    ]),
    Q("Comment appelle-t-on un argument passé sous la forme `nom='Alice'` lors d'un appel de fonction ?", "single", [
        A("Un argument positionnel"),
        A("Un argument nommé (mot-clé)", True),
        A("Un argument global"),
        A("Un argument anonyme"),
    ]),
    Q("Quelle est la conséquence d'utiliser une liste mutable comme valeur par défaut d'un paramètre ?", "single", [
        A("Aucune, c'est une pratique recommandée"),
        A("La liste est partagée entre tous les appels successifs, ce qui peut causer des bugs", True),
        A("Python lève systématiquement une erreur"),
        A("La liste est recréée vide à chaque appel automatiquement"),
    ]),
    Q("Parmi ces appels de la fonction `def f(a, b=2, c=3):`, lesquels sont valides ?", "multiple", [
        A("f(1)", True),
        A("f(1, 5)", True),
        A("f(a=1, c=9)", True),
        A("f()"),
    ]),
    TF("En Python, un argument nommé peut être placé avant un argument positionnel dans l'appel `f(b=2, 1)`.", False),
    TF("Les paramètres avec valeur par défaut doivent être déclarés après les paramètres sans valeur par défaut.", True),
])

add("*args et **kwargs", "Comprendre la capture d'un nombre variable d'arguments.", [
    Q("Que représente le paramètre `*args` dans une définition de fonction ?", "single", [
        A("Un dictionnaire des arguments nommés"),
        A("Un tuple contenant les arguments positionnels supplémentaires", True),
        A("Une liste obligatoire de 3 éléments"),
        A("Une variable globale"),
    ]),
    Q("Que représente le paramètre `**kwargs` dans une définition de fonction ?", "single", [
        A("Un tuple d'arguments positionnels"),
        A("Un dictionnaire des arguments nommés supplémentaires", True),
        A("Un ensemble (set) d'arguments"),
        A("Une erreur de syntaxe"),
    ]),
    Q("Soit `def f(*args): print(len(args))`. Que retourne l'appel `f(1, 2, 3, 4)` ?", "single", [
        A("1"),
        A("3"),
        A("4", True),
        A("Une erreur"),
    ]),
    Q("Parmi ces appels, lesquels sont valides pour la fonction `def f(*args, **kwargs): pass` ?", "multiple", [
        A("f(1, 2, 3)", True),
        A("f(a=1, b=2)", True),
        A("f(1, 2, a=3)", True),
        A("f(*args invalide*)"),
    ]),
    TF("Dans une définition de fonction, *args doit être déclaré avant **kwargs.", True),
    TF("On peut utiliser l'opérateur * pour déballer une liste en arguments positionnels lors d'un appel, par exemple f(*ma_liste).", True),
])

add("Compréhensions de listes", "Maîtriser la syntaxe concise des list comprehensions.", [
    Q("Que retourne `[x**2 for x in range(4)]` ?", "single", [
        A("[0, 1, 2, 3]"),
        A("[0, 1, 4, 9]", True),
        A("[1, 4, 9, 16]"),
        A("Une erreur"),
    ]),
    Q("Quelle compréhension de liste génère les nombres pairs entre 0 et 9 inclus ?", "single", [
        A("[x for x in range(10) if x % 2 == 0]", True),
        A("[x for x in range(10) if x % 2 == 1]"),
        A("[x for x in range(10) where x % 2 == 0]"),
        A("(x for x in range(10) if x % 2 == 0)"),
    ]),
    Q("Quel est l'équivalent en compréhension de la boucle `resultat = []; for x in donnees: resultat.append(x*2)` ?", "single", [
        A("[x*2 for x in donnees]", True),
        A("{x*2 for x in donnees}"),
        A("(x*2 in donnees)"),
        A("x*2 for x in donnees"),
    ]),
    Q("Parmi ces syntaxes, lesquelles sont des compréhensions valides en Python ?", "multiple", [
        A("[x for x in range(5)]", True),
        A("{x: x**2 for x in range(5)}", True),
        A("{x for x in range(5)}", True),
        A("<x for x in range(5)>"),
    ]),
    TF("Une compréhension de liste peut contenir plusieurs clauses for imbriquées.", True),
    TF("Les compréhensions de listes sont généralement plus lentes qu'une boucle for équivalente avec append().", False),
])

add("Compréhensions de dictionnaires et d'ensembles", "Approfondir les compréhensions appliquées aux dicts et sets.", [
    Q("Que retourne `{x: x*2 for x in range(3)}` ?", "single", [
        A("{0: 0, 1: 2, 2: 4}", True),
        A("[0, 2, 4]"),
        A("{0, 2, 4}"),
        A("Une erreur"),
    ]),
    Q("Quelle syntaxe crée un ensemble des carrés des nombres de 0 à 4 via une compréhension ?", "single", [
        A("{x**2 for x in range(5)}", True),
        A("[x**2 for x in range(5)]"),
        A("(x**2 for x in range(5))"),
        A("set(x**2 for x in range(5)) ="),
    ]),
    Q("Soit `noms = ['a', 'bb', 'ccc']`. Que retourne `{n: len(n) for n in noms}` ?", "single", [
        A("{'a': 1, 'bb': 2, 'ccc': 3}", True),
        A("[1, 2, 3]"),
        A("{'a', 'bb', 'ccc'}"),
        A("Une erreur de syntaxe"),
    ]),
    Q("Parmi ces affirmations sur les compréhensions de dictionnaire, lesquelles sont vraies ?", "multiple", [
        A("Elles utilisent la syntaxe {clé: valeur for ...}", True),
        A("Elles peuvent inclure une clause if de filtrage", True),
        A("Elles créent un objet de type dict", True),
        A("Elles ne peuvent pas être imbriquées"),
    ]),
    TF("Une compréhension d'ensemble élimine automatiquement les doublons éventuels du résultat.", True),
    TF("La syntaxe `(x for x in range(5))` crée une liste en mémoire comme une compréhension de liste classique.", False),
])

add("Méthodes de chaînes courantes", "Explorer les méthodes utiles du type str : split, join, strip, replace.", [
    Q("Que retourne `'  Bonjour  '.strip()` ?", "single", [
        A("'  Bonjour  '"),
        A("'Bonjour'", True),
        A("'Bonjour  '"),
        A("Une erreur"),
    ]),
    Q("Que retourne `'a,b,c'.split(',')` ?", "single", [
        A("'a,b,c'"),
        A("['a', 'b', 'c']", True),
        A("('a', 'b', 'c')"),
        A("{'a', 'b', 'c'}"),
    ]),
    Q("Que retourne `'-'.join(['a', 'b', 'c'])` ?", "single", [
        A("'a-b-c'", True),
        A("['a', 'b', 'c']"),
        A("'abc'"),
        A("Une erreur de type"),
    ]),
    Q("Parmi ces méthodes, lesquelles renvoient une chaîne transformée sans modifier la chaîne d'origine ?", "multiple", [
        A("upper()", True),
        A("lower()", True),
        A("replace()", True),
        A("len()"),
    ]),
    TF("La méthode `'Python'.startswith('Py')` retourne True.", True),
    TF("Les méthodes de chaînes modifient l'objet str d'origine directement, car str est mutable.", False),
])

add("Les f-strings et le formatage", "Maîtriser le formatage moderne de chaînes avec les f-strings.", [
    Q("Soit `nom = 'Alice'`. Que retourne `f'Bonjour {nom}'` ?", "single", [
        A("'Bonjour {nom}'"),
        A("'Bonjour Alice'", True),
        A("Une erreur de syntaxe"),
        A("'Bonjour nom'"),
    ]),
    Q("Quel préfixe permet de créer une f-string en Python ?", "single", [
        A("s"),
        A("f", True),
        A("r"),
        A("u"),
    ]),
    Q("Que retourne `f'{3.14159:.2f}'` ?", "single", [
        A("'3.14'", True),
        A("'3.14159'"),
        A("'3,14'"),
        A("Une erreur"),
    ]),
    Q("Parmi ces méthodes, lesquelles permettent de formater des chaînes en Python ?", "multiple", [
        A("Les f-strings (f'...')", True),
        A("La méthode str.format()", True),
        A("L'opérateur %", True),
        A("La méthode str.template_format()"),
    ]),
    TF("On peut évaluer des expressions arbitraires à l'intérieur des accolades d'une f-string, par exemple f'{2+2}'.", True),
    TF("Les f-strings nécessitent d'importer un module spécifique avant utilisation.", False),
])

add("Slicing : tranches de séquences", "Comprendre la syntaxe de slicing sur les listes et chaînes.", [
    Q("Soit `liste = [0, 1, 2, 3, 4, 5]`. Que retourne `liste[1:4]` ?", "single", [
        A("[1, 2, 3]", True),
        A("[1, 2, 3, 4]"),
        A("[0, 1, 2, 3]"),
        A("[2, 3, 4]"),
    ]),
    Q("Soit `texte = 'Python'`. Que retourne `texte[::-1]` ?", "single", [
        A("'Python'"),
        A("'nohtyP'", True),
        A("''"),
        A("Une erreur"),
    ]),
    Q("Soit `liste = [0, 1, 2, 3, 4, 5]`. Que retourne `liste[::2]` ?", "single", [
        A("[0, 2, 4]", True),
        A("[1, 3, 5]"),
        A("[0, 1, 2]"),
        A("[5, 4, 3, 2, 1, 0]"),
    ]),
    Q("Parmi ces expressions de slicing sur `liste = [0,1,2,3,4]`, lesquelles renvoient `[0, 1, 2]` ?", "multiple", [
        A("liste[:3]", True),
        A("liste[0:3]", True),
        A("liste[-5:-2]", True),
        A("liste[1:3]"),
    ]),
    TF("Le slicing `liste[2:2]` retourne toujours une liste vide.", True),
    TF("Le slicing d'une liste retourne toujours une référence vers la liste d'origine, sans copie.", False),
])

# ===================== BLOC 3 : EXCEPTIONS & POO (quiz 21-35) =====================

add("Gestion des exceptions : try/except", "Apprendre les bases de la capture d'erreurs en Python.", [
    Q("Quel mot-clé permet de capturer une exception en Python ?", "single", [
        A("catch"),
        A("except", True),
        A("rescue"),
        A("error"),
    ]),
    Q("Que se passe-t-il si une exception levée dans un bloc try n'est capturée par aucun except correspondant ?", "single", [
        A("Le programme continue normalement"),
        A("Le programme s'arrête et affiche une trace d'erreur (traceback)", True),
        A("Python l'ignore silencieusement"),
        A("La boucle recommence automatiquement"),
    ]),
    Q("Quelle exception est levée par `10 / 0` en Python ?", "single", [
        A("ValueError"),
        A("ZeroDivisionError", True),
        A("TypeError"),
        A("ArithmeticOverflow"),
    ]),
    Q("Parmi ces blocs, lesquels peuvent faire partie d'une structure try complète en Python ?", "multiple", [
        A("except", True),
        A("else", True),
        A("finally", True),
        A("catch"),
    ]),
    TF("Le bloc `finally` s'exécute toujours, qu'une exception ait été levée ou non.", True),
    TF("On peut capturer plusieurs types d'exceptions différents avec plusieurs clauses except successives.", True),
])

add("Lever ses propres exceptions", "Comprendre raise et la création d'exceptions personnalisées.", [
    Q("Quel mot-clé permet de déclencher volontairement une exception en Python ?", "single", [
        A("throw"),
        A("raise", True),
        A("trigger"),
        A("error"),
    ]),
    Q("Comment crée-t-on une exception personnalisée en Python ?", "single", [
        A("En héritant de la classe Exception", True),
        A("En utilisant le mot-clé custom_error"),
        A("Ce n'est pas possible en Python"),
        A("En définissant une fonction nommée exception()"),
    ]),
    Q("Que fait `raise ValueError('valeur invalide')` ?", "single", [
        A("Affiche simplement un message sans interrompre le programme"),
        A("Lève une exception de type ValueError avec le message indiqué", True),
        A("Crée une variable nommée ValueError"),
        A("Ignore l'erreur"),
    ]),
    Q("Parmi ces classes, lesquelles sont des exceptions intégrées (built-in) de Python ?", "multiple", [
        A("ValueError", True),
        A("TypeError", True),
        A("KeyError", True),
        A("LoopError"),
    ]),
    TF("Une exception personnalisée doit obligatoirement hériter, directement ou indirectement, de la classe BaseException.", True),
    TF("L'instruction `raise` sans argument à l'intérieur d'un bloc except relève l'exception en cours de traitement.", True),
])

add("Classes et objets : les fondamentaux", "Découvrir la déclaration de classes et la création d'instances.", [
    Q("Quel mot-clé permet de définir une classe en Python ?", "single", [
        A("class", True),
        A("struct"),
        A("object"),
        A("define"),
    ]),
    Q("Quel est le nom conventionnel du premier paramètre d'une méthode d'instance en Python ?", "single", [
        A("this"),
        A("self", True),
        A("me"),
        A("instance"),
    ]),
    Q("Quelle méthode spéciale est automatiquement appelée lors de la création d'une instance ?", "single", [
        A("__new__()"),
        A("__init__()", True),
        A("__create__()"),
        A("__start__()"),
    ]),
    Q("Parmi ces affirmations sur les classes Python, lesquelles sont correctes ?", "multiple", [
        A("Une classe peut posséder des attributs d'instance", True),
        A("Une classe peut posséder des attributs de classe partagés", True),
        A("Une classe peut contenir des méthodes", True),
        A("Une classe ne peut avoir qu'une seule instance possible"),
    ]),
    TF("En Python, on instancie une classe Personne avec la syntaxe `Personne()`, comme un appel de fonction.", True),
    TF("Les attributs d'instance définis dans __init__ via self sont partagés entre toutes les instances de la classe.", False),
])

add("Héritage et classes dérivées", "Explorer l'héritage simple et l'utilisation de super().", [
    Q("Quelle syntaxe permet à la classe Chien d'hériter de la classe Animal ?", "single", [
        A("class Chien(Animal):", True),
        A("class Chien extends Animal:"),
        A("class Chien : Animal"),
        A("class Chien inherits Animal:"),
    ]),
    Q("À quoi sert la fonction `super()` dans une classe dérivée ?", "single", [
        A("À supprimer la classe parente"),
        A("À accéder aux méthodes et attributs de la classe parente", True),
        A("À créer une nouvelle instance de la classe courante"),
        A("À transformer la classe en module"),
    ]),
    Q("Si la classe B hérite de A et redéfinit une méthode `parler()`, que se passe-t-il lors de l'appel sur une instance de B ?", "single", [
        A("La méthode de A est toujours appelée"),
        A("La méthode de B est appelée (elle prévaut sur celle de A)", True),
        A("Python lève une erreur d'ambiguïté"),
        A("Les deux méthodes sont appelées simultanément"),
    ]),
    Q("Parmi ces affirmations sur l'héritage en Python, lesquelles sont vraies ?", "multiple", [
        A("Une classe peut hériter de plusieurs classes (héritage multiple)", True),
        A("La fonction isinstance() vérifie si un objet est une instance d'une classe ou sous-classe", True),
        A("Une sous-classe peut redéfinir (override) une méthode de sa classe parente", True),
        A("Une sous-classe perd automatiquement tous les attributs de sa classe parente"),
    ]),
    TF("La fonction `issubclass(Chien, Animal)` vérifie si Chien est une sous-classe d'Animal.", True),
    TF("En Python, toutes les classes héritent implicitement de la classe object.", True),
])

add("Méthodes magiques (dunder methods)", "Comprendre __str__, __repr__, __eq__ et autres méthodes spéciales.", [
    Q("Quelle méthode magique est appelée par `print(objet)` pour obtenir une représentation lisible ?", "single", [
        A("__str__()", True),
        A("__print__()"),
        A("__display__()"),
        A("__text__()"),
    ]),
    Q("Quelle méthode magique permet de personnaliser le comportement de l'opérateur == entre deux objets ?", "single", [
        A("__equals__()"),
        A("__eq__()", True),
        A("__compare__()"),
        A("__same__()"),
    ]),
    Q("Quelle méthode magique est utilisée pour définir le comportement de la fonction len() sur un objet personnalisé ?", "single", [
        A("__length__()"),
        A("__len__()", True),
        A("__size__()"),
        A("__count__()"),
    ]),
    Q("Parmi ces méthodes, lesquelles sont des méthodes magiques (dunder) reconnues par Python ?", "multiple", [
        A("__init__", True),
        A("__add__", True),
        A("__repr__", True),
        A("__function__"),
    ]),
    TF("Sans définition explicite de __eq__, comparer deux instances différentes d'une même classe avec == compare leur identité mémoire par défaut.", True),
    TF("La méthode __repr__ est destinée à fournir une représentation technique non ambiguë de l'objet, utile pour le débogage.", True),
])

add("Encapsulation et conventions de nommage", "Étudier les conventions publiques, protégées et privées en Python.", [
    Q("Quelle convention de nommage suggère qu'un attribut est destiné à un usage interne (protégé) ?", "single", [
        A("Un underscore en préfixe, comme _valeur", True),
        A("Toutes les lettres en majuscules"),
        A("Un underscore en suffixe, comme valeur_"),
        A("Aucune convention n'existe en Python"),
    ]),
    Q("Quel mécanisme Python applique au nommage `__valeur` (double underscore en préfixe) dans une classe ?", "single", [
        A("Aucun effet particulier"),
        A("Le name mangling, qui renomme l'attribut en _NomClasse__valeur", True),
        A("Une erreur de syntaxe systématique"),
        A("La transformation automatique en propriété"),
    ]),
    Q("Python possède-t-il un mécanisme strict d'attributs réellement privés comme en Java (private) ?", "single", [
        A("Oui, identique à Java"),
        A("Non, Python repose sur des conventions de nommage plutôt que sur une restriction stricte", True),
        A("Oui, mais seulement pour les méthodes"),
        A("Non, aucun mécanisme n'existe, même conventionnel"),
    ]),
    Q("Parmi ces affirmations sur l'encapsulation en Python, lesquelles sont vraies ?", "multiple", [
        A("Un attribut préfixé par un seul underscore reste accessible depuis l'extérieur de la classe", True),
        A("Le décorateur @property permet de contrôler l'accès en lecture à un attribut", True),
        A("Les conventions de nommage n'empêchent pas techniquement l'accès à l'attribut", True),
        A("Python interdit totalement l'accès aux attributs préfixés par un underscore"),
    ]),
    TF("Le décorateur @property permet de transformer une méthode en attribut accessible sans parenthèses.", True),
    TF("Un attribut nommé `__solde` (double underscore) devient totalement inaccessible depuis l'extérieur de la classe, sans aucune exception.", False),
])

add("Modules et imports", "Comprendre comment organiser et réutiliser du code avec import.", [
    Q("Quelle instruction permet d'importer uniquement la fonction sqrt du module math ?", "single", [
        A("import math.sqrt"),
        A("from math import sqrt", True),
        A("include math.sqrt"),
        A("using math.sqrt"),
    ]),
    Q("Quelle instruction importe le module entier random et permet d'y accéder via random.choice() ?", "single", [
        A("import random", True),
        A("from random import *"),
        A("include random"),
        A("use random"),
    ]),
    Q("À quoi sert la syntaxe `import numpy as np` ?", "single", [
        A("À importer uniquement la fonction as de numpy"),
        A("À importer le module numpy sous un alias plus court, np", True),
        A("À créer un nouveau module nommé np"),
        A("C'est une syntaxe invalide"),
    ]),
    Q("Parmi ces affirmations sur les modules Python, lesquelles sont vraies ?", "multiple", [
        A("Un module est simplement un fichier .py contenant du code réutilisable", True),
        A("Un package est un dossier contenant des modules, généralement avec un fichier __init__.py", True),
        A("On peut importer plusieurs noms d'un module avec from module import a, b", True),
        A("Un module ne peut être importé qu'une seule fois dans tout le programme, sinon erreur"),
    ]),
    TF("La variable spéciale `__name__` vaut '__main__' lorsque le script est exécuté directement.", True),
    TF("L'instruction `from module import *` importe uniquement la première fonction définie dans le module.", False),
])

add("Lecture et écriture de fichiers", "Manipuler les fichiers avec open() et l'instruction with.", [
    Q("Quelle fonction permet d'ouvrir un fichier en Python ?", "single", [
        A("open()", True),
        A("file()"),
        A("read()"),
        A("load()"),
    ]),
    Q("Quel mode d'ouverture de fichier permet d'ajouter du contenu à la fin d'un fichier existant sans l'effacer ?", "single", [
        A("'r'"),
        A("'w'"),
        A("'a'", True),
        A("'x'"),
    ]),
    Q("Quel est l'avantage principal d'utiliser `with open('fichier.txt') as f:` plutôt que `f = open('fichier.txt')` ?", "single", [
        A("Le fichier se ferme automatiquement à la fin du bloc, même en cas d'erreur", True),
        A("Cela rend la lecture du fichier plus rapide"),
        A("Cela permet de lire des fichiers plus volumineux"),
        A("Aucune différence, c'est juste une autre syntaxe"),
    ]),
    Q("Parmi ces méthodes, lesquelles permettent de lire le contenu d'un fichier ouvert ?", "multiple", [
        A("read()", True),
        A("readline()", True),
        A("readlines()", True),
        A("scan()"),
    ]),
    TF("Le mode d'ouverture 'w' efface le contenu existant du fichier avant d'écrire.", True),
    TF("Avec l'instruction with, il est nécessaire d'appeler manuellement f.close() à la fin du bloc.", False),
])

add("Fonctions lambda", "Comprendre la syntaxe et les usages des fonctions anonymes.", [
    Q("Quel mot-clé permet de créer une fonction anonyme en une seule expression ?", "single", [
        A("def"),
        A("lambda", True),
        A("anon"),
        A("func"),
    ]),
    Q("Que retourne `(lambda x: x * 2)(5)` ?", "single", [
        A("5"),
        A("10", True),
        A("x * 2"),
        A("Une erreur"),
    ]),
    Q("Quelle est une limitation importante des fonctions lambda par rapport aux fonctions def classiques ?", "single", [
        A("Elles ne peuvent contenir qu'une seule expression, pas plusieurs instructions", True),
        A("Elles ne peuvent pas prendre de paramètres"),
        A("Elles ne peuvent pas être stockées dans une variable"),
        A("Elles sont toujours plus lentes à l'exécution"),
    ]),
    Q("Parmi ces usages, lesquels sont des cas typiques d'utilisation d'une lambda ?", "multiple", [
        A("Comme clé de tri avec sorted(liste, key=lambda x: x[1])", True),
        A("Comme fonction de filtrage avec filter(lambda x: x > 0, liste)", True),
        A("Comme fonction de transformation avec map(lambda x: x*2, liste)", True),
        A("Pour définir une classe complète"),
    ]),
    TF("Une fonction lambda peut être assignée à une variable, par exemple `carre = lambda x: x**2`.", True),
    TF("Une fonction lambda peut contenir une instruction return explicite comme `lambda x: return x`.", False),
])

add("Générateurs et l'instruction yield", "Découvrir les générateurs et leur évaluation paresseuse (lazy).", [
    Q("Quel mot-clé transforme une fonction normale en générateur ?", "single", [
        A("return"),
        A("yield", True),
        A("generate"),
        A("lazy"),
    ]),
    Q("Quelle est la principale différence entre `return` et `yield` dans une fonction ?", "single", [
        A("yield met en pause la fonction et conserve son état pour reprendre plus tard, return termine la fonction", True),
        A("Il n'y a aucune différence"),
        A("return peut être utilisé plusieurs fois, yield une seule fois"),
        A("yield ne peut être utilisé que dans une classe"),
    ]),
    Q("Comment crée-t-on un générateur de façon concise, équivalent compact d'une compréhension de liste ?", "single", [
        A("Avec une expression génératrice : (x for x in range(5))", True),
        A("Avec une compréhension de liste : [x for x in range(5)]"),
        A("Avec une compréhension d'ensemble : {x for x in range(5)}"),
        A("Ce n'est pas possible de façon concise"),
    ]),
    Q("Parmi ces affirmations sur les générateurs, lesquelles sont vraies ?", "multiple", [
        A("Un générateur produit ses valeurs une à une, à la demande (lazy evaluation)", True),
        A("Un générateur peut être parcouru avec une boucle for", True),
        A("On peut obtenir la valeur suivante d'un générateur avec la fonction next()", True),
        A("Un générateur stocke toutes ses valeurs en mémoire dès sa création"),
    ]),
    TF("Une fois qu'un générateur est épuisé (toutes ses valeurs consommées), on ne peut pas le réutiliser depuis le début sans le recréer.", True),
    TF("Les générateurs consomment généralement moins de mémoire que les listes équivalentes pour de grandes séquences.", True),
])

add("Itérateurs et le protocole d'itération", "Comprendre __iter__, __next__ et la notion d'itérable.", [
    Q("Quelle méthode magique doit implémenter un objet itérable pour retourner un itérateur ?", "single", [
        A("__iter__()", True),
        A("__loop__()"),
        A("__each__()"),
        A("__iterate__()"),
    ]),
    Q("Quelle exception est levée par la méthode __next__() d'un itérateur lorsqu'il n'y a plus d'éléments ?", "single", [
        A("IndexError"),
        A("StopIteration", True),
        A("EndOfIterator"),
        A("ValueError"),
    ]),
    Q("Quelle fonction intégrée permet d'obtenir manuellement un itérateur à partir d'un itérable ?", "single", [
        A("iter()", True),
        A("next()"),
        A("loop()"),
        A("generator()"),
    ]),
    Q("Parmi ces objets, lesquels sont des itérables en Python (utilisables dans une boucle for) ?", "multiple", [
        A("Une liste", True),
        A("Un générateur", True),
        A("Un dictionnaire", True),
        A("Un entier simple comme 5"),
    ]),
    TF("Tout itérateur est également un itérable, car il possède une méthode __iter__ qui se retourne lui-même.", True),
    TF("La fonction next() appliquée à un itérateur épuisé retourne automatiquement None sans erreur.", False),
])

# ===================== BLOC 4 : CONTEXTE, BUILTINS, MUTABILITE, SCOPE (quiz 32-50) =====================

add("Gestionnaires de contexte et l'instruction with", "Approfondir le fonctionnement de with et des context managers.", [
    Q("Quelle méthode magique est appelée à l'entrée d'un bloc with pour un gestionnaire de contexte personnalisé ?", "single", [
        A("__enter__()", True),
        A("__start__()"),
        A("__open__()"),
        A("__with__()"),
    ]),
    Q("Quelle méthode magique est appelée à la sortie d'un bloc with, même en cas d'exception ?", "single", [
        A("__close__()"),
        A("__exit__()", True),
        A("__end__()"),
        A("__finally__()"),
    ]),
    Q("Quel module de la bibliothèque standard fournit le décorateur @contextmanager pour créer facilement un gestionnaire de contexte ?", "single", [
        A("contextlib", True),
        A("functools"),
        A("itertools"),
        A("context"),
    ]),
    Q("Parmi ces affirmations sur l'instruction with, lesquelles sont vraies ?", "multiple", [
        A("Elle garantit la libération des ressources même si une exception survient", True),
        A("On peut ouvrir plusieurs gestionnaires de contexte sur une seule ligne with a, b:", True),
        A("Elle est couramment utilisée pour la gestion de fichiers avec open()", True),
        A("Elle remplace obligatoirement tous les blocs try/except du programme"),
    ]),
    TF("La méthode __exit__ peut recevoir des informations sur une exception survenue dans le bloc with.", True),
    TF("L'instruction with ne peut être utilisée qu'avec des fichiers, aucun autre type d'objet.", False),
])

add("Fonctions intégrées map, filter et zip", "Utiliser les fonctions fonctionnelles intégrées de Python.", [
    Q("Que retourne `list(map(lambda x: x*2, [1, 2, 3]))` ?", "single", [
        A("[2, 4, 6]", True),
        A("[1, 2, 3]"),
        A("[1, 4, 9]"),
        A("Une erreur"),
    ]),
    Q("Que retourne `list(filter(lambda x: x > 2, [1, 2, 3, 4]))` ?", "single", [
        A("[1, 2]"),
        A("[3, 4]", True),
        A("[1, 2, 3, 4]"),
        A("[]"),
    ]),
    Q("Que fait la fonction `zip([1,2,3], ['a','b','c'])` ?", "single", [
        A("Elle compresse les listes en un fichier zip"),
        A("Elle associe les éléments des deux listes par position en paires", True),
        A("Elle additionne les éléments des deux listes"),
        A("Elle provoque une erreur car les types diffèrent"),
    ]),
    Q("Parmi ces affirmations sur map(), filter() et zip(), lesquelles sont vraies ?", "multiple", [
        A("map() applique une fonction à chaque élément d'un itérable", True),
        A("filter() conserve uniquement les éléments pour lesquels la fonction retourne une valeur vraie", True),
        A("zip() s'arrête dès que le plus court des itérables est épuisé", True),
        A("Ces trois fonctions retournent directement des listes en Python 3"),
    ]),
    TF("En Python 3, map() et filter() retournent des objets itérateurs et non des listes directement.", True),
    TF("La fonction zip() ne peut combiner que exactement deux itérables, jamais plus.", False),
])

add("Fonctions enumerate, sorted et range", "Maîtriser des fonctions intégrées essentielles pour itérer et trier.", [
    Q("Que retourne `list(enumerate(['a', 'b']))` ?", "single", [
        A("[(0, 'a'), (1, 'b')]", True),
        A("['a', 'b']"),
        A("[0, 1]"),
        A("Une erreur"),
    ]),
    Q("Que retourne `sorted([3, 1, 2])` ?", "single", [
        A("[3, 2, 1]"),
        A("[1, 2, 3]", True),
        A("[3, 1, 2]"),
        A("None"),
    ]),
    Q("Comment trier une liste de nombres par ordre décroissant avec sorted() ?", "single", [
        A("sorted(liste, reverse=True)", True),
        A("sorted(liste, desc=True)"),
        A("sorted(liste, order='desc')"),
        A("liste.sorted(down=True)"),
    ]),
    Q("Parmi ces affirmations, lesquelles sont vraies concernant sorted() et la méthode liste.sort() ?", "multiple", [
        A("sorted() retourne une nouvelle liste sans modifier l'originale", True),
        A("liste.sort() modifie la liste en place et retourne None", True),
        A("sorted() peut s'appliquer à n'importe quel itérable, pas seulement aux listes", True),
        A("liste.sort() fonctionne sur les tuples comme sur les listes"),
    ]),
    TF("La fonction range(1, 10, 2) génère les nombres 1, 3, 5, 7, 9.", True),
    TF("enumerate() permet de définir un point de départ différent de 0 grâce au paramètre start.", True),
])

add("Mutabilité vs immutabilité", "Comprendre la différence entre objets mutables et immuables en Python.", [
    Q("Parmi ces types, lequel est mutable en Python ?", "single", [
        A("tuple"),
        A("list", True),
        A("str"),
        A("int"),
    ]),
    Q("Parmi ces types, lequel est immuable en Python ?", "single", [
        A("dict"),
        A("set"),
        A("tuple", True),
        A("list"),
    ]),
    Q("Que se passe-t-il quand on exécute `a = [1,2]; b = a; b.append(3)` puis qu'on affiche `a` ?", "single", [
        A("a vaut [1, 2]"),
        A("a vaut [1, 2, 3], car a et b référencent la même liste", True),
        A("Une erreur est levée"),
        A("a devient None"),
    ]),
    Q("Parmi ces types Python, lesquels sont immuables ?", "multiple", [
        A("int", True),
        A("str", True),
        A("frozenset", True),
        A("list"),
    ]),
    TF("Modifier un tuple contenant une liste (ex : `t = ([1,2],)`) en changeant le contenu de cette liste interne est possible, même si le tuple lui-même reste immuable.", True),
    TF("Une chaîne de caractères Python peut être modifiée caractère par caractère via l'affectation `s[0] = 'X'`.", False),
])

add("Portée des variables : locale, globale, nonlocal", "Étudier le scope des variables dans les fonctions imbriquées.", [
    Q("Quel mot-clé permet de modifier une variable globale depuis l'intérieur d'une fonction ?", "single", [
        A("global", True),
        A("public"),
        A("extern"),
        A("static"),
    ]),
    Q("Quel mot-clé permet à une fonction imbriquée de modifier une variable de la fonction englobante (ni locale ni globale) ?", "single", [
        A("global"),
        A("nonlocal", True),
        A("outer"),
        A("parent"),
    ]),
    Q("Sans déclaration explicite, dans quelle portée Python crée-t-il une variable affectée à l'intérieur d'une fonction ?", "single", [
        A("Globale automatiquement"),
        A("Locale à la fonction", True),
        A("Dans le module appelant"),
        A("Cela dépend du système d'exploitation"),
    ]),
    Q("Parmi ces affirmations sur la portée des variables en Python, lesquelles sont vraies ?", "multiple", [
        A("Une variable locale à une fonction n'est pas accessible depuis l'extérieur de cette fonction", True),
        A("Le mot-clé global doit être utilisé pour réaffecter une variable globale dans une fonction", True),
        A("Les fonctions imbriquées peuvent lire (sans réaffecter) les variables de la fonction englobante sans mot-clé spécial", True),
        A("Toutes les variables Python sont globales par défaut"),
    ]),
    TF("Lire la valeur d'une variable globale depuis l'intérieur d'une fonction ne nécessite pas le mot-clé global, seule la réaffectation en a besoin.", True),
    TF("Le mot-clé nonlocal peut être utilisé directement au niveau global du module.", False),
])

add("Unpacking et affectations multiples", "Comprendre le déballage de séquences et l'opérateur étoile.", [
    Q("Que fait `a, b, c = [1, 2, 3]` ?", "single", [
        A("Provoque une erreur"),
        A("Affecte respectivement 1, 2 et 3 à a, b et c", True),
        A("Affecte la liste entière à a"),
        A("Affecte None à b et c"),
    ]),
    Q("Que retourne `a, *b = [1, 2, 3, 4]` pour la variable b ?", "single", [
        A("2"),
        A("[2, 3, 4]", True),
        A("[1, 2, 3, 4]"),
        A("Une erreur"),
    ]),
    Q("Comment échanger les valeurs de deux variables x et y sans variable temporaire explicite ?", "single", [
        A("x, y = y, x", True),
        A("swap(x, y)"),
        A("x = y; y = x"),
        A("x <-> y"),
    ]),
    Q("Parmi ces affectations, lesquelles sont syntaxiquement valides en Python ?", "multiple", [
        A("a, b = 1, 2", True),
        A("a, (b, c) = 1, (2, 3)", True),
        A("*a, b = [1, 2, 3]", True),
        A("a, b, c = 1, 2"),
    ]),
    TF("L'opérateur * dans le déballage permet de capturer plusieurs éléments restants dans une liste.", True),
    TF("Le nombre de variables à gauche d'une affectation multiple doit toujours être strictement supérieur au nombre de valeurs à droite.", False),
])

add("Opérateurs : is, ==, in", "Distinguer l'égalité de valeur, l'identité d'objet et l'appartenance.", [
    Q("Quelle est la différence fondamentale entre les opérateurs == et is en Python ?", "single", [
        A("== compare l'égalité de valeur, is compare l'identité (même objet en mémoire)", True),
        A("Ils sont totalement équivalents"),
        A("is ne fonctionne que sur les nombres"),
        A("== ne fonctionne que sur les chaînes"),
    ]),
    Q("Que retourne généralement `[1, 2] == [1, 2]` ?", "single", [
        A("True", True),
        A("False"),
        A("None"),
        A("Une erreur"),
    ]),
    Q("Que retourne généralement `[1, 2] is [1, 2]` (deux listes créées séparément) ?", "single", [
        A("True"),
        A("False", True),
        A("None"),
        A("Une erreur"),
    ]),
    Q("Parmi ces usages, lesquels sont des emplois corrects de l'opérateur in en Python ?", "multiple", [
        A("3 in [1, 2, 3]", True),
        A("'a' in 'abc'", True),
        A("'cle' in mon_dictionnaire", True),
        A("in(3, [1, 2, 3])"),
    ]),
    TF("La comparaison `x is None` est la manière recommandée de vérifier si une variable vaut None.", True),
    TF("L'opérateur is compare toujours les valeurs des objets, jamais leur identité mémoire.", False),
])

add("Opérateurs arithmétiques et de puissance", "Revoir les opérateurs +, -, *, /, //, %, ** en détail.", [
    Q("Que retourne `2 ** 10` en Python ?", "single", [
        A("20"),
        A("100"),
        A("1024", True),
        A("Une erreur"),
    ]),
    Q("Que retourne `-7 // 2` en Python ?", "single", [
        A("-3"),
        A("-4", True),
        A("-3.5"),
        A("3"),
    ]),
    Q("Que retourne `-7 % 2` en Python ?", "single", [
        A("-1"),
        A("1", True),
        A("3"),
        A("-3"),
    ]),
    Q("Parmi ces expressions, lesquelles sont équivalentes à 'élever 2 au cube' (2 puissance 3) en Python ?", "multiple", [
        A("2 ** 3", True),
        A("pow(2, 3)", True),
        A("2 * 2 * 2", True),
        A("2 ^ 3"),
    ]),
    TF("L'opérateur ^ effectue l'élévation à la puissance en Python, comme dans certains langages mathématiques.", False),
    TF("L'opérateur % appliqué à des float est valide, par exemple `5.5 % 2` retourne 1.5.", True),
])

add("Typage et annotations (type hints)", "Découvrir les annotations de type optionnelles introduites par Python.", [
    Q("Que fait l'annotation dans `def addition(a: int, b: int) -> int:` ?", "single", [
        A("Elle force Python à vérifier strictement les types à l'exécution"),
        A("Elle documente les types attendus sans les imposer à l'exécution", True),
        A("Elle provoque une erreur si on ne respecte pas les types"),
        A("Elle convertit automatiquement les arguments dans le type indiqué"),
    ]),
    Q("Quel module de la bibliothèque standard fournit des types génériques avancés comme List, Dict, Optional ?", "single", [
        A("types"),
        A("typing", True),
        A("generics"),
        A("annotations"),
    ]),
    Q("Que se passe-t-il si on appelle `addition('a', 'b')` avec `def addition(a: int, b: int) -> int: return a + b` ?", "single", [
        A("Python lève automatiquement une TypeError avant l'exécution"),
        A("La fonction s'exécute normalement et concatène les chaînes, car les annotations ne sont pas vérifiées à l'exécution", True),
        A("Le programme refuse de démarrer"),
        A("Python convertit automatiquement les chaînes en entiers"),
    ]),
    Q("Parmi ces affirmations sur le typage en Python, lesquelles sont vraies ?", "multiple", [
        A("Python est un langage à typage dynamique : le type d'une variable peut changer au cours de l'exécution", True),
        A("Les type hints sont une indication facultative à destination des développeurs et des outils", True),
        A("Des outils comme mypy peuvent vérifier statiquement les annotations de type", True),
        A("Les type hints rendent Python statiquement typé comme Java"),
    ]),
    TF("On peut annoter le type d'une variable simple, par exemple `age: int = 25`.", True),
    TF("Les annotations de type sont obligatoires depuis Python 3 pour que le code s'exécute.", False),
])

add("Modules standards : math et random", "Découvrir quelques fonctions essentielles des modules math et random.", [
    Q("Quelle fonction du module math permet de calculer la racine carrée d'un nombre ?", "single", [
        A("math.sqrt()", True),
        A("math.root()"),
        A("math.power()"),
        A("math.sq()"),
    ]),
    Q("Quelle fonction du module random génère un entier aléatoire compris entre deux bornes incluses ?", "single", [
        A("random.choice()"),
        A("random.randint()", True),
        A("random.sample()"),
        A("random.number()"),
    ]),
    Q("Quelle constante du module math représente la valeur de pi ?", "single", [
        A("math.pi", True),
        A("math.PI"),
        A("math.Pi"),
        A("math.circle"),
    ]),
    Q("Parmi ces fonctions, lesquelles appartiennent au module random de la bibliothèque standard ?", "multiple", [
        A("random.choice()", True),
        A("random.shuffle()", True),
        A("random.uniform()", True),
        A("random.sqrt()"),
    ]),
    TF("Il faut importer le module math avec `import math` avant d'utiliser math.sqrt().", True),
    TF("La fonction random.random() retourne un flottant aléatoire compris entre 0 inclus et 1 exclu.", True),
])

add("Le module datetime : notions de base", "Comprendre la manipulation élémentaire des dates et heures.", [
    Q("Quelle classe du module datetime représente une date sans heure (jour, mois, année) ?", "single", [
        A("datetime.date", True),
        A("datetime.time"),
        A("datetime.calendar"),
        A("datetime.day"),
    ]),
    Q("Quelle fonction du module datetime permet d'obtenir la date et l'heure actuelles ?", "single", [
        A("datetime.datetime.now()", True),
        A("datetime.today_time()"),
        A("datetime.current()"),
        A("datetime.get_now()"),
    ]),
    Q("Quel type d'objet obtient-on en soustrayant deux objets datetime entre eux ?", "single", [
        A("Un objet timedelta", True),
        A("Un entier représentant les secondes"),
        A("Une chaîne de caractères"),
        A("Une erreur, l'opération est interdite"),
    ]),
    Q("Parmi ces affirmations sur le module datetime, lesquelles sont vraies ?", "multiple", [
        A("La classe datetime.timedelta représente une durée", True),
        A("On peut formater une date en chaîne avec la méthode strftime()", True),
        A("On peut convertir une chaîne en date avec strptime()", True),
        A("Le module datetime ne fait pas partie de la bibliothèque standard"),
    ]),
    TF("Le module datetime fait partie de la bibliothèque standard de Python, sans installation supplémentaire.", True),
    TF("Un objet date du module datetime peut être directement additionné à un entier représentant des jours, par exemple `ma_date + 5`.", False),
])

add("Comparaisons et égalité d'objets personnalisés", "Approfondir le comportement de == et < sur des objets définis par l'utilisateur.", [
    Q("Sans définir __eq__ dans une classe, que compare l'opérateur == entre deux instances ?", "single", [
        A("Les valeurs de tous les attributs automatiquement"),
        A("L'identité des objets (équivalent à is) par défaut", True),
        A("Le nom de la classe uniquement"),
        A("Cela provoque systématiquement une erreur"),
    ]),
    Q("Quelle méthode magique faut-il définir pour permettre la comparaison avec l'opérateur < entre deux objets personnalisés ?", "single", [
        A("__lt__()", True),
        A("__less__()"),
        A("__compare__()"),
        A("__inferior__()"),
    ]),
    Q("Quel module de la bibliothèque standard fournit le décorateur @total_ordering pour générer automatiquement les comparaisons restantes ?", "single", [
        A("functools", True),
        A("operator"),
        A("itertools"),
        A("compare"),
    ]),
    Q("Parmi ces méthodes magiques, lesquelles concernent la comparaison entre objets ?", "multiple", [
        A("__eq__", True),
        A("__lt__", True),
        A("__le__", True),
        A("__init__"),
    ]),
    TF("Définir __eq__ dans une classe sans définir __hash__ peut rendre les instances non hashables (par défaut __hash__ devient None).", True),
    TF("L'opérateur != utilise automatiquement l'inverse de __eq__ si __ne__ n'est pas défini explicitement, depuis Python 3.", True),
])

add("Copie superficielle vs copie profonde", "Distinguer shallow copy et deep copy avec le module copy.", [
    Q("Que fait une copie superficielle (shallow copy) d'une liste contenant des sous-listes ?", "single", [
        A("Elle copie récursivement tous les objets imbriqués"),
        A("Elle crée une nouvelle liste, mais les sous-objets mutables restent partagés avec l'original", True),
        A("Elle ne copie que les éléments immuables"),
        A("Elle provoque toujours une erreur"),
    ]),
    Q("Quelle fonction du module copy permet d'effectuer une copie profonde (deep copy) ?", "single", [
        A("copy.copy()"),
        A("copy.deepcopy()", True),
        A("copy.clone()"),
        A("copy.duplicate()"),
    ]),
    Q("Quelle méthode de liste permet d'obtenir une copie superficielle simple, par exemple `nouvelle = ancienne.copy()` ?", "single", [
        A("copy()", True),
        A("clone()"),
        A("duplicate()"),
        A("replicate()"),
    ]),
    Q("Parmi ces affirmations sur les copies en Python, lesquelles sont vraies ?", "multiple", [
        A("Le slicing complet `liste[:]` crée une copie superficielle de la liste", True),
        A("Une deepcopy crée des copies indépendantes de tous les objets imbriqués", True),
        A("L'affectation simple `b = a` ne crée aucune copie, b référence le même objet que a", True),
        A("Une shallow copy duplique récursivement tous les sous-objets mutables"),
    ]),
    TF("Modifier un élément imbriqué mutable dans une copie superficielle affecte aussi l'objet original.", True),
    TF("Le module copy doit être importé pour utiliser deepcopy(), il ne fait pas partie des fonctions intégrées (builtins).", True),
])

add("Arguments positionnels vs nommés (approfondissement)", "Approfondir les règles d'ordre et de restriction des paramètres.", [
    Q("Que signifie le symbole / dans la signature `def f(a, b, /, c):` (Python 3.8+) ?", "single", [
        A("a et b doivent être passés uniquement en arguments positionnels", True),
        A("a et b sont optionnels"),
        A("c doit être passé en argument nommé uniquement"),
        A("C'est une erreur de syntaxe dans toutes les versions"),
    ]),
    Q("Que signifie le symbole * dans la signature `def f(a, *, b):` ?", "single", [
        A("a est optionnel"),
        A("b doit obligatoirement être passé en argument nommé (mot-clé)", True),
        A("a et b sont tous deux positionnels uniquement"),
        A("La fonction accepte un nombre illimité d'arguments"),
    ]),
    Q("Pour la fonction `def f(a, b=10):`, quel appel est invalide ?", "single", [
        A("f(1)"),
        A("f(1, 2)"),
        A("f(b=2)", True),
        A("f(a=1, b=2)"),
    ]),
    Q("Parmi ces appels de `def f(a, b, c=3):`, lesquels sont valides ?", "multiple", [
        A("f(1, 2)", True),
        A("f(1, 2, 3)", True),
        A("f(a=1, b=2, c=5)", True),
        A("f(c=1)"),
    ]),
    TF("Dans un appel de fonction, on ne peut pas placer un argument positionnel après un argument nommé.", True),
    TF("Les paramètres définis après un paramètre *args doivent obligatoirement être passés en arguments nommés.", True),
])

# ===================== BLOC 5 : DECORATEURS, POO AVANCEE, DIVERS (quiz 46-65) =====================

add("Décorateurs : principes de base", "Comprendre comment un décorateur modifie le comportement d'une fonction.", [
    Q("Quel symbole précède le nom d'un décorateur appliqué à une fonction ?", "single", [
        A("@", True),
        A("#"),
        A("&"),
        A("%"),
    ]),
    Q("Qu'est-ce qu'un décorateur en Python, fondamentalement ?", "single", [
        A("Une fonction qui prend une fonction en argument et retourne une fonction modifiée", True),
        A("Un commentaire spécial pour la documentation"),
        A("Une classe abstraite obligatoire"),
        A("Un type de boucle particulier"),
    ]),
    Q("À quoi sert généralement `functools.wraps` lors de l'écriture d'un décorateur ?", "single", [
        A("À accélérer l'exécution de la fonction décorée"),
        A("À préserver les métadonnées (nom, docstring) de la fonction originale", True),
        A("À transformer le décorateur en générateur"),
        A("À supprimer les arguments de la fonction décorée"),
    ]),
    Q("Parmi ces décorateurs, lesquels sont fournis nativement par Python (built-in) ?", "multiple", [
        A("@staticmethod", True),
        A("@classmethod", True),
        A("@property", True),
        A("@override"),
    ]),
    TF("On peut appliquer plusieurs décorateurs successifs à une même fonction, en les empilant.", True),
    TF("Un décorateur ne peut jamais accepter de paramètres propres en plus de la fonction décorée.", False),
])

add("Méthodes statiques et méthodes de classe", "Distinguer @staticmethod, @classmethod et les méthodes d'instance.", [
    Q("Quel décorateur permet de définir une méthode qui n'a accès ni à self ni à cls ?", "single", [
        A("@staticmethod", True),
        A("@classmethod"),
        A("@property"),
        A("@abstractmethod"),
    ]),
    Q("Quel décorateur permet de définir une méthode dont le premier paramètre conventionnel est cls (la classe elle-même) ?", "single", [
        A("@staticmethod"),
        A("@classmethod", True),
        A("@instancemethod"),
        A("@property"),
    ]),
    Q("Pourquoi utiliser une méthode de classe (@classmethod) plutôt qu'une méthode d'instance pour une fabrique alternative (factory) ?", "single", [
        A("Car elle peut créer et retourner une nouvelle instance en utilisant cls, utile pour les constructeurs alternatifs", True),
        A("Car c'est obligatoire en Python"),
        A("Car elle s'exécute plus vite qu'une méthode normale"),
        A("Car elle ne peut pas être appelée depuis une instance"),
    ]),
    Q("Parmi ces affirmations sur les méthodes statiques et de classe, lesquelles sont vraies ?", "multiple", [
        A("Une méthode statique peut être appelée directement sur la classe sans instance", True),
        A("Une méthode de classe reçoit automatiquement la classe en premier argument", True),
        A("Une méthode statique se comporte comme une fonction normale rangée dans l'espace de noms de la classe", True),
        A("Une méthode statique reçoit automatiquement self en premier argument"),
    ]),
    TF("Une méthode de classe peut être utilisée pour modifier un attribut de classe partagé par toutes les instances.", True),
    TF("Le décorateur @staticmethod donne accès à self automatiquement, comme une méthode d'instance classique.", False),
])

add("Classes abstraites et interfaces", "Découvrir le module abc et la notion de classe abstraite en Python.", [
    Q("Quel module de la bibliothèque standard permet de définir des classes abstraites en Python ?", "single", [
        A("abc", True),
        A("abstract"),
        A("interface"),
        A("typing"),
    ]),
    Q("Quel décorateur, combiné à une classe héritant de ABC, marque une méthode comme abstraite (devant être réimplémentée) ?", "single", [
        A("@abstractmethod", True),
        A("@override"),
        A("@interface"),
        A("@mustimplement"),
    ]),
    Q("Que se passe-t-il si on essaie d'instancier directement une classe abstraite contenant une méthode abstraite non implémentée ?", "single", [
        A("Python lève une TypeError", True),
        A("L'instanciation fonctionne normalement"),
        A("La méthode abstraite est ignorée silencieusement"),
        A("Python convertit la classe automatiquement en classe concrète"),
    ]),
    Q("Parmi ces affirmations sur les classes abstraites en Python, lesquelles sont vraies ?", "multiple", [
        A("Une classe abstraite peut définir des méthodes concrètes en plus des méthodes abstraites", True),
        A("Une sous-classe doit implémenter toutes les méthodes abstraites pour être instanciable", True),
        A("Les classes abstraites servent à définir un contrat commun pour des sous-classes", True),
        A("Python interdit complètement la notion de classe abstraite, contrairement à Java"),
    ]),
    TF("La classe ABC du module abc est conçue pour empêcher l'instanciation directe d'une classe incomplète.", True),
    TF("Une méthode décorée par @abstractmethod doit obligatoirement contenir une implémentation complète et fonctionnelle.", False),
])

add("Propriétés avec @property", "Maîtriser l'encapsulation moderne grâce au décorateur property.", [
    Q("À quoi sert le décorateur @property appliqué à une méthode ?", "single", [
        A("À transformer la méthode en attribut accessible sans appel explicite avec parenthèses", True),
        A("À rendre la méthode statique"),
        A("À empêcher tout accès à la méthode"),
        A("À convertir la méthode en fonction globale"),
    ]),
    Q("Quel décorateur permet de définir le setter associé à une propriété nommée `valeur` ?", "single", [
        A("@valeur.setter", True),
        A("@property.set"),
        A("@setter.valeur"),
        A("@set_valeur"),
    ]),
    Q("Quel est l'un des principaux avantages d'utiliser @property plutôt que des méthodes get_x()/set_x() explicites ?", "single", [
        A("Cela permet de garder une syntaxe d'accès simple (obj.x) tout en ajoutant de la logique de validation", True),
        A("Cela rend le code incompatible avec l'héritage"),
        A("Cela supprime totalement le besoin de méthodes dans la classe"),
        A("Cela empêche toute modification future de l'attribut"),
    ]),
    Q("Parmi ces affirmations sur @property, lesquelles sont vraies ?", "multiple", [
        A("Une propriété en lecture seule peut être définie en omettant le setter", True),
        A("On peut valider une valeur avant de l'assigner dans le setter d'une propriété", True),
        A("L'accès à une propriété se fait sans parenthèses, comme un attribut normal", True),
        A("Une propriété ne peut jamais être combinée avec une logique de calcul interne"),
    ]),
    TF("Tenter de modifier une propriété définie sans setter provoque une erreur AttributeError.", True),
    TF("Le décorateur @property doit obligatoirement être utilisé avec un underscore devant l'attribut interne, sinon le code ne compile pas.", False),
])

add("Attributs de classe vs attributs d'instance", "Distinguer les attributs partagés et les attributs propres à chaque objet.", [
    Q("Où un attribut de classe est-il généralement défini ?", "single", [
        A("Directement dans le corps de la classe, en dehors de toute méthode", True),
        A("Uniquement dans __init__ avec self"),
        A("Dans une fonction globale"),
        A("Il est impossible de définir un attribut de classe en Python"),
    ]),
    Q("Que se passe-t-il si on modifie un attribut de classe mutable (comme une liste) via une instance sans utiliser self.attribut = nouvelle_valeur, mais via self.attribut.append(x) ?", "single", [
        A("Seule l'instance est affectée"),
        A("Toutes les instances partageant cet attribut de classe voient la modification", True),
        A("Une erreur est levée"),
        A("Rien ne se passe"),
    ]),
    Q("Comment accède-t-on généralement à un attribut de classe nommé compteur depuis une méthode d'instance ?", "single", [
        A("Via self.compteur ou NomClasse.compteur", True),
        A("Uniquement via this.compteur"),
        A("C'est impossible depuis une méthode d'instance"),
        A("Via global compteur"),
    ]),
    Q("Parmi ces affirmations sur les attributs de classe, lesquelles sont vraies ?", "multiple", [
        A("Un attribut de classe est partagé par défaut par toutes les instances", True),
        A("Affecter self.attribut = valeur dans une méthode crée ou modifie un attribut d'instance propre à cet objet", True),
        A("Les attributs de classe sont utiles pour des compteurs partagés entre instances", True),
        A("Les attributs de classe ne peuvent jamais être consultés depuis une instance"),
    ]),
    TF("Un attribut de classe peut être utilisé comme valeur par défaut partagée, tout en étant redéfini individuellement par certaines instances.", True),
    TF("Les attributs d'instance définis dans __init__ sont automatiquement visibles dans toutes les autres instances de la classe.", False),
])

add("Surcharge d'opérateurs avec les dunder methods", "Personnaliser le comportement des opérateurs +, -, * via les méthodes magiques.", [
    Q("Quelle méthode magique permet de personnaliser le comportement de l'opérateur + sur des objets personnalisés ?", "single", [
        A("__add__()", True),
        A("__plus__()"),
        A("__sum__()"),
        A("__concat__()"),
    ]),
    Q("Quelle méthode magique permet de personnaliser le comportement de l'opérateur * (multiplication) ?", "single", [
        A("__mul__()", True),
        A("__times__()"),
        A("__multiply__()"),
        A("__product__()"),
    ]),
    Q("Si la classe Vecteur définit __add__, que permet l'expression `v1 + v2` où v1 et v2 sont des instances de Vecteur ?", "single", [
        A("Une addition personnalisée définie par le développeur, par exemple l'addition composante par composante", True),
        A("Une erreur systématique, car + est réservé aux nombres"),
        A("La concaténation textuelle des deux objets"),
        A("Rien, l'opérateur + ne peut pas être surchargé en Python"),
    ]),
    Q("Parmi ces méthodes magiques, lesquelles correspondent à des opérateurs arithmétiques surchargeables ?", "multiple", [
        A("__sub__ pour -", True),
        A("__truediv__ pour /", True),
        A("__pow__ pour **", True),
        A("__print__ pour print()"),
    ]),
    TF("Si __add__ n'est pas défini dans une classe, l'opérateur + entre deux instances de cette classe provoque une erreur TypeError.", True),
    TF("La méthode __radd__ permet de gérer le cas où l'objet personnalisé se trouve à droite de l'opérateur + et l'opérande de gauche ne sait pas l'additionner.", True),
])

add("Listes chaînées et structures de données personnalisées", "Implémenter une structure de données simple avec des classes.", [
    Q("Dans une implémentation simple de liste chaînée en Python, que contient typiquement un attribut 'suivant' d'un nœud ?", "single", [
        A("Une référence vers le nœud suivant, ou None s'il n'y en a pas", True),
        A("Toujours une valeur entière"),
        A("La position du nœud dans la liste"),
        A("Le nombre total de nœuds"),
    ]),
    Q("Quelle structure de données intégrée à Python se comporte nativement comme une pile (LIFO) efficace avec append() et pop() ?", "single", [
        A("list", True),
        A("dict"),
        A("set"),
        A("frozenset"),
    ]),
    Q("Quelle structure du module collections est optimisée pour les insertions/suppressions rapides aux deux extrémités (file ou pile) ?", "single", [
        A("deque", True),
        A("Counter"),
        A("OrderedDict"),
        A("namedtuple"),
    ]),
    Q("Parmi ces opérations, lesquelles sont typiquement en O(1) (temps constant) sur une liste Python ?", "multiple", [
        A("Accès à un élément par index", True),
        A("append() en fin de liste", True),
        A("len(liste)", True),
        A("insert(0, x) en début de liste"),
    ]),
    TF("La classe Counter du module collections permet de compter facilement les occurrences d'éléments dans un itérable.", True),
    TF("Une pile (stack) suit le principe FIFO : le premier élément ajouté est le premier sorti.", False),
])

add("Récursivité en Python", "Comprendre les fonctions récursives et leurs limites.", [
    Q("Qu'est-ce qu'une fonction récursive ?", "single", [
        A("Une fonction qui s'appelle elle-même", True),
        A("Une fonction qui ne retourne jamais de valeur"),
        A("Une fonction qui s'exécute en parallèle"),
        A("Une fonction sans paramètre"),
    ]),
    Q("Quel élément est indispensable dans une fonction récursive pour éviter une boucle infinie ?", "single", [
        A("Une condition d'arrêt (cas de base)", True),
        A("Une boucle for imbriquée"),
        A("Un décorateur spécifique"),
        A("Un argument de type liste"),
    ]),
    Q("Quelle exception Python lève généralement lorsqu'une récursion dépasse la profondeur maximale autorisée ?", "single", [
        A("RecursionError", True),
        A("StackOverflowError"),
        A("MemoryError obligatoirement"),
        A("LoopError"),
    ]),
    Q("Parmi ces fonctions, lesquelles peuvent être naturellement implémentées de façon récursive ?", "multiple", [
        A("Le calcul de la factorielle d'un nombre", True),
        A("Le calcul des termes de la suite de Fibonacci", True),
        A("Le parcours d'une arborescence de dossiers", True),
        A("L'affichage d'une simple chaîne de caractères fixe"),
    ]),
    TF("Python possède une limite par défaut de profondeur de récursion, consultable via sys.getrecursionlimit().", True),
    TF("Une fonction récursive est toujours plus rapide qu'une boucle itérative équivalente.", False),
])

add("Expressions conditionnelles et opérateurs logiques", "Approfondir and, or, not et l'expression ternaire.", [
    Q("Quelle est la syntaxe de l'expression conditionnelle (ternaire) en Python ?", "single", [
        A("valeur_si_vrai if condition else valeur_si_faux", True),
        A("condition ? valeur_si_vrai : valeur_si_faux"),
        A("if condition then valeur_si_vrai else valeur_si_faux"),
        A("condition && valeur_si_vrai || valeur_si_faux"),
    ]),
    Q("Que retourne `True and False` ?", "single", [
        A("True"),
        A("False", True),
        A("None"),
        A("Une erreur"),
    ]),
    Q("Que retourne l'expression `0 or 'valeur par défaut'` ?", "single", [
        A("0"),
        A("'valeur par défaut'", True),
        A("True"),
        A("False"),
    ]),
    Q("Parmi ces opérateurs, lesquels sont des opérateurs logiques booléens en Python ?", "multiple", [
        A("and", True),
        A("or", True),
        A("not", True),
        A("xor"),
    ]),
    TF("L'opérateur and pratique l'évaluation court-circuit : si le premier opérande est faux, le second n'est pas évalué.", True),
    TF("En Python, il existe un mot-clé xor natif pour le ou exclusif logique entre deux booléens.", False),
])

add("La fonction zip et le déballage avancé", "Combiner zip(), unpacking et compréhensions pour manipuler des données.", [
    Q("Que retourne `list(zip([1, 2], [3, 4], [5, 6]))` ?", "single", [
        A("[(1, 3, 5), (2, 4, 6)]", True),
        A("[1, 2, 3, 4, 5, 6]"),
        A("[(1, 2), (3, 4), (5, 6)]"),
        A("Une erreur"),
    ]),
    Q("Comment 'dézipper' une liste de tuples `paires = [(1, 'a'), (2, 'b')]` en deux listes séparées ?", "single", [
        A("nombres, lettres = zip(*paires)", True),
        A("nombres, lettres = unzip(paires)"),
        A("nombres, lettres = paires.split()"),
        A("Ce n'est pas possible en Python"),
    ]),
    Q("Que retourne `dict(zip(['a', 'b'], [1, 2]))` ?", "single", [
        A("{'a': 1, 'b': 2}", True),
        A("[('a', 1), ('b', 2)]"),
        A("{1: 'a', 2: 'b'}"),
        A("Une erreur"),
    ]),
    Q("Parmi ces usages, lesquels sont des applications courantes de zip() en Python ?", "multiple", [
        A("Créer un dictionnaire à partir de deux listes parallèles", True),
        A("Parcourir simultanément plusieurs listes dans une même boucle for", True),
        A("Associer des indices à des valeurs (bien qu'enumerate soit souvent préféré pour cela)", True),
        A("Trier automatiquement une liste"),
    ]),
    TF("zip() en Python 3 retourne un itérateur, qu'il faut convertir en liste avec list() pour voir tous les éléments d'un coup.", True),
    TF("Si les itérables passés à zip() ont des longueurs différentes, Python lève systématiquement une exception par défaut.", False),
])

add("Itertools : combinatoire et itération avancée", "Découvrir quelques fonctions utiles du module itertools.", [
    Q("Quelle fonction d'itertools génère toutes les permutations possibles d'un itérable ?", "single", [
        A("itertools.permutations()", True),
        A("itertools.combinations()"),
        A("itertools.product()"),
        A("itertools.shuffle()"),
    ]),
    Q("Quelle fonction d'itertools génère toutes les combinaisons possibles de taille donnée, sans tenir compte de l'ordre ?", "single", [
        A("itertools.combinations()", True),
        A("itertools.permutations()"),
        A("itertools.cycle()"),
        A("itertools.chain()"),
    ]),
    Q("À quoi sert `itertools.chain(liste1, liste2)` ?", "single", [
        A("À enchaîner plusieurs itérables en un seul itérateur continu", True),
        A("À fusionner deux listes en supprimant les doublons"),
        A("À calculer la différence entre deux listes"),
        A("À trier les deux listes combinées"),
    ]),
    Q("Parmi ces fonctions, lesquelles appartiennent au module itertools ?", "multiple", [
        A("count()", True),
        A("cycle()", True),
        A("product()", True),
        A("median()"),
    ]),
    TF("Le module itertools fait partie de la bibliothèque standard de Python.", True),
    TF("itertools.count() génère un nombre fini d'éléments avant de s'arrêter automatiquement.", False),
])

add("La fonction sorted() avec key et lambda", "Approfondir le tri personnalisé d'objets complexes.", [
    Q("Soit `personnes = [('Alice', 30), ('Bob', 25)]`. Quelle expression trie par âge croissant ?", "single", [
        A("sorted(personnes, key=lambda p: p[1])", True),
        A("sorted(personnes, key=lambda p: p[0])"),
        A("sorted(personnes)"),
        A("personnes.sort(by='age')"),
    ]),
    Q("Comment trier une liste de chaînes par longueur décroissante ?", "single", [
        A("sorted(liste, key=len, reverse=True)", True),
        A("sorted(liste, key=len)"),
        A("sorted(liste, reverse=True)"),
        A("liste.sort(length=True)"),
    ]),
    Q("Que fait le paramètre `key` dans la fonction sorted() ?", "single", [
        A("Il indique une fonction appliquée à chaque élément pour déterminer la valeur de comparaison utilisée pour le tri", True),
        A("Il filtre les éléments à exclure du tri"),
        A("Il indique le nombre d'éléments à trier"),
        A("Il force un tri alphabétique uniquement"),
    ]),
    Q("Parmi ces expressions, lesquelles permettent de trier une liste de dictionnaires `personnes` par la clé 'age' ?", "multiple", [
        A("sorted(personnes, key=lambda p: p['age'])", True),
        A("sorted(personnes, key=operator.itemgetter('age'))", True),
        A("personnes.sort(key=lambda p: p['age'])", True),
        A("sorted(personnes, by='age')"),
    ]),
    TF("La fonction sorted() est stable : les éléments considérés égaux par la clé de tri conservent leur ordre relatif d'origine.", True),
    TF("Le paramètre key de sorted() doit obligatoirement être une fonction lambda, aucune autre fonction n'est acceptée.", False),
])

add("Closures et fonctions imbriquées", "Comprendre les fermetures (closures) en Python.", [
    Q("Qu'est-ce qu'une closure (fermeture) en Python ?", "single", [
        A("Une fonction interne qui capture et mémorise les variables de la portée englobante", True),
        A("Une fonction qui ferme automatiquement les fichiers ouverts"),
        A("Un type de boucle particulier"),
        A("Une structure de données immuable"),
    ]),
    Q("Que retourne typiquement une fonction qui crée et renvoie une autre fonction utilisant une variable de la portée englobante ?", "single", [
        A("Une closure qui se souvient de la valeur capturée même après la fin de la fonction externe", True),
        A("Toujours None"),
        A("Une erreur de syntaxe"),
        A("La valeur immédiate sans fonction"),
    ]),
    Q("Quel mot-clé est nécessaire si la fonction interne doit réaffecter (et pas seulement lire) une variable de la fonction englobante ?", "single", [
        A("nonlocal", True),
        A("global"),
        A("static"),
        A("Aucun mot-clé n'est nécessaire pour réaffecter"),
    ]),
    Q("Parmi ces affirmations sur les closures, lesquelles sont vraies ?", "multiple", [
        A("Une closure permet de créer des fonctions personnalisées dynamiquement (fabriques de fonctions)", True),
        A("Les décorateurs reposent souvent sur le principe des closures", True),
        A("Une closure peut accéder à une variable de la fonction externe même après que celle-ci a terminé son exécution", True),
        A("Une closure ne peut jamais être utilisée avec des fonctions lambda"),
    ]),
    TF("Une fonction interne peut lire (sans réaffecter) une variable de la fonction englobante sans avoir besoin du mot-clé nonlocal.", True),
    TF("Les closures n'existent pas en Python, elles sont spécifiques à JavaScript.", False),
])

add("Gestion avancée des exceptions personnalisées", "Hiérarchiser et enrichir des exceptions métier personnalisées.", [
    Q("Quel est l'intérêt de créer une hiérarchie d'exceptions personnalisées héritant d'une exception de base commune ?", "single", [
        A("Permettre de capturer plusieurs types d'erreurs liées avec un seul except sur la classe de base", True),
        A("Cela n'a aucun intérêt particulier"),
        A("Cela ralentit volontairement le programme"),
        A("Cela empêche toute capture d'exception"),
    ]),
    Q("Comment ajouter un attribut personnalisé (comme un code d'erreur) à une exception personnalisée ?", "single", [
        A("En définissant __init__ dans la classe d'exception pour stocker l'attribut", True),
        A("Ce n'est pas possible avec les exceptions"),
        A("En utilisant uniquement le module logging"),
        A("En modifiant la classe Exception native de Python"),
    ]),
    Q("Que fait `raise NouvelleErreur('message') from erreur_originale` ?", "single", [
        A("Chaîne l'exception, en indiquant explicitement la cause d'origine dans la trace", True),
        A("Supprime l'exception d'origine"),
        A("Provoque une erreur de syntaxe"),
        A("Ignore le message d'erreur"),
    ]),
    Q("Parmi ces pratiques, lesquelles sont considérées comme de bonnes pratiques pour les exceptions personnalisées ?", "multiple", [
        A("Hériter d'Exception ou d'une sous-classe pertinente plutôt que de BaseException directement", True),
        A("Donner un nom de classe clair se terminant souvent par 'Error' ou 'Exception'", True),
        A("Documenter dans quels cas l'exception est levée", True),
        A("Toujours capturer Exception de façon générique sans jamais préciser le type"),
    ]),
    TF("Une exception personnalisée peut surcharger __str__ pour personnaliser le message affiché lors de l'affichage de l'erreur.", True),
    TF("Il est interdit techniquement de définir plusieurs niveaux de hiérarchie entre exceptions personnalisées.", False),
])

add("Le module collections : structures spécialisées", "Explorer namedtuple, defaultdict et OrderedDict.", [
    Q("Que permet de créer `collections.namedtuple('Point', ['x', 'y'])` ?", "single", [
        A("Une classe légère de type tuple avec des champs nommés accessibles par attribut", True),
        A("Un dictionnaire ordonné"),
        A("Une liste chaînée"),
        A("Un ensemble immuable"),
    ]),
    Q("Quel est l'avantage principal de `collections.defaultdict(list)` par rapport à un dict classique ?", "single", [
        A("Il fournit automatiquement une valeur par défaut (ici une liste vide) pour toute clé absente", True),
        A("Il interdit les doublons de valeurs"),
        A("Il trie automatiquement les clés"),
        A("Il consomme moins de mémoire qu'un dict classique"),
    ]),
    Q("Depuis quelle version de Python l'ordre d'insertion des dictionnaires standards est-il garanti, rendant OrderedDict moins indispensable ?", "single", [
        A("Python 3.7", True),
        A("Python 2.7"),
        A("Python 3.0"),
        A("Aucune, l'ordre n'a jamais été garanti"),
    ]),
    Q("Parmi ces classes, lesquelles font partie du module collections de la bibliothèque standard ?", "multiple", [
        A("Counter", True),
        A("defaultdict", True),
        A("namedtuple", True),
        A("FastDict"),
    ]),
    TF("Un namedtuple reste immuable, comme un tuple classique : on ne peut pas modifier un de ses champs après création.", True),
    TF("Le module collections doit être installé séparément avec pip, il ne fait pas partie de la bibliothèque standard.", False),
])

add("Expressions régulières avec le module re", "Découvrir les bases de la correspondance de motifs textuels.", [
    Q("Quel module de la bibliothèque standard Python permet de travailler avec des expressions régulières ?", "single", [
        A("re", True),
        A("regex"),
        A("pattern"),
        A("string"),
    ]),
    Q("Quelle fonction du module re recherche une correspondance n'importe où dans la chaîne (pas seulement au début) ?", "single", [
        A("re.search()", True),
        A("re.match()"),
        A("re.find()"),
        A("re.locate()"),
    ]),
    Q("Que retourne `re.findall(r'\\d+', 'J\\'ai 3 chats et 12 poissons')` ?", "single", [
        A("['3', '12']", True),
        A("[3, 12]"),
        A("'3 12'"),
        A("Une erreur"),
    ]),
    Q("Parmi ces fonctions, lesquelles appartiennent au module re ?", "multiple", [
        A("re.match()", True),
        A("re.sub()", True),
        A("re.split()", True),
        A("re.replace()"),
    ]),
    TF("Le préfixe r devant une chaîne, comme r'\\d+', indique une chaîne brute (raw string) où les antislashs ne sont pas interprétés comme des séquences d'échappement.", True),
    TF("re.match() recherche une correspondance n'importe où dans la chaîne, comme re.search().", False),
])

add("Le module json : sérialisation de données", "Manipuler la conversion entre objets Python et JSON.", [
    Q("Quelle fonction du module json convertit un dictionnaire Python en chaîne JSON ?", "single", [
        A("json.dumps()", True),
        A("json.loads()"),
        A("json.encode()"),
        A("json.write()"),
    ]),
    Q("Quelle fonction du module json convertit une chaîne JSON en objet Python (dict, list, etc.) ?", "single", [
        A("json.loads()", True),
        A("json.dumps()"),
        A("json.parse()"),
        A("json.decode()"),
    ]),
    Q("Quelle fonction permet d'écrire directement un objet Python sous forme JSON dans un fichier déjà ouvert ?", "single", [
        A("json.dump()", True),
        A("json.dumps()"),
        A("json.save()"),
        A("json.write()"),
    ]),
    Q("Parmi ces types Python, lesquels sont directement sérialisables en JSON par le module json sans configuration supplémentaire ?", "multiple", [
        A("dict", True),
        A("list", True),
        A("str", True),
        A("set"),
    ]),
    TF("Le module json fait partie de la bibliothèque standard de Python.", True),
    TF("Le module json peut sérialiser nativement n'importe quel objet Python personnalisé sans aucune configuration.", False),
])

# ===================== BLOC 6 : AVANCE (quiz 63-80) =====================

add("Gestion des fichiers CSV", "Découvrir le module csv pour lire et écrire des fichiers tabulaires.", [
    Q("Quel module de la bibliothèque standard Python permet de lire et écrire des fichiers CSV ?", "single", [
        A("csv", True),
        A("table"),
        A("excel"),
        A("data"),
    ]),
    Q("Quelle fonction du module csv permet de créer un objet capable de lire ligne par ligne un fichier CSV ouvert ?", "single", [
        A("csv.reader()", True),
        A("csv.read()"),
        A("csv.parse()"),
        A("csv.load()"),
    ]),
    Q("Quelle classe du module csv permet de lire chaque ligne directement sous forme de dictionnaire (clé = en-tête de colonne) ?", "single", [
        A("csv.DictReader", True),
        A("csv.reader"),
        A("csv.DictWriter"),
        A("csv.MapReader"),
    ]),
    Q("Parmi ces affirmations sur le module csv, lesquelles sont vraies ?", "multiple", [
        A("Le module csv fait partie de la bibliothèque standard de Python", True),
        A("On peut personnaliser le délimiteur utilisé (virgule, point-virgule, tabulation)", True),
        A("csv.writer() permet d'écrire des lignes dans un fichier CSV", True),
        A("Le module csv ne peut traiter que des fichiers encodés en UTF-16"),
    ]),
    TF("Il est recommandé d'ouvrir les fichiers CSV avec l'argument newline='' sous certains systèmes pour éviter des lignes vides ajoutées.", True),
    TF("Le module csv ne fonctionne qu'avec des fichiers dont l'extension est strictement '.csv'.", False),
])

add("Sérialisation avec pickle", "Comprendre la sérialisation binaire d'objets Python avec le module pickle.", [
    Q("Quel module de la bibliothèque standard permet de sérialiser des objets Python complexes en format binaire ?", "single", [
        A("pickle", True),
        A("json"),
        A("csv"),
        A("marshal_data"),
    ]),
    Q("Quelle fonction de pickle permet de convertir un objet Python en flux d'octets (bytes) ?", "single", [
        A("pickle.dumps()", True),
        A("pickle.loads()"),
        A("pickle.encode()"),
        A("pickle.write()"),
    ]),
    Q("Pourquoi est-il déconseillé de désérialiser (unpickle) des données provenant de sources non fiables ?", "single", [
        A("Cela peut exécuter du code arbitraire et poser un risque de sécurité", True),
        A("Cela n'a aucun risque particulier"),
        A("Cela ralentit uniquement le programme"),
        A("pickle refuse automatiquement les sources externes"),
    ]),
    Q("Parmi ces affirmations sur pickle, lesquelles sont vraies ?", "multiple", [
        A("pickle peut sérialiser des objets Python personnalisés, contrairement à json qui se limite aux types simples", True),
        A("Le format produit par pickle est binaire et non lisible directement comme du texte", True),
        A("pickle.load() permet de désérialiser depuis un fichier ouvert en mode binaire", True),
        A("pickle produit toujours un résultat strictement identique à json"),
    ]),
    TF("Le module pickle fait partie de la bibliothèque standard de Python.", True),
    TF("Les fichiers produits par pickle sont destinés à être lus et modifiés facilement par un humain dans un éditeur de texte.", False),
])

add("Programmation fonctionnelle : functools", "Découvrir reduce, partial et lru_cache du module functools.", [
    Q("Quelle fonction de functools permet de cumuler les éléments d'un itérable via une fonction binaire, comme une somme cumulative ?", "single", [
        A("functools.reduce()", True),
        A("functools.partial()"),
        A("functools.cache()"),
        A("functools.apply()"),
    ]),
    Q("À quoi sert `functools.partial()` ?", "single", [
        A("À créer une nouvelle fonction avec certains arguments déjà fixés", True),
        A("À paralléliser l'exécution d'une fonction"),
        A("À transformer une fonction en générateur"),
        A("À supprimer certains arguments d'une fonction"),
    ]),
    Q("À quoi sert le décorateur `functools.lru_cache` ?", "single", [
        A("À mémoriser (cache) les résultats d'une fonction pour éviter de recalculer les mêmes appels", True),
        A("À limiter le nombre d'arguments d'une fonction"),
        A("À convertir une fonction en méthode de classe"),
        A("À forcer l'exécution séquentielle d'une fonction"),
    ]),
    Q("Parmi ces fonctions, lesquelles appartiennent au module functools ?", "multiple", [
        A("reduce", True),
        A("partial", True),
        A("lru_cache", True),
        A("compress"),
    ]),
    TF("functools.reduce(lambda a, b: a + b, [1, 2, 3, 4]) retourne 10.", True),
    TF("functools.lru_cache ne peut être utilisé que sur des fonctions sans aucun argument.", False),
])

add("Gestion de la mémoire et identité des objets", "Comprendre id(), le garbage collector et les petites optimisations de CPython.", [
    Q("Que retourne la fonction `id(objet)` en Python ?", "single", [
        A("Un identifiant unique représentant l'adresse mémoire (ou équivalent) de l'objet durant sa vie", True),
        A("Le type de l'objet"),
        A("La taille en octets de l'objet"),
        A("Le nom de la variable"),
    ]),
    Q("Pourquoi `a = 5; b = 5; a is b` retourne souvent True dans CPython pour de petits entiers ?", "single", [
        A("CPython met en cache (interning) les petits entiers, qui partagent alors le même objet en mémoire", True),
        A("C'est toujours faux, il y a une erreur dans l'énoncé"),
        A("Les entiers sont toujours des objets distincts en Python"),
        A("Cela dépend uniquement du système d'exploitation"),
    ]),
    Q("Quel mécanisme Python utilise-t-il principalement pour libérer automatiquement la mémoire des objets non référencés ?", "single", [
        A("Le comptage de références (reference counting), complété par un ramasse-miettes (garbage collector)", True),
        A("Une libération manuelle obligatoire avec del uniquement"),
        A("Aucun mécanisme, Python ne libère jamais la mémoire"),
        A("Une compilation préalable en code machine"),
    ]),
    Q("Parmi ces affirmations sur la gestion mémoire en Python, lesquelles sont vraies ?", "multiple", [
        A("L'instruction del supprime une référence à un objet, pas nécessairement l'objet lui-même immédiatement", True),
        A("Le module gc permet d'interagir avec le ramasse-miettes", True),
        A("Un objet est généralement libéré quand son compteur de références atteint zéro", True),
        A("Python alloue la mémoire de façon strictement identique à C, sans aucune abstraction"),
    ]),
    TF("La fonction sys.getsizeof() permet d'obtenir une estimation de la taille en mémoire d'un objet Python.", True),
    TF("En Python, deux grandes chaînes de caractères identiques créées séparément sont toujours automatiquement le même objet en mémoire (is renvoie toujours True).", False),
])

add("Encodage de caractères et bytes", "Comprendre la différence entre str et bytes, encode et decode.", [
    Q("Quelle méthode permet de convertir une chaîne str en objet bytes ?", "single", [
        A("encode()", True),
        A("decode()"),
        A("bytes_convert()"),
        A("to_bytes_str()"),
    ]),
    Q("Quelle méthode permet de convertir un objet bytes en chaîne str ?", "single", [
        A("decode()", True),
        A("encode()"),
        A("str_convert()"),
        A("to_string()"),
    ]),
    Q("Quel est l'encodage le plus couramment recommandé par défaut pour encoder du texte en bytes en Python ?", "single", [
        A("UTF-8", True),
        A("ASCII strict"),
        A("Latin-1 obligatoirement"),
        A("UTF-32 uniquement"),
    ]),
    Q("Parmi ces affirmations sur str et bytes en Python 3, lesquelles sont vraies ?", "multiple", [
        A("str représente du texte Unicode, bytes représente des données binaires brutes", True),
        A("On ne peut pas concaténer directement un str et un bytes avec + sans conversion", True),
        A("Un littéral bytes s'écrit avec le préfixe b, par exemple b'hello'", True),
        A("str et bytes sont strictement le même type en Python 3"),
    ]),
    TF("En Python 3, str et bytes sont deux types distincts, contrairement à Python 2 où str se comportait plus comme des bytes.", True),
    TF("La méthode encode() appliquée à un objet bytes permet de le convertir en str.", False),
])

add("Programmation orientée objet : composition", "Distinguer la composition de l'héritage comme stratégie de conception.", [
    Q("Qu'est-ce que la composition en programmation orientée objet ?", "single", [
        A("Construire une classe en y intégrant des instances d'autres classes comme attributs", True),
        A("Faire hériter une classe d'une autre classe"),
        A("Utiliser uniquement des fonctions sans aucune classe"),
        A("Définir une classe sans aucun attribut"),
    ]),
    Q("Quel principe de conception orientée objet résume l'idée 'préférer la composition à l'héritage' lorsque c'est pertinent ?", "single", [
        A("Favoriser des relations 'a un' (has-a) plutôt que des relations 'est un' (is-a) quand cela réduit le couplage", True),
        A("Toujours utiliser l'héritage multiple"),
        A("Ne jamais utiliser de classes"),
        A("Dupliquer le code dans chaque classe"),
    ]),
    Q("Si une classe Voiture possède un attribut moteur qui est une instance de la classe Moteur, quelle relation cela illustre-t-il ?", "single", [
        A("Une relation de composition ('a un' moteur)", True),
        A("Une relation d'héritage"),
        A("Une relation d'interface"),
        A("Aucune relation, ce sont deux objets indépendants"),
    ]),
    Q("Parmi ces affirmations sur la composition, lesquelles sont vraies ?", "multiple", [
        A("La composition permet de réutiliser du code sans créer de lien hiérarchique strict entre classes", True),
        A("La composition peut réduire le couplage par rapport à un héritage profond", True),
        A("Une classe composée peut déléguer certains appels de méthode à l'objet qu'elle contient", True),
        A("La composition est strictement interdite en Python"),
    ]),
    TF("La composition et l'héritage peuvent coexister dans une même conception orientée objet.", True),
    TF("La composition signifie qu'une classe hérite obligatoirement d'une autre classe.", False),
])

add("Le mot-clé pass et les corps de fonction vides", "Comprendre l'utilité du mot-clé pass en Python.", [
    Q("À quoi sert le mot-clé `pass` en Python ?", "single", [
        A("À indiquer un bloc syntaxiquement requis mais qui ne fait rien (no-op)", True),
        A("À passer à la ligne suivante du programme"),
        A("À arrêter l'exécution du programme"),
        A("À ignorer une exception silencieusement"),
    ]),
    Q("Pourquoi `def ma_fonction(): pass` est-elle valide alors que `def ma_fonction():` seul provoquerait une erreur ?", "single", [
        A("Parce que Python exige un corps de bloc non vide après les deux-points, et pass fournit ce contenu minimal", True),
        A("Les deux syntaxes sont strictement interdites"),
        A("pass n'a aucun effet sur la validité syntaxique"),
        A("def ma_fonction(): seul est en réalité tout à fait valide aussi"),
    ]),
    Q("Dans quel contexte utilise-t-on souvent `pass` lors du développement progressif d'un programme ?", "single", [
        A("Comme espace réservé (placeholder) pour une classe ou fonction à implémenter plus tard", True),
        A("Uniquement dans les boucles infinies"),
        A("Pour remplacer définitivement return"),
        A("Pour fermer un fichier ouvert"),
    ]),
    Q("Parmi ces emplacements, lesquels peuvent légitimement contenir uniquement l'instruction pass ?", "multiple", [
        A("Le corps d'une fonction non encore implémentée", True),
        A("Le corps d'une classe vide", True),
        A("Une branche except qui ignore volontairement l'erreur", True),
        A("Un import de module"),
    ]),
    TF("L'instruction pass ne produit aucun effet à l'exécution, elle existe uniquement pour satisfaire la syntaxe.", True),
    TF("pass et continue ont exactement le même effet à l'intérieur d'une boucle.", False),
])

add("Conversion de types (casting) explicite", "Maîtriser les conversions explicites entre int, float, str, list, etc.", [
    Q("Que retourne `int('42')` ?", "single", [
        A("42", True),
        A("'42'"),
        A("42.0"),
        A("Une erreur"),
    ]),
    Q("Que retourne `int('abc')` ?", "single", [
        A("0"),
        A("Une exception ValueError", True),
        A("None"),
        A("'abc'"),
    ]),
    Q("Que retourne `str(3.14)` ?", "single", [
        A("'3.14'", True),
        A("3.14"),
        A("Une erreur"),
        A("'3'"),
    ]),
    Q("Parmi ces conversions, lesquelles s'exécutent sans erreur en Python ?", "multiple", [
        A("float('3.5')", True),
        A("list('abc')", True),
        A("int(3.9)", True),
        A("int('3.9')"),
    ]),
    TF("La conversion `int(3.9)` tronque la partie décimale et retourne 3 (et non 4, ce n'est pas un arrondi).", True),
    TF("La fonction list() appliquée à une chaîne retourne une liste de ses caractères individuels.", True),
])

add("Espaces de noms et résolution de noms (LEGB)", "Comprendre la règle LEGB de résolution des identifiants en Python.", [
    Q("Que signifie l'acronyme LEGB en Python concernant la résolution des noms de variables ?", "single", [
        A("Local, Enclosing, Global, Built-in : l'ordre de recherche d'un nom de variable", True),
        A("Liste, Ensemble, Générateur, Booléen"),
        A("Une commande spécifique du module sys"),
        A("Un type de boucle avancée"),
    ]),
    Q("Dans quel ordre Python recherche-t-il un identifiant utilisé dans une fonction imbriquée, selon la règle LEGB ?", "single", [
        A("D'abord local, puis englobant (enclosing), puis global, puis built-in", True),
        A("D'abord built-in, puis global, puis local"),
        A("Uniquement dans la portée globale"),
        A("Aléatoirement selon l'ordre de déclaration"),
    ]),
    Q("Que désigne la portée 'built-in' dans la règle LEGB ?", "single", [
        A("L'espace de noms contenant les fonctions et noms intégrés à Python comme print, len, etc.", True),
        A("Les variables définies par l'utilisateur uniquement"),
        A("Le système de fichiers du projet"),
        A("Les modules tiers installés via pip"),
    ]),
    Q("Parmi ces affirmations sur la résolution de noms en Python, lesquelles sont vraies ?", "multiple", [
        A("Une variable locale masque une variable globale de même nom à l'intérieur de la fonction", True),
        A("Le mot-clé global permet de remonter explicitement à la portée globale pour une réaffectation", True),
        A("Les noms comme print ou len appartiennent à la portée built-in", True),
        A("La portée 'enclosing' n'existe que pour les classes, jamais pour les fonctions"),
    ]),
    TF("Une fonction interne peut accéder en lecture à une variable définie dans la fonction externe qui l'entoure (portée 'enclosing').", True),
    TF("La règle LEGB signifie que Python cherche toujours en priorité dans la portée globale avant la portée locale.", False),
])

add("Vérité, égalité et identité combinées", "Synthèse sur bool(), == et is dans des cas pratiques.", [
    Q("Que retourne `[] == []` (deux listes vides distinctes) ?", "single", [
        A("True", True),
        A("False"),
        A("None"),
        A("Une erreur"),
    ]),
    Q("Que retourne `not []` (liste vide) ?", "single", [
        A("True", True),
        A("False"),
        A("[]"),
        A("Une erreur"),
    ]),
    Q("Pourquoi est-il généralement déconseillé d'utiliser `==` pour comparer une variable à None, et préférer `is` ?", "single", [
        A("Parce qu'un objet personnalisé pourrait redéfinir __eq__ de façon inattendue, alors que is compare toujours l'identité réelle", True),
        A("Parce que == ne fonctionne pas du tout avec None"),
        A("Il n'y a en réalité aucune raison, les deux sont strictement interchangeables dans tous les cas"),
        A("Parce que is est plus lent que =="),
    ]),
    Q("Parmi ces expressions, lesquelles retournent True ?", "multiple", [
        A("'' == ''", True),
        A("bool([1,2,3])", True),
        A("10 == 10.0", True),
        A("[1] is [1]"),
    ]),
    TF("Deux objets peuvent être égaux avec == sans être le même objet en mémoire (is renverrait False).", True),
    TF("bool(None) retourne True.", False),
])

add("Le module sys et les arguments de ligne de commande", "Découvrir sys.argv et quelques fonctions de base du module sys.", [
    Q("Quelle variable du module sys contient la liste des arguments passés au script en ligne de commande ?", "single", [
        A("sys.argv", True),
        A("sys.args"),
        A("sys.params"),
        A("sys.input"),
    ]),
    Q("Que contient toujours `sys.argv[0]` ?", "single", [
        A("Le nom (ou chemin) du script exécuté lui-même", True),
        A("Le premier argument fourni par l'utilisateur"),
        A("Toujours une chaîne vide"),
        A("Le nom de l'interpréteur Python"),
    ]),
    Q("Quelle fonction du module sys permet de quitter immédiatement un script avec un code de sortie donné ?", "single", [
        A("sys.exit()", True),
        A("sys.stop()"),
        A("sys.quit()"),
        A("sys.terminate()"),
    ]),
    Q("Parmi ces attributs/fonctions, lesquels appartiennent au module sys ?", "multiple", [
        A("sys.path", True),
        A("sys.version", True),
        A("sys.exit()", True),
        A("sys.read_args()"),
    ]),
    TF("Le module sys fait partie de la bibliothèque standard de Python et ne nécessite pas d'installation via pip.", True),
    TF("sys.argv contient uniquement les arguments, sans jamais inclure le nom du script.", False),
])

add("Découpage de problèmes : fonctions pures et effets de bord", "Distinguer fonctions pures et fonctions à effets de bord en Python.", [
    Q("Qu'est-ce qu'une fonction pure en programmation ?", "single", [
        A("Une fonction qui, pour les mêmes arguments, retourne toujours le même résultat sans modifier d'état extérieur", True),
        A("Une fonction qui n'a jamais de paramètres"),
        A("Une fonction qui affiche toujours quelque chose à l'écran"),
        A("Une fonction qui ne retourne jamais de valeur"),
    ]),
    Q("Lequel de ces exemples illustre un effet de bord typique dans une fonction Python ?", "single", [
        A("Modifier une variable globale ou une liste passée en argument depuis l'intérieur de la fonction", True),
        A("Retourner simplement la somme de deux paramètres"),
        A("Calculer un carré sans rien modifier d'extérieur"),
        A("Une fonction qui ne fait que des calculs locaux sans état partagé"),
    ]),
    Q("Pourquoi les fonctions pures sont-elles souvent plus simples à tester unitairement ?", "single", [
        A("Parce que leur résultat dépend uniquement de leurs arguments, sans état caché à simuler", True),
        A("Parce qu'elles n'acceptent jamais d'arguments"),
        A("Parce qu'elles sont toujours plus courtes en nombre de lignes"),
        A("Cela n'a aucun rapport avec la testabilité"),
    ]),
    Q("Parmi ces affirmations sur les fonctions pures, lesquelles sont vraies ?", "multiple", [
        A("Une fonction pure ne dépend pas d'un état externe mutable", True),
        A("Une fonction pure ne modifie pas les arguments qu'on lui passe", True),
        A("Les fonctions pures favorisent la prévisibilité et facilitent les tests", True),
        A("Toutes les fonctions Python sont obligatoirement pures par défaut"),
    ]),
    TF("Une fonction qui modifie une liste mutable reçue en argument (par exemple via append) introduit un effet de bord visible à l'appelant.", True),
    TF("Une fonction pure peut légitimement afficher un message avec print() sans que cela soit considéré comme un effet de bord.", False),
])

add("Listes vs générateurs : performance et mémoire", "Comparer les compréhensions de liste et les expressions génératrices.", [
    Q("Quelle est la principale différence de comportement mémoire entre `[x for x in range(1000000)]` et `(x for x in range(1000000))` ?", "single", [
        A("La liste stocke tous les éléments en mémoire immédiatement, le générateur les produit à la demande", True),
        A("Il n'y a aucune différence de mémoire entre les deux"),
        A("Le générateur consomme toujours plus de mémoire que la liste"),
        A("La liste ne peut contenir que 1000 éléments maximum"),
    ]),
    Q("Dans quel cas privilégier une expression génératrice plutôt qu'une liste complète ?", "single", [
        A("Quand on traite une grande séquence de données une seule fois, séquentiellement, sans besoin d'accès aléatoire", True),
        A("Quand on a besoin d'accéder plusieurs fois aux éléments par index"),
        A("Quand on veut absolument utiliser plus de mémoire"),
        A("Jamais, les générateurs sont toujours moins efficaces"),
    ]),
    Q("Que se passe-t-il si on essaie d'utiliser len() directement sur une expression génératrice ?", "single", [
        A("Une exception TypeError est levée, car les générateurs n'ont pas de longueur connue à l'avance", True),
        A("Cela retourne toujours 0"),
        A("Cela fonctionne normalement comme pour une liste"),
        A("Cela retourne automatiquement l'infini"),
    ]),
    Q("Parmi ces affirmations comparant listes et générateurs, lesquelles sont vraies ?", "multiple", [
        A("Une liste peut être parcourue plusieurs fois, un générateur s'épuise après un seul parcours complet", True),
        A("Un générateur peut représenter une séquence potentiellement infinie sans consommer toute la mémoire", True),
        A("Les deux peuvent être parcourus avec une boucle for", True),
        A("Une liste est toujours plus rapide à créer qu'un générateur, sans exception"),
    ]),
    TF("Convertir un générateur déjà épuisé en liste avec list() renvoie une liste vide.", True),
    TF("Les expressions génératrices utilisent la même syntaxe que les compréhensions de liste, mais avec des parenthèses au lieu de crochets.", True),
])

add("Tests unitaires avec unittest et assert", "Découvrir les bases des tests automatisés en Python.", [
    Q("Quel module de la bibliothèque standard Python fournit un framework de tests unitaires orienté objet ?", "single", [
        A("unittest", True),
        A("test"),
        A("checker"),
        A("verify"),
    ]),
    Q("Quelle instruction Python permet de vérifier rapidement une condition et de lever une AssertionError si elle est fausse ?", "single", [
        A("assert", True),
        A("check"),
        A("verify"),
        A("test"),
    ]),
    Q("Dans une classe de test héritant de unittest.TestCase, quelle méthode est typiquement utilisée pour vérifier qu'une valeur correspond à une valeur attendue ?", "single", [
        A("self.assertEqual(valeur, attendu)", True),
        A("self.checkEqual(valeur, attendu)"),
        A("self.isEqual(valeur, attendu)"),
        A("self.compare(valeur, attendu)"),
    ]),
    Q("Parmi ces affirmations sur les tests unitaires en Python, lesquelles sont vraies ?", "multiple", [
        A("unittest fait partie de la bibliothèque standard de Python", True),
        A("Les méthodes de test dans unittest commencent généralement par test_", True),
        A("L'instruction assert peut être utilisée en dehors de tout framework de test", True),
        A("Les tests unitaires garantissent l'absence totale de tout bug dans le programme"),
    ]),
    TF("L'instruction assert peut être désactivée globalement en exécutant Python avec l'option -O (optimisation).", True),
    TF("Le module unittest nécessite obligatoirement une installation via pip, il n'est pas inclus avec Python.", False),
])

add("Bonnes pratiques de nommage et PEP 8", "Découvrir les conventions de style recommandées par la PEP 8.", [
    Q("Quelle convention de casse la PEP 8 recommande-t-elle pour les noms de variables et de fonctions ?", "single", [
        A("snake_case (mots en minuscules séparés par des underscores)", True),
        A("camelCase"),
        A("PascalCase"),
        A("CONSTANTCASE"),
    ]),
    Q("Quelle convention de casse la PEP 8 recommande-t-elle pour les noms de classes ?", "single", [
        A("PascalCase (ou CapWords), par exemple MaClasse", True),
        A("snake_case"),
        A("camelCase"),
        A("kebab-case"),
    ]),
    Q("Quelle convention est généralement utilisée pour nommer une constante au niveau du module en Python ?", "single", [
        A("Toutes les lettres en majuscules avec underscores, par exemple TAUX_TVA", True),
        A("camelCase"),
        A("Toujours préfixée par const_"),
        A("Aucune convention n'existe pour les constantes"),
    ]),
    Q("Parmi ces recommandations, lesquelles font partie des conseils de la PEP 8 ?", "multiple", [
        A("Utiliser 4 espaces par niveau d'indentation", True),
        A("Limiter la longueur des lignes (traditionnellement autour de 79 caractères)", True),
        A("Nommer les fonctions en snake_case", True),
        A("Toujours utiliser des tabulations plutôt que des espaces"),
    ]),
    TF("La PEP 8 est un guide de style officiel pour écrire du code Python lisible et cohérent.", True),
    TF("Respecter la PEP 8 est une obligation imposée par l'interpréteur Python, qui refuse d'exécuter du code non conforme.", False),
])

# ===================== BLOC 7 : FINAL (quiz 78-100) =====================

add("Multi-héritage et l'ordre de résolution des méthodes (MRO)", "Comprendre le MRO et la fonction super() dans un contexte d'héritage multiple.", [
    Q("Que signifie l'acronyme MRO en Python ?", "single", [
        A("Method Resolution Order, l'ordre dans lequel Python recherche les méthodes parmi les classes parentes", True),
        A("Multiple Return Object"),
        A("Module Registration Order"),
        A("Memory Reference Optimization"),
    ]),
    Q("Quel algorithme Python utilise-t-il pour déterminer le MRO en cas d'héritage multiple ?", "single", [
        A("L'algorithme C3 linearization", True),
        A("Un tri alphabétique des classes parentes"),
        A("L'ordre inverse de déclaration des classes parentes"),
        A("Un choix aléatoire à chaque exécution"),
    ]),
    Q("Quelle méthode/attribut permet d'afficher l'ordre de résolution des méthodes d'une classe en Python ?", "single", [
        A("NomClasse.__mro__ ou NomClasse.mro()", True),
        A("NomClasse.order()"),
        A("NomClasse.resolution()"),
        A("NomClasse.hierarchy()"),
    ]),
    Q("Parmi ces affirmations sur l'héritage multiple en Python, lesquelles sont vraies ?", "multiple", [
        A("Une classe peut hériter de plusieurs classes parentes en les listant entre parenthèses", True),
        A("super() suit l'ordre du MRO et non nécessairement l'ordre littéral d'héritage", True),
        A("Le MRO garantit qu'une classe apparaît avant ses propres parents dans la liste de résolution", True),
        A("Python interdit totalement l'héritage multiple, contrairement à C++"),
    ]),
    TF("Le problème du diamant (diamond problem) peut survenir en cas d'héritage multiple avec une classe ancêtre commune.", True),
    TF("L'héritage multiple n'existe pas du tout en Python.", False),
])

add("Métaclasses : notions introductives", "Découvrir le concept de métaclasse comme 'classe qui crée des classes'.", [
    Q("Quelle est la métaclasse par défaut de toutes les classes Python (sauf si une métaclasse personnalisée est précisée) ?", "single", [
        A("type", True),
        A("object"),
        A("class"),
        A("meta"),
    ]),
    Q("Comment décrit-on succinctement une métaclasse en Python ?", "single", [
        A("Une classe dont les instances sont elles-mêmes des classes", True),
        A("Une fonction qui retourne toujours None"),
        A("Un module spécial de la bibliothèque standard"),
        A("Un synonyme strict du mot-clé class"),
    ]),
    Q("Quel paramètre de la déclaration de classe permet de spécifier une métaclasse personnalisée ?", "single", [
        A("class MaClasse(metaclass=MaMetaclasse):", True),
        A("class MaClasse(meta=MaMetaclasse):"),
        A("class MaClasse uses MaMetaclasse:"),
        A("class MaClasse::MaMetaclasse:"),
    ]),
    Q("Parmi ces affirmations sur les métaclasses, lesquelles sont vraies ?", "multiple", [
        A("Les métaclasses permettent de personnaliser la création des classes elles-mêmes", True),
        A("type() peut être utilisé pour créer dynamiquement une nouvelle classe à l'exécution", True),
        A("La plupart des développeurs Python n'ont jamais besoin de définir leurs propres métaclasses", True),
        A("Une métaclasse est obligatoire pour définir n'importe quelle classe simple"),
    ]),
    TF("En Python, les classes sont elles-mêmes des objets, instances de leur métaclasse.", True),
    TF("Toute classe Python doit obligatoirement définir explicitement sa métaclasse, sinon le code ne s'exécute pas.", False),
])

add("Décorateurs paramétrés", "Construire des décorateurs qui acceptent eux-mêmes des arguments.", [
    Q("Pourquoi un décorateur paramétré (comme `@repeat(3)`) nécessite-t-il un niveau d'imbrication de fonctions supplémentaire ?", "single", [
        A("Parce que l'appel @repeat(3) doit d'abord retourner le décorateur réel, qui sera ensuite appliqué à la fonction", True),
        A("Ce n'est techniquement pas possible en Python"),
        A("Parce que Python limite les décorateurs à zéro argument"),
        A("Parce qu'il faut redéfinir la classe Decorator chaque fois"),
    ]),
    Q("Dans `def repeat(n): def decorateur(fonction): ... return decorateur`, à quoi correspond le rôle de `repeat` ?", "single", [
        A("Une fabrique de décorateur (decorator factory) qui retourne le décorateur configuré avec n", True),
        A("Une simple fonction sans rapport avec le décorateur"),
        A("Le décorateur final appliqué directement à la fonction"),
        A("Une classe abstraite"),
    ]),
    Q("Quel est l'ordre d'application si on empile `@decorateur_a` puis `@decorateur_b` juste au-dessus d'une fonction `def f():` ?", "single", [
        A("decorateur_a(decorateur_b(f)) : le plus proche de la fonction s'applique en premier", True),
        A("decorateur_b(decorateur_a(f))"),
        A("Les deux s'appliquent simultanément sans ordre défini"),
        A("Seul le premier décorateur listé est réellement appliqué"),
    ]),
    Q("Parmi ces affirmations sur les décorateurs paramétrés, lesquelles sont vraies ?", "multiple", [
        A("Ils permettent de configurer le comportement du décorateur via des arguments", True),
        A("Ils nécessitent généralement trois niveaux de fonctions imbriquées (fabrique, décorateur, wrapper)", True),
        A("functools.wraps reste utile pour préserver les métadonnées de la fonction décorée", True),
        A("Un décorateur paramétré ne peut jamais être réutilisé sur plusieurs fonctions différentes"),
    ]),
    TF("Un décorateur paramétré comme @repeat(3) est en réalité un appel de fonction qui retourne le véritable décorateur.", True),
    TF("Les décorateurs paramétrés sont interdits en Python, seuls les décorateurs simples sans argument existent.", False),
])

add("Gestion des erreurs : bonnes pratiques avec except", "Approfondir les bonnes pratiques de capture sélective des exceptions.", [
    Q("Pourquoi est-il généralement déconseillé d'utiliser un `except:` nu (sans préciser de type d'exception) ?", "single", [
        A("Parce qu'il capture absolument toutes les exceptions, y compris celles qu'on ne voudrait pas masquer, comme KeyboardInterrupt", True),
        A("Parce que la syntaxe n'est pas valide en Python"),
        A("Parce qu'il ne capture aucune exception réelle"),
        A("Il n'y a en réalité aucun inconvénient à l'utiliser"),
    ]),
    Q("Quelle est la bonne pratique recommandée pour capturer une exception tout en gardant une trace utile ?", "single", [
        A("Capturer le type précis d'exception attendu et, si besoin, le logger ou le relancer avec des informations utiles", True),
        A("Toujours ignorer silencieusement l'exception sans rien faire"),
        A("Toujours arrêter le programme immédiatement avec exit()"),
        A("Ne jamais utiliser try/except, uniquement des if préventifs"),
    ]),
    Q("Que permet de faire la clause `except (TypeError, ValueError) as e:` ?", "single", [
        A("Capturer deux types d'exceptions différents dans un seul bloc except, en récupérant l'objet exception dans e", True),
        A("Capturer uniquement TypeError, ValueError étant ignoré"),
        A("Une erreur de syntaxe, on ne peut pas grouper les exceptions ainsi"),
        A("Créer deux nouvelles exceptions personnalisées"),
    ]),
    Q("Parmi ces pratiques, lesquelles sont considérées comme de bonnes pratiques de gestion d'exceptions ?", "multiple", [
        A("Capturer des exceptions spécifiques plutôt qu'Exception de façon trop générale", True),
        A("Utiliser finally pour libérer des ressources, qu'il y ait eu erreur ou non", True),
        A("Documenter ou logger les exceptions capturées plutôt que les ignorer silencieusement", True),
        A("Toujours utiliser un except nu pour être certain de tout capturer"),
    ]),
    TF("Capturer Exception de manière trop large peut masquer des bugs réels qui auraient dû interrompre le programme.", True),
    TF("L'ordre des clauses except n'a strictement aucune importance, même si certaines exceptions sont des sous-classes d'autres.", False),
])

add("Slicing avancé et modification de listes par tranche", "Approfondir le slicing pour insérer, remplacer ou supprimer des portions de liste.", [
    Q("Soit `liste = [1, 2, 3, 4, 5]`. Que devient `liste` après `liste[1:3] = [9, 9, 9]` ?", "single", [
        A("[1, 9, 9, 9, 4, 5]", True),
        A("[1, 9, 9, 4, 5]"),
        A("[9, 9, 9, 4, 5]"),
        A("Une erreur"),
    ]),
    Q("Soit `liste = [1, 2, 3, 4, 5]`. Que devient `liste` après `del liste[1:3]` ?", "single", [
        A("[1, 4, 5]", True),
        A("[1, 2, 5]"),
        A("[4, 5]"),
        A("Une erreur"),
    ]),
    Q("Comment vider complètement le contenu d'une liste existante sans changer sa référence (utile si d'autres variables y pointent) ?", "single", [
        A("liste[:] = []", True),
        A("liste = None"),
        A("del liste"),
        A("liste.remove()"),
    ]),
    Q("Parmi ces opérations sur `liste = [1, 2, 3, 4, 5]`, lesquelles modifient effectivement la liste en place ?", "multiple", [
        A("liste[0:2] = [0]", True),
        A("liste.clear()", True),
        A("del liste[0]", True),
        A("nouvelle = liste[:]"),
    ]),
    TF("L'affectation par slicing comme liste[1:3] = [9, 9, 9] peut changer la longueur totale de la liste si le nombre d'éléments insérés diffère de la tranche remplacée.", True),
    TF("L'instruction `liste[:] = []` crée une toute nouvelle liste à une adresse mémoire différente.", False),
])

add("Walrus operator et nouveautés syntaxiques récentes", "Découvrir l'opérateur d'affectation expressive := introduit par Python 3.8.", [
    Q("Quel symbole représente le 'walrus operator' introduit en Python 3.8 ?", "single", [
        A(":=", True),
        A("=:"),
        A("::"),
        A("=>"),
    ]),
    Q("À quoi sert principalement le walrus operator `:=` ?", "single", [
        A("À affecter une valeur à une variable au sein même d'une expression, par exemple dans une condition while", True),
        A("À comparer deux valeurs pour l'égalité"),
        A("À créer un dictionnaire rapidement"),
        A("À déclarer une constante immuable"),
    ]),
    Q("Dans `if (n := len(donnees)) > 10:`, que se passe-t-il concrètement ?", "single", [
        A("La variable n reçoit la valeur de len(donnees), qui est ensuite comparée à 10 dans la même expression", True),
        A("Une erreur de syntaxe est levée car cette construction n'existe pas"),
        A("n est comparé directement à donnees"),
        A("Cela crée une nouvelle fonction nommée n"),
    ]),
    Q("Parmi ces affirmations sur le walrus operator, lesquelles sont vraies ?", "multiple", [
        A("Il a été introduit avec Python 3.8", True),
        A("Il permet d'éviter de répéter un appel de fonction dans une condition et son corps", True),
        A("Il peut être utilisé à l'intérieur d'une compréhension de liste", True),
        A("Il remplace obligatoirement tous les signes égal = du langage"),
    ]),
    TF("Le walrus operator := affecte une valeur tout en retournant cette même valeur comme résultat de l'expression.", True),
    TF("Le walrus operator existe depuis la toute première version de Python.", False),
])

add("Le module operator", "Découvrir les équivalents fonctionnels des opérateurs avec le module operator.", [
    Q("Quelle fonction du module operator est équivalente à l'expression `a + b` ?", "single", [
        A("operator.add(a, b)", True),
        A("operator.plus(a, b)"),
        A("operator.sum(a, b)"),
        A("operator.combine(a, b)"),
    ]),
    Q("À quoi sert `operator.itemgetter('age')` couramment utilisé comme clé de tri ?", "single", [
        A("À récupérer la valeur associée à la clé 'age' d'un objet indexable comme un dictionnaire", True),
        A("À supprimer la clé 'age' d'un dictionnaire"),
        A("À créer un nouveau dictionnaire avec seulement la clé 'age'"),
        A("À vérifier si la clé 'age' existe"),
    ]),
    Q("Quelle fonction du module operator correspond à l'opérateur de multiplication `*` ?", "single", [
        A("operator.mul()", True),
        A("operator.multiply()"),
        A("operator.times()"),
        A("operator.product()"),
    ]),
    Q("Parmi ces fonctions, lesquelles appartiennent au module operator ?", "multiple", [
        A("operator.add", True),
        A("operator.itemgetter", True),
        A("operator.attrgetter", True),
        A("operator.merge"),
    ]),
    TF("Le module operator fournit des versions fonctionnelles des opérateurs, utiles notamment avec map(), filter() ou comme clé de tri.", True),
    TF("operator.itemgetter ne peut être utilisé qu'avec des dictionnaires, jamais avec des listes ou tuples.", False),
])

add("Validation de données et assertions défensives", "Utiliser assert et la levée d'exceptions pour valider des entrées de fonction.", [
    Q("Pourquoi privilégier `raise ValueError(...)` plutôt que `assert` pour valider les entrées d'une fonction destinée à être utilisée en production ?", "single", [
        A("Parce que les assertions peuvent être désactivées globalement avec l'option -O, alors que raise reste toujours actif", True),
        A("Parce que assert n'existe pas réellement en Python"),
        A("Parce que raise est plus rapide dans tous les cas"),
        A("Il n'y a aucune différence pratique entre les deux"),
    ]),
    Q("Que fait `assert age >= 0, 'L\\'âge doit être positif'` si age vaut -5 ?", "single", [
        A("Lève une AssertionError avec le message indiqué", True),
        A("Affiche simplement un avertissement sans interrompre le programme"),
        A("Corrige automatiquement la valeur à 0"),
        A("Ne fait rien, car assert ignore les messages personnalisés"),
    ]),
    Q("Dans quel contexte assert est-il le plus adapté en Python ?", "single", [
        A("Pour des vérifications de débogage ou des invariants internes pendant le développement", True),
        A("Pour valider systématiquement les entrées utilisateur en production"),
        A("Pour remplacer entièrement les boucles for"),
        A("Pour gérer les erreurs réseau critiques"),
    ]),
    Q("Parmi ces affirmations sur la validation défensive en Python, lesquelles sont vraies ?", "multiple", [
        A("Lever une exception explicite (ValueError, TypeError) documente clairement la nature du problème", True),
        A("Valider les types et valeurs des paramètres tôt permet de détecter des erreurs plus rapidement", True),
        A("Les assertions sont désactivées si Python est lancé avec l'option -O", True),
        A("Toute fonction doit obligatoirement utiliser assert pour valider chaque paramètre"),
    ]),
    TF("Une AssertionError non capturée interrompt l'exécution du programme, comme toute autre exception non gérée.", True),
    TF("Les instructions assert sont garanties de toujours s'exécuter, quelles que soient les options de lancement de l'interpréteur Python.", False),
])

add("Hashabilité et utilisation comme clé de dictionnaire", "Comprendre la notion de hashable et ses implications pratiques.", [
    Q("Pourquoi une liste ne peut-elle pas être utilisée comme clé dans un dictionnaire Python ?", "single", [
        A("Parce qu'elle est mutable et donc non hashable", True),
        A("Parce que les dictionnaires n'acceptent que des chaînes comme clés"),
        A("Parce que les listes sont trop volumineuses en mémoire"),
        A("Ce n'est pas vrai, les listes peuvent être utilisées comme clés sans problème"),
    ]),
    Q("Quelle fonction intégrée permet d'obtenir la valeur de hachage d'un objet hashable ?", "single", [
        A("hash()", True),
        A("hashcode()"),
        A("digest()"),
        A("checksum()"),
    ]),
    Q("Pourquoi un tuple contenant uniquement des éléments immuables peut-il être utilisé comme clé de dictionnaire, contrairement à une liste ?", "single", [
        A("Parce que le tuple lui-même est immuable et donc hashable si son contenu l'est aussi", True),
        A("Parce que les tuples sont toujours plus petits que les listes"),
        A("Ce n'est pas possible non plus pour les tuples"),
        A("Parce que Python convertit automatiquement le tuple en chaîne"),
    ]),
    Q("Parmi ces types, lesquels sont hashables et peuvent donc servir de clé de dictionnaire ?", "multiple", [
        A("str", True),
        A("int", True),
        A("tuple contenant uniquement des éléments immuables", True),
        A("list"),
    ]),
    TF("Un objet hashable doit avoir une valeur de hachage qui ne change jamais durant sa vie, ce qui est cohérent avec l'immuabilité.", True),
    TF("Un set (ensemble) peut lui-même être utilisé comme élément d'un autre set, car il est hashable.", False),
])

add("Fonctions de plus haut niveau et programmation fonctionnelle", "Synthèse sur les fonctions qui prennent ou retournent d'autres fonctions.", [
    Q("Qu'appelle-t-on une 'fonction d'ordre supérieur' (higher-order function) ?", "single", [
        A("Une fonction qui prend une autre fonction en argument, ou qui retourne une fonction", True),
        A("Une fonction qui s'exécute plus rapidement que les autres"),
        A("Une fonction définie au niveau le plus haut d'un module"),
        A("Une fonction qui ne peut être appelée qu'une seule fois"),
    ]),
    Q("Parmi map(), filter() et sorted(), pourquoi sont-elles qualifiées de fonctions d'ordre supérieur ?", "single", [
        A("Parce qu'elles acceptent une fonction (ou un callable) comme argument pour définir leur comportement", True),
        A("Parce qu'elles sont définies dans un module séparé nommé higher_order"),
        A("Parce qu'elles ne peuvent traiter que des nombres"),
        A("Ce n'est pas le cas, elles n'ont rien de spécial"),
    ]),
    Q("Que retourne une fonction fabrique comme `def multiplicateur(n): return lambda x: x * n` lorsqu'on appelle `multiplicateur(3)` ?", "single", [
        A("Une nouvelle fonction qui multiplie son argument par 3", True),
        A("Directement la valeur 3"),
        A("Une erreur de syntaxe"),
        A("None"),
    ]),
    Q("Parmi ces affirmations sur les fonctions d'ordre supérieur en Python, lesquelles sont vraies ?", "multiple", [
        A("En Python, les fonctions sont des objets de première classe pouvant être passées en argument", True),
        A("Une fonction peut retourner une autre fonction comme résultat", True),
        A("Les décorateurs sont un exemple concret de fonctions d'ordre supérieur", True),
        A("Seuls les langages fonctionnels purs permettent de passer des fonctions en argument"),
    ]),
    TF("En Python, on peut stocker une fonction dans une variable et la passer comme n'importe quel autre objet.", True),
    TF("Les fonctions en Python ne peuvent jamais être utilisées comme valeurs dans un dictionnaire.", False),
])

add("Tableaux multidimensionnels avec des listes imbriquées", "Manipuler des listes de listes pour représenter des matrices simples.", [
    Q("Comment représente-t-on typiquement une matrice 2x2 avec des listes imbriquées en Python ?", "single", [
        A("[[1, 2], [3, 4]]", True),
        A("(1, 2, 3, 4)"),
        A("{1: 2, 3: 4}"),
        A("[1, 2, 3, 4]"),
    ]),
    Q("Soit `matrice = [[1, 2], [3, 4]]`. Que retourne `matrice[1][0]` ?", "single", [
        A("2"),
        A("3", True),
        A("1"),
        A("4"),
    ]),
    Q("Pourquoi `[[0]*3]*3` est-il un piège courant pour créer une matrice 3x3 initialisée à zéro ?", "single", [
        A("Parce que les trois sous-listes sont en réalité la même liste partagée en mémoire, modifier l'une modifie les autres", True),
        A("Parce que cette syntaxe provoque une erreur immédiate"),
        A("Parce que cela crée une matrice de taille 9x9 au lieu de 3x3"),
        A("Il n'y a en réalité aucun piège, c'est la méthode recommandée"),
    ]),
    Q("Parmi ces façons de créer correctement une matrice 3x3 de zéros sans le piège du partage de référence, lesquelles fonctionnent ?", "multiple", [
        A("[[0 for _ in range(3)] for _ in range(3)]", True),
        A("[[0]*3 for _ in range(3)]", True),
        A("[list([0,0,0]) for _ in range(3)]", True),
        A("[[0]*3]*3"),
    ]),
    TF("Parcourir une matrice représentée par une liste de listes nécessite généralement deux boucles for imbriquées pour accéder à chaque élément.", True),
    TF("En Python natif (sans bibliothèque externe comme NumPy), il existe un type 'array2D' intégré dédié aux matrices.", False),
])

add("Constantes, énumérations et le module enum", "Découvrir le module enum pour représenter des ensembles de valeurs nommées.", [
    Q("Quel module de la bibliothèque standard permet de créer des énumérations en Python ?", "single", [
        A("enum", True),
        A("constants"),
        A("types"),
        A("static"),
    ]),
    Q("Comment définit-on typiquement une énumération des couleurs primaires avec le module enum ?", "single", [
        A("class Couleur(Enum): ROUGE = 1; VERT = 2; BLEU = 3", True),
        A("Couleur = ['ROUGE', 'VERT', 'BLEU']"),
        A("def Couleur(): return {'ROUGE': 1, 'VERT': 2, 'BLEU': 3}"),
        A("Couleur = Enum.create('ROUGE', 'VERT', 'BLEU')"),
    ]),
    Q("Quel est l'avantage principal d'utiliser une énumération (Enum) plutôt que de simples constantes entières séparées ?", "single", [
        A("Regrouper logiquement des valeurs liées sous un même espace de noms, avec des noms lisibles et un typage plus sûr", True),
        A("Les énumérations s'exécutent plus rapidement que n'importe quelle variable"),
        A("Les énumérations remplacent obligatoirement toutes les variables du programme"),
        A("Il n'y a aucun avantage réel"),
    ]),
    Q("Parmi ces affirmations sur le module enum, lesquelles sont vraies ?", "multiple", [
        A("Une classe Enum regroupe un ensemble fixe de membres nommés", True),
        A("On peut accéder à la valeur d'un membre via Couleur.ROUGE.value", True),
        A("Le module enum fait partie de la bibliothèque standard de Python", True),
        A("Les membres d'une Enum peuvent être librement modifiés après définition de la classe"),
    ]),
    TF("Une énumération Python rend explicite et lisible un ensemble limité de valeurs possibles, comme les jours de la semaine.", True),
    TF("Le module enum nécessite une installation séparée via pip avant de pouvoir être importé.", False),
])

add("Optimisation : éviter les pièges de performance courants", "Identifier quelques erreurs classiques de performance en Python.", [
    Q("Pourquoi concaténer une chaîne dans une boucle avec `+=` répété est-il généralement déconseillé pour de grandes quantités de texte ?", "single", [
        A("Parce que les chaînes sont immuables, chaque += crée une nouvelle chaîne en mémoire, ce qui devient coûteux", True),
        A("Parce que += est interdit sur les chaînes en Python"),
        A("Parce que cela ne fonctionne tout simplement pas"),
        A("Il n'y a en réalité aucun problème de performance"),
    ]),
    Q("Quelle alternative est généralement recommandée pour assembler efficacement de nombreux morceaux de texte ?", "single", [
        A("Accumuler les morceaux dans une liste puis utiliser str.join() à la fin", True),
        A("Utiliser uniquement des boucles while imbriquées"),
        A("Convertir le texte en liste de tuples"),
        A("Utiliser systématiquement des f-strings dans une boucle infinie"),
    ]),
    Q("Pourquoi tester l'appartenance avec `in` est-il généralement plus rapide sur un set que sur une liste pour de grandes collections ?", "single", [
        A("Parce que la recherche dans un set utilise le hachage, en moyenne en temps constant, contre un parcours linéaire pour une liste", True),
        A("Parce que les sets sont toujours plus petits que les listes"),
        A("Ce n'est pas vrai, c'est rigoureusement la même performance"),
        A("Parce que les listes ne supportent pas l'opérateur in"),
    ]),
    Q("Parmi ces pratiques, lesquelles sont généralement de bonnes pratiques de performance en Python ?", "multiple", [
        A("Utiliser des compréhensions plutôt que des boucles explicites quand cela améliore la clarté et la vitesse", True),
        A("Préférer un set ou un dict pour des tests d'appartenance fréquents", True),
        A("Éviter les imports inutiles dans une fonction appelée très fréquemment en boucle serrée", True),
        A("Toujours préférer une liste à un set, quel que soit le cas d'usage"),
    ]),
    TF("Le module timeit de la bibliothèque standard permet de mesurer précisément le temps d'exécution de petits extraits de code Python.", True),
    TF("Les listes et les sets ont exactement la même complexité algorithmique pour vérifier si un élément y est présent.", False),
])

add("Modules et packages : organisation d'un projet", "Comprendre la structure d'un package Python avec __init__.py.", [
    Q("Quel fichier spécial indique traditionnellement à Python qu'un dossier doit être traité comme un package ?", "single", [
        A("__init__.py", True),
        A("package.py"),
        A("main.py"),
        A("setup.cfg"),
    ]),
    Q("Quelle instruction permet d'importer un module nommé `utils.py` situé dans un sous-dossier `outils` traité comme un package ?", "single", [
        A("from outils import utils", True),
        A("import outils.utils.py"),
        A("include outils/utils"),
        A("require('outils/utils')"),
    ]),
    Q("Que se passe-t-il généralement quand un module est importé plusieurs fois dans différents fichiers d'un même programme ?", "single", [
        A("Python ne l'exécute réellement qu'une seule fois et réutilise le module déjà chargé en cache (sys.modules)", True),
        A("Le module est exécuté à chaque import, sans aucune mise en cache"),
        A("Cela provoque systématiquement une erreur de double import"),
        A("Seul le premier import fonctionne, les suivants sont ignorés silencieusement"),
    ]),
    Q("Parmi ces affirmations sur l'organisation en modules et packages, lesquelles sont vraies ?", "multiple", [
        A("Un package peut contenir des sous-packages imbriqués", True),
        A("Le fichier __init__.py peut rester vide tout en remplissant son rôle de marqueur de package", True),
        A("On peut utiliser des imports relatifs comme from . import module dans un package", True),
        A("Un seul fichier .py ne peut jamais constituer un module valide à lui seul"),
    ]),
    TF("sys.modules est un dictionnaire qui garde en cache les modules déjà importés durant l'exécution.", True),
    TF("Depuis Python 3.3, un fichier __init__.py est strictement obligatoire pour que tout dossier soit reconnu comme un package.", False),
])

add("Environnements virtuels et gestion des dépendances", "Comprendre l'utilité de venv et de pip pour isoler les projets Python.", [
    Q("À quoi sert principalement un environnement virtuel Python (créé par exemple avec le module venv) ?", "single", [
        A("À isoler les dépendances d'un projet pour éviter les conflits de versions entre projets", True),
        A("À accélérer l'exécution du code Python"),
        A("À remplacer complètement l'interpréteur Python par un autre langage"),
        A("À chiffrer le code source du projet"),
    ]),
    Q("Quel outil en ligne de commande est le plus couramment utilisé pour installer des paquets tiers en Python ?", "single", [
        A("pip", True),
        A("npm"),
        A("apt seulement"),
        A("composer"),
    ]),
    Q("Quel fichier liste traditionnellement les dépendances d'un projet Python pour pouvoir les réinstaller facilement avec pip ?", "single", [
        A("requirements.txt", True),
        A("package.json"),
        A("Gemfile"),
        A("dependencies.yaml"),
    ]),
    Q("Parmi ces affirmations sur les environnements virtuels et pip, lesquelles sont vraies ?", "multiple", [
        A("Le module venv fait partie de la bibliothèque standard de Python depuis la version 3.3", True),
        A("pip install nom_paquet permet d'installer un paquet depuis PyPI", True),
        A("Activer un environnement virtuel modifie temporairement le chemin de recherche des paquets utilisés", True),
        A("Un environnement virtuel partage obligatoirement les mêmes paquets installés que le système global"),
    ]),
    TF("Travailler dans un environnement virtuel permet d'avoir des versions différentes d'une même bibliothèque selon les projets.", True),
    TF("pip est un langage de programmation concurrent de Python.", False),
])

add("Débogage et le module logging", "Découvrir le module logging comme alternative structurée à print() pour le débogage.", [
    Q("Pourquoi le module logging est-il souvent préféré à print() pour le suivi d'une application en production ?", "single", [
        A("Parce qu'il permet de gérer des niveaux de gravité, des formats et des destinations (fichier, console) configurables", True),
        A("Parce que print() est interdit en Python"),
        A("Parce que logging s'exécute plus rapidement dans tous les cas"),
        A("Il n'y a en réalité aucune différence pratique"),
    ]),
    Q("Parmi ces niveaux de gravité, lequel est le plus élevé dans le module logging ?", "single", [
        A("DEBUG"),
        A("INFO"),
        A("CRITICAL", True),
        A("WARNING"),
    ]),
    Q("Quelle fonction du module logging permet d'enregistrer un message de niveau erreur ?", "single", [
        A("logging.error()", True),
        A("logging.fail()"),
        A("logging.crash()"),
        A("logging.print_error()"),
    ]),
    Q("Parmi ces affirmations sur le module logging, lesquelles sont vraies ?", "multiple", [
        A("logging fait partie de la bibliothèque standard de Python", True),
        A("On peut configurer le niveau minimal de gravité affiché avec basicConfig ou setLevel", True),
        A("Les messages de logging peuvent être redirigés vers un fichier plutôt que la console", True),
        A("logging ne propose qu'un seul niveau de gravité unique pour tous les messages"),
    ]),
    TF("L'ordre croissant de gravité standard dans logging est DEBUG, INFO, WARNING, ERROR, CRITICAL.", True),
    TF("Le module logging doit être installé séparément via pip avant de pouvoir être utilisé.", False),
])

add("Itérables personnalisés et la classe Iterable", "Créer une classe itérable personnalisée en implémentant __iter__ et __next__.", [
    Q("Que doit implémenter une classe pour être considérée comme un itérateur conforme au protocole d'itération de Python ?", "single", [
        A("Les méthodes __iter__() et __next__()", True),
        A("Uniquement la méthode __getitem__()"),
        A("La méthode __len__() uniquement"),
        A("Aucune méthode particulière n'est requise"),
    ]),
    Q("Que doit retourner la méthode __iter__() d'un objet itérable classique (non itérateur lui-même) ?", "single", [
        A("Un objet itérateur, capable de produire les éléments un par un via __next__", True),
        A("Toujours None"),
        A("Une liste complète de tous les éléments"),
        A("Le nombre total d'éléments"),
    ]),
    Q("Comment une classe peut-elle devenir itérable sans implémenter explicitement __iter__ et __next__, en utilisant un générateur ?", "single", [
        A("En définissant une méthode __iter__ qui est elle-même un générateur utilisant yield", True),
        A("Ce n'est pas possible sans implémenter manuellement __next__"),
        A("En héritant obligatoirement de la classe list"),
        A("En définissant uniquement __init__"),
    ]),
    Q("Parmi ces affirmations sur les itérables personnalisés, lesquelles sont vraies ?", "multiple", [
        A("Une classe peut être rendue itérable en définissant __iter__ pour qu'elle fonctionne dans une boucle for", True),
        A("Une classe implémentant __getitem__ avec des index entiers consécutifs peut aussi être itérée par Python (protocole alternatif)", True),
        A("Un objet personnalisé itérable peut être passé à des fonctions comme list() ou sorted()", True),
        A("Toute classe Python est automatiquement itérable par défaut sans aucune implémentation"),
    ]),
    TF("Si __iter__ d'une classe est définie comme un générateur (avec yield à l'intérieur), elle gère automatiquement l'état entre les appels successifs.", True),
    TF("Une classe qui ne définit ni __iter__ ni __getitem__ peut tout de même être utilisée directement dans une boucle for sans erreur.", False),
])

add("Tests de type avec isinstance et duck typing", "Comprendre isinstance(), type() et la philosophie du duck typing en Python.", [
    Q("Quelle fonction intégrée permet de vérifier si un objet est une instance d'une classe donnée (ou d'une sous-classe) ?", "single", [
        A("isinstance()", True),
        A("typeof()"),
        A("instanceof()"),
        A("checktype()"),
    ]),
    Q("Pourquoi `isinstance(objet, NomClasse)` est-il généralement préféré à `type(objet) == NomClasse` pour vérifier un type ?", "single", [
        A("Parce qu'isinstance() prend aussi en compte l'héritage (les sous-classes), contrairement à une comparaison stricte de type", True),
        A("Parce que type() ne fonctionne pas du tout en Python"),
        A("Les deux sont rigoureusement identiques dans tous les cas"),
        A("Parce qu'isinstance() est plus lent dans tous les cas"),
    ]),
    Q("Que signifie l'expression 'duck typing' en Python, en lien avec le proverbe 'si ça marche comme un canard...' ?", "single", [
        A("Un objet est considéré compatible avec un usage s'il possède les méthodes/attributs attendus, indépendamment de son type déclaré", True),
        A("Une technique de typage strict obligatoire en Python"),
        A("Un module spécifique de gestion des animaux dans la bibliothèque standard"),
        A("Une erreur fréquente des débutants à éviter absolument"),
    ]),
    Q("Parmi ces affirmations sur isinstance() et le duck typing, lesquelles sont vraies ?", "multiple", [
        A("isinstance() peut accepter un tuple de classes pour vérifier l'appartenance à plusieurs types possibles", True),
        A("Le duck typing favorise la vérification du comportement (méthodes disponibles) plutôt que du type exact", True),
        A("Python est souvent qualifié de langage favorisant le duck typing grâce à son typage dynamique", True),
        A("isinstance() ne peut jamais être utilisé avec des classes personnalisées, seulement avec les types intégrés"),
    ]),
    TF("isinstance(True, int) retourne True, car bool est une sous-classe d'int en Python.", True),
    TF("Le duck typing impose de vérifier explicitement le type exact d'un objet avant tout appel de méthode.", False),
])

add("Programmation asynchrone : notions de base avec async/await", "Découvrir les bases conceptuelles de la programmation asynchrone en Python.", [
    Q("Quel mot-clé permet de définir une fonction asynchrone (coroutine) en Python ?", "single", [
        A("async", True),
        A("await"),
        A("coroutine"),
        A("concurrent"),
    ]),
    Q("À quoi sert le mot-clé `await` à l'intérieur d'une fonction asynchrone ?", "single", [
        A("À suspendre l'exécution de la coroutine jusqu'à ce que l'opération attendue se termine, sans bloquer tout le programme", True),
        A("À arrêter définitivement le programme"),
        A("À transformer la fonction en boucle infinie"),
        A("À convertir la fonction en générateur classique sans rapport avec l'asynchrone"),
    ]),
    Q("Quel module de la bibliothèque standard fournit la boucle d'événements nécessaire pour exécuter du code asynchrone ?", "single", [
        A("asyncio", True),
        A("threading"),
        A("multiprocessing"),
        A("concurrent"),
    ]),
    Q("Parmi ces affirmations sur async/await en Python, lesquelles sont vraies ?", "multiple", [
        A("Une fonction définie avec async def retourne un objet coroutine quand on l'appelle", True),
        A("await ne peut être utilisé qu'à l'intérieur d'une fonction définie avec async def", True),
        A("La programmation asynchrone est particulièrement utile pour les opérations d'entrée-sortie (réseau, fichiers)", True),
        A("async/await rend automatiquement le code plus rapide pour tous les types de calculs, y compris purement intensifs en CPU"),
    ]),
    TF("L'asynchrone avec asyncio est concurrent mais s'exécute sur un seul thread, en alternant entre tâches lors des points d'attente (await).", True),
    TF("Toute fonction Python normale (sans async def) peut utiliser await directement sans restriction.", False),
])

add("Threads et parallélisme : notions de base", "Distinguer le threading, le multiprocessing et la notion de GIL en Python.", [
    Q("Que signifie l'acronyme GIL dans l'implémentation standard CPython ?", "single", [
        A("Global Interpreter Lock, un verrou limitant l'exécution simultanée de bytecode Python à un seul thread à la fois", True),
        A("General Input Library"),
        A("Generic Iteration Loop"),
        A("Global Index List"),
    ]),
    Q("Pourquoi le module multiprocessing est-il souvent préféré au threading pour des tâches intensives en calcul (CPU-bound) en CPython ?", "single", [
        A("Parce que multiprocessing utilise des processus séparés, chacun avec son propre interpréteur, contournant ainsi la limitation du GIL", True),
        A("Parce que threading n'existe pas en Python"),
        A("Les deux sont rigoureusement équivalents en performance CPU"),
        A("Parce que multiprocessing est plus simple syntaxiquement dans tous les cas"),
    ]),
    Q("Pour quel type de tâches le module threading reste-t-il généralement utile malgré le GIL ?", "single", [
        A("Les tâches d'entrée-sortie (I/O bound), comme les requêtes réseau ou la lecture de fichiers", True),
        A("Les calculs mathématiques intensifs purement CPU"),
        A("Aucune tâche, threading est totalement inutile en Python"),
        A("Uniquement le rendu graphique 3D"),
    ]),
    Q("Parmi ces affirmations sur le threading et le multiprocessing en Python, lesquelles sont vraies ?", "multiple", [
        A("Le module threading fait partie de la bibliothèque standard de Python", True),
        A("Le module multiprocessing crée de véritables processus séparés du système d'exploitation", True),
        A("Le GIL est une spécificité de l'implémentation CPython, pas une règle universelle du langage Python", True),
        A("Le multiprocessing partage automatiquement toute la mémoire entre les processus sans copie ni communication explicite"),
    ]),
    TF("Le GIL empêche deux threads Python d'exécuter du bytecode Python strictement en même temps dans CPython.", True),
    TF("Le module multiprocessing ne fait pas partie de la bibliothèque standard de Python et nécessite pip.", False),
])

add("Bonnes pratiques de documentation : docstrings", "Comprendre l'utilité et la syntaxe des docstrings en Python.", [
    Q("Comment écrit-on une docstring documentant une fonction juste après sa signature ?", "single", [
        A("Avec une chaîne de caractères entre triple guillemets juste après la ligne def", True),
        A("Avec un commentaire # juste avant la fonction uniquement"),
        A("Dans un fichier séparé obligatoirement"),
        A("Avec la syntaxe /** ... */ comme en Java"),
    ]),
    Q("Quel attribut spécial permet d'accéder programmatiquement à la docstring d'une fonction nommée ma_fonction ?", "single", [
        A("ma_fonction.__doc__", True),
        A("ma_fonction.docstring"),
        A("ma_fonction.help()"),
        A("ma_fonction.__doc()"),
    ]),
    Q("Quelle fonction intégrée affiche dans la console la documentation disponible d'un objet, incluant sa docstring ?", "single", [
        A("help()", True),
        A("doc()"),
        A("info()"),
        A("describe()"),
    ]),
    Q("Parmi ces affirmations sur les docstrings, lesquelles sont vraies ?", "multiple", [
        A("Une docstring peut documenter un module, une classe ou une fonction", True),
        A("Des outils comme Sphinx peuvent générer une documentation HTML à partir des docstrings", True),
        A("Une docstring est généralement délimitée par des triples guillemets doubles", True),
        A("Les docstrings sont obligatoires pour que le code Python s'exécute correctement"),
    ]),
    TF("Une docstring placée en première ligne du corps d'une fonction devient accessible via l'attribut __doc__ de cette fonction.", True),
    TF("Les docstrings sont strictement équivalentes aux commentaires # et n'offrent aucune fonctionnalité supplémentaire.", False),
])
