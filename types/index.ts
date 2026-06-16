export type QuizCategory = "HTML" | "CSS" | "JS" | "C" | "SQL" | "IA" | "Autre";
export type QuizStatus = "draft" | "waiting" | "live" | "finished";
export type QuestionType = "single" | "multiple" | "truefalse";

export interface Quiz {
  id: string;
  title: string;
  category: QuizCategory;
  description: string | null;
  join_code: string;
  status: QuizStatus;
  current_question_index: number;
  created_at: string;
}

export interface Question {
  id: string;
  quiz_id: string;
  statement: string;
  type: QuestionType;
  time_limit: number | null;
  order_index: number;
}

export interface Answer {
  id: string;
  question_id: string;
  text: string;
  is_correct: boolean;
}

export interface Participant {
  id: string;
  quiz_id: string;
  username: string;
  score: number;
  joined_at: string;
}

export interface Response {
  id: string;
  participant_id: string;
  question_id: string;
  answer_ids: string[];
  is_correct: boolean;
  answered_at: string;
}

export interface QuestionWithAnswers extends Question {
  answers: Answer[];
}

export interface QuizWithQuestions extends Quiz {
  questions: QuestionWithAnswers[];
}

// Payload côté admin pour création/édition
export interface QuestionDraft {
  id?: string;
  statement: string;
  type: QuestionType;
  time_limit: number | null;
  order_index: number;
  answers: AnswerDraft[];
}

export interface AnswerDraft {
  id?: string;
  text: string;
  is_correct: boolean;
}

export interface QuizDraft {
  title: string;
  category: QuizCategory;
  description: string | null;
  questions: QuestionDraft[];
}
