# -*- coding: utf-8 -*-
"""Quiz 1-10 : Selecteurs CSS (simples, combinateurs, pseudo-classes, pseudo-elements, attributs)."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Les sélecteurs CSS de base",
        "Premiers pas avec les sélecteurs d'éléments, de classe et d'identifiant.",
        [
            S("Quel sélecteur cible tous les éléments <p> d'une page ?",
              ["p", ".p", "#p", "*p"]),
            S("Quel caractère précède le nom d'une classe dans un sélecteur CSS ?",
              [".", "#", "*", "&"]),
            S("Quel caractère précède le nom d'un identifiant (id) dans un sélecteur CSS ?",
              ["#", ".", "@", "%"]),
            M("Parmi ces sélecteurs, lesquels ciblent un élément par son attribut id=\"menu\" ?",
              ["#menu", "[id=\"menu\"]"], {0, 1}, ["wrong-id", ".menu"]),
            T("Le sélecteur universel `*` sélectionne tous les éléments du document.", True),
            T("Un sélecteur de classe peut s'appliquer à plusieurs éléments en même temps.", True),
        ],
    )

    quiz(
        "Combinateurs de sélecteurs",
        "Comprendre les relations entre éléments avec les combinateurs CSS.",
        [
            S("Quel combinateur sélectionne uniquement les enfants directs d'un élément ?",
              [">", " ", "+", "~"]),
            S("Que sélectionne `div p` (avec un espace) ?",
              ["Tous les <p> descendants de <div>, à n'importe quel niveau", "Seulement les <p> enfants directs de <div>", "Le premier <p> après un <div>", "Tous les <p> qui précèdent un <div>"]),
            S("Quel combinateur sélectionne l'élément frère immédiatement suivant ?",
              ["+", "~", ">", "="]),
            M("Quels combinateurs permettent de cibler des éléments frères (siblings) ?",
              ["+", "~"], {0, 1}, [">", " "]),
            T("Le sélecteur `ul > li` cible uniquement les <li> qui sont des enfants directs d'un <ul>.", True),
            T("Le combinateur `~` sélectionne tous les frères suivants qui correspondent, pas seulement le premier.", True),
        ],
    )

    quiz(
        "Pseudo-classes de structure",
        "Cibler des éléments selon leur position dans l'arborescence du document.",
        [
            S("Quelle pseudo-classe cible le premier élément enfant d'un parent ?",
              [":first-child", ":first-of-type", ":first", ":nth(1)"]),
            S("Que fait la pseudo-classe `:nth-child(2n)` ?",
              ["Elle sélectionne les enfants de rang pair", "Elle sélectionne les enfants de rang impair", "Elle sélectionne uniquement le deuxième enfant", "Elle sélectionne tous les enfants sauf le deuxième"]),
            S("Quelle pseudo-classe sélectionne un élément qui n'a aucun enfant ?",
              [":empty", ":only-child", ":blank", ":void"]),
            M("Quelles pseudo-classes permettent de cibler des éléments selon leur position parmi leurs frères ?",
              [":nth-child()", ":last-child"], {0, 1}, [":hover", ":focus"]),
            T("`:last-of-type` sélectionne le dernier élément de son type parmi ses frères, quel que soit son nom de balise réel par rapport aux autres frères.", True),
            T("`:nth-child(0)` sélectionne le premier enfant d'un élément.", False),
        ],
    )

    quiz(
        "Pseudo-classes d'état et d'interaction",
        "Réagir à l'état des éléments interactifs : survol, focus, validité.",
        [
            S("Quelle pseudo-classe applique un style lorsque la souris survole un élément ?",
              [":hover", ":active", ":focus", ":visited"]),
            S("Quelle pseudo-classe cible un élément de formulaire actuellement sélectionné par le clavier ou un clic ?",
              [":focus", ":hover", ":target", ":checked"]),
            S("Quelle pseudo-classe permet de styliser une case à cocher cochée ?",
              [":checked", ":selected", ":active", ":valid"]),
            M("Quelles pseudo-classes concernent l'état de validation d'un champ de formulaire ?",
              [":valid", ":invalid"], {0, 1}, [":hover", ":root"]),
            T("La pseudo-classe `:disabled` cible les éléments de formulaire désactivés.", True),
            T("`:visited` peut être utilisée pour changer la couleur de fond d'un lien visité de la même façon que n'importe quelle propriété CSS sans restriction.", False),
        ],
    )

    quiz(
        "Pseudo-éléments CSS",
        "Générer et cibler des portions virtuelles de contenu avec ::before, ::after et consorts.",
        [
            S("Quel pseudo-élément permet d'insérer du contenu juste avant le contenu réel d'un élément ?",
              ["::before", "::after", "::first-line", "::start"]),
            S("Quelle propriété est obligatoire pour qu'un pseudo-élément ::before ou ::after soit visible ?",
              ["content", "display", "visibility", "opacity"]),
            S("Quel pseudo-élément cible la première ligne affichée d'un bloc de texte ?",
              ["::first-line", "::first-child", "::first-letter", "::line"]),
            M("Lesquels de ces éléments sont des pseudo-éléments valides en CSS ?",
              ["::after", "::placeholder"], {0, 1}, [":hover", ":root"]),
            T("Les pseudo-éléments s'écrivent avec deux deux-points (`::`) selon la syntaxe moderne CSS3.", True),
            T("Le pseudo-élément `::first-letter` permet de cibler uniquement la première lettre d'un bloc de texte.", True),
        ],
    )

    quiz(
        "Sélecteurs d'attributs",
        "Cibler des éléments en fonction de la présence ou de la valeur de leurs attributs HTML.",
        [
            S("Quel sélecteur cible tous les éléments possédant un attribut `title`, quelle que soit sa valeur ?",
              ["[title]", "[title=*]", ".title", "title()"]),
            S("Quel sélecteur d'attribut cible une valeur qui commence exactement par une chaîne donnée ?",
              ["[attr^=\"valeur\"]", "[attr$=\"valeur\"]", "[attr*=\"valeur\"]", "[attr~=\"valeur\"]"]),
            S("Quel sélecteur d'attribut cible une valeur qui se termine par une chaîne donnée ?",
              ["[attr$=\"valeur\"]", "[attr^=\"valeur\"]", "[attr=\"valeur\"]", "[attr#\"valeur\"]"]),
            M("Quels sélecteurs d'attributs permettent de tester une sous-chaîne dans la valeur de l'attribut ?",
              ["[attr*=\"valeur\"]", "[attr^=\"valeur\"]"], {0, 1}, ["[attr]", "[attr=\"valeur\"]"]),
            T("Le sélecteur `input[type=\"checkbox\"]` cible uniquement les champs <input> dont l'attribut type vaut exactement checkbox.", True),
            T("Les sélecteurs d'attributs sont sensibles à la casse par défaut pour la valeur, sauf si on ajoute le drapeau `i` avant le crochet fermant.", True),
        ],
    )

    quiz(
        "Sélecteurs de négation et de correspondance",
        "Exclure ou combiner des conditions de sélection avec :not(), :is() et :where().",
        [
            S("Que fait la pseudo-classe `:not(.actif)` ?",
              ["Elle sélectionne tous les éléments qui n'ont pas la classe actif", "Elle sélectionne uniquement les éléments avec la classe actif", "Elle désactive le style des éléments actifs", "Elle inverse les couleurs des éléments actifs"]),
            S("Quelle pseudo-classe permet d'écrire une liste de sélecteurs sans augmenter la spécificité du sélecteur global ?",
              [":where()", ":not()", ":is()", ":has()"]),
            S("Quelle pseudo-classe récente permet de sélectionner un parent en fonction de son contenu descendant ?",
              [":has()", ":is()", ":where()", ":contains()"]),
            M("Quelles pseudo-classes acceptent une liste de sélecteurs séparés par des virgules comme argument ?",
              [":is()", ":not()"], {0, 1}, [":hover", ":root"]),
            T("`:is(h1, h2, h3)` est équivalent à écrire séparément des règles pour h1, h2 et h3 avec le même style.", True),
            T("La pseudo-classe `:has()` permet de cibler un élément parent si celui-ci contient un élément correspondant au sélecteur passé en argument.", True),
        ],
    )

    quiz(
        "Sélecteur universel et groupement",
        "Appliquer des styles à grande échelle et regrouper des sélecteurs.",
        [
            S("Comment écrit-on le sélecteur universel en CSS ?",
              ["*", "%", "#all", "any"]),
            S("Quel symbole permet de regrouper plusieurs sélecteurs pour leur appliquer le même bloc de déclarations ?",
              [",", "+", "&", "|"]),
            S("Que fait la règle `h1, h2, h3 { color: navy; }` ?",
              ["Elle applique la couleur navy à h1, h2 et h3", "Elle applique la couleur navy uniquement à h3 imbriqué dans h2 dans h1", "Elle crée une erreur de syntaxe", "Elle applique la couleur uniquement au premier élément trouvé"]),
            M("Quels sélecteurs ciblent strictement TOUS les éléments d'une page sans exception possible via une simple combinaison ?",
              ["*"], {0}, ["html *", "body"]),
            T("`* { box-sizing: border-box; }` est une pratique courante pour uniformiser le modèle de boîte sur tous les éléments.", True),
            T("On ne peut jamais combiner le sélecteur universel avec une classe, comme dans `*.actif`.", False),
        ],
    )

    quiz(
        "Spécificité des sélecteurs",
        "Comprendre comment le navigateur choisit quelle règle CSS appliquer en cas de conflit.",
        [
            S("Entre un sélecteur de classe et un sélecteur d'élément, lequel a la spécificité la plus forte ?",
              ["Le sélecteur de classe", "Le sélecteur d'élément", "Ils ont la même spécificité", "Cela dépend de l'ordre d'écriture uniquement"]),
            S("Quel type de sélecteur a la spécificité la plus élevée parmi id, classe et élément ?",
              ["L'identifiant (id)", "La classe", "L'élément (balise)", "Le sélecteur universel"]),
            S("Que se passe-t-il quand deux règles CSS ont exactement la même spécificité et ciblent la même propriété ?",
              ["La règle déclarée en dernier dans la feuille de style l'emporte", "La règle déclarée en premier l'emporte toujours", "Le navigateur applique une moyenne des deux valeurs", "Aucune des deux règles n'est appliquée"]),
            M("Quels éléments augmentent la spécificité d'un sélecteur CSS ?",
              ["Les identifiants (id)", "Les classes"], {0, 1}, ["Les commentaires CSS", "Les espaces dans le sélecteur"]),
            T("Un style en ligne (attribut `style=\"\"` dans le HTML) a une spécificité plus forte qu'une règle id dans une feuille de style externe (hors !important).", True),
            T("Le sélecteur universel `*` a une spécificité plus élevée qu'un sélecteur de classe.", False),
        ],
    )
