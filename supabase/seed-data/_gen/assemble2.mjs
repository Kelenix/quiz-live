import { writeFileSync } from "node:fs";
import { part1 } from "./part1.mjs";
import { part2 } from "./part2.mjs";
import { part3 } from "./part3.mjs";
import { part4 } from "./part4c.mjs";
import { part5 } from "./part5.mjs";
import { part6 } from "./part6.mjs";

const quizzes = [...part1, ...part2, ...part3, ...part4, ...part5, ...part6];

console.log("Total quizzes:", quizzes.length);

const normalize = (s) => String(s ?? "").trim().toLowerCase().replace(/\s+/g, " ");
const seenTitles = new Map();
const seenStatements = new Map();
const errors = [];

quizzes.forEach((quiz, qi) => {
  const nt = normalize(quiz.title);
  if (seenTitles.has(nt)) {
    errors.push(`Titre dupliqué: "${quiz.title}" (quiz[${qi}] vs quiz[${seenTitles.get(nt)}])`);
  } else {
    seenTitles.set(nt, qi);
  }

  if (quiz.questions.length !== 6) {
    errors.push(`Quiz "${quiz.title}" n'a pas 6 questions: ${quiz.questions.length}`);
  }

  const types = new Set();
  quiz.questions.forEach((q, qqi) => {
    const ns = normalize(q.statement);
    if (seenStatements.has(ns)) {
      errors.push(`Statement dupliqué: "${q.statement}" (quiz "${quiz.title}" vs ${seenStatements.get(ns)})`);
    } else {
      seenStatements.set(ns, `quiz "${quiz.title}" q[${qqi}]`);
    }
    types.add(q.type);

    if (!Array.isArray(q.answers) || q.answers.some(a => !a.text || !String(a.text).trim())) {
      errors.push(`Réponse vide dans quiz "${quiz.title}" q[${qqi}]: ${q.statement}`);
    }

    const correct = q.answers.filter(a => a.is_correct === true);
    if (q.type === "single") {
      if (q.answers.length < 2 || correct.length !== 1) {
        errors.push(`single invalide dans quiz "${quiz.title}": ${q.statement} (answers=${q.answers.length}, correct=${correct.length})`);
      }
    } else if (q.type === "multiple") {
      if (q.answers.length < 3 || correct.length < 2 || correct.length >= q.answers.length) {
        errors.push(`multiple invalide dans quiz "${quiz.title}": ${q.statement} (answers=${q.answers.length}, correct=${correct.length})`);
      }
    } else if (q.type === "truefalse") {
      const texts = q.answers.map(a => String(a.text).trim());
      if (q.answers.length !== 2 || !texts.includes("Vrai") || !texts.includes("Faux") || correct.length !== 1) {
        errors.push(`truefalse invalide dans quiz "${quiz.title}": ${q.statement}`);
      }
    } else {
      errors.push(`type inconnu "${q.type}" dans quiz "${quiz.title}": ${q.statement}`);
    }
  });

  for (const t of ["single", "multiple", "truefalse"]) {
    if (!types.has(t)) {
      errors.push(`Quiz "${quiz.title}" n'a pas de question de type ${t}`);
    }
  }
});

if (quizzes.length < 100) {
  errors.push(`Seulement ${quizzes.length} quiz, il en faut au moins 100`);
}

if (errors.length) {
  console.error(`${errors.length} erreur(s) détectée(s) avant écriture :`);
  errors.forEach(e => console.error(" - " + e));
  process.exit(1);
}

const output = {
  category: "Java",
  quizzes,
};

const json = JSON.stringify(output, null, 2);
const outPath = process.argv[2] || "./java.generated.json";
writeFileSync(outPath, json, "utf8");
console.log("Écrit:", outPath);
console.log("Quizzes:", quizzes.length, "| Questions uniques:", seenStatements.size);
