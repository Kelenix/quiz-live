// Part 3: accessibilité (quizzes 11-15)
export const part3 = [
{
  title: "Accessibilité web : les fondamentaux ARIA",
  description: "Comprendre le rôle des attributs ARIA pour rendre une interface accessible aux technologies d'assistance.",
  questions: [
    { statement: "Que signifie l'acronyme ARIA dans le contexte de l'accessibilité web ?", type: "single", time_limit: 20, answers: [
      { text: "Accessible Rich Internet Applications", is_correct: true }, { text: "Automated Responsive Interface Adapter", is_correct: false }, { text: "Advanced Rendering Interactive API", is_correct: false }, { text: "Application Resource Identifier Attribute", is_correct: false } ] },
    { statement: "Quel attribut ARIA permet de définir explicitement le rôle sémantique d'un élément pour les lecteurs d'écran ?", type: "single", time_limit: 20, answers: [
      { text: "role", is_correct: true }, { text: "aria-type", is_correct: false }, { text: "type", is_correct: false }, { text: "semantic", is_correct: false } ] },
    { statement: "Quel attribut ARIA permet d'indiquer qu'un élément est actuellement masqué ou désactivé pour les technologies d'assistance ?", type: "single", time_limit: 20, answers: [
      { text: "aria-hidden", is_correct: true }, { text: "aria-disabled-visual", is_correct: false }, { text: "hidden-aria", is_correct: false }, { text: "aria-invisible", is_correct: false } ] },
    { statement: "La règle d'or d'ARIA est de préférer un élément HTML natif avec une sémantique adaptée plutôt que d'ajouter des attributs ARIA sur un élément générique.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Les attributs ARIA modifient le comportement par défaut du navigateur (focus, clavier) sans qu'aucun code JavaScript ne soit nécessaire.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces attributs, lesquels appartiennent à la spécification ARIA ?", type: "multiple", time_limit: 30, answers: [
      { text: "aria-label", is_correct: true }, { text: "aria-expanded", is_correct: true }, { text: "aria-live", is_correct: true }, { text: "aria-color", is_correct: false } ] },
    { statement: "Quel attribut ARIA fournit un texte alternatif accessible pour un élément interactif lorsqu'aucun texte visible n'est pertinent (par exemple une icône bouton) ?", type: "single", time_limit: 20, answers: [
      { text: "aria-label", is_correct: true }, { text: "aria-text", is_correct: false }, { text: "aria-name", is_correct: false }, { text: "alt", is_correct: false } ] },
    { statement: "Lesquelles de ces pratiques contribuent réellement à l'accessibilité d'une interface web ?", type: "multiple", time_limit: 30, answers: [
      { text: "Utiliser des attributs alt descriptifs sur les images informatives", is_correct: true }, { text: "Garantir un contraste suffisant entre texte et fond", is_correct: true }, { text: "Permettre la navigation complète au clavier", is_correct: true }, { text: "Supprimer tous les attributs id du document", is_correct: false } ] }
  ]
},
{
  title: "Texte alternatif et accessibilité des images",
  description: "Bien renseigner l'attribut alt et choisir la bonne stratégie selon le type d'image.",
  questions: [
    { statement: "Quel attribut de la balise <img> fournit un texte alternatif décrivant l'image pour les utilisateurs ne pouvant pas la voir ?", type: "single", time_limit: 20, answers: [
      { text: "alt", is_correct: true }, { text: "title", is_correct: false }, { text: "desc", is_correct: false }, { text: "longdesc", is_correct: false } ] },
    { statement: "Pour une image purement décorative qui n'apporte aucune information, quelle est la pratique recommandée concernant l'attribut alt ?", type: "single", time_limit: 20, answers: [
      { text: "Laisser alt=\"\" (vide) pour que les lecteurs d'écran l'ignorent", is_correct: true }, { text: "Omettre totalement l'attribut alt", is_correct: false }, { text: "Mettre alt=\"image\"", is_correct: false }, { text: "Mettre le nom du fichier dans alt", is_correct: false } ] },
    { statement: "Un attribut alt manquant sur une image informative pénalise l'expérience des utilisateurs de lecteurs d'écran.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "L'attribut alt et l'attribut title ont exactement le même rôle et peuvent être utilisés indifféremment.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces recommandations pour rédiger un bon texte alternatif, lesquelles sont pertinentes ?", type: "multiple", time_limit: 30, answers: [
      { text: "Décrire le contenu ou la fonction de l'image, pas son apparence technique", is_correct: true }, { text: "Rester concis et pertinent pour le contexte", is_correct: true }, { text: "Éviter de répéter \"image de\" ou \"photo de\"", is_correct: true }, { text: "Toujours indiquer la résolution en pixels de l'image", is_correct: false } ] },
    { statement: "Pour une image utilisée comme seul contenu d'un lien cliquable, que doit décrire l'attribut alt ?", type: "single", time_limit: 20, answers: [
      { text: "La destination ou l'action du lien plutôt que l'apparence visuelle", is_correct: true }, { text: "Le format de fichier de l'image", is_correct: false }, { text: "Le nom du photographe", is_correct: false }, { text: "Rien, alt doit rester vide", is_correct: false } ] },
    { statement: "Quel élément HTML peut accompagner une <img> pour fournir une légende visible associée sémantiquement à l'image ?", type: "single", time_limit: 20, answers: [
      { text: "<figcaption> à l'intérieur d'un <figure>", is_correct: true }, { text: "<caption>", is_correct: false }, { text: "<legend>", is_correct: false }, { text: "<summary>", is_correct: false } ] },
    { statement: "Une image strictement décorative doit recevoir un attribut alt vide plutôt qu'un attribut alt absent.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] }
  ]
},
{
  title: "Navigation clavier et gestion du focus",
  description: "Garantir qu'une page reste utilisable sans souris grâce à une bonne gestion du focus et de l'ordre de tabulation.",
  questions: [
    { statement: "Quel attribut HTML permet de définir ou modifier l'ordre de tabulation au clavier d'un élément ?", type: "single", time_limit: 20, answers: [
      { text: "tabindex", is_correct: true }, { text: "focusorder", is_correct: false }, { text: "keyindex", is_correct: false }, { text: "navindex", is_correct: false } ] },
    { statement: "Quelle valeur de tabindex retire un élément de l'ordre de tabulation naturel tout en le laissant focalisable par script ?", type: "single", time_limit: 20, answers: [
      { text: "tabindex=\"-1\"", is_correct: true }, { text: "tabindex=\"0\"", is_correct: false }, { text: "tabindex=\"none\"", is_correct: false }, { text: "tabindex=\"disabled\"", is_correct: false } ] },
    { statement: "Donner systématiquement des valeurs positives élevées et arbitraires à tabindex sur de nombreux éléments est une bonne pratique recommandée.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Les éléments <a> munis d'un attribut href et les éléments <button> sont nativement focalisables au clavier sans ajouter tabindex.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Parmi ces pratiques, lesquelles favorisent une navigation clavier correcte ?", type: "multiple", time_limit: 30, answers: [
      { text: "Conserver un indicateur visuel de focus visible (outline)", is_correct: true }, { text: "Respecter un ordre de tabulation logique suivant l'ordre visuel", is_correct: true }, { text: "Permettre d'activer les boutons avec la touche Entrée ou Espace", is_correct: true }, { text: "Supprimer systématiquement le contour de focus par défaut sans alternative", is_correct: false } ] },
    { statement: "Pourquoi est-il déconseillé d'utiliser tabindex=\"0\" sur un <div> cliquable plutôt que d'utiliser un <button> natif ?", type: "single", time_limit: 20, answers: [
      { text: "Parce qu'il faut alors recréer manuellement la gestion clavier (Entrée/Espace) et le rôle ARIA, alors qu'un <button> les fournit nativement", is_correct: true }, { text: "Parce que les <div> ne supportent aucun style CSS", is_correct: false }, { text: "Parce que tabindex est interdit sur les <div>", is_correct: false }, { text: "Parce que cela ralentit le chargement de la page", is_correct: false } ] },
    { statement: "Quel attribut ARIA permet d'indiquer dynamiquement si un menu déroulant contrôlé par un bouton est actuellement ouvert ?", type: "single", time_limit: 20, answers: [
      { text: "aria-expanded", is_correct: true }, { text: "aria-open", is_correct: false }, { text: "aria-visible", is_correct: false }, { text: "aria-toggled", is_correct: false } ] },
    { statement: "Quelle touche clavier standard permet généralement d'activer un élément <a> ou <button> qui possède le focus ?", type: "single", time_limit: 20, answers: [
      { text: "Entrée", is_correct: true }, { text: "Tabulation", is_correct: false }, { text: "Échap", is_correct: false }, { text: "Barre d'espace uniquement pour les liens", is_correct: false } ] }
  ]
},
{
  title: "Rôles ARIA et sémantique implicite des éléments HTML",
  description: "Comprendre comment les éléments HTML natifs exposent déjà un rôle d'accessibilité par défaut.",
  questions: [
    { statement: "Quel rôle ARIA implicite possède naturellement un élément <nav> sans qu'il soit nécessaire de l'ajouter explicitement ?", type: "single", time_limit: 20, answers: [
      { text: "navigation", is_correct: true }, { text: "menu", is_correct: false }, { text: "list", is_correct: false }, { text: "region", is_correct: false } ] },
    { statement: "Quel rôle ARIA implicite est associé par défaut à l'élément <button> ?", type: "single", time_limit: 20, answers: [
      { text: "button", is_correct: true }, { text: "link", is_correct: false }, { text: "submit", is_correct: false }, { text: "input", is_correct: false } ] },
    { statement: "Ajouter role=\"button\" sur un élément qui est déjà un <button> natif est redondant mais sans risque particulier.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "L'élément <main> possède un rôle ARIA implicite équivalent à role=\"main\".", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Parmi ces éléments HTML, lesquels possèdent un rôle ARIA implicite correspondant à une région de page identifiable (landmark) ?", type: "multiple", time_limit: 30, answers: [
      { text: "<header>", is_correct: true }, { text: "<nav>", is_correct: true }, { text: "<footer>", is_correct: true }, { text: "<span>", is_correct: false } ] },
    { statement: "Que recommande la règle dite \"first rule of ARIA\" concernant l'usage des attributs ARIA ?", type: "single", time_limit: 20, answers: [
      { text: "Ne pas utiliser ARIA si un élément HTML natif possède déjà la sémantique et le comportement désirés", is_correct: true }, { text: "Toujours ajouter un rôle ARIA sur chaque élément de la page", is_correct: false }, { text: "Utiliser ARIA uniquement sur les images", is_correct: false }, { text: "Remplacer tous les éléments HTML par des <div> avec rôle ARIA", is_correct: false } ] },
    { statement: "Quel rôle ARIA correspond sémantiquement à l'élément <aside> lorsqu'il est utilisé en dehors d'un <article> ?", type: "single", time_limit: 20, answers: [
      { text: "complementary", is_correct: true }, { text: "sidebar", is_correct: false }, { text: "secondary", is_correct: false }, { text: "note", is_correct: false } ] },
    { statement: "Surcharger un élément sémantique natif avec un rôle ARIA contradictoire (par exemple role=\"presentation\" sur un <nav> porteur de sens) peut nuire à l'accessibilité.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] }
  ]
},
{
  title: "Formulaires accessibles : messages d'erreur et live regions",
  description: "Annoncer dynamiquement les changements d'état et les erreurs de validation aux technologies d'assistance.",
  questions: [
    { statement: "Quel attribut ARIA permet d'annoncer dynamiquement à un lecteur d'écran le contenu d'une zone qui se met à jour sans rechargement de page ?", type: "single", time_limit: 20, answers: [
      { text: "aria-live", is_correct: true }, { text: "aria-update", is_correct: false }, { text: "aria-refresh", is_correct: false }, { text: "aria-dynamic", is_correct: false } ] },
    { statement: "Quel attribut ARIA relie un champ de formulaire invalide à son message d'erreur descriptif affiché à proximité ?", type: "single", time_limit: 20, answers: [
      { text: "aria-describedby", is_correct: true }, { text: "aria-error", is_correct: false }, { text: "aria-message", is_correct: false }, { text: "aria-feedback", is_correct: false } ] },
    { statement: "Quel attribut booléen ARIA indique explicitement qu'un champ de formulaire est actuellement en état invalide ?", type: "single", time_limit: 20, answers: [
      { text: "aria-invalid", is_correct: true }, { text: "aria-error", is_correct: false }, { text: "aria-bad", is_correct: false }, { text: "aria-wrong", is_correct: false } ] },
    { statement: "Un message d'erreur affiché uniquement par une couleur de texte rouge, sans aucun texte ni icône, est suffisant pour l'accessibilité.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "La valeur aria-live=\"polite\" demande au lecteur d'écran d'annoncer la mise à jour sans interrompre brutalement la lecture en cours.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Parmi ces bonnes pratiques pour des formulaires accessibles, lesquelles sont pertinentes ?", type: "multiple", time_limit: 30, answers: [
      { text: "Associer chaque champ à un <label> explicite", is_correct: true }, { text: "Décrire clairement la nature de l'erreur, pas seulement la signaler par une couleur", is_correct: true }, { text: "Utiliser aria-describedby pour lier le message d'erreur au champ concerné", is_correct: true }, { text: "Faire disparaître le focus clavier dès la moindre erreur", is_correct: false } ] },
    { statement: "Quelle valeur de aria-live convient le mieux pour une alerte critique qui doit interrompre immédiatement la lecture du lecteur d'écran ?", type: "single", time_limit: 20, answers: [
      { text: "assertive", is_correct: true }, { text: "polite", is_correct: false }, { text: "urgent", is_correct: false }, { text: "immediate", is_correct: false } ] },
    { statement: "L'attribut required seul, sans aucun retour visuel ni textuel, suffit toujours à informer clairement tous les utilisateurs qu'un champ est obligatoire.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] }
  ]
}
];
