# -*- coding: utf-8 -*-
def build(quiz, S, Sx, M, T):

    quiz("Le module sys et les arguments de ligne de commande (Intermédiaire)",
         "Accédez à l'environnement d'exécution Python avec le module sys.",
         [
        Sx("Quelle liste du module sys contient les arguments passés en ligne de commande ?", ["sys.args", "sys.argv", "sys.params", "sys.input"], 1),
        Sx("Quelle fonction du module sys termine immédiatement le programme avec un code de sortie ?", ["sys.exit()", "sys.stop()", "sys.quit()", "sys.end()"], 0),
        Sx("Quel attribut de sys indique la version de Python utilisée ?", ["sys.version", "sys.python_version", "sys.release", "sys.ver"], 0),
        M("Quelles affirmations sur le module sys sont correctes ?",
          ["sys.argv[0] correspond généralement au nom du script exécuté", "sys.path liste les répertoires où Python recherche les modules",
           "sys fait partie de la bibliothèque standard", "sys.argv exclut toujours le nom du script lui-même"], {0, 1, 2}),
        M("Quels éléments appartiennent au module sys ?",
          ["argv", "exit", "path", "request"], {0, 1, 2}),
        T("sys.argv est une liste de chaînes représentant les arguments de la ligne de commande, le premier élément étant le nom du script.", True),
         ])

    quiz("Le module os et le système de fichiers (Intermédiaire)",
         "Interagissez avec le système d'exploitation via le module os.",
         [
        Sx("Quelle fonction du module os renvoie le répertoire de travail courant ?", ["os.getcwd()", "os.pwd()", "os.cwd", "os.dir()"], 0),
        Sx("Quelle fonction du module os liste le contenu d'un répertoire ?", ["os.list()", "os.listdir()", "os.scan()", "os.files()"], 1),
        Sx("Quelle fonction du module os permet de créer un nouveau répertoire ?", ["os.newdir()", "os.mkdir()", "os.createdir()", "os.makepath()"], 1),
        M("Quelles affirmations sur le module os sont correctes ?",
          ["os.environ donne accès aux variables d'environnement", "os.path contient des utilitaires pour manipuler les chemins",
           "os.remove() supprime un fichier", "os ne fonctionne que sous Windows"], {0, 1, 2}),
        M("Quelles fonctions appartiennent au module os ?",
          ["getcwd", "listdir", "mkdir", "render"], {0, 1, 2}),
        T("Le module os permet d'interagir avec le système de fichiers et l'environnement de façon portable entre systèmes d'exploitation.", True),
         ])

    quiz("Compréhensions imbriquées et aplatissement de listes (Avancé)",
         "Combinez plusieurs boucles for dans une compréhension pour aplatir des structures imbriquées.",
         [
        Sx("Que renvoie [x for ligne in [[1, 2], [3, 4]] for x in ligne] ?", ["[[1, 2], [3, 4]]", "[1, 2, 3, 4]", "[1, 3]", "[2, 4]"], 1),
        Sx("Dans une compréhension imbriquée [x for a in A for x in a], quel for est exécuté en premier (le plus externe) ?", ["for x in a", "for a in A", "Les deux en même temps", "Cela dépend de l'ordre des données"], 1),
        Sx("Quelle expression aplatit une liste de listes en une seule liste plate ?", ["[x for sous in liste for x in sous]", "[liste]", "list(liste)", "sum(liste)"], 0),
        M("Quelles affirmations sur les compréhensions imbriquées sont correctes ?",
          ["On peut combiner plusieurs clauses for dans une seule compréhension", "L'ordre des clauses for reproduit l'ordre de boucles for imbriquées classiques",
           "Elles peuvent aussi inclure une clause if de filtrage", "Une compréhension ne peut contenir qu'une seule clause for au maximum"], {0, 1, 2}),
        M("Quelles expressions aplatissent correctement [[1, 2], [3], [4, 5]] en [1, 2, 3, 4, 5] ?",
          ["[x for sous in m for x in sous]", "sum(m, [])", "[m]", "list(itertools.chain(*m))"], {0, 1, 3}),
        T("Une compréhension de liste imbriquée comme [x for ligne in matrice for x in ligne] équivaut à deux boucles for classiques imbriquées dans le même ordre.", True),
         ])

    quiz("Le mot-clé del et la suppression de références (Intermédiaire)",
         "Supprimez des variables, des éléments de liste ou des clés de dictionnaire avec del.",
         [
        Sx("Que fait l'instruction del x sur une variable x ?", ["Met x à zéro", "Supprime la liaison du nom x à son objet", "Met x à None", "Affiche x"], 1),
        Sx("Soit l = [1, 2, 3]; del l[0]. Que vaut l ensuite ?", ["[1, 2, 3]", "[2, 3]", "[1, 2]", "[]"], 1),
        Sx("Soit d = {'a': 1, 'b': 2}; del d['a']. Que vaut d ensuite ?", ["{'a': 1, 'b': 2}", "{'b': 2}", "{}", "Erreur"], 1),
        M("Quelles affirmations sur del sont correctes ?",
          ["del peut supprimer un élément d'une liste par index", "del peut supprimer une clé d'un dictionnaire",
           "del peut supprimer une tranche (slice) d'une liste", "del supprime physiquement l'objet de la mémoire même s'il est référencé ailleurs"], {0, 1, 2}),
        M("Quelles instructions utilisant del sont valides ?",
          ["del ma_liste[0]", "del mon_dict['cle']", "del ma_variable", "del 5"], {0, 1, 2}),
        T("del l[1:3] supprime une tranche d'éléments d'une liste, exactement comme on pourrait le faire avec un slicing en lecture.", True),
         ])

    quiz("La fonction zip pour combiner plusieurs séquences (Intermédiaire)",
         "Associez les éléments de plusieurs itérables position par position avec zip.",
         [
        Sx("Que renvoie list(zip([1, 2], ['a', 'b'])) ?", ["[(1, 'a'), (2, 'b')]", "[1, 2, 'a', 'b']", "[(1, 2), ('a', 'b')]", "Erreur"], 0),
        Sx("Que se passe-t-il si les itérables passés à zip ont des longueurs différentes ?", ["Une erreur est levée systématiquement", "zip s'arrête dès que le plus court itérable est épuisé", "Les éléments manquants sont remplacés par None", "zip répète le plus court itérable"], 1),
        Sx("Comment 'dézipper' une liste de tuples en deux listes séparées ?", ["zip(*liste_de_tuples)", "unzip(liste_de_tuples)", "liste_de_tuples.unzip()", "split(liste_de_tuples)"], 0),
        M("Quelles affirmations sur zip sont correctes ?",
          ["zip accepte plus de deux itérables en argument", "zip renvoie un itérateur d'objets tuple",
           "list(zip(*paires)) permet de transposer une liste de paires", "zip trie automatiquement les éléments combinés"], {0, 1, 2}),
        M("Quelles expressions utilisant zip sont valides ?",
          ["dict(zip(['a','b'], [1,2]))", "list(zip([1,2,3], [4,5,6], [7,8,9]))", "zip([1,2], [3,4], [5,6])", "zip()"], {0, 1, 2, 3}),
        T("dict(zip(cles, valeurs)) est une idiome courante pour construire un dictionnaire à partir de deux listes parallèles.", True),
         ])

    quiz("Arguments par mot-clé et ordre des paramètres (Intermédiaire)",
         "Maîtrisez l'ordre correct des paramètres : positionnels, défaut, *args, **kwargs.",
         [
        Sx("Quel est l'ordre correct des catégories de paramètres dans une signature de fonction Python ?", ["**kwargs, *args, positionnels, défaut", "Positionnels, défaut, *args, mots-clés seulement, **kwargs", "**kwargs, positionnels, *args", "Aucun ordre n'est imposé"], 1),
        Sx("Soit def f(a, b=2, *args, **kwargs). Quel appel est invalide ?", ["f(1)", "f(1, 2, 3, 4, x=5)", "f(a=1, b=2)", "f(c=3, 1)"], 3),
        Sx("Que reçoit kwargs si on appelle f(1, x=2, y=3) avec def f(a, **kwargs) ?", ["{'x': 2, 'y': 3}", "[2, 3]", "(2, 3)", "Erreur"], 0),
        M("Quelles affirmations sur l'ordre des paramètres sont correctes ?",
          ["Les paramètres avec valeur par défaut doivent venir après les paramètres sans défaut", "*args doit précéder **kwargs dans la signature",
           "On ne peut pas placer un paramètre positionnel sans défaut après un paramètre avec défaut", "L'ordre des paramètres n'a strictement aucune importance en Python"], {0, 1, 2}),
        M("Quelles signatures de fonction sont syntaxiquement valides ?",
          ["def f(a, b=1, *args, **kwargs):", "def f(a, *args, b=1, **kwargs):", "def f(b=1, a):", "def f(*args, a, **kwargs):"], {0, 1}),
        T("Écrire def f(b=1, a): est invalide car un paramètre sans valeur par défaut ne peut pas suivre un paramètre avec valeur par défaut.", True),
         ])

    quiz("Vérité et opérateurs logiques and, or, not (Débutant)",
         "Combinez des conditions avec les opérateurs logiques and, or et not.",
         [
        Sx("Que renvoie True and False ?", ["True", "False", "None", "Erreur"], 1),
        Sx("Que renvoie True or False ?", ["True", "False", "None", "Erreur"], 0),
        Sx("Que renvoie not True ?", ["True", "False", "None", "1"], 1),
        M("Quelles affirmations sur and, or et not sont correctes ?",
          ["and renvoie le premier opérande s'il est falsy, sinon le second", "or renvoie le premier opérande s'il est truthy, sinon le second",
           "and et or pratiquent l'évaluation paresseuse (short-circuit)", "not a toujours pour effet de renvoyer un entier"], {0, 1, 2}),
        M("Quelles expressions renvoient une valeur truthy ?",
          ["1 and 2", "0 or 5", "not False", "0 and 5"], {0, 1, 2}),
        T("En raison de l'évaluation paresseuse, dans a or b, b n'est évalué que si a est falsy.", True),
         ])

    quiz("Le module math (Débutant)",
         "Effectuez des calculs mathématiques avancés avec le module math de la bibliothèque standard.",
         [
        Sx("Quelle fonction du module math calcule la racine carrée ?", ["math.sqrt", "math.root", "math.pow2", "math.sqr"], 0),
        Sx("Quelle constante du module math représente Pi ?", ["math.PI", "math.pi", "math.Pi", "math.P"], 1),
        Sx("Quelle fonction du module math arrondit vers le haut (plafond) ?", ["math.floor", "math.ceil", "math.round", "math.top"], 1),
        M("Quelles affirmations sur le module math sont correctes ?",
          ["math.floor arrondit vers le bas (plancher)", "math.pow(a, b) calcule a élevé à la puissance b sous forme de float",
           "math fait partie de la bibliothèque standard de Python", "math peut effectuer des opérations sur des nombres complexes directement"], {0, 1, 2}),
        M("Quelles fonctions ou constantes appartiennent au module math ?",
          ["sqrt", "pi", "floor", "random"], {0, 1, 2}),
        T("La fonction native round() arrondit un nombre, mais elle n'appartient pas au module math : c'est une fonction intégrée (builtin).", True),
         ])

    quiz("Exceptions multiples et capture groupée (Avancé)",
         "Capturez plusieurs types d'exceptions dans un seul bloc except.",
         [
        Sx("Comment capturer à la fois ValueError et TypeError dans un même bloc except ?", ["except ValueError, TypeError:", "except (ValueError, TypeError):", "except [ValueError, TypeError]:", "except ValueError and TypeError:"], 1),
        Sx("Que fait 'except Exception as e:' ?", ["Capture l'exception et la stocke dans la variable e", "Ignore l'exception", "Relance automatiquement l'exception", "Provoque une erreur de syntaxe"], 0),
        Sx("Que se passe-t-il si aucun bloc except ne correspond au type de l'exception levée ?", ["L'exception est ignorée silencieusement", "L'exception se propage et peut arrêter le programme si non gérée plus haut", "Python la convertit automatiquement en Warning", "Le bloc finally l'attrape automatiquement"], 1),
        M("Quelles affirmations sur la capture d'exceptions multiples sont correctes ?",
          ["On peut empiler plusieurs blocs except pour des types différents", "Un tuple de types dans un seul except capture n'importe lequel de ces types",
           "L'ordre des blocs except a de l'importance (le plus spécifique doit souvent venir avant le plus général)", "On ne peut capturer qu'un seul type d'exception par programme entier"], {0, 1, 2}),
        M("Quelles syntaxes de capture d'exception sont valides ?",
          ["except ValueError:", "except (ValueError, KeyError):", "except Exception as e:", "except ValueError, KeyError:"], {0, 1, 2}),
        T("Capturer Exception de façon trop large peut masquer des bugs inattendus ; il est souvent préférable de cibler des exceptions précises.", True),
         ])

    quiz("La fonction format() et l'alignement de texte (Intermédiaire)",
         "Alignez et formatez des valeurs avec la fonction format() et la mini-syntaxe de spécification.",
         [
        Sx("Que renvoie format(42, '05d') ?", ["'42'", "'00042'", "'42000'", "Erreur"], 1),
        Sx("Que renvoie format(3.14159, '.2f') ?", ["'3.14'", "'3.1'", "'3.14159'", "'3'"], 0),
        Sx("Quel caractère de spécification aligne une valeur à droite sur une largeur donnée ?", [">", "<", "^", "v"], 0),
        M("Quelles affirmations sur format() et la mini-syntaxe de spécification sont correctes ?",
          ["On peut spécifier une largeur minimale d'affichage", "Le caractère ^ centre la valeur dans la largeur spécifiée",
           "On peut combiner alignement et précision décimale", "format() ne fonctionne que sur les chaînes de caractères"], {0, 1, 2}),
        M("Quelles expressions sont valides avec la mini-syntaxe de format ?",
          ["f'{42:>10}'", "f'{3.14159:.1f}'", "f'{5:^7}'", "f'{5:invalid}'"], {0, 1, 2}),
        T("La mini-syntaxe de spécification utilisée par format() et les f-strings est partagée entre les deux mécanismes.", True),
         ])

    quiz("Test d'égalité entre structures composées (Intermédiaire)",
         "Comparez listes, tuples et dictionnaires en valeur plutôt qu'en identité.",
         [
        Sx("Que renvoie [1, 2, 3] == [1, 2, 3] (deux listes distinctes mais avec le même contenu) ?", ["True", "False", "Erreur", "None"], 0),
        Sx("Que renvoie [1, 2, 3] is [1, 2, 3] (deux listes littérales distinctes) ?", ["True", "False", "Erreur", "None"], 1),
        Sx("Que renvoie {'a': 1, 'b': 2} == {'b': 2, 'a': 1} ?", ["True (l'ordre des clés n'affecte pas l'égalité)", "False", "Erreur", "None"], 0),
        M("Quelles affirmations sur la comparaison de structures composées sont correctes ?",
          ["== compare le contenu (valeur) des structures", "is compare l'identité mémoire des objets",
           "Deux dictionnaires avec les mêmes paires clé-valeur sont égaux avec == quel que soit l'ordre", "Deux listes contenant les mêmes éléments dans un ordre différent sont toujours égales avec =="], {0, 1, 2}),
        M("Quelles comparaisons renvoient True ?",
          ["(1, 2) == (1, 2)", "{1, 2, 3} == {3, 2, 1}", "[1, 2] == [2, 1]", "{'x': 1} == {'x': 1}"], {0, 1, 3}),
        T("Pour les listes et les tuples, l'ordre des éléments compte dans la comparaison d'égalité, contrairement aux sets.", True),
         ])

    quiz("Hashabilité et clés de dictionnaire (Avancé)",
         "Comprenez quels types d'objets peuvent servir de clés de dictionnaire ou d'éléments de set.",
         [
        Sx("Qu'est-ce qu'un objet hachable en Python ?", ["Un objet qui possède une méthode __hash__ valide et constante pendant sa vie", "Un objet toujours mutable", "Un objet de type liste uniquement", "Un objet qui ne peut pas être comparé"], 0),
        Sx("Pourquoi une liste ne peut-elle pas être utilisée comme clé de dictionnaire ?", ["Parce qu'elle est trop grande", "Parce qu'elle est mutable et donc non hachable", "Parce que Python l'interdit arbitrairement", "Parce qu'elle contient des nombres"], 1),
        Sx("Quel type immuable peut servir de clé de dictionnaire alors qu'un type mutable équivalent ne le peut pas ?", ["set", "tuple (face à list)", "dict", "bytearray"], 1),
        M("Quelles affirmations sur la hashabilité sont correctes ?",
          ["Les types immuables comme int, str, tuple sont hachables (sous conditions)", "Les listes, dictionnaires et sets sont non hachables car mutables",
           "Une clé de dictionnaire doit être hachable", "Un tuple contenant une liste reste toujours hachable"], {0, 1, 2}),
        M("Quels objets peuvent être utilisés comme clé de dictionnaire ?",
          ["Une chaîne de caractères", "Un entier", "Un tuple de chaînes", "Une liste"], {0, 1, 2}),
        T("Un tuple contenant un objet mutable comme une liste n'est en réalité pas hachable, malgré l'immutabilité apparente du tuple lui-même.", True),
         ])

    quiz("Conversion entre collections : list, tuple, set, dict (Intermédiaire)",
         "Convertissez librement entre les principales structures de données de Python.",
         [
        Sx("Que renvoie list((1, 2, 3)) ?", ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "Erreur"], 1),
        Sx("Que renvoie set([1, 2, 2, 3]) ?", ["{1, 2, 2, 3}", "{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)"], 1),
        Sx("Que renvoie dict([('a', 1), ('b', 2)]) ?", ["{'a': 1, 'b': 2}", "['a', 1, 'b', 2]", "(('a',1),('b',2))", "Erreur"], 0),
        M("Quelles affirmations sur les conversions entre collections sont correctes ?",
          ["list(set([3, 1, 2])) ne garantit pas un ordre particulier des éléments avant tri explicite", "tuple([1, 2, 3]) renvoie (1, 2, 3)",
           "dict() peut construire un dictionnaire à partir d'une liste de paires", "set() conserve l'ordre d'insertion comme une liste"], {0, 1, 2}),
        M("Quelles conversions sont valides en Python ?",
          ["list('abc')", "set('aabbcc')", "tuple({1, 2, 3})", "dict([1, 2, 3])"], {0, 1, 2}),
        T("Convertir une liste contenant des doublons en set élimine automatiquement ces doublons.", True),
         ])

    quiz("Le bloc try/except/else/finally complet (Avancé)",
         "Assemblez try, except, else et finally pour une gestion d'erreurs complète et précise.",
         [
        Sx("Dans quel ordre les blocs try/except/else/finally s'exécutent-ils logiquement (cas sans exception) ?", ["try, finally, else", "try, else, finally", "else, try, finally", "finally, try, else"], 1),
        Sx("Si une exception est levée et capturée par except, le bloc else s'exécute-t-il ?", ["Oui, toujours", "Non, else est ignoré dans ce cas", "Seulement si finally existe", "Cela dépend du type d'exception"], 1),
        Sx("Le bloc finally s'exécute-t-il même si le bloc except contient un return ?", ["Non, jamais", "Oui, finally s'exécute presque toujours, même après un return", "Seulement sans exception", "Cela dépend de la version de Python"], 1),
        M("Quelles affirmations sur try/except/else/finally sont correctes ?",
          ["else s'exécute uniquement si aucune exception ne survient dans try", "finally s'exécute systématiquement, qu'il y ait eu une exception capturée ou non",
           "On peut avoir plusieurs blocs except mais un seul else et un seul finally", "Le bloc else est obligatoire dès qu'on utilise try/except"], {0, 1, 2}),
        M("Dans quels cas utiliser le bloc else d'un try est-il pertinent ?",
          ["Exécuter du code seulement si aucune exception n'a eu lieu, sans risquer de capturer une nouvelle exception de ce code par erreur", "Nettoyer des ressources quoi qu'il arrive", "Séparer clairement la logique de succès de la logique de gestion d'erreur", "Remplacer complètement le bloc except"], {0, 2}),
        T("Le bloc finally est généralement utilisé pour libérer des ressources (fichiers, connexions) indépendamment du succès ou de l'échec du bloc try.", True),
         ])

    quiz("L'opérateur d'étoile pour le déballage d'arguments (Avancé)",
         "Déballez des listes ou dictionnaires en arguments de fonction avec * et **.",
         [
        Sx("Soit def f(a, b, c): ... et l = [1, 2, 3]. Comment appeler f en déballant la liste ?", ["f(l)", "f(*l)", "f(**l)", "f(l[0], l[1], l[2], l)"], 1),
        Sx("Soit def f(a, b): ... et d = {'a': 1, 'b': 2}. Comment appeler f en déballant le dictionnaire en arguments nommés ?", ["f(d)", "f(*d)", "f(**d)", "f(d.items())"], 2),
        Sx("Que fait l'expression [*[1, 2], *[3, 4]] ?", ["Lève une erreur", "Construit la liste [1, 2, 3, 4]", "Construit [[1, 2], [3, 4]]", "Construit (1, 2, 3, 4)"], 1),
        M("Quelles affirmations sur le déballage avec * et ** sont correctes ?",
          ["* déballe un itérable en arguments positionnels", "** déballe un dictionnaire en arguments nommés",
           "On peut combiner le déballage avec des arguments explicites dans le même appel", "** ne peut être utilisé que dans la définition d'une fonction, jamais lors d'un appel"], {0, 1, 2}),
        M("Quelles expressions sont valides en Python ?",
          ["f(*[1, 2, 3])", "f(**{'a': 1})", "{**{'x': 1}, **{'y': 2}}", "f(**[1, 2, 3])"], {0, 1, 2}),
        T("L'opérateur ** ne peut déballer qu'un mapping (comme un dict) car il doit produire des paires clé/valeur pour les arguments nommés.", True),
         ])
