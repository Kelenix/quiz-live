#!/usr/bin/env node
/**
 * Seed Supabase avec les banques de quiz générées (supabase/seed-data/*.json).
 *
 * Usage :
 *   npm run seed              -> insère tout (réexécutable, ignore les quiz déjà présents)
 *   npm run seed:dry          -> valide et compte sans toucher à la base (aucune variable d'env requise)
 *   node scripts/seed.mjs --only=html,css   -> limite à certaines catégories
 *   node scripts/seed.mjs --limit=5         -> n'insère que 5 quiz par catégorie (tests)
 *
 * Variables d'environnement requises (lues depuis .env.local puis .env) :
 *   NEXT_PUBLIC_SUPABASE_URL
 *   SUPABASE_SERVICE_ROLE_KEY   (clé admin — bypasse les RLS, comme lib/supabase.ts:createAdminClient)
 */
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import path from "node:path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SEED_DIR = path.join(ROOT, "supabase", "seed-data");
const ALLOWED_CATEGORIES = ["HTML", "CSS", "JS", "Java", "Python", "SQL"];
const JOIN_CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; // identique à lib/utils.ts

// --- Arguments CLI -----------------------------------------------------
const args = process.argv.slice(2);
const DRY_RUN = args.includes("--dry-run");
const onlyArg = args.find((a) => a.startsWith("--only="));
const ONLY = onlyArg ? onlyArg.slice("--only=".length).split(",").map((s) => s.trim().toLowerCase()) : null;
const limitArg = args.find((a) => a.startsWith("--limit="));
const LIMIT = limitArg ? parseInt(limitArg.slice("--limit=".length), 10) : null;
const CONCURRENCY = 4;

// --- Charge .env.local puis .env (sans dépendance externe) -------------
function loadEnvFile(file) {
  if (!existsSync(file)) return;
  const content = readFileSync(file, "utf8");
  for (const rawLine of content.split("\n")) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) continue;
    const eq = line.indexOf("=");
    if (eq === -1) continue;
    const key = line.slice(0, eq).trim();
    let value = line.slice(eq + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    if (!(key in process.env)) process.env[key] = value;
  }
}
loadEnvFile(path.join(ROOT, ".env.local"));
loadEnvFile(path.join(ROOT, ".env"));

const normalize = (s) => String(s ?? "").trim().toLowerCase().replace(/\s+/g, " ");

// --- 1. Repère les fichiers de seed et les valide avec le validateur officiel --
let files = readdirSync(SEED_DIR).filter((f) => f.endsWith(".json"));
if (ONLY) {
  files = files.filter((f) => ONLY.includes(f.replace(/\.json$/, "").toLowerCase()));
}
if (files.length === 0) {
  console.error("Aucun fichier supabase/seed-data/*.json trouvé (ou filtré par --only).");
  process.exit(1);
}

console.log(`Validation de ${files.length} fichier(s) avant seed...\n`);
const datasets = [];
for (const file of files) {
  const fullPath = path.join(SEED_DIR, file);
  try {
    execFileSync(
      process.execPath,
      [path.join(ROOT, "scripts", "validate-seed.mjs"), path.join("supabase", "seed-data", file)],
      { cwd: ROOT, stdio: "inherit" },
    );
  } catch {
    console.error(`\n❌ ${file} n'a pas passé la validation. Seed annulé.`);
    process.exit(1);
  }
  const data = JSON.parse(readFileSync(fullPath, "utf8"));
  if (!ALLOWED_CATEGORIES.includes(data.category)) {
    console.error(`❌ Catégorie invalide dans ${file}: ${data.category}`);
    process.exit(1);
  }
  let quizzes = data.quizzes;
  if (LIMIT) quizzes = quizzes.slice(0, LIMIT);
  datasets.push({ file, category: data.category, quizzes });
}

const totalQuizzes = datasets.reduce((n, d) => n + d.quizzes.length, 0);
const totalQuestions = datasets.reduce(
  (n, d) => n + d.quizzes.reduce((m, q) => m + q.questions.length, 0),
  0,
);
console.log(
  `\n✅ Tous les fichiers sont valides. ${totalQuizzes} quiz / ${totalQuestions} questions au total à traiter.\n`,
);

if (DRY_RUN) {
  for (const d of datasets) {
    console.log(`  - ${d.category}: ${d.quizzes.length} quiz`);
  }
  console.log("\n(--dry-run : aucune écriture en base, aucune variable Supabase requise)");
  process.exit(0);
}

// --- 2. Connexion Supabase (clé service_role, comme createAdminClient) --
const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL;
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
if (!SUPABASE_URL || !SERVICE_KEY) {
  console.error(
    "❌ NEXT_PUBLIC_SUPABASE_URL et/ou SUPABASE_SERVICE_ROLE_KEY manquent.\n" +
      "   Crée un fichier .env.local à la racine du projet (voir .env.local.example) avec ces valeurs,\n" +
      "   trouvables dans Supabase > Project Settings > API.",
  );
  process.exit(1);
}

