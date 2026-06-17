// Générateur de banque de questions JS - 100 quiz x 8 questions
import { writeFileSync } from "node:fs";

const quizzes = [];

function Q(statement, type, time_limit, answers) {
  return { statement, type, time_limit, answers };
}
function S(statement, correctIdx, options) {
  // single: 4 options
  return Q(statement, "single", 20, options.map((t, i) => ({ text: t, is_correct: i === correctIdx })));
}
function M(statement, correctIdxs, options) {
  return Q(statement, "multiple", 30, options.map((t, i) => ({ text: t, is_correct: correctIdxs.includes(i) })));
}
function TF(statement, isTrue) {
  return Q(statement, "truefalse", 15, [
    { text: "Vrai", is_correct: isTrue === true },
    { text: "Faux", is_correct: isTrue === false },
  ]);
}

function quiz(title, description, questions) {
  if (questions.length !== 8) throw new Error("Quiz " + title + " has " + questions.length + " questions, need 8");
  quizzes.push({ title, description, questions });
}

// ============================================================
// Les quiz seront ajoutés ici par les fichiers suivants (concat)
// ============================================================

export { quizzes, Q, S, M, TF, quiz };
