export function S(statement, correct, wrongs, time_limit = 20) {
  return {
    statement,
    type: "single",
    time_limit,
    answers: [
      { text: correct, is_correct: true },
      ...wrongs.map(w => ({ text: w, is_correct: false })),
    ],
  };
}
export function M(statement, corrects, wrongs, time_limit = 30) {
  return {
    statement,
    type: "multiple",
    time_limit,
    answers: [
      ...corrects.map(c => ({ text: c, is_correct: true })),
      ...wrongs.map(w => ({ text: w, is_correct: false })),
    ],
  };
}
export function TF(statement, isTrue, time_limit = 15) {
  return {
    statement,
    type: "truefalse",
    time_limit,
    answers: [
      { text: "Vrai", is_correct: isTrue === true },
      { text: "Faux", is_correct: isTrue === false },
    ],
  };
}
export function Quiz(title, description, questions) {
  if (questions.length !== 6) throw new Error("Quiz '" + title + "' n'a pas 6 questions: " + questions.length);
  return { title, description, questions };
}
