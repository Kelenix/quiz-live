import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
import type {
  Answer,
  Question,
  QuestionType,
  QuizStatus,
} from "@/types";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

const JOIN_CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";

/** Génère un code de 6 caractères alphanumériques (sans caractères ambigus). */
export function generateJoinCode(length = 6): string {
  let out = "";
  for (let i = 0; i < length; i++) {
    out += JOIN_CODE_ALPHABET[Math.floor(Math.random() * JOIN_CODE_ALPHABET.length)];
  }
  return out;
}

export function statusLabel(status: QuizStatus): string {
  switch (status) {
    case "draft":
      return "Brouillon";
    case "waiting":
      return "En attente";
    case "live":
      return "En direct";
    case "finished":
      return "Terminé";
  }
}

export function statusColor(status: QuizStatus): string {
  switch (status) {
    case "draft":
      return "bg-zinc-700/40 text-zinc-300 border-zinc-600";
    case "waiting":
      return "bg-amber-500/15 text-amber-300 border-amber-500/40";
    case "live":
      return "bg-emerald-500/15 text-emerald-300 border-emerald-500/40 animate-pulse-soft";
    case "finished":
      return "bg-sky-500/15 text-sky-300 border-sky-500/40";
  }
}

export function questionTypeLabel(t: QuestionType): string {
  switch (t) {
    case "single":
      return "QCM unique";
    case "multiple":
      return "QCM multiple";
    case "truefalse":
      return "Vrai / Faux";
  }
}

/**
 * Calcule le score d'une réponse.
 *
 * - Single / Vrai-Faux : +10 si correcte
 * - Multiple : +15 si toutes correctes ET aucune incorrecte
 *              +5 si au moins une correcte mais pas parfaite
 * - Bonus rapidité : +5 si time_limit défini et réponse dans la 1ère moitié
 */
export interface ScoreInput {
  question: Pick<Question, "type" | "time_limit">;
  correctAnswerIds: string[];
  selectedAnswerIds: string[];
  elapsedMs: number | null;
}

export interface ScoreResult {
  points: number;
  isCorrect: boolean;
  isPartial: boolean;
}

export function computeScore({
  question,
  correctAnswerIds,
  selectedAnswerIds,
  elapsedMs,
}: ScoreInput): ScoreResult {
  const correctSet = new Set(correctAnswerIds);
  const selectedSet = new Set(selectedAnswerIds);

  const correctSelected = [...selectedSet].filter((id) => correctSet.has(id));
  const wrongSelected = [...selectedSet].filter((id) => !correctSet.has(id));

  let points = 0;
  let isCorrect = false;
  let isPartial = false;

  if (question.type === "multiple") {
    const allCorrectFound = correctAnswerIds.every((id) => selectedSet.has(id));
    const perfect = allCorrectFound && wrongSelected.length === 0;
    if (perfect) {
      points = 15;
      isCorrect = true;
    } else if (correctSelected.length > 0 && wrongSelected.length === 0) {
      // Partiel : au moins une bonne, aucune mauvaise.
      points = 5;
      isPartial = true;
    } else {
      points = 0;
    }
  } else {
    // single / truefalse : il doit y avoir exactement 1 bonne réponse cochée
    const exactlyOne =
      selectedAnswerIds.length === 1 && correctSet.has(selectedAnswerIds[0]);
    if (exactlyOne) {
      points = 10;
      isCorrect = true;
    }
  }

  // Bonus rapidité
  if (
    (isCorrect || isPartial) &&
    question.time_limit &&
    elapsedMs !== null &&
    elapsedMs <= (question.time_limit * 1000) / 2
  ) {
    points += 5;
  }

  return { points, isCorrect, isPartial };
}

export function correctAnswerIds(answers: Answer[]): string[] {
  return answers.filter((a) => a.is_correct).map((a) => a.id);
}

export function joinUrl(code: string, base?: string): string {
  const root =
    base ??
    (typeof window !== "undefined" ? window.location.origin : "");
  return `${root}/live/${code}`;
}
