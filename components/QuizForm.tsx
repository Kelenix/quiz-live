"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { Loader2, Plus, Save } from "lucide-react";
import { QuestionEditor } from "./QuestionEditor";
import type { QuizCategory, QuizDraft, QuestionDraft } from "@/types";

const CATEGORIES: QuizCategory[] = ["HTML", "CSS", "JS", "Java", "Python", "SQL"];

function emptyQuestion(order: number): QuestionDraft {
  return {
    statement: "",
    type: "single",
    time_limit: 20,
    order_index: order,
    answers: [
      { text: "", is_correct: true },
      { text: "", is_correct: false },
    ],
  };
}

export function QuizForm({
  initial,
  quizId,
}: {
  initial?: QuizDraft;
  quizId?: string;
}) {
  const router = useRouter();
  const [draft, setDraft] = useState<QuizDraft>(
    initial ?? {
      title: "",
      category: "HTML",
      description: "",
      questions: [emptyQuestion(0)],
    },
  );
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const updateQuestion = (i: number, q: QuestionDraft) => {
    const questions = draft.questions.map((qq, idx) => (idx === i ? q : qq));
    setDraft({ ...draft, questions });
  };

  const moveQuestion = (i: number, dir: -1 | 1) => {
    const j = i + dir;
    if (j < 0 || j >= draft.questions.length) return;
    const arr = [...draft.questions];
    [arr[i], arr[j]] = [arr[j], arr[i]];
    setDraft({
      ...draft,
      questions: arr.map((q, idx) => ({ ...q, order_index: idx })),
    });
  };

  const deleteQuestion = (i: number) => {
    if (draft.questions.length === 1) return;
    setDraft({
      ...draft,
      questions: draft.questions
        .filter((_, idx) => idx !== i)
        .map((q, idx) => ({ ...q, order_index: idx })),
    });
  };

  const addQuestion = () =>
    setDraft({
      ...draft,
      questions: [...draft.questions, emptyQuestion(draft.questions.length)],
    });

  const validate = (): string | null => {
    if (!draft.title.trim()) return "Le titre est obligatoire.";
    if (draft.questions.length === 0) return "Ajoute au moins une question.";
    for (let i = 0; i < draft.questions.length; i++) {
      const q = draft.questions[i];
      if (!q.statement.trim()) return `Question ${i + 1} : énoncé vide.`;
      if (q.answers.length < 2)
        return `Question ${i + 1} : au moins 2 réponses requises.`;
      if (q.answers.some((a) => !a.text.trim()))
        return `Question ${i + 1} : toutes les réponses doivent avoir un texte.`;
      const correctCount = q.answers.filter((a) => a.is_correct).length;
      if (correctCount === 0)
        return `Question ${i + 1} : marque au moins une bonne réponse.`;
      if (q.type !== "multiple" && correctCount > 1)
        return `Question ${i + 1} : une seule bonne réponse autorisée (QCM unique / Vrai-Faux).`;
    }
    return null;
  };

  const submit = async () => {
    setError(null);
    const v = validate();
    if (v) {
      setError(v);
      return;
    }
    setSaving(true);
    try {
      const url = quizId ? `/api/quizzes/${quizId}` : "/api/quizzes";
      const method = quizId ? "PUT" : "POST";
      const res = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(draft),
      });
      if (!res.ok) {
        const j = await res.json().catch(() => ({}));
        throw new Error(j.error ?? "Erreur enregistrement");
      }
      router.push("/admin");
      router.refresh();
    } catch (e: any) {
      setError(e.message ?? "Erreur");
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="card p-6 space-y-4">
        <div>
          <label className="label">Titre</label>
          <input
            className="input"
            placeholder="Ex. Quiz HTML — niveau intermédiaire"
            value={draft.title}
            onChange={(e) => setDraft({ ...draft, title: e.target.value })}
          />
        </div>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
          <div>
            <label className="label">Catégorie</label>
            <select
              className="input"
              value={draft.category}
              onChange={(e) =>
                setDraft({ ...draft, category: e.target.value as QuizCategory })
              }
            >
              {CATEGORIES.map((c) => (
                <option key={c} value={c}>
                  {c}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label className="label">Description</label>
            <input
              className="input"
              placeholder="Description courte (optionnel)"
              value={draft.description ?? ""}
              onChange={(e) =>
                setDraft({ ...draft, description: e.target.value })
              }
            />
          </div>
        </div>
      </div>

      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-semibold">
            Questions <span className="text-zinc-500">({draft.questions.length})</span>
          </h2>
        </div>
        <div className="space-y-4">
          {draft.questions.map((q, i) => (
            <QuestionEditor
              key={i}
              question={q}
              index={i}
              total={draft.questions.length}
              onChange={(qq) => updateQuestion(i, qq)}
              onMove={(d) => moveQuestion(i, d)}
              onDelete={() => deleteQuestion(i)}
            />
          ))}
        </div>
        <button onClick={addQuestion} className="btn-ghost w-full">
          <Plus className="h-4 w-4" /> Ajouter une question
        </button>
      </div>

      {error && (
        <div className="rounded-xl border border-red-500/40 bg-red-500/10 p-4 text-sm text-red-300">
          {error}
        </div>
      )}

      <div className="sticky bottom-4 z-10 flex flex-col-reverse items-stretch gap-2 sm:flex-row sm:justify-end">
        <button
          onClick={() => router.push("/admin")}
          className="btn-ghost"
          type="button"
        >
          Annuler
        </button>
        <button onClick={submit} disabled={saving} className="btn-primary">
          {saving ? (
            <Loader2 className="h-4 w-4 animate-spin" />
          ) : (
            <Save className="h-4 w-4" />
          )}
          {quizId ? "Enregistrer les modifications" : "Créer le quiz"}
        </button>
      </div>
    </div>
  );
}
