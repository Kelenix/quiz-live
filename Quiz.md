Tu es un développeur full-stack expert. Crée une plateforme de Quiz Live complète, 
fonctionnant de manière autonome (sans intégration YouTube ou externe), avec Supabase 
comme base de données. Voici le cahier des charges complet :

---

## STACK TECHNIQUE
- Frontend : Next.js 14 (App Router) + TypeScript + Tailwind CSS
- Backend : API Routes Next.js
- Base de données : Supabase (PostgreSQL)
- Temps réel : Supabase Realtime (websockets)
- QR Code : librairie `qrcode` ou `react-qr-code`
- Hébergement : Vercel-ready

---

## SCHÉMA BASE DE DONNÉES SUPABASE

Crée les tables suivantes :

**quizzes**
- id (uuid, PK)
- title (text, NOT NULL)
- category (text) — valeurs : HTML, CSS, JS, C, SQL, IA, Autre
- description (text, nullable)
- join_code (text, UNIQUE) — ex: "ABC123"
- status (text) — valeurs : draft | waiting | live | finished
- current_question_index (int, default 0)
- created_at (timestamp)

**questions**
- id (uuid, PK)
- quiz_id (uuid, FK → quizzes.id)
- statement (text, NOT NULL)
- type (text) — valeurs : single | multiple | truefalse
- time_limit (int, nullable) — en secondes
- order_index (int)

**answers**
- id (uuid, PK)
- question_id (uuid, FK → questions.id)
- text (text, NOT NULL)
- is_correct (boolean, default false)

**participants**
- id (uuid, PK)
- quiz_id (uuid, FK → quizzes.id)
- username (text, NOT NULL)
- score (int, default 0)
- joined_at (timestamp)

**responses**
- id (uuid, PK)
- participant_id (uuid, FK → participants.id)
- question_id (uuid, FK → questions.id)
- answer_ids (uuid[]) — tableau des réponses choisies
- is_correct (boolean)
- answered_at (timestamp)

Active Supabase Realtime sur les tables : quizzes, participants, responses.

---

## PAGES & FONCTIONNALITÉS

### 1. ESPACE ADMINISTRATEUR (préfixe /admin)

**Page /admin** — Dashboard
- Liste de tous les quiz avec leur statut (badge coloré : draft/waiting/live/finished)
- Boutons : Créer, Modifier, Supprimer, Générer le lien, Lancer

**Page /admin/quiz/new** — Création de quiz
- Formulaire : titre, catégorie (select), description
- Section "Questions" avec bouton "Ajouter une question"
- Pour chaque question : 
  - Énoncé
  - Type (QCM unique / QCM multiple / Vrai-Faux)
  - Temps limite (optionnel, en secondes)
  - Réponses dynamiques (ajouter/supprimer) avec checkbox "bonne réponse"
- Sauvegarde en base Supabase
- Questions réorganisables (drag & drop ou flèches haut/bas)

**Page /admin/quiz/[id]/edit** — Modification du quiz
- Même formulaire que la création, pré-rempli

**Page /admin/quiz/[id]/manage** — Gestion du quiz en live
- Affiche le lien de participation + QR Code (généré avec join_code)
- Bouton "Démarrer le quiz" → passe le statut à "live"
- Question en cours affichée (énoncé + réponses)
- Bouton "Question suivante" → incrémente current_question_index
- Bouton "Terminer le quiz" → passe le statut à "finished"
- Compteur de participants connectés (temps réel)
- Nombre de réponses reçues pour la question en cours (temps réel)
- Classement en temps réel (top 10)

---

### 2. ESPACE PARTICIPANT

**Page /live/[code]** — Rejoindre le quiz
- Si le quiz n'existe pas → message d'erreur
- Si le quiz est "finished" → message "Quiz terminé"
- Si le quiz est "draft" → message "Quiz pas encore disponible"
- Si le quiz est "waiting" ou "live" → Formulaire de saisie du username
  - Vérification unicité du username dans la session (parmi les participants du quiz)
  - En cas de doublon → message d'erreur "Ce pseudo est déjà pris"
  - Après validation → redirige vers /live/[code]/play

**Page /live/[code]/play** — Interface de jeu
- Affiche le nom du quiz et le pseudo du joueur
- **Si statut = "waiting"** → Écran d'attente animé "En attente du lancement..."
  avec liste des participants rejoints (temps réel)
- **Si statut = "live"** → Affiche la question en cours :
  - Énoncé de la question
  - Timer si time_limit défini (compte à rebours)
  - Boutons de réponse (radio pour single/truefalse, checkbox pour multiple)
  - Bouton "Valider" → enregistre la réponse, bouton désactivé ensuite
  - Après validation → message "Réponse enregistrée, attente de la prochaine question..."
- **Si statut = "finished"** → Écran de résultats :
  - Classement final (top 10 avec médailles 🥇🥈🥉)
  - Score individuel du joueur
  - Message personnalisé si le joueur est dans le top 3

---

## LOGIQUE TEMPS RÉEL (Supabase Realtime)

- L'interface participant s'abonne aux changements de la table `quizzes` 
  (colonne status et current_question_index) pour le quiz concerné
- Quand current_question_index change → nouvelle question affichée automatiquement
- Quand status passe à "finished" → écran résultats affiché automatiquement
- Le dashboard admin s'abonne à `participants` et `responses` pour mise à jour live

---

## CALCUL DES SCORES

- Réponse correcte (single/truefalse) : +10 points
- Réponse correcte (multiple, toutes cochées correctement) : +15 points
- Réponse partielle (multiple) : +5 points
- Réponse incorrecte : 0 point
- Bonus rapidité (optionnel) : si time_limit défini, +5 pts si réponse dans la 1ère moitié du temps

Mettre à jour le score du participant dans la table `participants` à chaque réponse validée.

---

## GÉNÉRATION DU JOIN CODE

À la création d'un quiz, génère automatiquement un join_code unique de 6 caractères 
alphanumériques (ex: "ABC123"). Vérifie l'unicité en base avant d'assigner.

---

## UI / UX

- Design sombre et moderne (dark mode par défaut)
- Palette : fond #0f0f1a, accents violet/bleu (#7c3aed, #2563eb)
- Animations Tailwind sur les transitions de questions
- Responsive mobile-first (les participants joueront sur mobile)
- Page de résultats avec animation confetti (librairie `canvas-confetti`)
- Police : Inter ou Geist
- Le site doit etre moderne, pas d'emoji.. utilise les librairy adapté.

---

## STRUCTURE DES FICHIERS

Organise le projet en suivant la structure Next.js 14 App Router :
- /app/admin/... pour les pages admin
- /app/live/[code]/... pour les pages participants
- /components/... pour les composants réutilisables
- /lib/supabase.ts pour le client Supabase
- /lib/utils.ts pour les fonctions utilitaires
- /types/index.ts pour les types TypeScript

---

## CONFIGURATION

Crée un fichier .env.local.example avec :
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

---

## LIVRABLE ATTENDU

1. Tous les fichiers du projet avec leur contenu complet
2. Le script SQL complet pour créer les tables Supabase (avec RLS policies)
3. Un fichier README.md avec les instructions d'installation et de déploiement
4. Les policies Supabase RLS :
   - Lecture publique sur quizzes, questions, answers, participants
   - Insertion publique sur participants et responses
   - Écriture complète uniquement via service_role (côté admin)

Commence par le schéma SQL, puis les types TypeScript, puis les composants 
de base, puis les pages dans l'ordre logique.