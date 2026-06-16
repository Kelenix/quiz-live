"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import confetti from "canvas-confetti";
import { CheckCircle2, Loader2, Sparkles } from "lucide-react";
import { getBrowserClient } from "@/lib/supabase";
import { Timer } from "@/components/Timer";
import { Leaderboard } from "@/components/Leaderboard";
import { cn, questionTypeLabel } from "@/lib/utils";
import type {
  Participant,
  Quiz,
  QuestionWithAnswers,
} from "@/types";

interface StoredSession {
  participant_id: string;
  username: string;
}

export function PlayClient({
  quiz: initialQuiz,
  questions,
  code,
}: {
  quiz: Quiz;
  questions: QuestionWithAnswers[];
  code: string;
}) {
  const router = useRouter();
  const [quiz, setQuiz] = useState<Quiz>(initialQuiz);
  const [session, setSession] = useState<StoredSession | null>(null);
  const [participants, setParticipants] = useState<Participant[]>([]);
  const [selected, setSelected] = useState<string[]>([]);
  const [submitting, setSubmitting] = useState(false);
  const [submittedFor, setSubmittedFor] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<{
    points: number;
    is_correct: boolean;
    is_partial: boolean;
  } | null>(null);
  const questionStartedAt = useRef<number>(Date.now());
  const confettiFired = useRef(false);

  // Charge session locale
  useEffect(() => {
    const raw = sessionStorage.getItem(`quizlive:${code}`);
    if (!raw) {
      router.replace(`/live/${code}`);
      return;
    }
    try {
      setSession(JSON.parse(raw));
    } catch {
      router.replace(`/live/${code}`);
    }
  }, [code, router]);

  const currentQuestion = useMemo(
    () => questions[quiz.current_question_index] ?? null,
    [questions, quiz.current_question_index],
  );

  // Realtime subscriptions
  useEffect(() => {
    const sb = getBrowserClient();

    sb.from("participants")
      .select("*")
      .eq("quiz_id", quiz.id)
      .then(({ data }) => setParticipants((data ?? []) as Participant[]));

    const ch = sb
      .channel(`play-quiz-${quiz.id}`)
      .on(
        "postgres_changes",
        {
          event: "UPDATE",
          schema: "public",
          table: "quizzes",
          filter: `id=eq.${quiz.id}`,
        },
        (payload) => setQuiz(payload.new as Quiz),
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
      .subscribe();

    return () => {
      sb.removeChannel(ch);
    };
  }, [quiz.id]);

  // Réinitialise la sélection à chaque changement de question
  useEffect(() => {
    setSelected([]);
    setSubmittedFor(null);
    setFeedback(null);
    questionStartedAt.current = Date.now();
  }, [currentQuestion?.id]);

  // Confetti à l'écran de fin si on est dans le top 3
  useEffect(() => {
    if (quiz.status !== "finished" || confettiFired.current || !session) return;
    const sorted = [...participants].sort((a, b) => b.score - a.score);
    const myRank = sorted.findIndex((p) => p.id === session.participant_id);
    if (myRank >= 0 && myRank <= 2) {
      confettiFired.current = true;
      confetti({
        particleCount: 140,
        spread: 90,
        origin: { y: 0.6 },
        colors: ["#7c3aed", "#2563eb", "#a78bfa", "#22c55e", "#f59e0b"],
      });
    }
  }, [quiz.status, participants, session]);

  const toggle = (answerId: string) => {
    if (!currentQuestion) return;
    if (currentQuestion.type === "multiple") {
      setSelected((prev) =>
        prev.includes(answerId)
          ? prev.filter((id) => id !== answerId)
          : [...prev, answerId],
      );
    } else {
      setSelected([answerId]);
    }
  };

  const submit = async () => {
    if (!currentQuestion || !session || selected.length === 0) return;
    setSubmitting(true);
    try {
      const res = await fetch("/api/responses", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          participant_id: session.participant_id,
          question_id: currentQuestion.id,
          answer_ids: selected,
          elapsed_ms: Date.now() - questionStartedAt.current,
        }),
      });
      const data = await res.json();
      if (!res.ok && res.status !== 409) {
        throw new Error(data.error ?? "Erreur");
      }
      setSubmittedFor(currentQuestion.id);
      if (res.ok) {
        setFeedback({
          points: data.points,
          is_correct: data.is_correct,
          is_partial: data.is_partial,
        });
      }
    } catch (e: any) {
      alert(e.message);
    } finally {
      setSubmitting(false);
    }
  };

  if (!session) {
    return (
      <main className="flex min-h-screen items-center justify-center text-zinc-400">
        <Loader2 className="h-5 w-5 animate-spin" />
      </main>
    );
  }

  // === FINISHED ===
  if (quiz.status === "finished") {
    const sorted = [...participants].sort((a, b) => b.score - a.score);
    const me = sorted.find((p) => p.id === session.participant_id);
    const myRank = sorted.findIndex((p) => p.id === session.participant_id) + 1;
    return (
      <main className="mx-auto min-h-screen max-w-2xl px-6 py-10 animate-fade-in">
        <div className="space-y-6">
          <div className="text-center">
            <span className="mb-3 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-violet to-accent-blue shadow-glow">
              <Sparkles className="h-5 w-5 text-white" />
            </span>
            <h1 className="text-3xl font-bold">Quiz terminé</h1>
            <p className="mt-1 text-sm text-zinc-400">{quiz.title}</p>
          </div>

          {me && (
            <div className="card p-6 text-center">
              <p className="text-xs uppercase tracking-widest text-zinc-400">
                Ton score
              </p>
              <p className="my-2 text-5xl font-bold text-accent-glow">
                {me.score}
              </p>
              <p className="text-sm text-zinc-400">
                Position {myRank} / {sorted.length}
              </p>
              {myRank >= 1 && myRank <= 3 && (
                <p className="mt-3 text-sm font-medium text-emerald-300">
                  {myRank === 1
                    ? "Bravo, tu remportes ce quiz !"
                    : myRank === 2
                      ? "Excellent — médaille d'argent !"
                      : "Beau podium — médaille de bronze !"}
                </p>
              )}
            </div>
          )}

          <div className="card p-6">
            <h2 className="mb-4 text-sm font-semibold uppercase tracking-wider text-zinc-400">
              Classement final
            </h2>
            <Leaderboard
              participants={participants}
              highlightId={session.participant_id}
            />
          </div>
        </div>
      </main>
    );
  }

  // === WAITING ===
  if (quiz.status === "waiting") {
    return (
      <main className="mx-auto min-h-screen max-w-md px-6 py-10">
        <div className="space-y-6 text-center animate-fade-in">
          <span className="mb-3 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-violet to-accent-blue shadow-glow animate-pulse-soft">
            <Sparkles className="h-5 w-5 text-white" />
          </span>
          <div>
            <h1 className="text-xl font-bold">En attente du lancement…</h1>
            <p className="mt-1 text-sm text-zinc-400">
              {quiz.title}
            </p>
            <p className="mt-2 text-xs text-zinc-500">
              Connecté en tant que{" "}
              <span className="font-mono text-accent-glow">
                {session.username}
              </span>
            </p>
          </div>

          <div className="card p-6 text-left">
            <h2 className="mb-3 text-xs font-semibold uppercase tracking-wider text-zinc-400">
              Participants ({participants.length})
            </h2>
            <ul className="space-y-2">
              {[...participants]
                .sort((a, b) => a.joined_at.localeCompare(b.joined_at))
                .map((p) => (
                  <li
                    key={p.id}
                    className={cn(
                      "flex items-center gap-2 rounded-lg border border-bg-border bg-bg-soft/30 px-3 py-2 text-sm",
                      p.id === session.participant_id &&
                        "border-accent-violet/60",
                    )}
                  >
                    <span className="h-2 w-2 rounded-full bg-emerald-400" />
                    {p.username}
                    {p.id === session.participant_id && (
                      <span className="ml-auto text-xs text-accent-glow">vous</span>
                    )}
                  </li>
                ))}
            </ul>
            {participants.length === 0 && (
              <p className="text-sm text-zinc-500">Tu es le premier ici.</p>
            )}
          </div>
        </div>
      </main>
    );
  }

  // === LIVE ===
  if (!currentQuestion) {
    return (
      <main className="flex min-h-screen items-center justify-center text-zinc-400">
        <Loader2 className="h-5 w-5 animate-spin" />
      </main>
    );
  }

  const hasSubmitted = submittedFor === currentQuestion.id;
  const totalQuestions = questions.length;

  return (
    <main className="mx-auto min-h-screen max-w-2xl px-6 py-10">
      <div className="space-y-6 animate-fade-in">
        <div className="flex items-center justify-between text-xs text-zinc-500">
          <span>
            Question {quiz.current_question_index + 1} / {totalQuestions}
          </span>
          <span className="font-mono text-accent-glow">{session.username}</span>
        </div>

        <div className="card p-6 space-y-5">
          <div>
            <span className="chip border-bg-border bg-bg-soft text-zinc-300">
              {questionTypeLabel(currentQuestion.type)}
            </span>
            <h1 className="mt-3 text-xl font-semibold leading-snug">
              {currentQuestion.statement}
            </h1>
          </div>

          {currentQuestion.time_limit && !hasSubmitted && (
            <Timer
              seconds={currentQuestion.time_limit}
              resetKey={currentQuestion.id}
              onExpire={() => {
                if (selected.length > 0 && !submitting) submit();
              }}
            />
          )}

          <div className="space-y-2">
            {currentQuestion.answers.map((a) => {
              const checked = selected.includes(a.id);
              return (
                <button
                  key={a.id}
                  type="button"
                  disabled={hasSubmitted}
                  onClick={() => toggle(a.id)}
                  className={cn(
                    "w-full rounded-xl border px-4 py-3 text-left transition",
                    checked
                      ? "border-accent-violet/60 bg-accent-violet/15 text-white shadow-glow"
                      : "border-bg-border bg-bg-soft/40 hover:border-accent-violet/40 hover:bg-bg-soft",
                    hasSubmitted && "opacity-60",
                  )}
                >
                  <div className="flex items-center gap-3">
                    <span
                      className={cn(
                        "flex h-5 w-5 shrink-0 items-center justify-center border-2",
                        currentQuestion.type === "multiple"
                          ? "rounded-md"
                          : "rounded-full",
                        checked
                          ? "border-accent-glow bg-accent-glow"
                          : "border-zinc-500",
                      )}
                    >
                      {checked && (
                        <CheckCircle2 className="h-3 w-3 text-bg" />
                      )}
                    </span>
                    <span className="flex-1 text-sm">{a.text}</span>
                  </div>
                </button>
              );
            })}
          </div>

          {!hasSubmitted ? (
            <button
              onClick={submit}
              disabled={selected.length === 0 || submitting}
              className="btn-primary w-full"
            >
              {submitting ? (
                <Loader2 className="h-4 w-4 animate-spin" />
              ) : (
                "Valider ma réponse"
              )}
            </button>
          ) : (
            <div
              className={cn(
                "rounded-xl border p-4 text-center text-sm",
                feedback?.is_correct
                  ? "border-emerald-500/40 bg-emerald-500/10 text-emerald-200"
                  : feedback?.is_partial
                    ? "border-amber-500/40 bg-amber-500/10 text-amber-200"
                    : feedback
                      ? "border-bg-border bg-bg-soft/40 text-zinc-300"
                      : "border-bg-border bg-bg-soft/40 text-zinc-300",
              )}
            >
              {feedback ? (
                <>
                  <p className="font-semibold">
                    {feedback.is_correct
                      ? "Bonne réponse !"
                      : feedback.is_partial
                        ? "Presque ! Réponse partielle."
                        : "Pas tout à fait."}
                    {feedback.points > 0 && ` +${feedback.points} pts`}
                  </p>
                  <p className="mt-1 text-xs text-zinc-400">
                    En attente de la prochaine question…
                  </p>
                </>
              ) : (
                <p>Réponse enregistrée, en attente de la prochaine question…</p>
              )}
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
