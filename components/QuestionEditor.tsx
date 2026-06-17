"use client";

import { ArrowDown, ArrowUp, Plus, Trash2, GripVertical } from "lucide-react";
import { cn, questionTypeLabel } from "@/lib/utils";
import type { QuestionDraft, QuestionType, AnswerDraft } from "@/types";

interface QuestionEditorProps {
  question: QuestionDraft;
  index: number;
  total: number;
  onChange: (q: QuestionDraft) => void;
  onMove: (dir: -1 | 1) => void;
  onDelete: () => void;
}

const TRUE_FALSE_TEMPLATE: AnswerDraft[] = [
  { text: "Vrai", is_correct: true },
  { text: "Faux", is_correct: false },
];

export function QuestionEditor({
  question,
  index,
  total,
  onChange,
  onMove,
  onDelete,
}: QuestionEditorProps) {
  const setField = <K extends keyof QuestionDraft>(k: K, v: QuestionDraft[K]) =>
    onChange({ ...question, [k]: v });

  const setType = (t: QuestionType) => {
    if (t === "truefalse") {
      onChange({
        ...question,
        type: t,
        answers: TRUE_FALSE_TEMPLATE.map((a) => ({ ...a })),
      });
      return;
    }
    if (t === "single" && question.type === "multiple") {
      // Garde au plus 1 bonne réponse
      let firstCorrectKept = false;
      const answers = question.answers.map((a) => {
        if (a.is_correct && !firstCorrectKept) {
          firstCorrectKept = true;
          return a;
        }
        return { ...a, is_correct: false };
      });
      onChange({ ...question, type: t, answers });
      return;
    }
    onChange({ ...question, type: t });
  };

  const updateAnswer = (i: number, patch: Partial<AnswerDraft>) => {
    const answers = question.answers.map((a, idx) =>
      idx === i ? { ...a, ...patch } : a,
    );
    onChange({ ...question, answers });
  };

  const toggleCorrect = (i: number) => {
    if (question.type === "multiple") {
      updateAnswer(i, { is_correct: !question.answers[i].is_correct });
      return;
    }
    // single / truefalse : une seule bonne réponse
    const answers = question.answers.map((a, idx) => ({
      ...a,
      is_correct: idx === i,
    }));
    onChange({ ...question, answers });
  };

  const addAnswer = () => {
    if (question.type === "truefalse") return;
    onChange({
      ...question,
      answers: [...question.answers, { text: "", is_correct: false }],
    });
  };

  const removeAnswer = (i: number) => {
    if (question.type === "truefalse") return;
    if (question.answers.length <= 2) return;
    onChange({
      ...question,
      answers: question.answers.filter((_, idx) => idx !== i),
    });
  };

  return (
    <div className="card p-5 space-y-5 animate-fade-in">
      <div className="flex items-start gap-3">
        <div className="flex flex-col items-center gap-1 pt-1.5 text-zinc-500">
          <GripVertical className="h-5 w-5" />
          <span className="text-xs font-bold text-zinc-400">Q{index + 1}</span>
        </div>
        <div className="flex-1 space-y-4">
          <div>
            <label className="label">Énoncé</label>
            <textarea
              className="input min-h-[72px] resize-y"
              placeholder="Écris ta question ici…"
              value={question.statement}
              onChange={(e) => setField("statement", e.target.value)}
            />
          </div>

          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <label className="label">Type</label>
              <div className="flex gap-2">
                {(["single", "multiple", "truefalse"] as QuestionType[]).map((t) => (
                  <button
                    key={t}
                    type="button"
                    onClick={() => setType(t)}
                    className={cn(
                      "flex-1 rounded-xl border px-3 py-2 text-xs font-medium transition",
                      question.type === t
                        ? "border-accent-primary/60 bg-accent-primary/20 text-white"
                        : "border-bg-border bg-bg-soft/40 text-zinc-400 hover:text-zinc-200",
                    )}
                  >
                    {questionTypeLabel(t)}
                  </button>
                ))}
              </div>
            </div>
            <div>
              <label className="label">Temps limite (sec, optionnel)</label>
              <input
                className="input"
                type="number"
                min={5}
                max={600}
                placeholder="Aucun"
                value={question.time_limit ?? ""}
                onChange={(e) =>
                  setField(
                    "time_limit",
                    e.target.value === "" ? null : Math.max(0, Number(e.target.value)),
                  )
                }
              />
            </div>
          </div>

          <div>
            <div className="mb-2 flex items-center justify-between">
              <label className="label !mb-0">Réponses</label>
              {question.type !== "truefalse" && (
                <button
                  type="button"
                  onClick={addAnswer}
                  className="text-xs text-accent-glow hover:underline"
                >
                  <Plus className="-mt-0.5 mr-1 inline h-3 w-3" />
                  Ajouter
                </button>
              )}
            </div>
            <div className="space-y-2">
              {question.answers.map((a, i) => (
                <div
                  key={i}
                  className={cn(
                    "flex items-center gap-2 rounded-xl border bg-bg-soft/30 p-2 transition",
                    a.is_correct
                      ? "border-emerald-500/40 bg-emerald-500/5"
                      : "border-bg-border",
                  )}
                >
                  <button
                    type="button"
                    onClick={() => toggleCorrect(i)}
                    className={cn(
                      "h-5 w-5 shrink-0 rounded-md border-2 transition",
                      question.type === "multiple" ? "rounded-md" : "rounded-full",
                      a.is_correct
                        ? "border-emerald-400 bg-emerald-400"
                        : "border-zinc-500 hover:border-emerald-400",
                    )}
                    aria-label="Bonne réponse"
                  />
                  <input
                    className="input !py-1.5 !border-0 !bg-transparent flex-1"
                    placeholder={`Réponse ${i + 1}`}
                    value={a.text}
                    disabled={question.type === "truefalse"}
                    onChange={(e) => updateAnswer(i, { text: e.target.value })}
                  />
                  {question.type !== "truefalse" && question.answers.length > 2 && (
                    <button
                      type="button"
                      onClick={() => removeAnswer(i)}
                      className="rounded-lg p-1.5 text-zinc-500 hover:bg-red-500/10 hover:text-red-400"
                    >
                      <Trash2 className="h-4 w-4" />
                    </button>
                  )}
                </div>
              ))}
            </div>
            <p className="mt-2 text-xs text-zinc-500">
              {question.type === "multiple"
                ? "Coche toutes les bonnes réponses."
                : "Coche la bonne réponse."}
            </p>
          </div>
        </div>

        <div className="flex flex-col gap-1">
          <button
            type="button"
            onClick={() => onMove(-1)}
            disabled={index === 0}
            className="rounded-lg border border-bg-border bg-bg-soft/40 p-1.5 text-zinc-400 hover:text-white disabled:opacity-30"
            aria-label="Monter"
          >
            <ArrowUp className="h-4 w-4" />
          </button>
          <button
            type="button"
            onClick={() => onMove(1)}
            disabled={index === total - 1}
            className="rounded-lg border border-bg-border bg-bg-soft/40 p-1.5 text-zinc-400 hover:text-white disabled:opacity-30"
            aria-label="Descendre"
          >
            <ArrowDown className="h-4 w-4" />
          </button>
          <button
            type="button"
            onClick={onDelete}
            className="mt-2 rounded-lg border border-red-500/30 bg-red-500/10 p-1.5 text-red-300 hover:bg-red-500/20"
            aria-label="Supprimer"
          >
            <Trash2 className="h-4 w-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
