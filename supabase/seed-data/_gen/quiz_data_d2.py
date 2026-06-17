# -*- coding: utf-8 -*-
def build(quiz, S, Sx, M, T):

    quiz("Méthodes de chaînes : recherche et test (Intermédiaire)",
         "Recherchez des sous-chaînes et testez la composition d'une chaîne de caractères.",
         [
        Sx("Que renvoie 'Bonjour'.find('jour') ?", ["3", "4", "-1", "True"], 1),
        Sx("Que renvoie 'abc'.find('z') ?", ["0", "-1", "None", "Erreur"], 1),
        Sx("Que renvoie '123'.isdigit() ?", ["True", "False", "'123'", "Erreur"], 0),
        M("Quelles méthodes de chaîne renvoient un booléen ?",
          ["isdigit", "isalpha", "startswith", "find"], {0, 1, 2}),
        M("Quelles affirmations sur la recherche dans les chaînes sont correctes ?",
          ["'in' teste la présence d'une sous-chaîne", "find renvoie -1 si la sous-chaîne est absente",
           "index lève une ValueError si la sous-chaîne est absente", "find lève toujours une exception si absente"], {0, 1, 2}),
        T("'Hello'.endswith('lo') renvoie True.", True),
         ])

    quiz("Découpage et assemblage de chaînes : split et join (Intermédiaire)",
         "Transformez des chaînes en listes et inversement avec split et join.",
         [
        Sx("Que renvoie 'a,b,c'.split(',') ?", ["['a', 'b', 'c']", "'a,b,c'", "('a','b','c')", "Erreur"], 0),
        Sx("Que renvoie '-'.join(['a', 'b', 'c']) ?", ["'a-b-c'", "['a-b-c']", "'abc'", "Erreur"], 0),
        Sx("Que renvoie '  Python  '.strip() ?", ["'  Python  '", "'Python'", "'Python  '", "'  Python'"], 1),
        M("Quelles affirmations sur split et join sont correctes ?",
          ["split() sans argument découpe sur les espaces blancs", "join s'appelle sur le séparateur, avec la liste en argument",
           "split renvoie toujours une liste de chaînes", "join peut joindre des éléments de n'importe quel type sans conversion"], {0, 1, 2}),
        M("Quelles expressions renvoient 'a-b-c' ?",
          ["'-'.join(['a','b','c'])", "'-'.join('a,b,c'.split(','))", "'a,b,c'.replace(',', '-')", "'_'.join(['a','b','c'])"], {0, 1, 2}),
        T("La méthode strip() supprime les espaces (et autres caractères blancs) en début et fin de chaîne, mais pas au milieu.", True),
         ])

    quiz("Méthodes de listes avancées (Intermédiaire)",
         "Approfondissez les méthodes remove, pop, sort, reverse et count des listes.",
         [
        Sx("Que fait l.pop() sur une liste sans argument ?", ["Supprime le premier élément", "Supprime et renvoie le dernier élément", "Vide toute la liste", "Erreur"], 1),
        Sx("Que fait l.remove(x) si x apparaît plusieurs fois dans la liste ?", ["Supprime toutes les occurrences", "Supprime uniquement la première occurrence trouvée", "Lève toujours une erreur", "Ne fait rien"], 1),
        Sx("Que renvoie [3, 1, 2].count(1) ?", ["0", "1", "2", "3"], 1),
        M("Quelles affirmations sur les méthodes de liste sont correctes ?",
          ["sort() trie la liste en place", "reverse() inverse l'ordre des éléments en place",
           "pop(i) supprime et renvoie l'élément à l'index i", "remove(x) recherche x par index et non par valeur"], {0, 1, 2}),
        M("Quelles méthodes modifient la liste sur laquelle elles sont appelées (en place) ?",
          ["sort()", "reverse()", "append()", "sorted()"], {0, 1, 2}),
        T("l.remove(x) lève une ValueError si x n'est pas présent dans la liste.", True),
         ])

    quiz("Listes imbriquées et matrices (Intermédiaire)",
         "Manipulez des listes de listes pour représenter des structures à deux dimensions.",
         [
        Sx("Soit m = [[1, 2], [3, 4]]. Que renvoie m[1][0] ?", ["1", "2", "3", "4"], 2),
        Sx("Comment crée-t-on une matrice 2x2 remplie de zéros avec une compréhension ?", ["[[0, 0] for _ in range(2)]", "[0, 0, 0, 0]", "{0: 0}", "(0, 0)"], 0),
        Sx("Que renvoie len([[1, 2, 3], [4, 5]]) ?", ["5", "2", "3", "Erreur"], 1),
        M("Quelles affirmations sur les listes imbriquées sont correctes ?",
          ["Une liste peut contenir d'autres listes comme éléments", "m[i][j] accède à la ligne i puis à la colonne j",
           "On peut parcourir une matrice avec des boucles for imbriquées", "Une liste imbriquée est automatiquement convertie en tableau NumPy"], {0, 1, 2}),
        M("Quelles expressions créent une matrice 3x3 de zéros correctement (sans partager les lignes par référence) ?",
          ["[[0]*3 for _ in range(3)]", "[[0, 0, 0] for _ in range(3)]", "[[0]*3]*3", "[[0 for _ in range(3)] for _ in range(3)]"], {0, 1, 3}),
        T("Écrire [[0]*3]*3 crée trois références vers la même sous-liste, ce qui peut causer des effets de bord inattendus.", True),
         ])

    quiz("Les dictionnaires : méthodes avancées (Intermédiaire)",
         "Manipulez les dictionnaires avec update, pop, setdefault et la fusion.",
         [
        Sx("Que fait d.setdefault('x', 0) si 'x' n'existe pas encore dans d ?", ["Lève une erreur", "Ajoute 'x' avec la valeur 0 et la renvoie", "Ne fait rien", "Supprime 'x'"], 1),
        Sx("Que fait d.pop('x') si 'x' existe dans d ?", ["Renvoie et supprime la valeur associée à 'x'", "Renvoie seulement la clé", "Ajoute 'x'", "Ne fait rien"], 0),
        Sx("Depuis Python 3.9, quel opérateur permet de fusionner deux dictionnaires ?", ["+", "|", "&", "%"], 1),
        M("Quelles affirmations sur les méthodes de dictionnaire sont correctes ?",
          ["update() ajoute ou met à jour des paires clé-valeur depuis un autre dict", "pop(cle, defaut) évite une KeyError si la clé est absente",
           "setdefault ajoute la clé seulement si elle est absente", "Un dictionnaire ne peut avoir que des clés de type chaîne"], {0, 1, 2}),
        M("Quelles expressions fusionnent deux dictionnaires d1 et d2 (d2 prioritaire en cas de conflit) ?",
          ["{**d1, **d2}", "d1 | d2", "d1.update(d2) puis utiliser d1", "d1 + d2"], {0, 1, 2}),
        T("d.get(cle, valeur_par_defaut) ne modifie jamais le dictionnaire, contrairement à setdefault qui peut l'ajouter.", True),
         ])

    quiz("Itération avancée sur les dictionnaires (Intermédiaire)",
         "Parcourez clés, valeurs et paires d'un dictionnaire efficacement.",
         [
        Sx("Quelle méthode renvoie les paires clé-valeur d'un dictionnaire pour itération ?", ["keys()", "values()", "items()", "pairs()"], 2),
        Sx("Soit d = {'a': 1, 'b': 2}. Que fait for k, v in d.items(): ?", ["Itère sur les clés seulement", "Itère sur les valeurs seulement", "Itère sur chaque paire clé-valeur", "Lève une erreur"], 2),
        Sx("Par défaut, sur quoi itère for x in d: pour un dictionnaire d ?", ["Les valeurs", "Les clés", "Les paires (clé, valeur)", "Rien, c'est une erreur"], 1),
        M("Quelles affirmations sur l'itération de dictionnaires sont correctes ?",
          ["items() permet de récupérer simultanément clé et valeur", "values() ne donne accès qu'aux valeurs",
           "L'ordre d'itération suit l'ordre d'insertion depuis Python 3.7", "On ne peut jamais modifier un dictionnaire pendant qu'on itère dessus sans risque d'erreur"], {0, 1, 2}),
        M("Quelles expressions sont valides pour parcourir d = {'x': 1, 'y': 2} ?",
          ["for k in d:", "for k, v in d.items():", "for v in d.values():", "for k, v in d:"], {0, 1, 2}),
        T("Modifier la taille d'un dictionnaire (ajout/suppression de clé) pendant une itération directe sur lui peut lever une RuntimeError.", True),
         ])

    quiz("Les ensembles : méthodes et opérations avancées (Intermédiaire)",
         "Approfondissez les opérations ensemblistes : différence, sous-ensemble et frozenset.",
         [
        Sx("Que renvoie {1, 2, 3} - {2, 3} ?", ["{1}", "{2, 3}", "{1, 2, 3}", "{}"], 0),
        Sx("Quelle méthode ajoute un seul élément à un set ?", ["append", "add", "insert", "push"], 1),
        Sx("Quelle est la version immuable (non modifiable) d'un set en Python ?", ["tuple", "frozenset", "constset", "fixedset"], 1),
        M("Quelles affirmations sur les opérations d'ensembles sont correctes ?",
          ["issubset() teste si un ensemble est inclus dans un autre", "symmetric_difference renvoie les éléments présents dans un seul des deux ensembles",
           "Les sets sont non ordonnés et sans doublons", "Un frozenset peut être modifié après création comme un set normal"], {0, 1, 2}),
        M("Quelles expressions impliquant des sets sont valides ?",
          ["{1, 2}.issubset({1, 2, 3})", "{1, 2} ^ {2, 3}", "frozenset([1, 2, 3])", "{1, 2}.append(3)"], {0, 1, 2}),
        T("Un frozenset est hachable et peut donc être utilisé comme clé de dictionnaire, contrairement à un set classique.", True),
         ])

    quiz("Fonctions imbriquées et closures (Avancé)",
         "Comprenez les fonctions définies à l'intérieur d'autres fonctions et leurs closures.",
         [
        Sx("Qu'est-ce qu'une fonction imbriquée (nested function) ?", ["Une fonction définie à l'intérieur d'une autre fonction", "Une fonction sans paramètre", "Une fonction qui appelle une API", "Une fonction décorée"], 0),
        Sx("Qu'est-ce qu'une closure en Python ?", ["Une fonction qui capture des variables de la portée englobante même après le retour de cette dernière", "Une boucle infinie", "Un type de dictionnaire", "Une fonction sans corps"], 0),
        Sx("Quel mot-clé permet à une fonction imbriquée de modifier une variable de la fonction englobante ?", ["global", "nonlocal", "outer", "static"], 1),
        M("Quelles affirmations sur les closures sont correctes ?",
          ["Une closure conserve l'accès aux variables de son environnement de création", "Les fabriques de fonctions (function factories) utilisent souvent des closures",
           "Une fonction imbriquée peut lire les variables de la fonction englobante sans nonlocal", "Une closure ne peut jamais être renvoyée par une fonction"], {0, 1, 2}),
        M("Dans quels cas une closure est-elle utile ?",
          ["Créer des compteurs personnalisés", "Créer des décorateurs", "Mémoriser un état entre plusieurs appels sans variable globale", "Trier une liste"], {0, 1, 2}),
        T("Une closure permet à une fonction interne de continuer à accéder aux variables de la fonction externe même après que celle-ci a fini de s'exécuter.", True),
         ])

    quiz("Arguments positionnels uniquement et nommés uniquement (Avancé)",
         "Restreignez la façon d'appeler vos fonctions avec / et * dans la signature.",
         [
        Sx("Dans def f(a, b, /, c), quels paramètres doivent être passés en position uniquement ?", ["a et b", "c uniquement", "Aucun", "a, b et c"], 0),
        Sx("Dans def f(a, *, b), comment doit-on obligatoirement passer b lors de l'appel ?", ["En position uniquement", "Par mot-clé uniquement (b=valeur)", "On ne peut pas le passer", "Comme a"], 1),
        Sx("Depuis quelle version de Python le séparateur / pour les paramètres positionnels uniquement est-il disponible ?", ["3.0", "3.6", "3.8", "3.11"], 2),
        M("Quelles affirmations sur ces restrictions de paramètres sont correctes ?",
          ["Le symbole / sépare les paramètres positionnels uniquement des autres", "Le symbole * impose que les paramètres suivants soient nommés",
           "Ces restrictions clarifient et stabilisent l'API d'une fonction", "Ces restrictions sont obligatoires pour toute fonction Python"], {0, 1, 2}),
        M("Soit def f(a, /, b, *, c). Quels appels sont valides ?",
          ["f(1, 2, c=3)", "f(1, b=2, c=3)", "f(a=1, b=2, c=3)", "f(1, 2, 3)"], {0, 1}),
        T("Dans def f(a, /, b), l'appel f(a=1, b=2) est invalide car a est positionnel uniquement.", True),
         ])

    quiz("Fonctions comme objets de première classe (Intermédiaire)",
         "Manipulez les fonctions comme n'importe quelle autre valeur en Python.",
         [
        Sx("Peut-on assigner une fonction à une variable en Python ?", ["Non, jamais", "Oui, les fonctions sont des objets de première classe", "Seulement les lambdas", "Seulement les méthodes"], 1),
        Sx("Peut-on passer une fonction comme argument à une autre fonction ?", ["Non", "Oui", "Seulement avec lambda", "Seulement en POO"], 1),
        Sx("Que renvoie une fonction qui définit et renvoie une autre fonction (sans l'appeler) ?", ["Le résultat de la fonction interne", "La fonction interne elle-même (l'objet fonction)", "None", "Une erreur"], 1),
        M("Quelles affirmations sur les fonctions de première classe sont correctes ?",
          ["On peut stocker des fonctions dans une liste ou un dictionnaire", "On peut renvoyer une fonction depuis une autre fonction",
           "Une fonction peut être passée en argument à une autre fonction", "Une fonction ne peut être appelée qu'une seule fois dans tout le programme"], {0, 1, 2}),
        M("Quelles expressions illustrent les fonctions comme objets de première classe ?",
          ["operations = {'add': lambda a, b: a + b}", "def applique(f, x): return f(x)", "fonctions = [str, int, float]", "def f(): pass; del f"], {0, 1, 2}),
        T("En Python, les fonctions définies avec def sont des instances de la classe 'function', tout comme les lambdas.", True),
         ])

    quiz("Constantes, conventions de nommage et PEP 8 (Débutant)",
         "Adoptez les bonnes pratiques de style recommandées par la PEP 8.",
         [
        Sx("Quelle convention de casse PEP 8 recommande-t-on pour les noms de variables et de fonctions ?", ["camelCase", "snake_case", "PascalCase", "kebab-case"], 1),
        Sx("Quelle convention de casse recommande-t-on pour les noms de classes ?", ["snake_case", "PascalCase (CamelCase)", "UPPER_CASE", "kebab-case"], 1),
        Sx("Comment nomme-t-on traditionnellement une constante en Python (bien qu'aucune vraie constante n'existe) ?", ["en minuscules", "en MAJUSCULES_AVEC_UNDERSCORES", "avec un prefixe const_", "avec un point final"], 1),
        M("Quelles affirmations sur la PEP 8 sont correctes ?",
          ["Elle recommande 4 espaces pour l'indentation", "Elle recommande le snake_case pour les fonctions et variables",
           "Elle recommande des lignes limitées en longueur (souvent 79 caractères)", "Elle impose l'usage exclusif de tabulations"], {0, 1, 2}),
        M("Quels noms respectent la convention snake_case ?",
          ["mon_compteur", "calculer_total", "nombreDePoints", "valeur_max"], {0, 1, 3}),
        T("PEP 8 est un guide de style officieux mais largement adopté par la communauté Python, pas une règle imposée par l'interpréteur.", True),
         ])

    quiz("Les chaînes brutes et l'échappement (Intermédiaire)",
         "Maîtrisez les séquences d'échappement et les chaînes brutes (raw strings).",
         [
        Sx("Que représente la séquence '\\n' dans une chaîne Python ?", ["Une tabulation", "Un saut de ligne", "Un antislash littéral", "Un espace"], 1),
        Sx("Quel préfixe crée une chaîne brute où les antislashs ne sont pas interprétés comme échappement ?", ["b'...'", "r'...'", "f'...'", "u'...'"], 1),
        Sx("Pourquoi utilise-t-on souvent des chaînes brutes pour les expressions régulières ?", ["Pour accélérer l'exécution", "Pour éviter que Python interprète les antislashs avant que re ne les utilise", "Parce que re l'exige obligatoirement", "Pour les rendre immuables"], 1),
        M("Quelles affirmations sur les séquences d'échappement sont correctes ?",
          ["'\\t' représente une tabulation", "'\\\\' représente un antislash littéral",
           "'\\'' permet d'inclure une apostrophe dans une chaîne entre apostrophes", "Toutes les chaînes Python sont automatiquement des chaînes brutes"], {0, 1, 2}),
        M("Quelles expressions sont des chaînes brutes valides ?",
          ["r'C:\\\\nouveau\\\\dossier'", "r'\\d+'", "f'\\d+'", "rb'donnees'"], {0, 1, 3}),
        T("Dans une chaîne brute comme r'\\n', le texte contient littéralement un antislash suivi de la lettre n, et non un saut de ligne.", True),
         ])

    quiz("L'opérateur d'identité is et l'égalité == (Intermédiaire)",
         "Distinguez la comparaison de valeurs (==) et la comparaison d'identité (is).",
         [
        Sx("Que teste l'opérateur is en Python ?", ["L'égalité des valeurs", "Si deux variables référencent le même objet en mémoire", "La différence de type", "La taille mémoire"], 1),
        Sx("Que teste l'opérateur == en Python ?", ["L'identité des objets", "L'égalité des valeurs (via __eq__)", "Le type uniquement", "Rien, il n'existe pas"], 1),
        Sx("Quelle est la bonne pratique pour comparer une variable à None ?", ["x == None", "x is None", "x.equals(None)", "x = None"], 1),
        M("Quelles affirmations sur is et == sont correctes ?",
          ["is compare l'identité (l'adresse mémoire) des objets", "== compare la valeur via la méthode __eq__",
           "Deux listes ayant le même contenu peuvent être égales (==) sans être identiques (is)", "is et == donnent toujours le même résultat pour tous les objets"], {0, 1, 2}),
        M("Quelles affirmations sur le petit cache d'entiers de CPython sont vraies dans la pratique courante (à titre indicatif) ?",
          ["De petits entiers comme 1 ou 2 peuvent être mis en cache et partagés par CPython", "Le comportement de is sur les entiers ne doit pas être considéré comme garanti dans tous les cas", "is est recommandé pour comparer des entiers de façon fiable", "== est recommandé pour comparer des valeurs numériques"], {0, 1, 3}),
        T("On utilise is None plutôt que == None car is vérifie l'identité de l'objet singleton None, ce qui est plus sûr et idiomatique.", True),
         ])

    quiz("Les valeurs par défaut mutables : un piège classique (Avancé)",
         "Évitez le piège classique des arguments par défaut mutables en Python.",
         [
        Sx("Que se passe-t-il si on définit def f(items=[]): items.append(1); return items et qu'on appelle f() plusieurs fois ?", ["Une nouvelle liste vide est créée à chaque appel", "La même liste par défaut est réutilisée et s'accumule entre les appels", "Une erreur est levée au second appel", "items est automatiquement réinitialisée"], 1),
        Sx("Quand l'expression par défaut d'un paramètre (comme []) est-elle évaluée ?", ["À chaque appel de la fonction", "Une seule fois, à la définition de la fonction", "Jamais", "Au moment de l'import du module seulement si appelé"], 1),
        Sx("Quelle est la solution idiomatique recommandée pour éviter ce piège ?", ["Utiliser une liste vide [] comme avant", "Utiliser None comme valeur par défaut et créer la liste dans le corps de la fonction", "Toujours utiliser des tuples", "Ne jamais utiliser de valeur par défaut"], 1),
        M("Quelles affirmations sur les valeurs par défaut mutables sont correctes ?",
          ["Les objets mutables (liste, dict, set) comme valeur par défaut sont partagés entre les appels", "Le piège peut entraîner des bugs difficiles à diagnostiquer",
           "def f(items=None): puis 'items = items or []' est une solution courante", "Ce piège ne se produit jamais avec un dictionnaire vide {} par défaut"], {0, 1, 2}),
        M("Quels types de valeurs par défaut sont sûrs (sans piège de mutation partagée) ?",
          ["None", "Un entier comme 0", "Une chaîne comme ''", "Une liste vide [] directement"], {0, 1, 2}),
        T("Le piège des arguments par défaut mutables vient du fait que l'objet par défaut est créé une seule fois, lors de la définition de la fonction, et non à chaque appel.", True),
         ])

    quiz("Itérables vs itérateurs (Avancé)",
         "Distinguez précisément la notion d'itérable et celle d'itérateur en Python.",
         [
        Sx("Qu'est-ce qu'un itérable en Python ?", ["Un objet sur lequel on peut appeler iter() pour obtenir un itérateur", "Uniquement une liste", "Un objet qui définit obligatoirement __next__", "Un type numérique"], 0),
        Sx("Qu'est-ce qui distingue un itérateur d'un simple itérable ?", ["Un itérateur définit __next__ en plus de __iter__", "Un itérateur ne peut pas être parcouru avec for", "Un itérateur est toujours une liste", "Aucune différence, ce sont des synonymes"], 0),
        Sx("Une liste Python est-elle un itérateur ?", ["Oui, directement", "Non, c'est un itérable ; il faut appeler iter() pour obtenir un itérateur", "Cela dépend de sa taille", "Oui, mais seulement en Python 2"], 1),
        M("Quelles affirmations sur itérables et itérateurs sont correctes ?",
          ["Toute liste, tuple ou dict est un itérable", "iter(une_liste) renvoie un itérateur sur cette liste",
           "Un itérateur garde en mémoire sa position courante dans la séquence", "Tous les itérables sont aussi des itérateurs"], {0, 1, 2}),
        M("Quels objets sont des itérables en Python ?",
          ["Une liste", "Une chaîne de caractères", "Un dictionnaire", "Un entier simple"], {0, 1, 2}),
        T("Une fonction génératrice produit un objet qui est à la fois itérable et itérateur.", True),
         ])

    quiz("Les chaînes : immutabilité et concatenation efficace (Intermédiaire)",
         "Comprenez les implications de l'immutabilité des chaînes sur la performance.",
         [
        Sx("Pourquoi concaténer des chaînes avec + dans une boucle peut être inefficace pour de grands volumes ?", ["Parce que + est interdit sur les chaînes", "Parce que chaque concaténation crée une nouvelle chaîne immuable en mémoire", "Parce que Python limite la taille des chaînes", "Parce que + ne fonctionne qu'avec des nombres"], 1),
        Sx("Quelle méthode est généralement recommandée pour assembler efficacement de nombreux fragments de texte ?", ["La boucle avec +=", "''.join(liste_de_fragments)", "print() répété", "L'opérateur %"], 1),
        Sx("Quel comportement résulte de l'immutabilité des chaînes lors d'une opération comme s = s.upper() ?", ["s est modifiée en place", "Une nouvelle chaîne est créée et réassignée à s", "Une erreur est levée", "Rien ne se passe"], 1),
        M("Quelles affirmations sur l'immutabilité des chaînes sont correctes ?",
          ["Une chaîne ne peut pas être modifiée caractère par caractère via l'indexation", "Les méthodes de chaîne comme upper() ou replace() renvoient toujours une nouvelle chaîne",
           "join() est plus efficace que des concaténations répétées avec + dans une boucle", "L'immutabilité empêche toute manipulation de texte en Python"], {0, 1, 2}),
        M("Quelles opérations créent une nouvelle chaîne sans modifier l'originale ?",
          ["s.upper()", "s.replace('a', 'b')", "s + 'x'", "s[0] = 'X'"], {0, 1, 2}),
        T("Tenter d'exécuter s[0] = 'X' sur une chaîne s lève une TypeError car les chaînes sont immuables.", True),
         ])

    quiz("L'instruction pass et les blocs vides (Débutant)",
         "Utilisez l'instruction pass comme espace réservé syntaxique.",
         [
        Sx("À quoi sert l'instruction pass en Python ?", ["À arrêter le programme", "À ne rien faire, comme espace réservé syntaxique", "À répéter une boucle", "À importer un module"], 1),
        Sx("Dans quel contexte utilise-t-on souvent pass ?", ["Un bloc de fonction ou de classe temporairement vide", "Pour terminer une boucle", "Pour déclarer une variable", "Pour formatter une chaîne"], 0),
        Sx("Que se passe-t-il si on écrit def f(): (sans corps ni pass) ?", ["Cela fonctionne normalement", "Une IndentationError est levée car un bloc ne peut pas être vide", "f devient automatiquement une lambda", "Rien de spécial"], 1),
        M("Quelles affirmations sur pass sont correctes ?",
          ["pass ne produit aucun effet à l'exécution", "pass permet de satisfaire la syntaxe d'un bloc sans implémentation",
           "pass peut être utilisé dans une classe, une fonction, une boucle ou un if", "pass est obligatoire dans toute fonction Python"], {0, 1, 2}),
        M("Dans quels blocs peut-on légitimement utiliser pass ?",
          ["class MaClasse: pass", "def f(): pass", "if condition: pass", "import pass"], {0, 1, 2}),
        T("pass est sémantiquement un no-op : il ne modifie ni ne produit aucune valeur, il sert uniquement à respecter la syntaxe.", True),
         ])

    quiz("Les variables et l'affectation multiple (Débutant)",
         "Affectez plusieurs variables en une seule ligne et comprenez le typage dynamique.",
         [
        Sx("Que fait l'instruction a = b = c = 0 ?", ["Seul c vaut 0", "a, b et c valent tous 0", "Erreur de syntaxe", "Seul a vaut 0"], 1),
        Sx("Python est-il un langage à typage statique ou dynamique ?", ["Statique", "Dynamique", "Ni l'un ni l'autre", "Cela dépend du système"], 1),
        Sx("Que se passe-t-il si on réaffecte x = 'texte' alors que x valait 5 auparavant ?", ["Une erreur de type est levée", "x référence désormais une chaîne, sans erreur (typage dynamique)", "x garde la valeur 5", "Le programme plante"], 1),
        M("Quelles affirmations sur les variables en Python sont correctes ?",
          ["Une variable est en réalité une référence vers un objet en mémoire", "On peut changer le type de la valeur référencée par une variable au cours du programme",
           "a, b = 1, 2 affecte 1 à a et 2 à b", "Une variable doit être déclarée avec un type fixe avant utilisation comme en Java"], {0, 1, 2}),
        M("Quelles instructions d'affectation sont valides en Python ?",
          ["x = 5", "x, y = 1, 2", "x = y = 0", "int x = 5"], {0, 1, 2}),
        T("Le typage dynamique de Python signifie que le type d'une variable peut changer au fil de l'exécution selon la valeur qui lui est assignée.", True),
         ])

    quiz("Opérateurs d'affectation augmentée (Débutant)",
         "Simplifiez vos affectations avec les opérateurs +=, -=, *= et leurs équivalents.",
         [
        Sx("Que fait x += 1 si x vaut 5 ?", ["x vaut 6", "x vaut 5", "x vaut 1", "Erreur"], 0),
        Sx("Que fait x *= 3 si x vaut 4 ?", ["x vaut 7", "x vaut 12", "x vaut 3", "x vaut 4"], 1),
        Sx("Quel opérateur d'affectation augmentée correspond à x = x // 2 ?", ["x //= 2", "x /= 2", "x %= 2", "x **= 2"], 0),
        M("Quelles affirmations sur les opérateurs d'affectation augmentée sont correctes ?",
          ["Ils combinent une opération et une affectation", "x += 1 équivaut à x = x + 1 dans le cas général",
           "Ils existent pour +, -, *, /, //, %, ** entre autres", "Ils ne fonctionnent que sur des entiers"], {0, 1, 2}),
        M("Quelles expressions sont équivalentes à x = x - 3 et donc diminuent x de 3 ?",
          ["x -= 3", "x = x - 3", "x.subtract(3)", "x -3"], {0, 1}),
        T("Pour une liste, l += [4] modifie potentiellement la liste en place via __iadd__, alors que l = l + [4] crée une nouvelle liste.", True),
         ])

    quiz("Indentation et blocs de code (Débutant)",
         "Approfondissez le rôle central de l'indentation dans la syntaxe Python.",
         [
        Sx("Quel rôle joue l'indentation en Python ?", ["Purement esthétique, sans impact sur l'exécution", "Elle délimite les blocs de code (obligatoire)", "Elle sert uniquement aux commentaires", "Elle n'existe pas en Python"], 1),
        Sx("Que se passe-t-il si deux lignes consécutives d'un même bloc n'ont pas la même indentation ?", ["Rien de particulier", "Une IndentationError est levée", "Python corrige automatiquement", "Un avertissement seulement, sans erreur"], 1),
        Sx("Combien d'espaces la PEP 8 recommande-t-elle par niveau d'indentation ?", ["2", "4", "8", "1"], 1),
        M("Quelles affirmations sur l'indentation sont correctes ?",
          ["Elle remplace les accolades utilisées dans d'autres langages", "Mélanger tabulations et espaces peut provoquer des erreurs",
           "Chaque bloc imbriqué augmente le niveau d'indentation", "L'indentation est optionnelle si le code est sur une seule ligne avec point-virgule"], {0, 1, 2}),
        M("Quels blocs nécessitent une indentation après les deux-points (:) ?",
          ["Le corps d'une fonction (def)", "Le corps d'une boucle for", "Le corps d'un if", "Une simple variable globale"], {0, 1, 2}),
        T("Contrairement à des langages comme le C ou Java, Python utilise l'indentation elle-même comme syntaxe de délimitation des blocs, et non des accolades.", True),
         ])

    quiz("None et son usage (Débutant)",
         "Comprenez la valeur spéciale None représentant l'absence de valeur.",
         [
        Sx("Que représente None en Python ?", ["Le nombre zéro", "L'absence de valeur ou un résultat nul", "Une chaîne vide", "Une erreur"], 1),
        Sx("Que renvoie une fonction qui n'a pas d'instruction return explicite ?", ["0", "None", "''", "Une erreur"], 1),
        Sx("Quel est le type de None ?", ["NoneType", "null", "void", "empty"], 0),
        M("Quelles affirmations sur None sont correctes ?",
          ["None est un singleton (une seule instance existe en mémoire)", "bool(None) vaut False",
           "On le compare idiomatiquement avec is None plutôt que == None", "None est équivalent à 0 lors d'une comparaison =="], {0, 1, 2}),
        M("Quelles expressions impliquant None s'évaluent à True ?",
          ["None is None", "not None", "None == None", "bool(None) == True"], {0, 1, 2}),
        T("None est souvent utilisé comme valeur par défaut sûre pour un paramètre de fonction, notamment pour éviter le piège des objets mutables par défaut.", True),
         ])

    quiz("Fonctions intégrées utiles : min, max, sum, len, abs (Débutant)",
         "Découvrez les fonctions natives incontournables pour manipuler des séquences.",
         [
        Sx("Que renvoie sum([1, 2, 3, 4]) ?", ["10", "4", "24", "1234"], 0),
        Sx("Que renvoie max([3, 7, 2]) ?", ["2", "3", "7", "12"], 2),
        Sx("Que renvoie abs(-8) ?", ["-8", "8", "0", "Erreur"], 1),
        M("Quelles affirmations sur ces fonctions intégrées sont correctes ?",
          ["len() fonctionne sur les listes, chaînes, tuples et dictionnaires", "sum() peut accepter un argument start pour une valeur initiale",
           "min() et max() acceptent un paramètre key pour personnaliser la comparaison", "abs() ne fonctionne que sur les entiers positifs"], {0, 1, 2}),
        M("Quelles expressions sont valides ?",
          ["max([1, 2], key=lambda x: -x)", "sum(range(5))", "len('Python')", "abs('texte')"], {0, 1, 2}),
        T("min() et max() peuvent être appelées avec plusieurs arguments séparés, par exemple max(3, 7, 2), pas seulement avec un itérable.", True),
         ])

    quiz("Conventions et docstrings (Intermédiaire)",
         "Documentez vos fonctions et modules avec des docstrings standardisées.",
         [
        Sx("Comment écrit-on une docstring de fonction en Python ?", ["Avec # juste après def", "Avec une chaîne entre triples guillemets juste après la définition", "Avec //", "Avec /* */"], 1),
        Sx("Quel attribut spécial permet d'accéder à la docstring d'une fonction depuis le code ?", ["f.docstring", "f.__doc__", "f.help()", "f.comment"], 1),
        Sx("Quelle fonction native affiche la documentation et la signature d'un objet de façon interactive ?", ["doc()", "help()", "info()", "describe()"], 1),
        M("Quelles affirmations sur les docstrings sont correctes ?",
          ["Elles se placent juste après la ligne def ou class", "Elles sont accessibles via l'attribut __doc__",
           "help(objet) les affiche de façon formatée", "Elles sont obligatoires pour que le code s'exécute"], {0, 1, 2}),
        M("Quels éléments peuvent posséder une docstring en Python ?",
          ["Une fonction", "Une classe", "Un module", "Une simple variable entière"], {0, 1, 2}),
        T("Une docstring est techniquement une chaîne littérale placée en première instruction d'un module, d'une fonction, d'une classe ou d'une méthode.", True),
         ])

    quiz("Mutabilité et passage d'arguments (Avancé)",
         "Comprenez comment Python transmet les arguments aux fonctions (passage par référence d'objet).",
         [
        Sx("Comment Python transmet-il les arguments aux fonctions ?", ["Toujours par copie complète de la valeur (passage par valeur strict)", "Par référence à l'objet (parfois appelé pass-by-object-reference)", "Toujours par pointeur explicite", "Cela dépend du système d'exploitation"], 1),
        Sx("Que se passe-t-il si une fonction modifie en place (append) une liste reçue en paramètre ?", ["La liste originale à l'extérieur de la fonction est aussi modifiée", "Seule la copie locale change", "Une erreur est levée", "Rien ne change jamais"], 0),
        Sx("Que se passe-t-il si une fonction réaffecte complètement le paramètre (par exemple x = []) sans le modifier en place ?", ["L'objet original à l'extérieur change aussi", "Seule la variable locale référence un nouvel objet, l'original reste inchangé", "Une erreur est levée", "Le programme plante"], 1),
        M("Quelles affirmations sur le passage d'arguments en Python sont correctes ?",
          ["Les objets mutables modifiés en place dans une fonction sont affectés aussi à l'extérieur", "Réassigner un paramètre ne change pas la variable originale appelante",
           "Le mécanisme s'applique aussi bien aux objets mutables qu'immuables", "Python copie systématiquement toute la structure de données à chaque appel de fonction"], {0, 1, 2}),
        M("Quels objets, étant immuables, ne peuvent jamais être modifiés en place via une fonction ?",
          ["int", "str", "tuple", "list"], {0, 1, 2}),
        T("Le fait qu'une liste passée à une fonction soit modifiable en place provient de la mutabilité de la liste, pas d'un mécanisme spécial de passage par référence classique.", True),
         ])

    quiz("Boucles : else, break et continue combinés (Intermédiaire)",
         "Maîtrisez les interactions subtiles entre break, continue et la clause else des boucles.",
         [
        Sx("Quand la clause else d'une boucle for s'exécute-t-elle ?", ["Toujours après la boucle", "Seulement si la boucle se termine sans rencontrer de break", "Seulement si la boucle rencontre un break", "Jamais en Python"], 1),
        Sx("Que fait continue à l'intérieur d'une boucle ?", ["Termine définitivement la boucle", "Passe directement à l'itération suivante", "Met la boucle en pause", "Relance la boucle depuis le début"], 1),
        Sx("Que fait break à l'intérieur d'une boucle ?", ["Passe à l'itération suivante", "Termine immédiatement la boucle englobante", "Ne fait rien", "Relance la boucle"], 1),
        M("Quelles affirmations sur break, continue et else dans les boucles sont correctes ?",
          ["else après une boucle for/while est une particularité du langage Python", "break empêche l'exécution du else associé à la boucle",
           "continue ne désactive pas le else de la boucle", "continue arrête définitivement la boucle comme break"], {0, 1, 2}),
        M("Dans quels cas le bloc else d'une boucle for s'exécute-t-il ?",
          ["La boucle parcourt tous les éléments sans rencontrer de break", "La boucle est vide (zéro itération)", "Un break est exécuté au milieu de la boucle", "Une exception est levée pendant la boucle"], {0, 1}),
        T("La clause else d'une boucle for ou while en Python s'exécute uniquement si aucun break n'a interrompu la boucle.", True),
         ])

    quiz("Listes vs générateurs : impact mémoire (Avancé)",
         "Comparez la consommation mémoire entre une liste complète et un générateur paresseux.",
         [
        Sx("Pourquoi range(10**9) ne consomme-t-il pas immédiatement une grande quantité de mémoire en Python 3 ?", ["Parce que range est limité à 1000 éléments", "Parce que range produit un objet paresseux qui calcule les valeurs à la demande", "Parce que Python compresse automatiquement les entiers", "Ce n'est pas vrai, il consomme toute la mémoire immédiatement"], 1),
        Sx("Quelle expression construit immédiatement toute une liste en mémoire ?", ["(x for x in range(1000000))", "[x for x in range(1000000)]", "range(1000000)", "iter(range(1000000))"], 1),
        Sx("Quel est l'avantage principal d'un générateur sur une liste pour de très grands volumes de données ?", ["Un accès aléatoire plus rapide", "Une empreinte mémoire réduite car les valeurs sont produites à la demande", "Un tri automatique", "Une syntaxe plus courte uniquement"], 1),
        M("Quelles affirmations sur listes et générateurs sont correctes ?",
          ["Une liste garde tous ses éléments en mémoire simultanément", "Un générateur ne garde généralement que l'état nécessaire pour produire la valeur suivante",
           "On ne peut parcourir un générateur qu'une seule fois", "Un générateur permet un accès aléatoire instantané par index comme une liste"], {0, 1, 2}),
        M("Dans quels cas préférer un générateur à une liste complète ?",
          ["Traitement de très gros fichiers ligne par ligne", "Flux de données infini ou très long", "Besoin d'accéder plusieurs fois aléatoirement aux éléments", "Économie de mémoire prioritaire sur la réutilisation"], {0, 1, 3}),
        T("sum(x for x in range(1000000)) utilise un générateur et évite de construire une liste intermédiaire complète en mémoire.", True),
         ])

    quiz("L'opérateur in et l'appartenance (Débutant)",
         "Testez l'appartenance d'un élément à une séquence avec l'opérateur in.",
         [
        Sx("Que renvoie 3 in [1, 2, 3] ?", ["True", "False", "3", "Erreur"], 0),
        Sx("Que renvoie 'a' in 'banana' ?", ["False", "True", "1", "Erreur"], 1),
        Sx("Que renvoie 'z' not in 'abc' ?", ["True", "False", "Erreur", "None"], 0),
        M("Quelles affirmations sur l'opérateur in sont correctes ?",
          ["Il fonctionne sur les listes, tuples, chaînes, sets et dictionnaires", "Sur un dictionnaire, in teste la présence parmi les clés par défaut",
           "Le test d'appartenance dans un set est généralement très rapide (O(1) en moyenne)", "in ne fonctionne que sur des listes"], {0, 1, 2}),
        M("Quelles expressions s'évaluent à True ?",
          ["2 in {1, 2, 3}", "'py' in 'python'", "'x' in {'x': 1}", "5 in (1, 2, 3)"], {0, 1, 2}),
        T("Pour tester l'appartenance d'un élément, un set est généralement plus rapide qu'une liste lorsque la collection est grande.", True),
         ])

    quiz("Encodage de caractères et le type bytes (Avancé)",
         "Distinguez chaînes (str) et données binaires (bytes), et comprenez l'encodage UTF-8.",
         [
        Sx("Quelle méthode convertit une chaîne str en objet bytes ?", ["str.decode()", "str.encode()", "bytes.str()", "str.to_bytes()"], 1),
        Sx("Quelle méthode convertit un objet bytes en chaîne str ?", ["bytes.decode()", "bytes.encode()", "str.from_bytes()", "bytes.str()"], 0),
        Sx("Quel encodage est le plus couramment utilisé par défaut pour le texte Unicode en Python ?", ["ASCII", "UTF-8", "Latin-1", "UTF-32"], 1),
        M("Quelles affirmations sur str et bytes sont correctes ?",
          ["str représente du texte Unicode", "bytes représente une séquence d'octets bruts",
           "encode() transforme du texte en octets selon un encodage donné", "str et bytes sont strictement interchangeables sans conversion"], {0, 1, 2}),
        M("Quelles expressions sont valides en Python 3 ?",
          ["'texte'.encode('utf-8')", "b'donnees'.decode('utf-8')", "b'abc' + b'def'", "'abc' + b'def'"], {0, 1, 2}),
        T("Concaténer directement une chaîne str et un objet bytes avec + lève une TypeError en Python 3 sans conversion explicite.", True),
         ])

    quiz("Le module random (Intermédiaire)",
         "Générez des nombres aléatoires et effectuez des tirages avec le module random.",
         [
        Sx("Quelle fonction du module random renvoie un float entre 0.0 inclus et 1.0 exclu ?", ["random.randint", "random.random", "random.choice", "random.uniform"], 1),
        Sx("Quelle fonction du module random choisit un élément aléatoire dans une liste ?", ["random.sample", "random.choice", "random.shuffle", "random.pick"], 1),
        Sx("Quelle fonction mélange une liste en place ?", ["random.shuffle", "random.choice", "random.random", "random.mix"], 0),
        M("Quelles affirmations sur le module random sont correctes ?",
          ["random.randint(a, b) inclut les deux bornes a et b", "random.seed() permet de rendre une séquence aléatoire reproductible",
           "random.sample permet de tirer plusieurs éléments distincts sans remise", "random.random() peut renvoyer exactement 1.0"], {0, 1, 2}),
        M("Quelles fonctions appartiennent au module random ?",
          ["randint", "choice", "shuffle", "compute"], {0, 1, 2}),
        T("Fixer une graine avec random.seed(valeur) permet d'obtenir une séquence de nombres pseudo-aléatoires reproductible.", True),
         ])
