// Assembleur de la banque de quiz JS.
// Importe tous les modules de parts, vérifie la cohérence globale,
// puis écrit le JSON final à supabase/seed-data/js.json
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

import { quizzes as p1 } from "./part1b.mjs";
import { quizzes as p2 } from "./part2b.mjs";
import { quizzes as p3 } from "./part3.mjs";
import { quizzes as p4 } from "./part4.mjs";
import { quizzes as p5 } from "./part5.mjs";
import { quizzes as p6 } from "./part6b.mjs";
import { quizzes as p7 } from "./part7.mjs";
import { quizzes as p8 } from "./part8.mjs";
import { quizzes as p9 } from "./part9.mjs";

const __dirname = dirname(fileURLToPath(import.meta.url));

const allQuizzes = [...p1, ...p2, ...p3, ...p4, ...p5, ...p6, ...p7, ...p8, ...p9];

const REQUIRED_TYPES = ["single", "multiple", "truefalse"];
const normalize = (s) => String(s ?? "").trim().toLowerCase().replace(/\s+/g, " ");

const errors = [];
const seenTitles = new Map();
const seenStatements = new Map();

allQuizzes.forEach((quiz, qi) => {
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

  if (!Array.isArray(quiz?.questions) || quiz.questions.length !== 6) {
    errors.push(`${qLabel}: doit avoir exactement 6 questions, trouvé ${quiz?.questions?.length ?? 0}`);
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
      if (q.answers.length !== 2 || !texts.includes("Vrai") || !texts.includes("Faux")) {
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

if (allQuizzes.length < 100) {
  errors.push(`Il faut au moins 100 quiz, trouvé ${allQuizzes.length}.`);
}

if (errors.length) {
  console.error(`${errors.length} erreur(s) trouvée(s) lors de l'assemblage :`);
  errors.slice(0, 100).forEach((e) => console.error(" - " + e));
  if (errors.length > 100) console.error(`  ... et ${errors.length - 100} de plus.`);
  process.exit(1);
}

const output = {
  category: "JS",
  quizzes: allQuizzes,
};

const outPath = join(__dirname, "..", "js.json");
writeFileSync(outPath, JSON.stringify(output, null, 2), "utf8");

console.log(
  `Assemblage OK : ${allQuizzes.length} quiz, ${seenStatements.size} questions uniques. Écrit dans ${outPath}`,
);
