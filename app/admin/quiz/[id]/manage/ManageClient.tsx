"use client";

import { useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import {
  CheckCircle2,
  ChevronRight,
  Flag,
  Loader2,
  Play,
  Users,
} from "lucide-react";
import { getBrowserClient } from "@/lib/supabase";
import { StatusBadge } from "@/components/StatusBadge";
import { JoinQR } from "@/components/JoinQR";
import { Leaderboard } from "@/components/Leaderboard";
import { cn, questionTypeLabel } from "@/lib/utils";
import type {
  Participant,
  Quiz,
  QuestionWithAnswers,
  Response,
} from "@/types";

export function ManageClient({
  quiz: initialQuiz,
  questions,
}: {
  quiz: Quiz;
  questions: QuestionWithAnswers[];
}) {
  const router = useRouter();
  const [quiz, setQuiz] = useState<Quiz>(initialQuiz);
  const [participants, setParticipants] = useState<Participant[]>([]);
  const [responseCount, setResponseCount] = useState(0);
  const [busy, setBusy] = useState(false);

  const currentQuestion = useMemo(
    () => questions[quiz.current_question_index] ?? null,
    [questions, quiz.current_question_index],
  );

  // Realtime subscriptions
  useEffect(() => {
    const sb = getBrowserClient();

    // Initial fetch participants
    sb.from("participants")
      .select("*")
      .eq("quiz_id", quiz.id)
      .then(({ data }) => setParticipants((data ?? []) as Participant[]));

    const ch = sb
      .channel(`admin-quiz-${quiz.id}`)
      .on(
        "postgres_changes",
        {
          event: "*",
          schema: "public",
          table: "quizzes",
          filter: `id=eq.${quiz.id}`,
        },
        (payload) => {
          if (payload.new) setQuiz(payload.new as Quiz);
        },
      )
      .on(
        "postgres_changes",
        {
          event: "*",
          schema: "public",
          table: "participants",
          filter: `quiz_id=eq.${quiz.id}`,
        },
        (payload) => {
          if (payload.eventType === "INSERT") {
            setParticipants((prev) => [...prev, payload.new as Participant]);
          } else if (payload.eventType === "UPDATE") {
            const np = payload.new as Participant;
            setParticipants((prev) => prev.map((p) => (p.id === np.id ? np : p)));
          } else if (payload.eventType === "DELETE") {
            const op = payload.old as Participant;
            setParticipants((prev) => prev.filter((p) => p.id !== op.id));
          }
        },
      )
      .on(
        "postgres_changes",
        {
          event: "INSERT",
          schema: "public",
          table: "responses",
        },
        (payload) => {
          const r = payload.new as Response;
          if (r.question_id === currentQuestion?.id) {
            setResponseCount((c) => c + 1);
          }
        },
      )
      .subscribe();

    return () => {
      sb.removeChannel(ch);
    };
  }, [quiz.id, currentQuestion?.id]);

  // Reset compteur quand on change de question
  useEffect(() => {
    setResponseCount(0);
    if (!currentQuestion) return;
    const sb = getBrowserClient();
    sb.from("responses")
      .select("id", { count: "exact", head: true })
      .eq("question_id", currentQuestion.id)
      .then(({ count }) => setResponseCount(count ?? 0));
  }, [currentQuestion?.id]);

  const action = async (endpoint: string) => {
    setBusy(true);
    try {
      const res = await fetch(`/api/quizzes/${quiz.id}/${endpoint}`, {
        method: "POST",
      });
      if (!res.ok) throw new Error((await res.json()).error ?? "Erreur");
      router.refresh();
    } catch (e: any) {
      alert(e.message);
    } finally {
      setBusy(false);
    }
  };

  const totalQuestions = questions.length;
  const isLastQuestion = quiz.current_question_index >= totalQuestions - 1;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-2xl font-bold">{quiz.title}</h1>
          <p className="flex items-center gap-3 text-sm text-zinc-400">
            <StatusBadge status={quiz.status} />
            <span>{totalQuestions} questions</span>
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
        {/* Colonne gauche : QR + actions */}
        <div className="space-y-6 lg:col-span-1">
          <div className="card p-6">
            <h2 className="mb-4 text-sm font-semibold uppercase tracking-wider text-zinc-400">
              Lien de participation
            </h2>
            <JoinQR code={quiz.join_code} />
          </div>

          <div className="card p-6 space-y-3">
            <h2 className="text-sm font-semibold uppercase tracking-wider text-zinc-400">
              Contrôle du quiz
            </h2>
            {quiz.status === "waiting" && (
              <button
                disabled={busy || totalQuestions === 0}
                onClick={() => action("go-live")}
                className="btn-primary w-full"
              >
                {busy ? <Loader2 className="h-4 w-4 animate-spin" /> : <Play className="h-4 w-4" />}
                Démarrer le quiz
              </button>
            )}
            {quiz.status === "live" && (
              <button
                disabled={busy}
                onClick={() => action("next")}
                className="btn-primary w-full"
              >
                {busy ? (
                  <Loader2 className="h-4 w-4 animate-spin" />
                ) : isLastQuestion ? (
                  <Flag className="h-4 w-4" />
                ) : (
                  <ChevronRight className="h-4 w-4" />
                )}
                {isLastQuestion ? "Terminer le quiz" : "Question suivante"}
              </button>
            )}
            {(quiz.status === "waiting" || quiz.status === "live") && (
              <button
                disabled={busy}
                onClick={() => action("finish")}
                className="btn-ghost w-full"
              >
                <Flag className="h-4 w-4" /> Terminer maintenant
              </button>
            )}
            {quiz.status === "finished" && (
              <div className="rounded-xl border border-sky-500/40 bg-sky-500/10 p-3 text-center text-sm text-sky-200">
                Quiz terminé.
              </div>
            )}
          </div>
        </div>

        {/* Colonne centrale : question en cours */}
        <div className="space-y-6 lg:col-span-2">
          <div className="card p-6">
            <div className="mb-4 flex items-center justify-between">
              <h2 className="text-sm font-semibold uppercase tracking-wider text-zinc-400">
                {quiz.status === "waiting"
                  ? "En attente du lancement"
                  : `Question ${Math.min(quiz.current_question_index + 1, totalQuestions)} / ${totalQuestions}`}
              </h2>
              {currentQuestion && quiz.status === "live" && (
                <span className="chip border-bg-border bg-bg-soft text-zinc-300">
                  {questionTypeLabel(currentQuestion.type)}
                </span>
              )}
            </div>

            {quiz.status === "waiting" && (
              <div className="rounded-xl border border-dashed border-bg-border bg-bg-soft/30 p-8 text-center">
                <p className="text-zinc-300">
                  Partage le code ou le QR pour permettre aux participants de
                  rejoindre, puis démarre le quiz.
                </p>
              </div>
            )}

            {quiz.status !== "waiting" && currentQuestion && (
              <div className="space-y-4">
                <p className="text-lg font-medium leading-snug">
                  {currentQuestion.statement}
                </p>
                <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
                  {currentQuestion.answers.map((a) => (
                    <div
                      key={a.id}
                      className={cn(
                        "rounded-xl border px-4 py-3 text-sm",
                        a.is_correct
                          ? "border-emerald-500/40 bg-emerald-500/10 text-emerald-200"
                          : "border-bg-border bg-bg-soft/40",
                      )}
                    >
                      <div className="flex items-center gap-2">
                        {a.is_correct && (
                          <CheckCircle2 className="h-4 w-4 text-emerald-300" />
                        )}
                        <span>{a.text}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {quiz.status === "live" && currentQuestion && (
              <div className="mt-6 grid grid-cols-2 gap-4">
                <div className="rounded-xl border border-bg-border bg-bg-soft/40 p-4">
                  <p className="text-xs uppercase tracking-wide text-zinc-500">
                    Réponses reçues
                  </p>
                  <p className="text-2xl font-bold text-accent-glow">
                    {responseCount}
                    <span className="text-base text-zinc-500">
                      {" "}
                      / {participants.length}
                    </span>
                  </p>
                </div>
                <div className="rounded-xl border border-bg-border bg-bg-soft/40 p-4">
                  <p className="text-xs uppercase tracking-wide text-zinc-500">
                    Participants
                  </p>
                  <p className="flex items-center gap-2 text-2xl font-bold">
                    <Users className="h-5 w-5 text-zinc-400" />
                    {participants.length}
                  </p>
                </div>
              </div>
            )}
          </div>

          <div className="card p-6">
            <h2 className="mb-4 flex items-center justify-between text-sm font-semibold uppercase tracking-wider text-zinc-400">
              <span>Classement en direct</span>
              <span className="text-zinc-500">Top 10</span>
            </h2>
            <Leaderboard participants={participants} />
          </div>
        </div>
      </div>
    </div>
  );
}
