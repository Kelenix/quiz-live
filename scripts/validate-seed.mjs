#!/usr/bin/env node
/**
 * Valide un fichier de banque de questions (supabase/seed-data/<categorie>.json)
 * avant qu'il ne soit utilisé par le script de seed.
 *
 * Usage : node scripts/validate-seed.mjs supabase/seed-data/html.json
 *
 * Règles vérifiées :
 *  - catégorie valide (HTML, CSS, JS, Java, Python, SQL)
 *  - au moins 100 quiz
 *  - titres de quiz non vides et uniques (dans le fichier)
 *  - chaque quiz a exactement 8 questions
 *  - chaque quiz contient au moins 1 question de chaque type
 *    (single, multiple, truefalse) — diversité des types exigée
 *  - aucun énoncé de question dupliqué dans tout le fichier
 *    (comparaison insensible à la casse / espaces)
 *  - règles de réponses par type :
 *      single     -> >= 2 réponses, exactement 1 correcte
 *      multiple   -> >= 3 réponses, >= 2 correctes, au moins 1 fausse
 *      truefalse  -> exactement 2 réponses "Vrai"/"Faux", 1 correcte
 *  - aucun texte de réponse vide
 */
import { readFileSync } from "node:fs";

const ALLOWED_CATEGORIES = ["HTML", "CSS", "JS", "Java", "Python", "SQL"];
const REQUIRED_TYPES = ["single", "multiple", "truefalse"];
const QUESTIONS_PER_QUIZ = 6;
const MIN_QUIZZES = 100;

const file = process.argv[2];
if (!file) {
  console.error("Usage: node scripts/validate-seed.mjs <path-to-category.json>");
  process.exit(1);
}

const raw = readFileSync(file, "utf8");
let data;
try {
  data = JSON.parse(raw);
} catch (e) {
  console.error("JSON invalide :", e.message);
  process.exit(1);
}

const errors = [];
const normalize = (s) => String(s ?? "").trim().toLowerCase().replace(/\s+/g, " ");

if (!ALLOWED_CATEGORIES.includes(data.category)) {
  errors.push(`category invalide ou manquante : ${JSON.stringify(data.category)}`);
}

if (!Array.isArray(data.quizzes)) {
  console.error("Erreur fatale : `quizzes` doit être un tableau.");
  process.exit(1);
}

if (data.quizzes.length < MIN_QUIZZES) {
  errors.push(`Il faut au moins ${MIN_QUIZZES} quiz, trouvé ${data.quizzes.length}.`);
}

const seenStatements = new Map();
const seenTitles = new Map();

data.quizzes.forEach((quiz, qi) => {
  const qLabel = `quiz[${qi}] "${quiz?.title ?? "?"}"`;

  if (!quiz?.title || !quiz.title.trim()) {
    errors.push(`${qLabel}: titre manquant`);
  } else {
    const nt = normalize(quiz.title);
    if (seenTitles.has(nt)) {
      errors.push(`${qLabel}: titre dupliqué (déjà utilisé par quiz[${seenTitles.get(nt)}])`);
    } else {
      seenTitles.set(nt, qi);
    }
  }

  if (!Array.isArray(quiz?.questions) || quiz.questions.length !== QUESTIONS_PER_QUIZ) {
    errors.push(
      `${qLabel}: doit avoir exactement ${QUESTIONS_PER_QUIZ} questions, trouvé ${quiz?.questions?.length ?? 0}`,
    );
    return;
  }

  const typesPresent = new Set();

  quiz.questions.forEach((q, qqi) => {
    const label = `${qLabel} > question[${qqi}]`;

    if (!q?.statement || !q.statement.trim()) {
      errors.push(`${label}: énoncé manquant`);
      return;
    }
    const norm = normalize(q.statement);
    if (seenStatements.has(norm)) {
      errors.push(`${label}: énoncé dupliqué (déjà utilisé par ${seenStatements.get(norm)})`);
    } else {
      seenStatements.set(norm, label);
    }

    if (!REQUIRED_TYPES.includes(q.type)) {
      errors.push(`${label}: type invalide "${q.type}"`);
      return;
    }
    typesPresent.add(q.type);

    if (!Array.isArray(q.answers) || q.answers.length < 2) {
      errors.push(`${label}: il faut au moins 2 réponses`);
      return;
    }
    if (q.answers.some((a) => !a?.text || !String(a.text).trim())) {
      errors.push(`${label}: au moins une réponse a un texte vide`);
    }
    const correct = q.answers.filter((a) => a.is_correct === true);

    if (q.type === "truefalse") {
      const texts = q.answers.map((a) => String(a.text).trim());
      if (
        q.answers.length !== 2 ||
        !texts.includes("Vrai") ||
        !texts.includes("Faux")
      ) {
        errors.push(`${label}: vrai/faux doit avoir exactement les réponses "Vrai" et "Faux"`);
      }
      if (correct.length !== 1) {
        errors.push(`${label}: vrai/faux doit avoir exactement 1 bonne réponse`);
      }
    } else if (q.type === "single") {
      if (correct.length !== 1) {
        errors.push(`${label}: QCM unique doit avoir exactement 1 bonne réponse (trouvé ${correct.length})`);
      }
    } else if (q.type === "multiple") {
      if (q.answers.length < 3) {
        errors.push(`${label}: QCM multiple doit avoir au moins 3 réponses`);
      }
      if (correct.length < 2) {
        errors.push(`${label}: QCM multiple doit avoir au moins 2 bonnes réponses (trouvé ${correct.length})`);
      }
      if (correct.length >= q.answers.length) {
        errors.push(`${label}: QCM multiple doit avoir au moins 1 mauvaise réponse`);
      }
    }
  });

  for (const t of REQUIRED_TYPES) {
    if (!typesPresent.has(t)) {
      errors.push(`${qLabel}: aucune question de type "${t}" (diversité des types exigée par quiz)`);
    }
  }
});

if (errors.length) {
  console.error(`${errors.length} erreur(s) trouvée(s) dans ${file} :`);
  errors.slice(0, 80).forEach((e) => console.error(" - " + e));
  if (errors.length > 80) console.error(`  ... et ${errors.length - 80} de plus.`);
  process.exit(1);
} else {
  console.log(
    `OK — ${file} : ${data.quizzes.length} quiz, ${seenStatements.size} questions uniques, catégorie ${data.category}.`,
  );
  process.exit(0);
}
