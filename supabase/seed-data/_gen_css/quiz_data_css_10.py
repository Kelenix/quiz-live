# -*- coding: utf-8 -*-
"""Quiz 91-100 : angles complementaires (selecteurs avances, grid avance, flex avance, unites, cascade avancee, etc.)."""

def build(quiz, S, Sx, M, T):

    quiz(
        "Sélecteurs combinés avancés",
        "Construire des sélecteurs complexes en combinant plusieurs techniques.",
        [
            S("Que cible le sélecteur `ul li:first-child` ?",
              ["Le premier <li> enfant de chaque <ul> qui en contient", "Tous les <li> de la page", "Uniquement le premier <ul> de la page", "Le dernier élément de chaque liste"]),
            S("Que cible le sélecteur `a[href^=\"https\"]` ?",
              ["Les liens dont l'attribut href commence par https", "Les liens dont le texte contient https", "Tous les liens sans exception", "Les liens se terminant par .com uniquement"]),
            S("Que cible le sélecteur `p:not(:last-child)` ?",
              ["Tous les paragraphes sauf le dernier de leur groupe de frères", "Uniquement le dernier paragraphe", "Aucun paragraphe", "Tous les paragraphes sans exception"]),
            M("Lesquels de ces sélecteurs ciblent spécifiquement des éléments selon une condition de position parmi leurs frères ?",
              [":nth-child(odd)", ":last-of-type"], {0, 1}, [":hover", "[disabled]"]),
            T("On peut chaîner plusieurs pseudo-classes sur un même sélecteur, comme `li:first-child:hover`.", True),
            T("Le sélecteur `div p` et `div > p` ciblent exactement le même ensemble d'éléments dans tous les cas.", False),
        ],
    )

    quiz(
        "Spécificité avancée et résolution de conflits",
        "Analyser des cas concrets de conflits entre règles CSS multiples.",
        [
            S("Entre `#header .nav a` et `.nav a.active`, lequel a la spécificité la plus forte ?",
              ["#header .nav a (car il contient un id)", ".nav a.active", "Les deux sont strictement égaux", "Cela dépend uniquement de l'ordre d'écriture"]),
            S("Pourquoi écrire des sélecteurs très longs et très spécifiques est-il souvent déconseillé en pratique ?",
              ["Cela complique la possibilité de surcharger le style plus tard sans utiliser !important", "Cela ralentit considérablement le rendu visuel du navigateur", "C'est interdit par la spécification CSS officielle", "Cela empêche l'utilisation de classes"]),
            S("Quel est l'ordre de priorité correct, du plus faible au plus fort, parmi : élément, classe, id ?",
              ["élément, classe, id", "id, classe, élément", "classe, id, élément", "élément, id, classe"]),
            M("Quelles approches aident à limiter les problèmes de spécificité dans un grand projet CSS ?",
              ["Utiliser des méthodologies comme BEM avec des classes plates", "Éviter les imbrications de sélecteurs trop profondes"], {0, 1}, ["Utiliser systématiquement des id pour tout styliser", "Multiplier les !important pour chaque règle"]),
            T("Deux sélecteurs de même spécificité exacte voient leur conflit résolu par l'ordre d'apparition dans la feuille de style, le dernier l'emportant.", True),
            T("La spécificité d'un sélecteur dépend de la longueur en caractères du texte du sélecteur.", False),
        ],
    )

    quiz(
        "Flexbox en pratique : barre de navigation",
        "Appliquer Flexbox à un cas concret de barre de navigation horizontale.",
        [
            S("Pour aligner les liens d'une barre de navigation horizontalement avec un espace égal entre eux, quelle propriété de conteneur flex utiliser ?",
              ["justify-content: space-between;", "flex-direction: column;", "align-items: stretch;", "flex-wrap: wrap-reverse;"]),
            S("Pour qu'un logo reste à gauche et un menu utilisateur à droite dans une même barre flex, quelle propriété est la plus adaptée ?",
              ["justify-content: space-between;", "align-content: center;", "flex-wrap: nowrap; uniquement", "order: -1; sur tous les éléments"]),
            S("Si on souhaite qu'un seul élément d'une barre flex (ex: un bouton de recherche) soit repoussé à l'extrême droite alors que les autres restent groupés à gauche, quelle technique simple peut-on utiliser ?",
              ["Appliquer margin-left: auto; sur cet élément", "Changer flex-direction en column", "Mettre z-index: 999; sur l'élément", "Utiliser position: fixed; sur l'élément"]),
            M("Quelles propriétés flex sont couramment utilisées pour construire une barre de navigation responsive ?",
              ["flex-wrap", "justify-content"], {0, 1}, ["grid-template-areas", "object-fit"]),
            T("Flexbox est un choix courant et pertinent pour aligner horizontalement les éléments d'une barre de navigation.", True),
            T("Il est impossible de centrer verticalement le texte d'un lien dans une barre flex.", False),
        ],
    )

    quiz(
        "Grid en pratique : mise en page de page web",
        "Utiliser CSS Grid pour structurer un en-tête, un contenu principal et un pied de page.",
        [
            S("Pour créer une mise en page classique avec en-tête, contenu principal, barre latérale et pied de page, quelle propriété de Grid est particulièrement adaptée ?",
              ["grid-template-areas", "flex-wrap", "text-align", "vertical-align"]),
            S("Dans une grille définissant trois lignes (en-tête, contenu, pied de page), quelle propriété permet de fixer la hauteur de chaque ligne ?",
              ["grid-template-rows", "grid-template-columns", "row-height", "grid-line-size"]),
            S("Pourquoi CSS Grid est-il souvent préféré à Flexbox pour une mise en page globale de page (header/main/footer/sidebar) ?",
              ["Parce qu'il gère naturellement deux dimensions (lignes et colonnes) simultanément", "Parce que Flexbox ne fonctionne pas sur des balises <div>", "Parce que Grid est plus ancien que Flexbox", "Parce que Flexbox ne supporte pas les médias queries"]),
            M("Quelles zones sont typiquement nommées dans un schéma grid-template-areas pour une page classique ?",
              ["header", "footer"], {0, 1}, ["transition", "keyframes"]),
            T("On peut combiner CSS Grid pour la structure générale d'une page et Flexbox à l'intérieur de chaque zone de la grille pour aligner du contenu.", True),
            T("grid-template-areas exige que chaque zone nommée ait exactement la même taille que les autres zones.", False),
        ],
    )

    quiz(
        "Unités CSS : choisir la bonne unité selon le contexte",
        "Comparer px, %, em, rem, vh/vw et ch dans des cas d'usage concrets.",
        [
            S("Quelle unité est généralement recommandée pour la taille de police afin de respecter les préférences d'accessibilité de l'utilisateur (zoom du navigateur) ?",
              ["rem", "px", "vh", "ch uniquement"]),
            S("Quelle unité est la plus adaptée pour qu'un élément occupe toujours exactement la moitié de la largeur de son conteneur parent ?",
              ["Un pourcentage (%)", "vh", "ch", "deg"]),
            S("Quelle unité serait la plus adaptée pour garantir qu'une section occupe toute la hauteur visible de l'écran, peu importe la résolution ?",
              ["100vh", "100%", "100ch", "100em"]),
            M("Quelles unités sont considérées comme relatives plutôt qu'absolues en CSS ?",
              ["em", "rem", "%"], {0, 1, 2}, ["px", "cm"]),
            T("L'unité `px` est considérée comme une unité fixe alors que `rem`, `em` et `%` sont des unités relatives.", True),
            T("Toutes les unités CSS (px, em, rem, vh, vw, %) produisent toujours exactement le même rendu visuel, peu importe le contexte.", False),
        ],
    )

    quiz(
        "Cascade, couches (@layer) et ordre des sources",
        "Comprendre l'ordre dans lequel le navigateur combine les différentes sources de styles.",
        [
            S("Parmi les origines de styles (styles du navigateur, styles de l'auteur, styles utilisateur), laquelle a généralement la priorité la plus forte en l'absence de !important ?",
              ["Les styles de l'auteur (la feuille de style du site)", "Les styles par défaut du navigateur", "Les styles utilisateur uniquement", "Aucune priorité n'existe entre elles"]),
            S("À quoi servent les couches CSS définies avec la règle `@layer` ?",
              ["À organiser explicitement l'ordre de priorité de groupes de règles CSS, indépendamment de leur spécificité individuelle", "À créer des animations en couches superposées", "À charger des polices personnalisées", "À définir des media queries imbriquées"]),
            S("Si deux règles appartiennent à deux couches @layer différentes, laquelle l'emporte généralement en cas de conflit (hors !important) ?",
              ["La règle de la couche déclarée en dernier dans l'ordre des couches", "La règle ayant la spécificité la plus élevée, peu importe la couche", "La règle la plus courte en nombre de caractères", "Toujours la première couche déclarée"]),
            M("Quels éléments influencent la résolution finale de la cascade CSS moderne ?",
              ["L'origine de la règle (auteur, navigateur, utilisateur)", "La présence de !important"], {0, 1}, ["La couleur de fond de la page", "Le nombre total de fichiers CSS chargés"]),
            T("La règle @layer permet de regrouper des styles dans des couches dont l'ordre de priorité est défini explicitement, ce qui peut simplifier la gestion de !important.", True),
            T("Les styles par défaut du navigateur (user agent stylesheet) ont toujours la priorité la plus forte, avant même les styles de l'auteur du site.", False),
        ],
    )

    quiz(
        "Position sticky et fixed en situation réelle",
        "Construire des en-têtes persistants et des boutons flottants avec le positionnement CSS.",
        [
            S("Pour créer un en-tête de tableau qui reste visible pendant le défilement vertical du tableau, quelle valeur de position est couramment utilisée sur les cellules d'en-tête ?",
              ["sticky", "static", "relative seul sans top", "inherit"]),
            S("Pour créer un bouton \"retour en haut de page\" toujours visible dans le coin de l'écran quel que soit le défilement, quelle valeur de position utiliser ?",
              ["fixed", "static", "relative", "sticky avec bottom uniquement et un parent en overflow hidden"]),
            S("Pourquoi un élément `position: sticky` peut-il sembler ne pas fonctionner si son parent direct a `overflow: hidden` et une hauteur contrainte ?",
              ["Parce que le contexte de défilement du parent peut limiter ou bloquer l'effet sticky", "Parce que sticky est incompatible avec les balises <th>", "Parce que sticky nécessite obligatoirement JavaScript pour s'activer", "Parce que overflow: hidden désactive tout positionnement CSS sur la page"]),
            M("Quels cas d'usage concrets sont typiquement résolus avec position: sticky ou fixed ?",
              ["Un en-tête de site qui reste visible en haut de l'écran", "Une ligne d'en-tête de tableau qui reste visible pendant le défilement"], {0, 1}, ["Le centrage automatique d'un texte", "L'inversion des couleurs d'un bouton au survol"]),
            T("Un bouton flottant en `position: fixed` reste à la même position par rapport à la fenêtre du navigateur, même après défilement de toute la page.", True),
            T("position: sticky se comporte exactement comme position: static tant que le seuil de défilement défini par top/bottom n'est pas atteint.", True),
        ],
    )

    quiz(
        "Bonnes pratiques pour les transitions et animations accessibles",
        "Tenir compte des préférences de mouvement réduit pour une expérience inclusive.",
        [
            S("Quelle media query permet de détecter si un utilisateur a activé une préférence système de réduction des animations ?",
              ["@media (prefers-reduced-motion: reduce)", "@media (max-animation: none)", "@media (motion: off)", "@media print"]),
            S("Pourquoi est-il recommandé de proposer une alternative sans animation intense pour certains utilisateurs ?",
              ["Pour éviter l'inconfort ou les troubles vestibulaires que peuvent provoquer certaines animations chez certaines personnes", "Parce que les animations ralentissent toujours le référencement SEO", "Parce que les animations sont interdites par la spécification CSS3", "Parce que cela réduit automatiquement la taille du fichier CSS"]),
            S("Que peut-on faire concrètement dans une règle `@media (prefers-reduced-motion: reduce)` ?",
              ["Réduire ou désactiver les durées de transition et d'animation", "Forcer toutes les animations à devenir deux fois plus rapides", "Supprimer toutes les couleurs de la page", "Désactiver entièrement le CSS de la page"]),
            M("Quelles bonnes pratiques favorisent des animations CSS plus accessibles ?",
              ["Respecter la préférence prefers-reduced-motion", "Éviter les animations clignotantes trop rapides ou intenses"], {0, 1}, ["Animer systématiquement toutes les propriétés possibles", "Ignorer totalement les préférences système de l'utilisateur"]),
            T("La media query prefers-reduced-motion permet d'adapter ou de supprimer des animations pour les utilisateurs sensibles au mouvement.", True),
            T("Toutes les animations CSS sont obligatoirement désactivées sur tous les navigateurs si prefers-reduced-motion n'est pas explicitement géré par le développeur.", False),
        ],
    )

    quiz(
        "object-fit et object-position pour les médias",
        "Contrôler le redimensionnement des images et vidéos à l'intérieur de leur boîte.",
        [
            S("Quelle propriété contrôle la façon dont une image ou une vidéo se redimensionne à l'intérieur de sa boîte définie par width/height ?",
              ["object-fit", "background-size", "image-rendering", "object-resize"]),
            S("Quelle valeur d'`object-fit` recadre l'image pour qu'elle couvre toute la boîte sans déformation, en rognant l'excédent ?",
              ["cover", "contain", "fill", "none"]),
            S("Quelle valeur d'`object-fit` étire l'image pour remplir exactement la boîte, sans respecter ses proportions d'origine ?",
              ["fill", "cover", "contain", "scale-down"]),
            M("Quelles propriétés permettent de contrôler à la fois le redimensionnement et le positionnement d'une image dans sa boîte ?",
              ["object-fit", "object-position"], {0, 1}, ["text-align", "vertical-align"]),
            T("`object-fit: cover` appliqué à une balise <img> permet d'obtenir un effet similaire à background-size: cover mais pour une vraie balise image.", True),
            T("object-fit ne peut s'appliquer qu'aux balises <div> et jamais aux balises <img> ou <video>.", False),
        ],
    )

    quiz(
        "Synthèse : diagnostiquer un problème de mise en page CSS",
        "Mobiliser plusieurs notions pour résoudre des cas de mise en page courants.",
        [
            S("Un élément enfant en `position: absolute` ne se positionne pas par rapport au parent attendu mais par rapport à toute la page. Quelle est la cause la plus probable ?",
              ["Le parent n'a pas de position relative, absolute ou fixed définie", "L'élément enfant utilise display: flex", "Le parent a un z-index trop faible", "L'élément enfant a une marge négative"]),
            S("Deux blocs flex ne se répartissent pas l'espace comme attendu malgré `flex-grow: 1` sur les deux. Quelle propriété vérifier en priorité sur le conteneur ?",
              ["display: flex; est-il bien présent sur le conteneur parent ?", "La couleur de fond du conteneur", "La présence d'un @font-face", "Le nombre de balises <span> utilisées"]),
            S("Une grille CSS affiche des colonnes vides inattendues en bas de page. Quelle propriété du conteneur est la cause la plus probable ?",
              ["grid-auto-rows ou grid-auto-flow générant des lignes implicites supplémentaires", "color appliqué sur le body", "text-decoration sur les liens", "font-style sur les titres"]),
            M("Quelles vérifications sont pertinentes lorsqu'un z-index ne produit pas l'effet de superposition attendu ?",
              ["Vérifier que l'élément a bien une position différente de static", "Vérifier les contextes d'empilement créés par les parents"], {0, 1}, ["Vérifier la couleur de fond du body", "Vérifier le nombre de mots du texte"]),
            T("Un problème classique de centrage flex non fonctionnel vient souvent de l'absence de display: flex sur le bon élément parent.", True),
            T("Un débordement de contenu visuellement inattendu peut souvent être résolu en vérifiant box-sizing, padding et la propriété overflow.", True),
        ],
    )
