// Helpers de génération pour la banque de quiz JS.
// Pas d'exécution directe attendue : importé par les parts et l'assembleur.

export function S(statement, correct, wrongs, time_limit = 20) {
  const answers = [
    { text: correct, is_correct: true },
    ...wrongs.map((w) => ({ text: w, is_correct: false })),
  ];
  return { type: "single", statement, time_limit, answers };
}

export function M(statement, corrects, wrongs, time_limit = 30) {
  if (!Array.isArray(corrects) || corrects.length < 2) {
    throw new Error(`M() exige >=2 bonnes réponses : "${statement}"`);
  }
  if (!Array.isArray(wrongs) || wrongs.length < 1) {
    throw new Error(`M() exige >=1 mauvaise réponse : "${statement}"`);
  }
  const answers = [
    ...corrects.map((c) => ({ text: c, is_correct: true })),
    ...wrongs.map((w) => ({ text: w, is_correct: false })),
  ];
  return { type: "multiple", statement, time_limit, answers };
}

export function TF(statement, isTrue, time_limit = 15) {
  return {
    type: "truefalse",
    statement,
    time_limit,
    answers: [
      { text: "Vrai", is_correct: isTrue === true },
      { text: "Faux", is_correct: isTrue === false },
    ],
  };
}

export function Quiz(title, description, questions) {
  if (!Array.isArray(questions) || questions.length !== 6) {
    throw new Error(`Quiz "${title}" doit avoir exactement 6 questions (trouvé ${questions?.length}).`);
  }
  const types = new Set(questions.map((q) => q.type));
  for (const t of ["single", "multiple", "truefalse"]) {
    if (!types.has(t)) {
      throw new Error(`Quiz "${title}" doit contenir au moins une question de type "${t}".`);
    }
  }
  return { title, description, questions };
}
