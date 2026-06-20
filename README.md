# Quiz Live

Plateforme de quiz en direct, autonome, construite avec **Next.js 14 (App Router)**, **TypeScript**, **Tailwind CSS** et **Supabase** (PostgreSQL + Realtime).

Crée un quiz côté admin, partage un code à 6 caractères ou un QR Code, et lance la partie. Les participants jouent en temps réel depuis leur mobile, voient le classement final et reçoivent des confettis s'ils montent sur le podium.

---

## Fonctionnalités

- **Admin** : création / édition / suppression de quiz, gestion en direct (démarrer, question suivante, terminer).
- **Participant** : rejoindre via code ou QR, écran d'attente animé, réponse en temps réel, résultats finaux avec podium.
- **Temps réel** : Supabase Realtime sur `quizzes`, `participants`, `responses`.
- **Score** : single/truefalse +10, multiple parfait +15, partiel +5, bonus rapidité +5.
- **UI** : dark mode, accent vert (#3ecf8e → #1f9d63), Inter, animations Tailwind (slide/pop/float/dégradés), confettis, rendu full mobile.

---

## Stack

- Next.js 14 (App Router) + TypeScript
- Tailwind CSS
- Supabase (Postgres + Realtime + RLS)
- `qrcode.react` pour le QR
- `canvas-confetti` pour le podium
- `lucide-react` pour les icônes

---

## Installation locale

```bash
# 1. Cloner / arriver dans le projet
cd Quiz

# 2. Installer les dépendances
npm install

# 3. Configurer l'env
cp .env.local.example .env.local
# puis renseigner les 3 variables (voir ci-dessous)

# 4. Lancer le dev server
npm run dev
```

Ouvre [http://localhost:3000](http://localhost:3000).

---

## Configuration Supabase

1. Crée un projet sur [supabase.com](https://supabase.com).
2. Dans **SQL Editor**, exécute le contenu de [`supabase/schema.sql`](./supabase/schema.sql). Cela crée les tables, active Realtime sur `quizzes`/`participants`/`responses`, et applique les RLS policies.
3. Dans **Project Settings → API**, récupère :
   - `Project URL` → `NEXT_PUBLIC_SUPABASE_URL`
   - `anon public` → `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `service_role` (secret !) → `SUPABASE_SERVICE_ROLE_KEY`
4. Reporte-les dans `.env.local` :

```
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_ROLE_KEY=eyJ...
```

> **Sécurité** : la `service_role` n'est utilisée que côté serveur (API routes). Elle ne doit **jamais** être exposée côté client.

---



## Règles RLS

- **Lecture publique** sur `quizzes`, `questions`, `answers`, `participants`, `responses`.
- **Insertion publique** sur `participants` et `responses` (un joueur peut rejoindre et répondre).
- **Aucune politique** UPDATE / DELETE pour anon → seul le service_role (côté API admin) peut modifier ou supprimer.
- Toutes les actions admin (créer / modifier / supprimer un quiz, lancer, question suivante, terminer) passent par les routes `/api/quizzes/...` qui utilisent la `service_role`.

---

## Structure du projet

```
app/
  page.tsx                      # accueil
  JoinByCodeInline.tsx          # input "rejoindre par code"
  layout.tsx
  globals.css
  not-found.tsx
  admin/
    layout.tsx
    page.tsx                    # dashboard
    AdminQuizRowActions.tsx
    quiz/
      new/page.tsx              # création
      [id]/edit/page.tsx        # édition
      [id]/manage/
        page.tsx                # gestion live
        ManageClient.tsx
  live/
    [code]/
      page.tsx                  # join + statut
      JoinClient.tsx
      play/
        page.tsx                # interface de jeu
        PlayClient.tsx
  api/
    quizzes/route.ts            # POST create
    quizzes/[id]/route.ts       # PUT / DELETE
    quizzes/[id]/start/route.ts # waiting
    quizzes/[id]/go-live/route.ts
    quizzes/[id]/next/route.ts
    quizzes/[id]/finish/route.ts
    join/[code]/route.ts        # POST join
    responses/route.ts          # POST submit + scoring

components/
  StatusBadge.tsx
  Timer.tsx
  JoinQR.tsx
  Leaderboard.tsx
  QuestionEditor.tsx
  QuizForm.tsx

lib/
  supabase.ts                   # createPublicClient / createAdminClient
  utils.ts                      # joinCode, scoring, labels

types/index.ts                  # types partagés
supabase/schema.sql             # tout le schéma DB + RLS + Realtime
```

---

## Routes utilisateur

| Rôle        | URL                                  |
|-------------|--------------------------------------|
| Admin       | `/admin`                             |
| Admin       | `/admin/quiz/new`                    |
| Admin       | `/admin/quiz/[id]/edit`              |
| Admin       | `/admin/quiz/[id]/manage`            |
| Participant | `/live/[code]`                       |
| Participant | `/live/[code]/play`                  |

---

## Déploiement Vercel

### Prérequis

- Un projet Supabase opérationnel : `supabase/schema.sql` exécuté (tables + RLS + Realtime).
- La base **seedée** avec tes quiz : `npm run seed` (en local, avec un `.env.local` pointant vers ce projet). La base est partagée — une fois seedée, le site déployé verra les mêmes quiz.

### Étapes

1. **Pousser sur GitHub** (le `.env.local` est ignoré par git — ne le commite jamais).
   ```bash
   git add -A
   git commit -m "Prêt pour le déploiement"
   git push
   ```
2. Sur [vercel.com](https://vercel.com) → **Add New… → Project** → importe le repo GitHub.
3. Vercel détecte Next.js automatiquement (aucune config à changer : build `next build`, output par défaut).
4. Dans **Settings → Environment Variables**, ajoute les **3 variables** (pour les environnements Production + Preview) :

   | Variable | Valeur | Exposée au navigateur ? |
   |---|---|---|
   | `NEXT_PUBLIC_SUPABASE_URL` | `https://xxx.supabase.co` | Oui (préfixe `NEXT_PUBLIC_`) |
   | `NEXT_PUBLIC_SUPABASE_ANON_KEY` | `eyJ...` (clé anon) | Oui |
   | `SUPABASE_SERVICE_ROLE_KEY` | `eyJ...` (clé service_role) | **Non — secret, serveur uniquement** |
   | `ADMIN_PASSWORD` | mot de passe d'accès à `/admin` | **Non — secret, serveur uniquement** |

5. **Deploy**. À chaque `git push`, Vercel redéploie automatiquement.

### Authentification admin

- L'espace `/admin` (et les routes API `/api/quizzes/*`) est protégé par mot de passe via un **middleware** Next.js.
- Le mot de passe vit dans la variable d'environnement **`ADMIN_PASSWORD`** (jamais en dur dans le code). À la première visite, l'utilisateur est redirigé vers `/admin/login`.
- Connexion : cookie `httpOnly` valable 12 h. Bouton **Déconnexion** dans l'en-tête admin.
- **Si `ADMIN_PASSWORD` n'est pas défini sur Vercel, la connexion admin échouera** : pense à l'ajouter dans les variables d'environnement Production + Preview.

### ⚠️ Sécurité importante

- Ne mets **jamais** la `service_role` ni `ADMIN_PASSWORD` dans une variable préfixée `NEXT_PUBLIC_`, et ne les commite pas.
- Le fichier `.env.local.example` ne doit contenir que des valeurs factices (placeholders).
- Choisis un `ADMIN_PASSWORD` fort et différent de tes autres mots de passe.

> Auth Supabase non utilisée ici, donc aucune URL de redirection à configurer côté Supabase.

---

## Cycle d'un quiz

```
draft  ── (Lancer)        ──►  waiting  (participants rejoignent)
waiting ── (Démarrer)     ──►  live     (question 1, 2, 3…)
live    ── (Question suivante après la dernière)  ──►  finished
live/waiting ── (Terminer maintenant)              ──►  finished
```

Les changements de `status` et `current_question_index` sont diffusés instantanément à tous les clients connectés via Supabase Realtime.

---

## Scripts

```bash
npm run dev        # lance le dev server
npm run build      # build production
npm run start      # lance le build
npm run typecheck  # tsc --noEmit
npm run lint       # eslint
```

---

## Licence

MIT.
