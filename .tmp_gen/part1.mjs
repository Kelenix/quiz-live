// Part 1: éléments sémantiques + structure de document (quizzes 1-5)
export const part1 = [
{
  title: "Les balises sémantiques HTML5 : les fondamentaux",
  description: "Découvrez le rôle des principales balises sémantiques introduites avec HTML5.",
  questions: [
    { statement: "Quelle balise HTML5 sert à représenter l'en-tête introductif d'une page ou d'une section ?", type: "single", time_limit: 20, answers: [
      { text: "<header>", is_correct: true }, { text: "<head>", is_correct: false }, { text: "<top>", is_correct: false }, { text: "<title>", is_correct: false } ] },
    { statement: "Quelle balise sémantique permet de délimiter le contenu principal et unique d'une page ?", type: "single", time_limit: 20, answers: [
      { text: "<content>", is_correct: false }, { text: "<main>", is_correct: true }, { text: "<body>", is_correct: false }, { text: "<primary>", is_correct: false } ] },
    { statement: "À quoi sert la balise <nav> en HTML5 ?", type: "single", time_limit: 20, answers: [
      { text: "À afficher une barre de progression", is_correct: false }, { text: "À regrouper un ensemble de liens de navigation principaux", is_correct: true }, { text: "À créer un menu déroulant natif", is_correct: false }, { text: "À définir la zone de pied de page", is_correct: false } ] },
    { statement: "La balise <article> est faite pour contenir un contenu autonome, distribuable et réutilisable indépendamment du reste de la page.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Un document HTML5 ne peut contenir qu'une seule balise <section>.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces balises, lesquelles sont considérées comme des éléments sémantiques de structuration introduits par HTML5 ?", type: "multiple", time_limit: 30, answers: [
      { text: "<section>", is_correct: true }, { text: "<aside>", is_correct: true }, { text: "<footer>", is_correct: true }, { text: "<div>", is_correct: false } ] },
    { statement: "Quel est le rôle principal de la balise <aside> dans une page HTML5 ?", type: "single", time_limit: 20, answers: [
      { text: "Afficher le contenu principal de l'article", is_correct: false }, { text: "Contenir un contenu connexe ou tangentiel au contenu principal, comme une barre latérale", is_correct: true }, { text: "Définir le pied de page du site", is_correct: false }, { text: "Créer un formulaire de recherche", is_correct: false } ] },
    { statement: "Lesquelles de ces affirmations à propos de <footer> sont correctes ?", type: "multiple", time_limit: 30, answers: [
      { text: "Il peut contenir des informations sur l'auteur", is_correct: true }, { text: "Il peut être utilisé plusieurs fois dans une page, par exemple dans chaque <article>", is_correct: true }, { text: "Il peut contenir des liens vers des documents connexes", is_correct: true }, { text: "Il doit obligatoirement être l'unique élément enfant direct du <body>", is_correct: false } ] }
  ]
},
{
  title: "Sectionner une page web avec section, article et div",
  description: "Apprenez à choisir la bonne balise de regroupement selon le sens du contenu.",
  questions: [
    { statement: "Quelle est la principale différence sémantique entre <div> et <section> ?", type: "single", time_limit: 20, answers: [
      { text: "<div> n'a aucune signification sémantique alors que <section> représente une section thématique du contenu", is_correct: true }, { text: "<div> est obsolète en HTML5", is_correct: false }, { text: "<section> ne peut pas contenir de texte", is_correct: false }, { text: "Il n'y a aucune différence, ce sont des synonymes", is_correct: false } ] },
    { statement: "Si un regroupement de contenu n'a de sens que pour le style CSS ou le script JavaScript, sans valeur sémantique propre, quelle balise est recommandée ?", type: "single", time_limit: 20, answers: [
      { text: "<section>", is_correct: false }, { text: "<article>", is_correct: false }, { text: "<div>", is_correct: true }, { text: "<aside>", is_correct: false } ] },
    { statement: "Un commentaire d'utilisateur publié sous un billet de blog est un bon candidat pour être placé dans une balise <article>.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "La balise <section> doit toujours posséder un titre (h1-h6) pour être utilisée correctement selon les recommandations sémantiques.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Parmi les usages suivants, lesquels justifient l'emploi de la balise <article> plutôt que <section> ?", type: "multiple", time_limit: 30, answers: [
      { text: "Un billet de blog complet", is_correct: true }, { text: "Une actualité dans un flux d'actualités", is_correct: true }, { text: "Un commentaire utilisateur autonome", is_correct: true }, { text: "Un simple conteneur de mise en page sans signification", is_correct: false } ] },
    { statement: "Peut-on imbriquer plusieurs <article> à l'intérieur d'une même <section> ?", type: "single", time_limit: 20, answers: [
      { text: "Non, c'est interdit par la spécification", is_correct: false }, { text: "Oui, par exemple une section 'articles récents' contenant plusieurs articles", is_correct: true }, { text: "Seulement si chaque article contient un <header>", is_correct: false }, { text: "Oui mais uniquement avec un maximum de deux articles", is_correct: false } ] },
    { statement: "Quel critère doit-on utiliser pour décider d'utiliser <section> plutôt que <div> autour d'un bloc de contenu ?", type: "single", time_limit: 20, answers: [
      { text: "La présence d'une classe CSS particulière", is_correct: false }, { text: "Le fait que le contenu représente une unité thématique cohérente, idéalement avec un titre", is_correct: true }, { text: "Le nombre d'éléments enfants", is_correct: false }, { text: "La couleur de fond souhaitée", is_correct: false } ] },
    { statement: "Lesquelles de ces balises sont dites 'transparentes' au sens où elles n'imposent par elles-mêmes aucun style visuel particulier par défaut ?", type: "multiple", time_limit: 30, answers: [
      { text: "<div>", is_correct: true }, { text: "<section>", is_correct: true }, { text: "<article>", is_correct: true }, { text: "<table>", is_correct: false } ] }
  ]
},
{
  title: "Structure d'un document HTML : doctype, head et body",
  description: "Maîtrisez le squelette minimal et obligatoire de toute page HTML5 valide.",
  questions: [
    { statement: "Quelle déclaration doit obligatoirement figurer en toute première ligne d'un document HTML5 ?", type: "single", time_limit: 20, answers: [
      { text: "<!DOCTYPE html>", is_correct: true }, { text: "<html5>", is_correct: false }, { text: "<!-- HTML5 -->", is_correct: false }, { text: "<doctype>html</doctype>", is_correct: false } ] },
    { statement: "Que contrôle l'attribut lang sur la balise <html>, par exemple lang=\"fr\" ?", type: "single", time_limit: 20, answers: [
      { text: "La langue principale du contenu de la page, utile pour l'accessibilité et le SEO", is_correct: true }, { text: "Le format des nombres uniquement", is_correct: false }, { text: "La devise affichée dans les formulaires", is_correct: false }, { text: "Le fuseau horaire du serveur", is_correct: false } ] },
    { statement: "Quel élément contient les métadonnées d'un document HTML, non affichées directement dans la page (titre, liens vers feuilles de style, métadonnées) ?", type: "single", time_limit: 20, answers: [
      { text: "<meta>", is_correct: false }, { text: "<head>", is_correct: true }, { text: "<body>", is_correct: false }, { text: "<header>", is_correct: false } ] },
    { statement: "Le doctype HTML5 nécessite de préciser un numéro de version DTD comme en HTML4.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Un document HTML peut contenir deux balises <body> à condition qu'elles soient dans deux <html> séparés.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Quels éléments font partie intégrante de la structure minimale recommandée d'une page HTML5 valide ?", type: "multiple", time_limit: 30, answers: [
      { text: "<!DOCTYPE html>", is_correct: true }, { text: "<html>", is_correct: true }, { text: "<head>", is_correct: true }, { text: "<frameset>", is_correct: false } ] },
    { statement: "Quel est le rôle de la balise <title> placée dans le <head> ?", type: "single", time_limit: 20, answers: [
      { text: "Afficher un grand titre visible en haut de la page", is_correct: false }, { text: "Définir le titre affiché dans l'onglet du navigateur et utilisé par les moteurs de recherche", is_correct: true }, { text: "Définir le style du texte principal", is_correct: false }, { text: "Créer un lien d'ancre", is_correct: false } ] },
    { statement: "Parmi ces éléments, lesquels sont valides uniquement à l'intérieur de <head> ?", type: "multiple", time_limit: 30, answers: [
      { text: "<title>", is_correct: true }, { text: "<meta>", is_correct: true }, { text: "<link>", is_correct: true }, { text: "<p>", is_correct: false } ] }
  ]
},
{
  title: "Encodage et métadonnées : la balise meta charset",
  description: "Comprendre l'importance de l'encodage de caractères et des balises meta essentielles.",
  questions: [
    { statement: "Quelle balise meta permet de définir l'encodage de caractères d'une page HTML5 ?", type: "single", time_limit: 20, answers: [
      { text: "<meta charset=\"UTF-8\">", is_correct: true }, { text: "<meta encoding=\"UTF-8\">", is_correct: false }, { text: "<encoding>UTF-8</encoding>", is_correct: false }, { text: "<meta type=\"UTF-8\">", is_correct: false } ] },
    { statement: "Pourquoi est-il recommandé de déclarer l'encodage UTF-8 le plus tôt possible dans le <head> ?", type: "single", time_limit: 20, answers: [
      { text: "Pour accélérer le téléchargement des images", is_correct: false }, { text: "Pour éviter que le navigateur n'interprète mal les caractères avant d'avoir lu cette déclaration", is_correct: true }, { text: "Pour activer le mode strict de CSS", is_correct: false }, { text: "Pour désactiver JavaScript", is_correct: false } ] },
    { statement: "Que permet la balise <meta name=\"description\" content=\"...\"> ?", type: "single", time_limit: 20, answers: [
      { text: "Fournir un résumé de la page utilisé notamment par les moteurs de recherche dans les résultats", is_correct: true }, { text: "Définir le mot de passe de la page", is_correct: false }, { text: "Changer la langue de la page", is_correct: false }, { text: "Ajouter une description visible en haut de page", is_correct: false } ] },
    { statement: "UTF-8 est aujourd'hui l'encodage de caractères recommandé par défaut pour les pages HTML modernes.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "La balise <meta name=\"viewport\"> n'a aucun effet sur l'affichage des pages sur mobile.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Parmi ces attributs meta, lesquels sont couramment utilisés pour le référencement et le partage social ?", type: "multiple", time_limit: 30, answers: [
      { text: "<meta name=\"description\">", is_correct: true }, { text: "<meta property=\"og:title\">", is_correct: true }, { text: "<meta property=\"og:image\">", is_correct: true }, { text: "<meta charset=\"UTF-8\">", is_correct: false } ] },
    { statement: "Quel attribut de <meta name=\"viewport\"> permet d'indiquer que la largeur de la page doit correspondre à celle de l'appareil ?", type: "single", time_limit: 20, answers: [
      { text: "content=\"width=device-width, initial-scale=1\"", is_correct: true }, { text: "content=\"device=mobile\"", is_correct: false }, { text: "content=\"responsive=true\"", is_correct: false }, { text: "content=\"scale=auto\"", is_correct: false } ] },
    { statement: "Sans déclaration explicite d'encodage, certains caractères accentués comme 'é' ou 'à' peuvent s'afficher de façon corrompue dans le navigateur.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] }
  ]
},
{
  title: "Open Graph et SEO de base en HTML",
  description: "Les bonnes pratiques de balisage pour améliorer le référencement et le partage sur les réseaux sociaux.",
  questions: [
    { statement: "Que signifie le sigle SEO dans le contexte du développement web ?", type: "single", time_limit: 20, answers: [
      { text: "Search Engine Optimization (optimisation pour les moteurs de recherche)", is_correct: true }, { text: "Style Embedded Object", is_correct: false }, { text: "Secure Encrypted Output", is_correct: false }, { text: "Structured Element Order", is_correct: false } ] },
    { statement: "Quelle balise meta Open Graph définit l'image affichée lors du partage d'un lien sur un réseau social ?", type: "single", time_limit: 20, answers: [
      { text: "<meta property=\"og:image\">", is_correct: true }, { text: "<meta name=\"thumbnail\">", is_correct: false }, { text: "<img rel=\"social\">", is_correct: false }, { text: "<meta property=\"social:img\">", is_correct: false } ] },
    { statement: "Avoir un seul <h1> pertinent et bien rempli par page est généralement considéré comme une bonne pratique de structuration SEO.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: true }, { text: "Faux", is_correct: false } ] },
    { statement: "Le contenu de la balise <title> n'a aucune influence sur le référencement naturel d'une page.", type: "truefalse", time_limit: 15, answers: [
      { text: "Vrai", is_correct: false }, { text: "Faux", is_correct: true } ] },
    { statement: "Lesquelles de ces pratiques favorisent un bon référencement HTML de base ?", type: "multiple", time_limit: 30, answers: [
      { text: "Utiliser une hiérarchie de titres h1-h6 cohérente", is_correct: true }, { text: "Renseigner des attributs alt pertinents sur les images", is_correct: true }, { text: "Rédiger une meta description unique par page", is_correct: true }, { text: "Empiler plusieurs balises <h1> identiques sans rapport avec le contenu", is_correct: false } ] },
    { statement: "Quel attribut HTML permet d'indiquer aux robots d'indexation de ne pas suivre les liens d'une page ?", type: "single", time_limit: 20, answers: [
      { text: "<meta name=\"robots\" content=\"nofollow\">", is_correct: true }, { text: "<meta name=\"links\" content=\"deny\">", is_correct: false }, { text: "<a norobots>", is_correct: false }, { text: "<meta name=\"index\" content=\"false\">", is_correct: false } ] },
    { statement: "Pourquoi la balise <link rel=\"canonical\"> est-elle utile pour le SEO ?", type: "single", time_limit: 20, answers: [
      { text: "Elle indique l'URL de référence d'une page lorsqu'il existe plusieurs URLs menant à un contenu similaire", is_correct: true }, { text: "Elle accélère le chargement des polices", is_correct: false }, { text: "Elle remplace la balise <title>", is_correct: false }, { text: "Elle sert uniquement au style CSS", is_correct: false } ] },
    { statement: "Parmi ces balises Open Graph, lesquelles existent réellement dans la spécification Open Graph Protocol ?", type: "multiple", time_limit: 30, answers: [
      { text: "og:title", is_correct: true }, { text: "og:description", is_correct: true }, { text: "og:url", is_correct: true }, { text: "og:fontsize", is_correct: false } ] }
  ]
}
];
