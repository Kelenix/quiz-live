# -*- coding: utf-8 -*-
def build(quiz, S, Sx, M, T):

    quiz("Les compréhensions de liste (Intermédiaire)",
         "Construisez des listes de façon concise avec les list comprehensions.",
         [
        Sx("Que renvoie [x*2 for x in range(3)] ?", ["[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2]", "[1, 2, 3]"], 0),
        Sx("Que renvoie [x for x in range(5) if x % 2 == 0] ?", ["[0, 2, 4]", "[1, 3]", "[0, 1, 2, 3, 4]", "[2, 4]"], 0),
        Sx("Quelle est la syntaxe générale d'une compréhension de liste ?", ["[expr for item in iterable]", "(expr for item in iterable)", "{expr for item in iterable}", "expr for item in iterable"], 0),
        M("Quelles affirmations sur les compréhensions de liste sont correctes ?",
          ["Elles peuvent inclure une clause if", "Elles renvoient toujours une liste",
           "Elles peuvent être imbriquées", "Elles modifient la liste d'origine en place"], {0, 1, 2}),
        M("Quelles expressions produisent [1, 4, 9] ?",
          ["[x**2 for x in [1, 2, 3]]", "[x*x for x in (1, 2, 3)]", "list(x**2 for x in range(1, 4))", "[x for x in [1, 4, 9, 16]][:3]"], {0, 1, 2}),
        T("Une compréhension de liste est généralement plus rapide qu'une boucle for équivalente avec append.", True),
         ])

    quiz("Compréhensions de dictionnaire et d'ensemble (Intermédiaire)",
         "Étendez la syntaxe des compréhensions aux dictionnaires et aux sets.",
         [
        Sx("Que renvoie {x: x**2 for x in range(3)} ?", ["{0: 0, 1: 1, 2: 4}", "[0, 1, 4]", "{0, 1, 4}", "Erreur"], 0),
        Sx("Que renvoie {x % 3 for x in range(6)} ?", ["{0, 1, 2}", "{0, 1, 2, 3, 4, 5}", "[0, 1, 2]", "Erreur"], 0),
        Sx("Quelle syntaxe crée une compréhension d'ensemble ?", ["{expr for item in iterable}", "[expr for item in iterable]", "(expr for item in iterable)", "set(expr for item)"], 0),
        M("Quelles affirmations sur les compréhensions de dictionnaire sont vraies ?",
          ["Elles utilisent la syntaxe cle: valeur", "Elles peuvent filtrer avec if",
           "Elles produisent un objet dict", "Elles utilisent des crochets []"], {0, 1, 2}),
        M("Quelles expressions sont valides en Python ?",
          ["{k: v for k, v in [(1,2),(3,4)]}", "{x for x in range(3)}", "[x for x in range(3) if x]", "{x: for x in range(3)}"], {0, 1, 2}),
        T("Une compréhension d'ensemble élimine automatiquement les doublons du résultat.", True),
         ])

    quiz("Générateurs et l'instruction yield (Avancé)",
         "Créez des itérateurs paresseux avec les fonctions génératrices.",
         [
        Sx("Quel mot-clé transforme une fonction en générateur ?", ["return", "yield", "gen", "lazy"], 1),
        Sx("Que renvoie l'appel d'une fonction génératrice (sans itérer) ?", ["Une liste", "Un objet générateur", "None", "La première valeur"], 1),
        Sx("Quelle expression crée un générateur (et non une liste) ?", ["(x*2 for x in range(3))", "[x*2 for x in range(3)]", "{x*2 for x in range(3)}", "{x: x*2 for x in range(3)}"], 0),
        M("Quelles affirmations sur les générateurs sont correctes ?",
          ["Ils produisent les valeurs à la demande (paresseux)", "On les parcourt avec next() ou for",
           "Ils consomment généralement moins de mémoire qu'une liste", "Ils peuvent être relus depuis le début sans les recréer"], {0, 1, 2}),
        M("Quelles fonctions ou expressions créent un générateur ?",
          ["def f(): yield 1", "(x for x in range(5))", "lambda: yield 1", "[x for x in range(5)]"], {0, 1}),
        T("Une fois épuisé, un générateur ne peut pas être réutilisé sans être recréé.", True),
         ])

    quiz("Les décorateurs de fonction (Avancé)",
         "Modifiez le comportement de fonctions avec la syntaxe @decorateur.",
         [
        Sx("Quel symbole introduit l'application d'un décorateur ?", ["#", "@", "%", "&"], 1),
        Sx("Qu'est-ce qu'un décorateur en Python, fondamentalement ?", ["Un type de boucle", "Une fonction qui prend une fonction et en renvoie une autre", "Un mot-clé reserve", "Une classe abstraite obligatoire"], 1),
        Sx("Que fait généralement functools.wraps dans un décorateur ?", ["Il accélère la fonction", "Il préserve les métadonnées (nom, docstring) de la fonction décorée", "Il supprime les arguments", "Il rend la fonction asynchrone"], 1),
        M("Quelles affirmations sur les décorateurs sont vraies ?",
          ["@mon_decorateur au-dessus d'une fonction équivaut à f = mon_decorateur(f)", "Un décorateur peut accepter des arguments en étant lui-même une fabrique de décorateurs",
           "On peut empiler plusieurs décorateurs sur une même fonction", "Un décorateur doit obligatoirement modifier la valeur de retour"], {0, 1, 2}),
        M("Quels usages typiques des décorateurs rencontre-t-on en Python ?",
          ["Mesurer le temps d'exécution", "Mettre en cache un résultat (memoization)", "Vérifier des permissions", "Définir le type d'une variable"], {0, 1, 2}),
        T("Un décorateur peut être appliqué à une méthode de classe, pas seulement à une fonction libre.", True),
         ])

    quiz("Les gestionnaires de contexte et l'instruction with (Intermédiaire)",
         "Gérez proprement l'acquisition et la libération de ressources avec with.",
         [
        Sx("Quel bloc garantit la fermeture automatique d'un fichier ouvert ?", ["try/except", "with open(...) as f:", "for f in open(...)", "def open(...):"], 1),
        Sx("Quelles méthodes magiques un objet doit-il définir pour être un gestionnaire de contexte ?", ["__init__ et __del__", "__enter__ et __exit__", "__start__ et __stop__", "__open__ et __close__"], 1),
        Sx("Que renvoie typiquement la méthode __enter__ d'un gestionnaire de contexte de fichier ?", ["None", "L'objet fichier lui-même (ou une ressource)", "True", "Un tuple vide"], 1),
        M("Quelles affirmations sur l'instruction with sont correctes ?",
          ["Elle garantit la libération de la ressource même en cas d'exception", "On peut ouvrir plusieurs contextes sur une seule ligne avec des virgules",
           "Le module contextlib fournit des outils pour créer des gestionnaires de contexte", "with remplace obligatoirement toutes les boucles for"], {0, 1, 2}),
        M("Quels usages typiques de with rencontre-t-on ?",
          ["Ouverture de fichiers", "Verrous (locks) en programmation concurrente", "Connexions à une base de données", "Déclaration de variables globales"], {0, 1, 2}),
        T("La méthode __exit__ d'un gestionnaire de contexte est appelée même si une exception survient dans le bloc with.", True),
         ])

    quiz("Exceptions avancées : hiérarchie et personnalisation (Avancé)",
         "Approfondissez la gestion des erreurs avec des exceptions personnalisées et finally.",
         [
        Sx("De quelle classe doit hériter une exception personnalisée en Python ?", ["object", "BaseException ou une sous-classe comme Exception", "dict", "type"], 1),
        Sx("Quand le bloc finally d'un try s'exécute-t-il ?", ["Seulement si aucune exception ne survient", "Toujours, qu'il y ait eu exception ou non", "Seulement si une exception survient", "Jamais si on utilise return dans try"], 1),
        Sx("Quand le bloc else d'un try/except s'exécute-t-il ?", ["Toujours", "Si aucune exception n'a été levée dans le bloc try", "Seulement en cas d'exception", "Avant le bloc try"], 1),
        M("Quelles affirmations sur les exceptions sont correctes ?",
          ["On peut définir une exception personnalisée en héritant de Exception", "raise sans argument dans un except relève l'exception courante",
           "Plusieurs blocs except peuvent capturer différents types d'erreurs", "Une exception non capturée est silencieusement ignorée"], {0, 1, 2}),
        M("Quelles classes sont des exceptions intégrées standard de Python ?",
          ["ValueError", "KeyError", "ZeroDivisionError", "LoopError"], {0, 1, 2}),
        T("ValueError et TypeError héritent toutes deux de la classe de base Exception.", True),
         ])

    quiz("Classes et objets : les bases de la POO (Débutant)",
         "Découvrez la création de classes, d'instances et de l'attribut self.",
         [
        Sx("Quel mot-clé définit une classe en Python ?", ["def", "class", "struct", "object"], 1),
        Sx("Que représente le paramètre self dans une méthode ?", ["La classe elle-même", "L'instance courante de l'objet", "Une variable globale", "Le module courant"], 1),
        Sx("Quelle méthode spéciale sert de constructeur initialisant une instance ?", ["__new__", "__init__", "__create__", "__start__"], 1),
        M("Quelles affirmations sur les classes sont correctes ?",
          ["Une classe est un modèle pour créer des objets", "Les attributs d'instance sont définis via self.attribut",
           "On instancie une classe en l'appelant comme une fonction", "Toutes les instances d'une classe partagent obligatoirement le même état"], {0, 1, 2}),
        M("Soit class Chien: def __init__(self, nom): self.nom = nom. Quelles instructions sont valides ?",
          ["c = Chien('Rex')", "c.nom", "Chien()", "c = Chien"], {0, 1}),
        T("En Python, le mot-clé self doit obligatoirement être nommé 'self' par le langage lui-même.", False),
         ])

    quiz("Héritage et polymorphisme (Intermédiaire)",
         "Réutilisez et spécialisez du comportement grâce à l'héritage de classes.",
         [
        Sx("Comment une classe Chat hérite-t-elle d'une classe Animal ?", ["class Chat(Animal):", "class Chat extends Animal:", "class Chat: Animal", "class Chat use Animal:"], 0),
        Sx("Quelle fonction permet d'appeler la méthode de la classe parente depuis une sous-classe ?", ["parent()", "super()", "base()", "self.parent()"], 1),
        Sx("Quelle fonction vérifie si un objet est une instance d'une classe donnée ?", ["type()", "isinstance()", "issubclass()", "instanceof()"], 1),
        M("Quelles affirmations sur l'héritage et le polymorphisme sont correctes ?",
          ["Une sous-classe peut redéfinir (override) une méthode de sa classe parente", "Python autorise l'héritage multiple",
           "Le polymorphisme permet d'appeler la même méthode sur des objets de types différents", "Une classe ne peut hériter que d'une seule autre classe en Python"], {0, 1, 2}),
        M("Quelles fonctions intégrées sont utiles pour inspecter les relations entre classes ?",
          ["isinstance()", "issubclass()", "type()", "len()"], {0, 1, 2}),
        T("En Python, une classe peut hériter de plusieurs classes parentes simultanément (héritage multiple).", True),
         ])

    quiz("Méthodes magiques (dunder) (Avancé)",
         "Personnalisez le comportement de vos objets avec les méthodes spéciales.",
         [
        Sx("Quelle méthode magique définit la représentation affichée par print() ?", ["__repr__", "__str__", "__display__", "__print__"], 1),
        Sx("Quelle méthode magique permet de surcharger l'opérateur + ?", ["__plus__", "__add__", "__sum__", "__concat__"], 1),
        Sx("Quelle méthode magique est appelée par len(obj) ?", ["__length__", "__len__", "__size__", "__count__"], 1),
        M("Quelles méthodes magiques permettent de comparer deux objets ?",
          ["__eq__", "__lt__", "__gt__", "__cmp__"], {0, 1, 2}),
        M("Quelles affirmations sur les méthodes dunder sont correctes ?",
          ["Elles commencent et finissent par deux underscores", "__init__ initialise une instance après sa création",
           "__repr__ doit idéalement renvoyer une représentation non ambiguë", "Toute classe doit définir __add__ pour fonctionner"], {0, 1, 2}),
        T("La méthode __str__ est utilisée par str(obj) et print(obj), tandis que __repr__ sert plutôt au débogage.", True),
         ])

    quiz("property, classmethod et staticmethod (Avancé)",
         "Maîtrisez les décorateurs intégrés property, classmethod et staticmethod.",
         [
        Sx("Quel décorateur transforme une méthode en attribut accessible sans parenthèses ?", ["@staticmethod", "@property", "@classmethod", "@abstractmethod"], 1),
        Sx("Quel premier paramètre reçoit une méthode décorée par @classmethod ?", ["self", "cls (la classe)", "Aucun paramètre", "L'instance parente"], 1),
        Sx("Quel décorateur définit une méthode qui ne reçoit ni self ni cls automatiquement ?", ["@classmethod", "@staticmethod", "@property", "@instancemethod"], 1),
        M("Quelles affirmations sur @property sont correctes ?",
          ["Elle permet d'exposer une méthode comme un attribut en lecture", "On peut définir un setter associé avec @nom.setter",
           "Elle est souvent utilisée pour valider une valeur avant de l'assigner", "Elle transforme obligatoirement la méthode en méthode de classe"], {0, 1, 2}),
        M("Quels décorateurs sont fournis nativement par Python pour les méthodes de classe ?",
          ["@staticmethod", "@classmethod", "@property", "@final"], {0, 1, 2}),
        T("Une méthode statique (@staticmethod) peut être appelée directement sur la classe sans créer d'instance.", True),
         ])

    quiz("Classes abstraites et le module abc (Avancé)",
         "Définissez des interfaces avec le module abc et les méthodes abstraites.",
         [
        Sx("Quel module de la bibliothèque standard permet de définir des classes abstraites ?", ["abc", "abstract", "interface", "meta"], 0),
        Sx("Quel décorateur marque une méthode comme devant être implémentée par les sous-classes ?", ["@abstractmethod", "@mustimplement", "@override", "@virtual"], 0),
        Sx("Que se passe-t-il si on instancie directement une classe abstraite avec une méthode abstraite non implémentée ?", ["Rien de particulier", "Une TypeError est levée", "Elle s'instancie avec des valeurs par défaut", "Un avertissement seulement"], 1),
        M("Quelles affirmations sur les classes abstraites sont correctes ?",
          ["Elles héritent typiquement de ABC (Abstract Base Class)", "Elles ne peuvent pas être instanciées directement si une méthode abstraite n'est pas redéfinie",
           "Une sous-classe concrète doit implémenter toutes les méthodes abstraites", "Toute classe Python est abstraite par défaut"], {0, 1, 2}),
        M("Quels éléments sont nécessaires pour créer une classe abstraite avec abc ?",
          ["Hériter de ABC", "Utiliser @abstractmethod sur certaines méthodes", "Importer le module abc", "Utiliser obligatoirement __slots__"], {0, 1, 2}),
        T("Une classe abstraite peut tout de même contenir des méthodes concrètes déjà implémentées.", True),
         ])

    quiz("L'attribut __slots__ (Avancé)",
         "Optimisez la mémoire des instances en limitant leurs attributs avec __slots__.",
         [
        Sx("À quoi sert principalement __slots__ dans une classe ?", ["Trier les attributs alphabétiquement", "Réduire l'empreinte mémoire en limitant les attributs autorisés", "Rendre la classe abstraite", "Créer automatiquement un constructeur"], 1),
        Sx("Que se passe-t-il si on essaie d'assigner un attribut non déclaré dans __slots__ ?", ["Rien, l'attribut est créé normalement", "Une AttributeError est levée", "L'attribut est ignoré silencieusement", "Le programme plante sans message"], 1),
        Sx("Quel attribut spécial __slots__ remplace-t-il généralement pour chaque instance ?", ["__init__", "__dict__", "__class__", "__name__"], 1),
        M("Quelles affirmations sur __slots__ sont correctes ?",
          ["Il se déclare comme un tuple ou une liste de noms de chaînes", "Il peut réduire la consommation mémoire pour de nombreuses instances",
           "Il empêche l'ajout dynamique d'attributs non listés", "Il est obligatoire dans toutes les classes Python"], {0, 1, 2}),
        M("Dans quels contextes __slots__ est-il particulièrement utile ?",
          ["Création de très nombreuses petites instances", "Optimisation mémoire", "Classes de données simples", "Stockage de fonctions globales"], {0, 1, 2}),
        T("Avec __slots__ défini, une instance ne possède plus de __dict__ par défaut, ce qui économise de la mémoire.", True),
         ])

    quiz("Modules et packages (Intermédiaire)",
         "Organisez votre code en modules et packages réutilisables.",
         [
        Sx("Quel mot-clé importe un module entier en Python ?", ["include", "import", "require", "using"], 1),
        Sx("Quel fichier spécial indique traditionnellement qu'un dossier est un package Python ?", ["main.py", "__init__.py", "package.json", "setup.cfg"], 1),
        Sx("Quelle syntaxe importe uniquement la fonction sqrt du module math ?", ["import math.sqrt", "from math import sqrt", "import sqrt from math", "using math.sqrt"], 1),
        M("Quelles affirmations sur les modules sont correctes ?",
          ["Un module est simplement un fichier .py", "On peut renommer un import avec 'as'",
           "from module import *' importe tous les noms publics", "Un module ne peut être importé qu'une seule fois dans tout le programme sans exception"], {0, 1, 2}),
        M("Quelles syntaxes d'import sont valides en Python ?",
          ["import os", "from os import path", "import os as o", "include os"], {0, 1, 2}),
        T("Le nom spécial __name__ vaut '__main__' lorsque le script est exécuté directement (et non importé).", True),
         ])

    quiz("Lecture et écriture de fichiers (Intermédiaire)",
         "Manipulez les fichiers texte avec open, read, write et les modes d'accès.",
         [
        Sx("Quel mode d'ouverture de fichier sert à la lecture seule ?", ["'w'", "'r'", "'a'", "'x'"], 1),
        Sx("Quel mode d'ouverture ajoute du contenu à la fin d'un fichier existant ?", ["'r'", "'w'", "'a'", "'rb'"], 2),
        Sx("Que renvoie f.readlines() sur un fichier texte ?", ["Une chaîne unique", "Une liste de lignes", "Un dictionnaire", "Un tuple de caractères"], 1),
        M("Quelles affirmations sur la manipulation de fichiers sont correctes ?",
          ["with open(...) as f garantit la fermeture du fichier", "Le mode 'w' écrase le contenu existant du fichier",
           "Le mode 'a' n'efface pas le contenu existant", "Un fichier ouvert en 'r' permet d'écrire dedans par défaut"], {0, 1, 2}),
        M("Quelles méthodes permettent de lire le contenu d'un fichier ouvert en lecture ?",
          ["read()", "readline()", "readlines()", "write()"], {0, 1, 2}),
        T("Oublier de fermer un fichier ouvert sans with peut entraîner une perte de données ou une fuite de ressources.", True),
         ])

    quiz("Le module json (Intermédiaire)",
         "Sérialisez et désérialisez des données avec le module json de la bibliothèque standard.",
         [
        Sx("Quelle fonction du module json convertit un objet Python en chaîne JSON ?", ["json.load", "json.dumps", "json.parse", "json.read"], 1),
        Sx("Quelle fonction du module json convertit une chaîne JSON en objet Python ?", ["json.loads", "json.dump", "json.write", "json.encode"], 0),
        Sx("Quelle fonction écrit directement un objet Python en JSON dans un fichier ouvert ?", ["json.dump", "json.dumps", "json.loads", "json.save"], 0),
        M("Quelles affirmations sur le module json sont correctes ?",
          ["json.dumps(indent=2) produit une sortie indentée et lisible", "Un dictionnaire Python se convertit naturellement en objet JSON",
           "json.loads lit une chaîne et renvoie une structure Python", "json.dumps peut sérialiser n'importe quel objet Python sans configuration"], {0, 1, 2}),
        M("Quels types Python se convertissent nativement en JSON avec json.dumps ?",
          ["dict", "list", "str", "set"], {0, 1, 2}),
        T("Le module json ne peut pas sérialiser un set Python directement sans conversion préalable (par exemple en liste).", True),
         ])

    quiz("Le module re et les expressions régulières (Avancé)",
         "Recherchez et manipulez du texte avec les expressions régulières du module re.",
         [
        Sx("Quelle fonction du module re recherche une correspondance n'importe où dans la chaîne ?", ["re.match", "re.search", "re.fullmatch", "re.find"], 1),
        Sx("Que représente le motif \\d dans une expression régulière Python ?", ["Une lettre", "Un chiffre", "Un espace", "Un caractère quelconque"], 1),
        Sx("Quelle fonction remplace toutes les occurrences correspondant à un motif ?", ["re.replace", "re.sub", "re.change", "re.update"], 1),
        M("Quelles affirmations sur le module re sont correctes ?",
          ["re.match ne teste que le début de la chaîne", "re.findall renvoie toutes les correspondances sous forme de liste",
           "Le symbole '*' signifie zéro ou plusieurs répétitions", "Une expression régulière compilée ne peut être utilisée qu'une seule fois"], {0, 1, 2}),
        M("Quels symboles font partie de la syntaxe des expressions régulières ?",
          ["\\d", "\\w", "^", "&&"], {0, 1, 2}),
        T("re.compile() permet de pré-compiler un motif pour le réutiliser efficacement plusieurs fois.", True),
         ])

    quiz("Le module datetime (Intermédiaire)",
         "Manipulez dates et heures avec le module datetime de la bibliothèque standard.",
         [
        Sx("Quelle classe du module datetime représente une date sans heure ?", ["datetime.date", "datetime.time", "datetime.delta", "datetime.calendar"], 0),
        Sx("Quelle méthode renvoie la date et l'heure actuelles ?", ["datetime.now()", "datetime.today_time()", "datetime.current()", "datetime.get()"], 0),
        Sx("Quelle classe représente une durée ou différence entre deux dates ?", ["datetime.delta", "timedelta", "dateinterval", "timeperiod"], 1),
        M("Quelles affirmations sur le module datetime sont correctes ?",
          ["datetime.now() renvoie la date et l'heure courantes", "On peut soustraire deux objets datetime pour obtenir un timedelta",
           "strftime formate une date en chaîne de caractères", "Toutes les dates sont automatiquement converties en UTC"], {0, 1, 2}),
        M("Quelles classes appartiennent au module datetime ?",
          ["date", "time", "timedelta", "calendarweek"], {0, 1, 2}),
        T("La méthode strptime permet de convertir une chaîne de caractères en objet datetime selon un format donné.", True),
         ])

    quiz("Counter et defaultdict du module collections (Intermédiaire)",
         "Simplifiez le comptage et l'initialisation par défaut avec collections.",
         [
        Sx("Quelle classe de collections facilite le comptage d'éléments dans un itérable ?", ["Counter", "OrderedDict", "deque", "ChainMap"], 0),
        Sx("Que renvoie Counter('aabbc') pour la clé 'a' ?", ["1", "2", "3", "KeyError"], 1),
        Sx("Quel avantage offre defaultdict par rapport à un dict classique ?", ["Il trie les clés automatiquement", "Il fournit une valeur par défaut pour les clés absentes au lieu d'une KeyError", "Il interdit les doublons de clés", "Il est immuable"], 1),
        M("Quelles affirmations sur Counter sont correctes ?",
          ["Counter hérite du comportement d'un dictionnaire", "La méthode most_common() renvoie les éléments les plus fréquents",
           "On peut additionner deux objets Counter avec +", "Counter ne peut compter que des chaînes de caractères"], {0, 1, 2}),
        M("Quelles affirmations sur defaultdict sont correctes ?",
          ["On lui passe une fonction de fabrique (par exemple list ou int) à la création", "Accéder à une clé absente crée automatiquement une valeur par défaut",
           "defaultdict(int) initialise les nouvelles clés à 0", "defaultdict ne peut pas être utilisé avec list comme fabrique"], {0, 1, 2}),
        T("defaultdict(list)['x'].append(1) fonctionne sans lever d'erreur même si 'x' n'existait pas auparavant.", True),
         ])
