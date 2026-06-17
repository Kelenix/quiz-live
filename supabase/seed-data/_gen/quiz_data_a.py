# -*- coding: utf-8 -*-
def build(quiz, S, Sx, M, T):

    quiz("Types de base : entiers et flottants (Debutant)",
         "Decouvrez les nombres entiers et a virgule flottante en Python.",
         [
        Sx("Quel est le type de la valeur 42 en Python ?", ["str", "int", "float", "bool"], 1),
        Sx("Quel est le type de la valeur 3.14 en Python ?", ["int", "float", "decimal", "double"], 1),
        Sx("Que renvoie l'expression type(10) ?", ["<class 'int'>", "<class 'float'>", "int", "number"], 0),
        M("Parmi ces litteraux, lesquels sont des entiers (int) valides en Python 3 ?",
          ["100", "0x1F", "3.0", "1_000", "1e3"], {0, 1, 3}),
        M("Quelles affirmations sur le type float sont correctes ?",
          ["Il represente les nombres a virgule flottante", "0.1 + 0.2 vaut exactement 0.3",
           "float('inf') represente l'infini", "Un float peut etre note 2.5e3"], {0, 2, 3}),
        T("En Python 3, le type int n'a pas de limite fixe de taille (entiers de precision arbitraire).", True),
         ])

    quiz("Chaines de caracteres : bases (Debutant)",
         "Manipulez les chaines de caracteres et leurs principales operations.",
         [
        Sx("Que renvoie len('Python') ?", ["5", "6", "7", "Erreur"], 1),
        Sx("Que renvoie 'abc'.upper() ?", ["abc", "ABC", "Abc", "aBC"], 1),
        Sx("Que renvoie 'Bonjour'[0] ?", ["'B'", "'o'", "'Bonjour'", "0"], 0),
        M("Quelles methodes de chaine renvoient une nouvelle chaine sans modifier l'originale ?",
          ["replace", "upper", "lower", "append"], {0, 1, 2}),
        M("Quelles expressions produisent la chaine 'ab' ?",
          ["'a' + 'b'", "'ab'", "'a' * 2", "'aXb'.replace('X', '')"], {0, 1, 3}),
        T("Les chaines de caracteres sont immuables en Python (on ne peut pas modifier un caractere en place).", True),
         ])

    quiz("Booleens et valeurs de verite (Debutant)",
         "Comprenez les booleens et l'evaluation de verite des objets.",
         [
        Sx("Quel est le type du resultat de l'expression 5 > 3 ?", ["int", "bool", "str", "NoneType"], 1),
        Sx("Que vaut bool(0) ?", ["True", "False", "0", "None"], 1),
        Sx("Que vaut bool('') (chaine vide) ?", ["True", "False", "''", "Erreur"], 1),
        M("Quelles valeurs sont considerees comme 'fausses' (falsy) en Python ?",
          ["0", "[]", "None", "'0'"], {0, 1, 2}),
        M("Quelles expressions s'evaluent a True ?",
          ["bool(1)", "bool([1])", "bool('a')", "bool(None)"], {0, 1, 2}),
        T("En Python, True == 1 renvoie True car les booleens sont une sous-classe des entiers.", True),
         ])

    quiz("Operateurs arithmetiques (Debutant)",
         "Maitrisez les operateurs de calcul et leurs particularites.",
         [
        Sx("Que renvoie 7 // 2 en Python 3 ?", ["3", "3.5", "4", "2"], 0),
        Sx("Que renvoie 2 ** 5 ?", ["10", "25", "32", "16"], 2),
        Sx("Que renvoie 17 % 5 ?", ["2", "3", "5", "1"], 0),
        Sx("Que renvoie 7 / 2 en Python 3 ?", ["3", "3.5", "4", "3.0"], 1),
        M("Quels operateurs realisent une operation arithmetique en Python ?",
          ["+", "//", "**", "and"], {0, 1, 2}),
        T("En Python 3, l'operateur / entre deux entiers renvoie toujours un float.", True),
         ])

    quiz("Listes : creation et acces (Debutant)",
         "Apprenez a creer et acceder aux elements d'une liste.",
         [
        Sx("Comment cree-t-on une liste vide en Python ?", ["[]", "{}", "()", "list[]"], 0),
        Sx("Soit ma_liste = [10, 20, 30]. Que renvoie ma_liste[1] ?", ["10", "20", "30", "1"], 1),
        Sx("Soit ma_liste = [10, 20, 30]. Que renvoie ma_liste[-1] ?", ["10", "20", "30", "Erreur"], 2),
        M("Quelles methodes ajoutent un ou des elements a une liste ?",
          ["append", "extend", "insert", "remove"], {0, 1, 2}),
        M("Quelles affirmations sur les listes sont vraies ?",
          ["Elles sont mutables", "Elles peuvent contenir des types differents",
           "Elles sont indexees a partir de 0", "Elles sont immuables"], {0, 1, 2}),
        T("La methode append() ajoute un seul element a la fin de la liste.", True),
         ])

    quiz("Le slicing des sequences (Intermediaire)",
         "Decoupez listes et chaines avec la syntaxe de slicing [a:b:c].",
         [
        Sx("Soit s = 'Python'. Que renvoie s[1:4] ?", ["'Pyt'", "'yth'", "'ytho'", "'tho'"], 1),
        Sx("Soit l = [0, 1, 2, 3, 4]. Que renvoie l[::2] ?", ["[0, 2, 4]", "[1, 3]", "[0, 1, 2]", "[2, 4]"], 0),
        Sx("Soit s = 'abcdef'. Que renvoie s[::-1] ?", ["'abcdef'", "'fedcba'", "'fdb'", "Erreur"], 1),
        Sx("Soit l = [10, 20, 30, 40]. Que renvoie l[1:] ?", ["[10]", "[20, 30, 40]", "[10, 20]", "[40]"], 1),
        M("Quelles expressions de slicing sur s = 'Python' renvoient 'Pyt' ?",
          ["s[0:3]", "s[:3]", "s[0:3:1]", "s[3:]"], {0, 1, 2}),
        T("Un slicing avec un indice de fin superieur a la longueur ne provoque pas d'erreur.", True),
         ])

    quiz("Les f-strings (Intermediaire)",
         "Formatez vos chaines avec les f-strings introduites en Python 3.6.",
         [
        Sx("Soit nom = 'Lionel'. Que renvoie f'Salut {nom}' ?", ["'Salut {nom}'", "'Salut Lionel'", "'Salut '", "Erreur"], 1),
        Sx("Soit x = 5. Que renvoie f'{x * 2}' ?", ["'x * 2'", "'10'", "'5'", "'52'"], 1),
        Sx("Quel prefixe introduit une f-string ?", ["b'...'", "r'...'", "f'...'", "u'...'"], 2),
        Sx("Soit pi = 3.14159. Que renvoie f'{pi:.2f}' ?", ["'3.14159'", "'3.14'", "'3.1'", "'3'"], 1),
        M("Quelles affirmations sur les f-strings sont correctes ?",
          ["On peut y inserer des expressions", "Elles sont evaluees a l'execution",
           "On peut formater des nombres avec :", "Elles existent depuis Python 2.6"], {0, 1, 2}),
        T("Dans une f-string, f'{2+3}' affiche 5.", True),
         ])

    quiz("La fonction print et l'affichage (Debutant)",
         "Explorez les options de la fonction print pour afficher du texte.",
         [
        Sx("Que fait print('Bonjour') ?", ["Renvoie 'Bonjour'", "Affiche Bonjour a l'ecran", "Cree une variable", "Rien"], 1),
        Sx("Quel argument de print change le separateur entre les valeurs ?", ["end", "sep", "split", "file"], 1),
        Sx("Que fait print('a', end='') par rapport au print classique ?",
           ["Ajoute un saut de ligne", "N'ajoute pas de saut de ligne a la fin", "Affiche en majuscules", "Provoque une erreur"], 1),
        Sx("Que renvoie print('x') (sa valeur de retour) ?", ["'x'", "None", "0", "True"], 1),
        M("Quels arguments nommes la fonction print accepte-t-elle ?",
          ["sep", "end", "file", "color"], {0, 1, 2}),
        T("Par defaut, print ajoute un saut de ligne ('\\n') a la fin.", True),
         ])

    quiz("Conversions de type (Debutant)",
         "Convertissez les valeurs d'un type a un autre avec int, str, float.",
         [
        Sx("Que renvoie int('42') ?", ["'42'", "42", "42.0", "Erreur"], 1),
        Sx("Que renvoie str(100) ?", ["100", "'100'", "100.0", "Erreur"], 1),
        Sx("Que renvoie float('3.5') ?", ["3", "3.5", "'3.5'", "Erreur"], 1),
        Sx("Que provoque int('abc') ?", ["0", "None", "Une ValueError", "'abc'"], 2),
        M("Quelles conversions reussissent sans erreur ?",
          ["int('10')", "float('2.5')", "str(3.14)", "int('3.5')"], {0, 1, 2}),
        T("int(3.9) renvoie 3 car la conversion tronque la partie decimale (pas d'arrondi).", True),
         ])

    quiz("Les tuples (Intermediaire)",
         "Comprenez les tuples, sequences immuables de Python.",
         [
        Sx("Comment cree-t-on un tuple d'un seul element ?", ["(1)", "(1,)", "[1]", "{1}"], 1),
        Sx("Soit t = (1, 2, 3). Que provoque t[0] = 9 ?", ["t devient (9, 2, 3)", "Une TypeError", "Rien", "None"], 1),
        Sx("Quel est le type de (1, 2, 3) ?", ["list", "set", "tuple", "dict"], 2),
        M("Quelles affirmations sur les tuples sont vraies ?",
          ["Ils sont immuables", "Ils sont ordonnes", "Ils peuvent servir de cle de dictionnaire",
           "On peut leur ajouter des elements avec append"], {0, 1, 2}),
        M("Quelles operations sont valides sur un tuple t = (1, 2, 3) ?",
          ["len(t)", "t[0]", "t + (4,)", "t.append(4)"], {0, 1, 2}),
        T("Un tuple peut etre utilise comme cle de dictionnaire car il est hachable.", True),
         ])

    quiz("Les dictionnaires : bases (Debutant)",
         "Stockez des paires cle-valeur avec les dictionnaires.",
         [
        Sx("Comment cree-t-on un dictionnaire vide ?", ["[]", "{}", "()", "dict[]"], 1),
        Sx("Soit d = {'a': 1}. Que renvoie d['a'] ?", ["'a'", "1", "{'a': 1}", "Erreur"], 1),
        Sx("Que renvoie d.get('z') si 'z' n'existe pas dans d ?", ["None", "0", "Une KeyError", "''"], 0),
        Sx("Que provoque d['z'] si 'z' n'existe pas dans d ?", ["None", "0", "Une KeyError", "''"], 2),
        M("Quelles methodes existent sur les dictionnaires ?",
          ["keys", "values", "items", "indexof"], {0, 1, 2}),
        T("Depuis Python 3.7, les dictionnaires conservent l'ordre d'insertion des cles.", True),
         ])

    quiz("Les ensembles (set) (Intermediaire)",
         "Travaillez avec les ensembles, collections non ordonnees sans doublons.",
         [
        Sx("Que renvoie len({1, 2, 2, 3}) ?", ["4", "3", "2", "1"], 1),
        Sx("Comment cree-t-on un ensemble vide ?", ["{}", "set()", "[]", "()"], 1),
        Sx("Que renvoie {1, 2, 3} & {2, 3, 4} ?", ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "{}"], 1),
        Sx("Que renvoie {1, 2, 3} | {3, 4} ?", ["{1, 2, 3, 4}", "{3}", "{1, 2}", "{4}"], 0),
        M("Quelles affirmations sur les ensembles sont vraies ?",
          ["Ils ne contiennent pas de doublons", "Ils ne sont pas ordonnes",
           "L'operateur - calcule la difference", "Ils sont indexables avec [0]"], {0, 1, 2}),
        T("Un ensemble ne peut pas contenir deux fois la meme valeur.", True),
         ])

    quiz("La structure conditionnelle if/elif/else (Debutant)",
         "Prenez des decisions dans votre code avec les conditions.",
         [
        Sx("Quel mot-cle introduit une condition en Python ?", ["when", "if", "switch", "case"], 1),
        Sx("Quel mot-cle gere un cas alternatif intermediaire ?", ["else", "elif", "elseif", "otherwise"], 1),
        Sx("Que faut-il a la fin de la ligne d'un if avant le bloc ?", ["Un point-virgule", "Deux points (:)", "Des accolades", "Rien"], 1),
        M("Quels operateurs de comparaison existent en Python ?",
          ["==", "!=", ">=", "=>"], {0, 1, 2}),
        M("Quelles affirmations sur if/elif/else sont correctes ?",
          ["elif est facultatif", "else est facultatif", "On peut avoir plusieurs elif",
           "Chaque if doit avoir un else"], {0, 1, 2}),
        T("Le bloc else d'une instruction conditionnelle s'execute si aucune condition precedente n'est vraie.", True),
         ])

    quiz("La boucle for (Debutant)",
         "Iterez sur des sequences avec la boucle for.",
         [
        Sx("Sur quoi peut-on iterer avec une boucle for ?", ["Seulement des listes", "Tout objet iterable", "Seulement des nombres", "Seulement des chaines"], 1),
        Sx("Que produit for i in range(3): print(i) ?", ["1 2 3", "0 1 2", "0 1 2 3", "1 2"], 1),
        Sx("Soit for c in 'ab': print(c). Combien de lignes affiche-t-il ?", ["1", "2", "3", "0"], 1),
        M("Quels objets sont iterables avec une boucle for ?",
          ["une liste", "une chaine", "un dictionnaire", "un int"], {0, 1, 2}),
        M("Quelles affirmations sur range sont correctes ?",
          ["range(5) va de 0 a 4", "range(2, 5) va de 2 a 4", "range(0, 10, 2) donne les pairs",
           "range(5) inclut 5"], {0, 1, 2}),
        T("Iterer sur un dictionnaire avec for parcourt ses cles par defaut.", True),
         ])

    quiz("La boucle while (Debutant)",
         "Repetez des instructions tant qu'une condition est vraie.",
         [
        Sx("Quand une boucle while s'arrete-t-elle ?", ["Apres 10 iterations", "Quand sa condition devient fausse", "Jamais", "Apres un seul tour"], 1),
        Sx("Que provoque while True: sans break ?", ["Une boucle infinie", "Une erreur", "Un seul tour", "Rien"], 0),
        Sx("Quel mot-cle interrompt immediatement une boucle ?", ["continue", "break", "stop", "exit"], 1),
        Sx("Quel mot-cle passe a l'iteration suivante sans finir le bloc ?", ["break", "continue", "pass", "skip"], 1),
        M("Quelles affirmations sur while sont correctes ?",
          ["Elle teste la condition avant chaque tour", "break la termine immediatement",
           "continue saute a l'iteration suivante", "Elle s'execute toujours au moins une fois"], {0, 1, 2}),
        T("Une boucle while peut posseder une clause else executee si la boucle se termine sans break.", True),
         ])

    quiz("Les commentaires et la syntaxe (Debutant)",
         "Maitrisez les commentaires et les regles de syntaxe de base.",
         [
        Sx("Quel symbole introduit un commentaire sur une ligne ?", ["//", "#", "/*", "--"], 1),
        Sx("Comment Python delimite-t-il les blocs de code ?", ["Avec des accolades {}", "Par l'indentation", "Avec begin/end", "Avec des points-virgules"], 1),
        Sx("Que se passe-t-il si l'indentation est incoherente ?", ["Rien", "Une IndentationError", "Un avertissement", "Le code s'execute quand meme"], 1),
        M("Quelles affirmations sur la syntaxe Python sont vraies ?",
          ["L'indentation est significative", "Les commentaires commencent par #",
           "Le point-virgule en fin de ligne est facultatif", "Les blocs utilisent des accolades"], {0, 1, 2}),
        M("Comment ecrire une chaine de documentation (docstring) multi-lignes ?",
          ['Avec """..."""', "Avec '''...'''", "Avec # sur chaque ligne", "Avec /* ... */"], {0, 1}),
        T("En Python, l'indentation par convention PEP8 est de 4 espaces.", True),
         ])

    quiz("Les fonctions : definition (Debutant)",
         "Definissez et appelez vos propres fonctions.",
         [
        Sx("Quel mot-cle definit une fonction ?", ["function", "def", "func", "define"], 1),
        Sx("Que renvoie une fonction sans instruction return ?", ["0", "None", "''", "Une erreur"], 1),
        Sx("Soit def f(x): return x + 1. Que renvoie f(4) ?", ["4", "5", "1", "None"], 1),
        M("Quelles affirmations sur les fonctions sont correctes ?",
          ["Elles peuvent prendre des parametres", "Elles peuvent renvoyer une valeur",
           "Elles se definissent avec def", "On les declare avec function"], {0, 1, 2}),
        M("Quelles instructions appellent correctement def saluer(nom): ... ?",
          ["saluer('Lionel')", "saluer(nom='Lionel')", "saluer()", "saluer.call('Lionel')"], {0, 1}),
        T("Une instruction return termine immediatement l'execution de la fonction.", True),
         ])

    quiz("Parametres de fonction (Intermediaire)",
         "Decouvrez les valeurs par defaut et les arguments nommes.",
         [
        Sx("Soit def f(a, b=10): return a + b. Que renvoie f(5) ?", ["5", "10", "15", "Erreur"], 2),
        Sx("Dans def f(a, b=10), que represente b=10 ?", ["Une variable globale", "Une valeur par defaut", "Un type", "Une constante"], 1),
        Sx("Que sont les arguments passes sous la forme f(b=3, a=1) ?", ["Des arguments positionnels", "Des arguments nommes (mots-cles)", "Des args par defaut", "Une erreur"], 1),
        M("Quelles affirmations sur les parametres sont correctes ?",
          ["Un parametre peut avoir une valeur par defaut", "On peut passer les arguments par nom",
           "Les parametres avec defaut viennent apres ceux sans defaut", "L'ordre n'a aucune importance"], {0, 1, 2}),
        M("Soit def f(a, b=2, c=3). Quels appels sont valides ?",
          ["f(1)", "f(1, 5)", "f(1, c=9)", "f(b=2)"], {0, 1, 2}),
        T("En Python, on peut melanger arguments positionnels et nommes, mais les positionnels viennent en premier.", True),
         ])

    quiz("args et kwargs (Intermediaire)",
         "Acceptez un nombre variable d'arguments avec *args et **kwargs.",
         [
        Sx("Que collecte *args dans une fonction ?", ["Un dictionnaire", "Un tuple d'arguments positionnels", "Une liste de cles", "Une chaine"], 1),
        Sx("Que collecte **kwargs dans une fonction ?", ["Un tuple", "Un dictionnaire d'arguments nommes", "Une liste", "Un set"], 1),
        Sx("Soit def f(*args): return len(args). Que renvoie f(1, 2, 3) ?", ["1", "2", "3", "Erreur"], 2),
        M("Quelles affirmations sur *args et **kwargs sont correctes ?",
          ["*args capture les positionnels supplementaires", "**kwargs capture les nommes supplementaires",
           "args est un tuple", "kwargs est une liste"], {0, 1, 2}),
        M("Soit def f(a, *args, **kwargs). Quels appels sont valides ?",
          ["f(1)", "f(1, 2, 3)", "f(1, x=2)", "f()"], {0, 1, 2}),
        T("Le nom 'args' n'est qu'une convention : c'est l'asterisque * qui active la collecte.", True),
         ])

    quiz("Les fonctions lambda (Intermediaire)",
         "Ecrivez des fonctions anonymes concises avec lambda.",
         [
        Sx("Soit f = lambda x: x * 2. Que renvoie f(5) ?", ["5", "10", "2", "None"], 1),
        Sx("Combien d'expressions une lambda peut-elle contenir ?", ["Plusieurs lignes", "Une seule expression", "Aucune", "Trois maximum"], 1),
        Sx("Soit add = lambda a, b: a + b. Que renvoie add(3, 4) ?", ["7", "12", "34", "Erreur"], 0),
        M("Quelles affirmations sur lambda sont correctes ?",
          ["C'est une fonction anonyme", "Elle renvoie implicitement son expression",
           "Elle peut prendre plusieurs parametres", "Elle peut contenir une boucle for"], {0, 1, 2}),
        M("Avec quelles fonctions utilise-t-on couramment lambda ?",
          ["sorted (parametre key)", "map", "filter", "print"], {0, 1, 2}),
        T("Une lambda ne peut pas contenir d'instruction return explicite.", True),
         ])
