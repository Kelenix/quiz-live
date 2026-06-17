# -*- coding: utf-8 -*-
def build(quiz, S, Sx, M, T):

    quiz("namedtuple du module collections (Intermédiaire)",
         "Créez des tuples nommés et lisibles avec collections.namedtuple.",
         [
        Sx("Quelle fonction du module collections crée un type de tuple avec des champs nommés ?", ["namedtuple", "deque", "OrderedDict", "ChainMap"], 0),
        Sx("Soit Point = namedtuple('Point', ['x', 'y']) et p = Point(1, 2). Comment accéder à la coordonnée x ?", ["p['x']", "p.x", "p(x)", "p->x"], 1),
        Sx("Un namedtuple est-il mutable comme une liste ?", ["Oui, totalement", "Non, il reste immuable comme un tuple classique", "Seulement ses champs numériques", "Cela dépend de Python 2 ou 3"], 1),
        M("Quelles affirmations sur namedtuple sont correctes ?",
          ["Il permet d'accéder aux champs par nom ou par index", "Il reste compatible avec les opérations habituelles des tuples",
           "La méthode _asdict() le convertit en dictionnaire", "Il autorise l'ajout dynamique de nouveaux champs après création"], {0, 1, 2}),
        M("Quels avantages namedtuple apporte-t-il par rapport à un tuple classique ?",
          ["Lisibilité accrue du code", "Accès aux champs par attribut", "Conservation de l'immutabilité", "Tri automatique des champs"], {0, 1, 2}),
        T("Un namedtuple occupe généralement aussi peu de mémoire qu'un tuple classique.", True),
         ])

    quiz("deque du module collections (Intermédiaire)",
         "Utilisez une file double avec des insertions et suppressions efficaces aux deux extrémités.",
         [
        Sx("Quelle classe de collections offre des insertions/suppressions efficaces en O(1) aux deux extrémités ?", ["list", "deque", "tuple", "frozenset"], 1),
        Sx("Quelle méthode ajoute un élément à gauche d'une deque ?", ["append", "appendleft", "insert(0, x)", "push_front"], 1),
        Sx("Pourquoi privilégier deque plutôt qu'une liste pour des insertions fréquentes en début de séquence ?", ["deque est toujours plus lisible", "Une liste a une complexité O(n) pour insert(0, x), alors que deque est O(1)", "deque consomme toujours moins de mémoire", "Une liste ne supporte pas l'indexation"], 1),
        M("Quelles affirmations sur deque sont correctes ?",
          ["Elle dispose des méthodes append et appendleft", "Elle dispose des méthodes pop et popleft",
           "On peut limiter sa taille avec le paramètre maxlen", "Elle ne peut contenir que des entiers"], {0, 1, 2}),
        M("Dans quels cas deque est-elle particulièrement adaptée ?",
          ["Implémenter une file (queue)", "Implémenter une pile (stack)", "Garder un historique de taille fixe avec maxlen", "Trier rapidement de grandes listes"], {0, 1, 2}),
        T("deque provient du module collections de la bibliothèque standard de Python.", True),
         ])

    quiz("Le module itertools (Avancé)",
         "Combinez et transformez des itérables efficacement avec itertools.",
         [
        Sx("Quelle fonction d'itertools enchaîne plusieurs itérables en un seul ?", ["itertools.chain", "itertools.zip_longest", "itertools.product", "itertools.count"], 0),
        Sx("Quelle fonction d'itertools génère toutes les combinaisons possibles de paires d'éléments ?", ["itertools.permutations", "itertools.combinations", "itertools.product", "itertools.cycle"], 1),
        Sx("Quelle fonction d'itertools répète indéfiniment les éléments d'un itérable ?", ["itertools.repeat", "itertools.cycle", "itertools.count", "itertools.chain"], 1),
        M("Quelles affirmations sur itertools sont correctes ?",
          ["Les fonctions d'itertools renvoient généralement des itérateurs paresseux", "itertools.count() génère une suite infinie de nombres",
           "itertools.product calcule le produit cartésien d'itérables", "itertools fait partie d'une bibliothèque tierce à installer avec pip"], {0, 1, 2}),
        M("Quelles fonctions appartiennent au module itertools ?",
          ["chain", "permutations", "groupby", "sorted"], {0, 1, 2}),
        T("Comme les autres outils d'itertools, itertools.permutations renvoie un itérateur et non une liste directement.", True),
         ])

    quiz("functools : reduce et partial (Avancé)",
         "Manipulez les fonctions comme des objets avec functools.reduce et functools.partial.",
         [
        Sx("Que fait functools.reduce(lambda a, b: a + b, [1, 2, 3, 4]) ?", ["Renvoie [1, 2, 3, 4]", "Renvoie 10 (cumul des additions)", "Renvoie 4", "Lève une erreur"], 1),
        Sx("À quoi sert functools.partial ?", ["Trier une liste partiellement", "Créer une nouvelle fonction en fixant certains arguments d'une fonction existante", "Diviser une fonction en plusieurs morceaux", "Exécuter une fonction de façon asynchrone"], 1),
        Sx("Dans quel module trouve-t-on reduce et partial en Python 3 ?", ["builtins", "functools", "itertools", "operator"], 1),
        M("Quelles affirmations sur functools.reduce sont correctes ?",
          ["Elle applique une fonction cumulative à une séquence", "Elle peut accepter une valeur initiale en troisième argument",
           "Elle renvoie une valeur unique, pas une liste", "Elle est obligatoire pour additionner les éléments d'une liste (sum n'existe pas)"], {0, 1, 2}),
        M("Quels usages typiques de functools.partial rencontre-t-on ?",
          ["Pré-remplir certains arguments d'une fonction générique", "Créer des callbacks spécialisés", "Simplifier des appels répétitifs avec les mêmes paramètres", "Convertir une fonction en générateur"], {0, 1, 2}),
        T("Depuis Python 3, reduce n'est plus une fonction native (builtin) : il faut l'importer depuis functools.", True),
         ])

    quiz("functools.lru_cache (Avancé)",
         "Mémorisez les résultats de fonctions coûteuses avec le décorateur lru_cache.",
         [
        Sx("Quel décorateur de functools met en cache les résultats d'une fonction selon ses arguments ?", ["@functools.cache_only", "@functools.lru_cache", "@functools.memo", "@functools.store"], 1),
        Sx("Que signifie LRU dans lru_cache ?", ["Least Recently Used (le moins récemment utilisé)", "Long Running Unit", "Linear Recursive Update", "Last Result Unique"], 0),
        Sx("Quel type de paramètres une fonction décorée par lru_cache doit-elle recevoir pour être mise en cache correctement ?", ["Des paramètres mutables comme des listes", "Des paramètres hachables (immuables)", "Aucun paramètre", "Uniquement des chaînes"], 1),
        M("Quelles affirmations sur lru_cache sont correctes ?",
          ["Il évite de recalculer un résultat déjà obtenu pour les mêmes arguments", "Il est particulièrement utile pour accélérer une fonction récursive comme Fibonacci",
           "On peut limiter la taille du cache avec le paramètre maxsize", "Il fonctionne même avec des arguments de type liste"], {0, 1, 2}),
        M("Dans quels cas l'utilisation de lru_cache est-elle pertinente ?",
          ["Fonctions pures et déterministes", "Calculs coûteux répétés avec les mêmes arguments", "Appels API dont le résultat change à chaque appel", "Fonctions récursives comme le calcul de Fibonacci"], {0, 1, 3}),
        T("lru_cache est un décorateur fourni par le module functools de la bibliothèque standard.", True),
         ])

    quiz("Les annotations de type (type hints) (Intermédiaire)",
         "Documentez vos fonctions avec des annotations de type sans changer leur comportement à l'exécution.",
         [
        Sx("Que fait Python à l'exécution avec une annotation de type comme def f(x: int) -> int: ... ?", ["Il vérifie strictement le type et lève une erreur si non respecté", "Il ne fait aucune vérification automatique à l'exécution (c'est indicatif)", "Il convertit automatiquement x en int", "Il refuse de compiler le fichier"], 1),
        Sx("Quel module de la bibliothèque standard fournit des types génériques comme List ou Dict pour les annotations ?", ["types", "typing", "collections", "abc"], 1),
        Sx("Comment annoter une variable qui peut être soit un int, soit None ?", ["int | None ou Optional[int]", "int & None", "int + None", "AnyType"], 0),
        M("Quelles affirmations sur les type hints sont correctes ?",
          ["Ils servent surtout à la documentation et aux outils d'analyse statique (mypy)", "Ils n'empêchent pas d'exécuter du code avec un type différent",
           "Depuis Python 3.9+, on peut utiliser list[int] sans importer typing.List", "Ils sont obligatoires pour exécuter un script Python"], {0, 1, 2}),
        M("Quelles syntaxes d'annotation sont valides en Python moderne (3.9+) ?",
          ["def f(x: int) -> str:", "def f(x: list[int]) -> None:", "def f(x: int | str) -> bool:", "def f(x int) -> str:"], {0, 1, 2}),
        T("Les annotations de type sont purement indicatives : l'interpréteur Python standard ne les impose pas à l'exécution.", True),
         ])

    quiz("Les dataclasses (Avancé)",
         "Simplifiez la création de classes de données avec le décorateur @dataclass.",
         [
        Sx("Quel module fournit le décorateur @dataclass ?", ["typing", "dataclasses", "collections", "abc"], 1),
        Sx("Que génère automatiquement @dataclass pour une classe annotée de champs ?", ["Uniquement __str__", "Notamment __init__, __repr__ et __eq__", "Uniquement des getters", "Rien sans configuration explicite"], 1),
        Sx("Quel paramètre de @dataclass rend les instances immuables (comme un namedtuple) ?", ["frozen=True", "immutable=True", "readonly=True", "const=True"], 0),
        M("Quelles affirmations sur les dataclasses sont correctes ?",
          ["Elles réduisent le code répétitif (boilerplate) pour les classes de données", "Les champs se déclarent avec des annotations de type au niveau de la classe",
           "On peut leur donner une valeur par défaut", "Elles interdisent toute méthode personnalisée"], {0, 1, 2}),
        M("Quels éléments @dataclass peut générer automatiquement selon ses paramètres ?",
          ["__init__", "__repr__", "__eq__", "__del__"], {0, 1, 2}),
        T("Avec @dataclass(frozen=True), tenter de modifier un attribut après création lève une exception.", True),
         ])

    quiz("Les énumérations avec Enum (Intermédiaire)",
         "Définissez des ensembles de constantes nommées avec le module enum.",
         [
        Sx("Quelle classe de base du module enum sert à définir une énumération classique ?", ["Enum", "EnumSet", "Flag", "Const"], 0),
        Sx("Comment accède-t-on à la valeur associée à un membre d'énumération Couleur.ROUGE ?", ["Couleur.ROUGE.value", "Couleur.ROUGE()", "Couleur['ROUGE'].get()", "Couleur.ROUGE.val()"], 0),
        Sx("Que renvoie Couleur.ROUGE.name si ROUGE = 1 dans la classe Couleur(Enum) ?", ["1", "'ROUGE'", "'Couleur.ROUGE'", "None"], 1),
        M("Quelles affirmations sur Enum sont correctes ?",
          ["Chaque membre possède un nom (name) et une valeur (value)", "Les membres d'une même énumération sont uniques par identité",
           "On peut itérer sur tous les membres d'une énumération", "Une énumération doit obligatoirement utiliser des chaînes comme valeurs"], {0, 1, 2}),
        M("Quelles classes proviennent du module enum ?",
          ["Enum", "IntEnum", "Flag", "Counter"], {0, 1, 2}),
        T("IntEnum permet de comparer directement les membres d'une énumération à des entiers.", True),
         ])

    quiz("Notions d'async/await et asyncio (Avancé)",
         "Découvrez la programmation asynchrone avec les mots-clés async et await.",
         [
        Sx("Quel mot-clé définit une fonction asynchrone (coroutine) en Python ?", ["async def", "await def", "coroutine def", "yield def"], 0),
        Sx("Quel mot-clé suspend l'exécution d'une coroutine en attendant un résultat ?", ["yield", "await", "pause", "wait"], 1),
        Sx("Quelle fonction d'asyncio lance la boucle d'événements pour exécuter une coroutine principale ?", ["asyncio.start()", "asyncio.run()", "asyncio.exec()", "asyncio.launch()"], 1),
        M("Quelles affirmations sur async/await sont correctes ?",
          ["Une coroutine se définit avec async def", "await ne peut être utilisé qu'à l'intérieur d'une fonction async",
           "asyncio permet de gérer de nombreuses opérations d'E/S concurrentes sur un seul thread", "async/await crée automatiquement plusieurs processus séparés"], {0, 1, 2}),
        M("Dans quels cas la programmation asynchrone avec asyncio est-elle particulièrement utile ?",
          ["Opérations réseau avec beaucoup d'attente d'E/S", "Requêtes HTTP multiples en parallèle", "Calculs intensifs purement CPU", "Lecture de nombreux fichiers en attendant le disque"], {0, 1, 3}),
        T("asyncio repose sur une boucle d'événements à un seul thread plutôt que sur du vrai parallélisme CPU.", True),
         ])

    quiz("Threading et multiprocessing : notions (Avancé)",
         "Comprenez les différences entre threads et processus pour la concurrence en Python.",
         [
        Sx("Quel module de la bibliothèque standard permet de créer des threads ?", ["threading", "asyncio", "concurrent", "process"], 0),
        Sx("Quel module permet de créer de véritables processus séparés pour contourner le GIL ?", ["threading", "multiprocessing", "subprocess", "os"], 1),
        Sx("Pourquoi le multiprocessing est-il souvent préféré au threading pour des tâches intensives en calcul (CPU-bound) ?", ["Les threads sont toujours plus lents à créer", "Le GIL limite l'exécution parallèle réelle du code Python dans plusieurs threads", "multiprocessing ne fonctionne que sur Linux", "threading ne supporte pas les fonctions"], 1),
        M("Quelles affirmations sur threading et multiprocessing sont correctes ?",
          ["Les processus ont chacun leur propre espace mémoire", "Les threads partagent le même espace mémoire au sein d'un processus",
           "multiprocessing est généralement plus adapté aux tâches CPU-bound", "threading est inutile pour les tâches d'E/S (I/O-bound)"], {0, 1, 2}),
        M("Dans quels cas threading est-il généralement approprié ?",
          ["Opérations d'E/S comme les requêtes réseau", "Lecture/écriture de fichiers avec attente", "Calculs mathématiques intensifs purs", "Téléchargements multiples simultanés"], {0, 1, 3}),
        T("Le Global Interpreter Lock (GIL) empêche plusieurs threads Python d'exécuter du bytecode Python simultanément dans l'implémentation CPython classique.", True),
         ])

    quiz("pip et environnements virtuels (Intermédiaire)",
         "Gérez les dépendances Python avec pip et isolez vos projets avec venv.",
         [
        Sx("Quelle commande installe un paquet avec pip ?", ["pip get nom_paquet", "pip install nom_paquet", "pip add nom_paquet", "pip fetch nom_paquet"], 1),
        Sx("Quel module de la bibliothèque standard crée un environnement virtuel ?", ["venv", "virtualpy", "pipenv (uniquement)", "envpy"], 0),
        Sx("Quel fichier liste habituellement les dépendances d'un projet Python pour pip ?", ["requirements.txt", "package.json", "Gemfile", "dependencies.yaml"], 0),
        M("Quelles affirmations sur les environnements virtuels sont correctes ?",
          ["Ils isolent les dépendances d'un projet de l'installation Python globale", "On les active généralement via un script (activate)",
           "Ils évitent les conflits de versions entre projets différents", "Ils modifient la version de Python installée sur tout le système"], {0, 1, 2}),
        M("Quelles commandes pip sont valides et courantes ?",
          ["pip install -r requirements.txt", "pip freeze", "pip uninstall nom_paquet", "pip compile nom_paquet"], {0, 1, 2}),
        T("pip freeze affiche la liste des paquets installés avec leurs versions exactes dans l'environnement courant.", True),
         ])

    quiz("Tests unitaires : notions avec unittest et pytest (Intermédiaire)",
         "Vérifiez le comportement de votre code grâce aux tests automatisés.",
         [
        Sx("Quel module de la bibliothèque standard fournit un cadre de tests unitaires ?", ["unittest", "testpy", "checkmodule", "assertlib"], 0),
        Sx("Quelle instruction Python lève une AssertionError si la condition est fausse ?", ["check", "assert", "verify", "test"], 1),
        Sx("Dans unittest, de quelle classe doit hériter une classe de tests ?", ["unittest.TestSuite", "unittest.TestCase", "unittest.Test", "unittest.Assertion"], 1),
        M("Quelles affirmations sur les tests unitaires en Python sont correctes ?",
          ["pytest est une bibliothèque tierce très populaire pour les tests", "Une méthode de test commence généralement par test_ dans unittest",
           "Les assertions vérifient qu'un résultat correspond à une valeur attendue", "Les tests unitaires garantissent qu'un programme n'aura jamais aucun bug"], {0, 1, 2}),
        M("Quelles méthodes d'assertion existent typiquement dans unittest.TestCase ?",
          ["assertEqual", "assertTrue", "assertRaises", "assertPrint"], {0, 1, 2}),
        T("pytest permet d'écrire des tests sous forme de simples fonctions, sans obligatoirement créer de classe.", True),
         ])

    quiz("Formatage de chaînes avancé (Intermédiaire)",
         "Comparez les méthodes %, .format() et f-strings pour formater du texte.",
         [
        Sx("Que renvoie '{} a {} ans'.format('Lea', 30) ?", ["'Lea a 30 ans'", "'{} a {} ans'", "Erreur", "'Lea' 'a' '30' 'ans'"], 0),
        Sx("Que renvoie '%s a %d ans' % ('Lea', 30) ?", ["'Lea a 30 ans'", "Erreur de syntaxe", "'%s a %d ans'", "None"], 0),
        Sx("Quelle syntaxe permet de nommer explicitement un emplacement dans .format() ?", ["'{nom}'.format(nom='Lea')", "'{0}'.format[nom]", "'{}'.format.nom('Lea')", "format('{nom}', nom='Lea')"], 0),
        M("Quelles affirmations sur le formatage de chaînes sont correctes ?",
          ["Les f-strings sont généralement considérées comme la méthode la plus moderne et lisible", "La méthode .format() permet de réordonner les arguments avec des index {1} {0}",
           "Le formatage avec % est héritée du style proche du C", "Toutes les méthodes de formatage sont strictement interdites depuis Python 3.10"], {0, 1, 2}),
        M("Quelles expressions produisent la chaîne '03' (avec zéro de remplissage) ?",
          ["f'{3:02d}'", "'{:02d}'.format(3)", "'%02d' % 3", "str(3).zfill(1)"], {0, 1, 2}),
        T("Les f-strings permettent d'appeler directement des méthodes à l'intérieur des accolades, comme f'{nom.upper()}'.", True),
         ])

    quiz("Le tri avec sorted et le paramètre key (Intermédiaire)",
         "Triez des séquences personnalisées grâce au paramètre key de sorted et sort.",
         [
        Sx("Quelle fonction renvoie une nouvelle liste triée sans modifier l'originale ?", ["list.sort()", "sorted()", "list.order()", "reorder()"], 1),
        Sx("Quelle méthode trie une liste en place (modifie l'originale) ?", ["sorted()", "list.sort()", "list.order()", "list.reorder()"], 1),
        Sx("Comment trier une liste de chaînes par longueur croissante avec sorted ?", ["sorted(mots, key=len)", "sorted(mots, by=len)", "sorted(mots).len()", "mots.sort(len)"], 0),
        M("Quelles affirmations sur sorted et sort sont correctes ?",
          ["Le paramètre reverse=True inverse l'ordre du tri", "key accepte une fonction appliquée à chaque élément avant comparaison",
           "sorted() fonctionne sur tout itérable, pas seulement les listes", "list.sort() renvoie la liste triée (il faut donc faire l = l.sort())"], {0, 1, 2}),
        M("Quelles expressions trient correctement une liste de tuples par leur second élément ?",
          ["sorted(paires, key=lambda p: p[1])", "sorted(paires, key=lambda p: p[0])", "sorted(paires, key=lambda p: -p[1])[::-1]", "paires.sort(key=lambda p: p[1])"], {0, 2, 3}),
        T("list.sort() trie la liste en place et renvoie None (pas la liste elle-même).", True),
         ])

    quiz("copy : copie superficielle et profonde (Avancé)",
         "Distinguez copie superficielle (shallow) et profonde (deep) avec le module copy.",
         [
        Sx("Quelle fonction du module copy effectue une copie superficielle d'un objet ?", ["copy.copy()", "copy.deepcopy()", "copy.clone()", "copy.duplicate()"], 0),
        Sx("Quelle fonction du module copy copie aussi récursivement les objets imbriqués ?", ["copy.copy()", "copy.deepcopy()", "copy.shallow()", "copy.full()"], 1),
        Sx("Soit a = [[1, 2]]; b = copy.copy(a); b[0].append(3). Que devient a ?", ["[[1, 2]] (inchangé)", "[[1, 2, 3]] (modifié aussi)", "Une erreur est levée", "a devient vide"], 1),
        M("Quelles affirmations sur copy.copy et copy.deepcopy sont correctes ?",
          ["Une copie superficielle ne duplique pas les objets imbriqués", "Une copie profonde duplique récursivement tous les objets imbriqués",
           "list(a) ou a[:] créent aussi des copies superficielles d'une liste", "deepcopy est toujours plus rapide que copy"], {0, 1, 2}),
        M("Dans quels cas une copie profonde (deepcopy) est-elle nécessaire ?",
          ["Quand on veut modifier une structure imbriquée sans affecter l'originale", "Quand l'objet contient des listes ou dictionnaires imbriqués",
           "Quand on copie un entier simple", "Quand on veut une indépendance totale entre deux structures complexes"], {0, 1, 3}),
        T("Pour un objet sans aucune structure imbriquée (comme un entier ou une chaîne), copy et deepcopy ont un effet équivalent.", True),
         ])

    quiz("Portée des variables : global et nonlocal (Intermédiaire)",
         "Comprenez la portée des variables et les mots-clés global et nonlocal.",
         [
        Sx("Quel mot-clé permet de modifier une variable globale depuis l'intérieur d'une fonction ?", ["global", "nonlocal", "outer", "static"], 0),
        Sx("Quel mot-clé permet à une fonction imbriquée de modifier une variable de la fonction englobante (mais non globale) ?", ["global", "nonlocal", "outer", "extern"], 1),
        Sx("Par défaut, une variable assignée à l'intérieur d'une fonction est-elle locale ou globale ?", ["Globale", "Locale", "Cela dépend du système d'exploitation", "Statique"], 1),
        M("Quelles affirmations sur la portée des variables sont correctes ?",
          ["Sans le mot-clé global, une affectation crée une variable locale même si un nom identique existe globalement", "nonlocal s'utilise dans une fonction imbriquée pour cibler la portée englobante",
           "On peut lire une variable globale dans une fonction sans utiliser le mot-clé global", "Le mot-clé global rend une variable accessible depuis tous les autres fichiers automatiquement"], {0, 1, 2}),
        M("Dans quels cas utiliser nonlocal est-il pertinent ?",
          ["Une closure qui doit modifier une variable de la fonction parente", "Une fonction imbriquée incrémentant un compteur défini dans la fonction englobante", "Une fonction de niveau module sans imbrication", "Une variable strictement locale sans fonction parente"], {0, 1}),
        T("Sans le mot-clé global, tenter de réassigner une variable censée être globale dans une fonction crée en réalité une nouvelle variable locale.", True),
         ])

    quiz("La récursion (Intermédiaire)",
         "Résolvez des problèmes en faisant appel à une fonction depuis elle-même.",
         [
        Sx("Qu'est-ce qu'une fonction récursive ?", ["Une fonction qui ne renvoie rien", "Une fonction qui s'appelle elle-même", "Une fonction sans paramètre", "Une fonction définie dans une boucle"], 1),
        Sx("Quel élément est indispensable pour qu'une récursion se termine ?", ["Une boucle for", "Un cas de base (condition d'arrêt)", "Une variable globale", "Un import particulier"], 1),
        Sx("Que se passe-t-il si une fonction récursive n'a pas de cas de base atteignable ?", ["Elle s'exécute une seule fois", "Une RecursionError est levée (dépassement de la profondeur de récursion)", "Elle renvoie automatiquement None", "Python l'optimise en boucle infinie silencieuse"], 1),
        M("Quelles affirmations sur la récursion sont correctes ?",
          ["Le calcul de la factorielle peut s'écrire de façon récursive", "Chaque appel récursif ajoute un niveau à la pile d'appels",
           "Python a une limite par défaut de profondeur de récursion", "La récursion est toujours plus rapide qu'une boucle équivalente"], {0, 1, 2}),
        M("Quels problèmes se prêtent naturellement à une solution récursive ?",
          ["Le parcours d'une arborescence (arbre)", "Le calcul de la suite de Fibonacci", "Le calcul de la factorielle d'un nombre", "La simple addition de deux entiers"], {0, 1, 2}),
        T("sys.setrecursionlimit() permet d'augmenter la limite par défaut de profondeur de récursion en Python.", True),
         ])

    quiz("L'opérateur walrus := (Avancé)",
         "Affectez une valeur dans une expression avec l'opérateur d'affectation walrus introduit en Python 3.8.",
         [
        Sx("Quel symbole représente l'opérateur walrus en Python ?", [":=", "=:", "::", "->"], 0),
        Sx("Depuis quelle version de Python l'opérateur walrus est-il disponible ?", ["3.6", "3.7", "3.8", "3.10"], 2),
        Sx("Que fait if (n := len(donnees)) > 10: print(n) ?", ["Calcule len(donnees), l'affecte à n et teste si n > 10", "Compare directement deux longueurs sans affectation", "Provoque une erreur de syntaxe", "Crée une fonction nommée n"], 0),
        M("Quelles affirmations sur l'opérateur walrus sont correctes ?",
          ["Il permet d'affecter une valeur à une variable au sein d'une expression", "Il est souvent utilisé dans les conditions de boucles while ou de if",
           "Il peut éviter de calculer une même expression deux fois", "Il remplace obligatoirement tous les signes = classiques"], {0, 1, 2}),
        M("Dans quels contextes l'opérateur walrus est-il couramment utilisé ?",
          ["Dans une condition de while pour éviter une duplication de calcul", "Dans une compréhension de liste pour réutiliser une valeur intermédiaire", "Pour définir une fonction", "Pour importer un module"], {0, 1}),
        T("L'opérateur walrus a été introduit avec la PEP 572 dans Python 3.8.", True),
         ])

    quiz("L'instruction match (Avancé)",
         "Découvrez le pattern matching structurel introduit par match/case en Python 3.10.",
         [
        Sx("Depuis quelle version de Python l'instruction match/case est-elle disponible ?", ["3.8", "3.9", "3.10", "3.12"], 2),
        Sx("Quel motif dans un bloc case sert de cas par défaut (équivalent à else) ?", ["case default:", "case _:", "case *:", "case else:"], 1),
        Sx("Que permet de faire match en plus d'une simple comparaison comme avec if/elif ?", ["Uniquement comparer des entiers", "Décomposer (déstructurer) la forme d'une donnée, comme un tuple ou une classe", "Remplacer entièrement les boucles for", "Importer des modules dynamiquement"], 1),
        M("Quelles affirmations sur match/case sont correctes ?",
          ["Le motif _ capture n'importe quelle valeur sans la nommer", "On peut faire correspondre des motifs de séquences comme case [x, y]:",
           "match est une instruction, pas seulement une expression", "match remplace obligatoirement tous les dictionnaires"], {0, 1, 2}),
        M("Quels types de motifs peut-on écrire après case en Python 3.10+ ?",
          ["Une valeur littérale comme case 1:", "Un motif de séquence comme case [a, b]:", "Un motif avec garde comme case x if x > 0:", "Un import comme case import os:"], {0, 1, 2}),
        T("match/case a été introduit officiellement par la PEP 634 dans Python 3.10.", True),
         ])

    quiz("Le module pathlib (Intermédiaire)",
         "Manipulez les chemins de fichiers de façon orientée objet avec pathlib.",
         [
        Sx("Quelle classe principale du module pathlib représente un chemin de fichier système ?", ["pathlib.File", "pathlib.Path", "pathlib.Dir", "pathlib.Route"], 1),
        Sx("Quelle méthode de Path vérifie si un chemin correspond à un fichier existant ?", ["Path.is_file()", "Path.exists_file()", "Path.check()", "Path.find()"], 0),
        Sx("Quel opérateur pathlib permet de joindre des composants de chemin de façon lisible ?", ["+", "/", "&", "%"], 1),
        M("Quelles affirmations sur pathlib sont correctes ?",
          ["Il propose une approche orientée objet, contrairement à os.path qui manipule des chaînes", "Path('dossier') / 'fichier.txt' construit un nouveau chemin",
           "Path possède des méthodes comme exists(), is_dir() et mkdir()", "pathlib ne fonctionne que sous Linux"], {0, 1, 2}),
        M("Quelles méthodes ou propriétés appartiennent à la classe Path ?",
          ["name", "suffix", "parent", "length"], {0, 1, 2}),
        T("pathlib fait partie de la bibliothèque standard de Python depuis la version 3.4.", True),
         ])

    quiz("Le module logging (Intermédiaire)",
         "Tracez l'exécution de vos programmes avec le module logging plutôt qu'avec print.",
         [
        Sx("Quel module de la bibliothèque standard est recommandé pour journaliser des messages d'exécution ?", ["logging", "print", "trace", "debug"], 0),
        Sx("Parmi ces niveaux, lequel est le plus sévère dans le module logging ?", ["DEBUG", "INFO", "WARNING", "CRITICAL"], 3),
        Sx("Quelle fonction crée ou récupère un logger nommé ?", ["logging.getLogger(nom)", "logging.newLogger(nom)", "logging.Logger(nom)", "logging.create(nom)"], 0),
        M("Quelles affirmations sur le module logging sont correctes ?",
          ["Il permet de définir différents niveaux de gravité (DEBUG, INFO, WARNING, ERROR, CRITICAL)", "On peut diriger les logs vers un fichier ou la console",
           "logging est plus flexible que de multiples appels à print pour une application réelle", "logging.CRITICAL est moins sévère que logging.DEBUG"], {0, 1, 2}),
        M("Quels niveaux de gravité standard existent dans le module logging ?",
          ["DEBUG", "INFO", "ERROR", "VERBOSE"], {0, 1, 2}),
        T("Par défaut, le niveau de logging racine de Python est WARNING : les messages INFO et DEBUG sont ignorés tant qu'on ne change pas la configuration.", True),
         ])

    quiz("Le protocole itérateur : __iter__ et __next__ (Avancé)",
         "Créez vos propres objets itérables et itérateurs personnalisés.",
         [
        Sx("Quelle méthode magique doit renvoyer un objet itérateur depuis un objet itérable ?", ["__next__", "__iter__", "__getitem__", "__loop__"], 1),
        Sx("Quelle méthode magique renvoie l'élément suivant d'un itérateur, ou lève StopIteration ?", ["__iter__", "__next__", "__get__", "__step__"], 1),
        Sx("Quelle exception un itérateur doit-il lever pour signaler la fin de l'itération ?", ["IndexError", "StopIteration", "EOFError", "ValueError"], 1),
        M("Quelles affirmations sur le protocole itérateur sont correctes ?",
          ["Un objet itérable définit __iter__", "Un objet itérateur définit __next__",
           "La boucle for utilise implicitement ce protocole en interne", "Tout objet Python est automatiquement un itérateur sans rien définir"], {0, 1, 2}),
        M("Quelles affirmations sur la fonction native iter() et next() sont vraies ?",
          ["iter(obj) appelle __iter__ sur obj", "next(it) appelle __next__ sur it",
           "next() peut accepter une valeur par défaut renvoyée en cas de StopIteration", "iter() transforme n'importe quel objet en générateur infini"], {0, 1, 2}),
        T("Une fonction génératrice (avec yield) implémente automatiquement le protocole itérateur (__iter__ et __next__).", True),
         ])

    quiz("La surcharge d'opérateurs (Avancé)",
         "Redéfinissez le comportement des opérateurs (+, ==, <, ...) pour vos propres classes.",
         [
        Sx("Quelle méthode magique permet de définir le comportement de l'opérateur == pour une classe ?", ["__eq__", "__equals__", "__is__", "__compare__"], 0),
        Sx("Quelle méthode magique surcharge l'opérateur de multiplication * ?", ["__times__", "__mul__", "__multiply__", "__product__"], 1),
        Sx("Quelle méthode magique permet de définir le comportement de l'opérateur < ?", ["__less__", "__lt__", "__below__", "__compare__"], 1),
        M("Quelles affirmations sur la surcharge d'opérateurs sont correctes ?",
          ["Elle permet à des objets personnalisés de réagir aux opérateurs standard comme +, -, ==", "__add__ est appelée pour l'opérateur +",
           "On peut définir __radd__ pour gérer l'addition quand l'objet est à droite", "Surcharger un opérateur change aussi son comportement sur les types natifs comme int"], {0, 1, 2}),
        M("Quelles méthodes magiques sont liées aux opérateurs de comparaison ?",
          ["__eq__", "__lt__", "__ge__", "__hash__"], {0, 1, 2}),
        T("Si une classe définit __eq__ sans définir __hash__, ses instances deviennent par défaut non hachables dans certains cas (utile à savoir pour les sets et dict).", True),
         ])

    quiz("map, filter, zip et enumerate (Intermédiaire)",
         "Combinez ces fonctions intégrées pour transformer et parcourir des itérables élégamment.",
         [
        Sx("Que renvoie list(map(str, [1, 2, 3])) ?", ["[1, 2, 3]", "['1', '2', '3']", "'123'", "Erreur"], 1),
        Sx("Que renvoie list(filter(lambda x: x > 0, [-1, 0, 1, 2])) ?", ["[-1, 0, 1, 2]", "[1, 2]", "[-1, 0]", "[]"], 1),
        Sx("Que renvoie list(enumerate(['a', 'b'])) ?", ["[('a', 0), ('b', 1)]", "[(0, 'a'), (1, 'b')]", "['a', 'b']", "[0, 1]"], 1),
        M("Quelles affirmations sur map, filter, zip et enumerate sont correctes ?",
          ["map applique une fonction à chaque élément d'un itérable", "filter conserve uniquement les éléments pour lesquels la fonction renvoie une valeur vraie",
           "zip associe des éléments de plusieurs itérables par position", "enumerate renvoie uniquement les valeurs sans les index"], {0, 1, 2}),
        M("Quelles expressions renvoient un itérateur en Python 3 (et non une liste directement) ?",
          ["map(str, [1, 2])", "filter(None, [0, 1])", "zip([1, 2], [3, 4])", "[x for x in range(3)]"], {0, 1, 2}),
        T("zip() s'arrête dès que le plus court des itérables fournis est épuisé.", True),
         ])

    quiz("Unpacking avancé et affectations multiples (Intermédiaire)",
         "Décomposez des séquences avec l'unpacking, y compris l'opérateur étoile *.",
         [
        Sx("Soit a, b, c = [1, 2, 3]. Que vaut b ?", ["1", "2", "3", "Erreur"], 1),
        Sx("Soit a, *reste = [1, 2, 3, 4]. Que vaut reste ?", ["[2, 3, 4]", "2", "[1, 2, 3, 4]", "Erreur"], 0),
        Sx("Soit premier, *milieu, dernier = [1, 2, 3, 4, 5]. Que vaut milieu ?", ["[2, 3, 4]", "[1, 5]", "[3]", "2"], 0),
        M("Quelles affirmations sur l'unpacking sont correctes ?",
          ["On peut décomposer un tuple directement dans plusieurs variables", "L'opérateur * capture les éléments restants dans une liste",
           "On peut utiliser l'unpacking pour échanger deux variables : a, b = b, a", "On ne peut utiliser qu'une seule étoile * par affectation"], {0, 1, 2}),
        M("Quelles affectations sont valides en Python ?",
          ["x, y = 1, 2", "x, *y = [1, 2, 3]", "*x, y = [1, 2, 3]", "*x, *y = [1, 2, 3]"], {0, 1, 2}),
        T("L'instruction a, b = b, a permet d'échanger les valeurs de deux variables sans variable temporaire explicite.", True),
         ])

    quiz("Comparaisons chaînées et expressions ternaires (Intermédiaire)",
         "Écrivez des comparaisons concises et des expressions conditionnelles en une ligne.",
         [
        Sx("Que renvoie l'expression 1 < 2 < 3 en Python ?", ["True", "False", "Erreur de syntaxe", "2"], 0),
        Sx("Que renvoie l'expression ternaire 'pair' if 4 % 2 == 0 else 'impair' ?", ["'pair'", "'impair'", "True", "Erreur"], 0),
        Sx("Quelle est la syntaxe générale d'une expression ternaire en Python ?", ["valeur_si_vrai if condition else valeur_si_faux", "if condition then valeur1 else valeur2", "condition ? valeur1 : valeur2", "valeur1 else valeur2 if condition"], 0),
        M("Quelles affirmations sur les comparaisons chaînées sont correctes ?",
          ["1 < x < 10 équivaut à (1 < x) and (x < 10)", "Les comparaisons chaînées évitent de répéter la variable centrale",
           "On peut chaîner plus de deux comparaisons à la suite", "Une comparaison chaînée est toujours plus lente qu'un and explicite"], {0, 1, 2}),
        M("Quelles expressions sont des expressions ternaires valides en Python ?",
          ["x if x > 0 else -x", "max(x, 0) if x else 0", "(x > 0) ? x : -x", "'oui' if True else 'non'"], {0, 1, 3}),
        T("L'expression ternaire en Python place la condition au milieu, contrairement à certains langages comme le C où elle est en premier.", True),
         ])

    quiz("divmod et les opérateurs // et % (Débutant)",
         "Calculez quotient et reste simultanément avec divmod et les opérateurs associés.",
         [
        Sx("Que renvoie divmod(17, 5) ?", ["(3, 2)", "(2, 3)", "3.4", "[17, 5]"], 0),
        Sx("Que renvoie 17 // 5 ?", ["3", "3.4", "2", "5"], 0),
        Sx("Que renvoie 17 % 5 ?", ["3", "2", "5", "0"], 1),
        M("Quelles affirmations sur divmod et les opérateurs // et % sont correctes ?",
          ["divmod(a, b) renvoie un tuple (a // b, a % b)", "// est appelé division entière (floor division)",
           "% calcule le reste de la division euclidienne", "// renvoie toujours un float en Python 3"], {0, 1, 2}),
        M("Quelles expressions valent 2 ?",
          ["divmod(8, 3)[1]", "8 % 3", "8 // 4", "divmod(8, 3)[0]"], {0, 1, 2}),
        T("Pour des entiers positifs, a == (a // b) * b + (a % b) est toujours vrai en Python.", True),
         ])

    quiz("Gestion mémoire et GIL : notions (Avancé)",
         "Découvrez les notions de comptage de références, garbage collector et GIL en Python.",
         [
        Sx("Quelle technique principale CPython utilise-t-il pour gérer la mémoire des objets ?", ["Le comptage de références", "La compilation statique uniquement", "L'allocation manuelle obligatoire", "Le ramasse-miettes Java"], 0),
        Sx("Que signifie l'acronyme GIL ?", ["Global Interpreter Lock", "General Index List", "Garbage Interpreter Loop", "Global Iteration Limiter"], 0),
        Sx("Quel module permet de déclencher manuellement une collecte du garbage collector ?", ["gc", "memory", "gil", "ref"], 0),
        M("Quelles affirmations sur la gestion mémoire de Python sont correctes ?",
          ["Un objet est libéré quand son compteur de références atteint zéro", "Le garbage collector aide à détecter les cycles de références",
           "Le GIL empêche deux threads d'exécuter du bytecode Python en même temps dans CPython", "Python n'effectue jamais de gestion automatique de la mémoire"], {0, 1, 2}),
        M("Quelles conséquences pratiques le GIL peut-il avoir sur un programme Python ?",
          ["Limiter le gain de performance du threading pour des tâches CPU-bound", "Ne pas affecter les opérations d'E/S qui libèrent le GIL pendant l'attente",
           "Pousser à utiliser multiprocessing pour du parallélisme CPU réel", "Empêcher totalement toute forme de concurrence en Python"], {0, 1, 2}),
        T("Le comptage de références et le garbage collector cyclique fonctionnent ensemble dans l'implémentation standard CPython.", True),
         ])

    quiz("Listes, tuples et sets : performance et usage (Intermédiaire)",
         "Choisissez la structure de données adaptée selon mutabilité, ordre et performance.",
         [
        Sx("Quelle structure est mutable parmi liste, tuple et set ?", ["tuple uniquement", "liste et set", "Aucune des trois", "tuple et set"], 1),
        Sx("Quelle structure ne contient jamais de doublons ?", ["liste", "tuple", "set", "Aucune"], 2),
        Sx("Quelle est la complexité moyenne de la recherche d'un élément dans un set, comparée à une liste ?", ["O(1) pour le set contre O(n) pour la liste en moyenne", "O(n) pour les deux", "O(log n) pour les deux", "Le set est toujours plus lent"], 0),
        M("Quelles affirmations sur le choix entre liste, tuple et set sont correctes ?",
          ["Un tuple est préférable pour des données fixes qui ne doivent pas changer", "Un set est idéal pour tester rapidement l'appartenance d'un élément",
           "Une liste conserve l'ordre d'insertion des éléments", "Un set conserve l'ordre exact d'insertion comme une liste"], {0, 1, 2}),
        M("Dans quels cas un tuple est-il préférable à une liste ?",
          ["Quand les données ne doivent pas être modifiées", "Quand on veut utiliser la séquence comme clé de dictionnaire", "Quand on veut ajouter fréquemment des éléments", "Quand on veut une légère économie de mémoire pour des données fixes"], {0, 1, 3}),
        T("Un tuple peut servir de clé de dictionnaire car il est hachable, contrairement à une liste qui est mutable et donc non hachable.", True),
         ])