const { createClient } = await import("@supabase/supabase-js");
const admin = createClient(SUPABASE_URL, SERVICE_KEY, { auth: { persistSession: false } });

// --- 3. Évite les doublons si le script est relancé ---------------------
console.log("Lecture des quiz déjà présents en base (pour ne pas les recréer)...");
const existingTitles = new Set(); // `${category}::${normalized title}`
{
  const pageSize = 1000;
  let from = 0;
  while (true) {
    const { data, error } = await admin
      .from("quizzes")
      .select("title, category")
      .range(from, from + pageSize - 1);
    if (error) {
      console.error("❌ Impossible de lire les quiz existants:", error.message);
      process.exit(1);
    }
    for (const row of data) existingTitles.add(`${row.category}::${normalize(row.title)}`);
    if (data.length < pageSize) break;
    from += pageSize;
  }
}
console.log(`  -> ${existingTitles.size} quiz déjà en base, seront ignorés s'ils correspondent.\n`);

const usedCodes = new Set();
async function uniqueJoinCode() {
  for (let i = 0; i < 15; i++) {
    let code = "";
    for (let c = 0; c < 6; c++) {
      code += JOIN_CODE_ALPHABET[Math.floor(Math.random() * JOIN_CODE_ALPHABET.length)];
    }
    if (usedCodes.has(code)) continue;
    const { data, error } = await admin.from("quizzes").select("id").eq("join_code", code).maybeSingle();
    if (error) throw error;
    if (!data) {
      usedCodes.add(code);
      return code;
    }
  }
  throw new Error("Impossible de générer un join_code unique après 15 tentatives.");
}

async function insertQuiz(category, quizDef) {
  const code = await uniqueJoinCode();
  const { data: quizRow, error: e1 } = await admin
    .from("quizzes")
    .insert({
      title: quizDef.title.trim(),
      category,
      description: quizDef.description?.trim() || null,
      join_code: code,
      status: "draft",
    })
    .select("id")
    .single();
  if (e1) throw e1;

  const questionsPayload = quizDef.questions.map((q, i) => ({
    quiz_id: quizRow.id,
    statement: q.statement.trim(),
    type: q.type,
    time_limit: q.time_limit ?? null,
    order_index: i,
  }));
  const { data: qRows, error: e2 } = await admin
    .from("questions")
    .insert(questionsPayload)
    .select("id, order_index");
  if (e2) throw e2;

  const idByIndex = new Map(qRows.map((r) => [r.order_index, r.id]));
  const answersPayload = [];
  quizDef.questions.forEach((q, i) => {
    const qid = idByIndex.get(i);
    for (const a of q.answers) {
      answersPayload.push({ question_id: qid, text: a.text.trim(), is_correct: !!a.is_correct });
    }
  });
  const { error: e3 } = await admin.from("answers").insert(answersPayload);
  if (e3) throw e3;
}

// --- 4. File de travail avec concurrence limitée -------------------------
const jobs = [];
for (const d of datasets) {
  for (const quizDef of d.quizzes) {
    const key = `${d.category}::${normalize(quizDef.title)}`;
    if (existingTitles.has(key)) {
      jobs.push({ category: d.category, quizDef, skip: true });
    } else {
      jobs.push({ category: d.category, quizDef, skip: false });
    }
  }
}

let done = 0;
let inserted = 0;
let skipped = 0;
const failures = [];

async function worker() {
  while (jobs.length) {
    const job = jobs.shift();
    if (!job) return;
    done++;
    if (job.skip) {
      skipped++;
      continue;
    }
    try {
      await insertQuiz(job.category, job.quizDef);
      inserted++;
    } catch (err) {
      failures.push({ title: job.quizDef.title, category: job.category, message: err.message });
    }
    if (done % 25 === 0 || jobs.length === 0) {
      process.stdout.write(
        `\r  progression: ${done}/${totalQuizzes} (insérés: ${inserted}, ignorés: ${skipped}, échecs: ${failures.length})   `,
      );
    }
  }
}

console.log(`Insertion en cours (concurrence: ${CONCURRENCY})...`);
await Promise.all(Array.from({ length: CONCURRENCY }, worker));

console.log("\n\n=== Résumé du seed ===");
for (const d of datasets) {
  console.log(`  - ${d.category}: ${d.quizzes.length} quiz traités`);
}
console.log(`\nTotal: ${inserted} quiz insérés, ${skipped} déjà présents (ignorés), ${failures.length} échecs.`);
if (failures.length) {
  console.log("\nÉchecs :");
  for (const f of failures.slice(0, 30)) {
    console.log(`  - [${f.category}] "${f.title}": ${f.message}`);
  }
  if (failures.length > 30) console.log(`  ... et ${failures.length - 30} de plus.`);
  process.exit(1);
}
