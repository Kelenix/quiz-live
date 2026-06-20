"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import confetti from "canvas-confetti";
import {
  CheckCircle2,
  Loader2,
  Sparkles,
  PartyPopper,
  Trophy,
} from "lucide-react";
import { getBrowserClient } from "@/lib/supabase";
import { Timer } from "@/components/Timer";
import { Leaderboard } from "@/components/Leaderboard";
import { cn, questionTypeLabel } from "@/lib/utils";
import type { Participant, Quiz, QuestionWithAnswers } from "@/types";

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
        particleCount: 160,
        spread: 95,
        origin: { y: 0.6 },
        colors: ["#3ecf8e", "#1f9d63", "#7ffbc4", "#38bdf8", "#a855f7", "#fbbf24"],
      });
    }
  }, [quiz.status, participants, session]);

  // Petit éclat de confetti quand on a une bonne réponse
  useEffect(() => {
    if (feedback?.is_correct) {
      confetti({
        particleCount: 60,
        spread: 70,
        startVelocity: 32,
        origin: { y: 0.7 },
        colors: ["#3ecf8e", "#7ffbc4", "#38bdf8", "#fbbf24"],
      });
    }
  }, [feedback]);

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
        <Loader2 className="h-6 w-6 animate-spin text-accent-primary" />
      </main>
    );
  }

  // === FINISHED ===
  if (quiz.status === "finished") {
    const sorted = [...participants].sort((a, b) => b.score - a.score);
    const me = sorted.find((p) => p.id === session.participant_id);
    const myRank = sorted.findIndex((p) => p.id === session.participant_id) + 1;
    const podium = myRank >= 1 && myRank <= 3;
    return (
      <main className="mx-auto min-h-screen max-w-2xl safe-px safe-pb py-10">
        <div className="space-y-6">
          <div className="text-center animate-slide-up">
            <span className="mb-3 inline-flex h-16 w-16 items-center justify-center rounded-3xl bg-gradient-to-br from-accent-primary to-accent-secondary shadow-glow-lg animate-float">
              {podium ? (
                <Trophy className="h-7 w-7 text-white" />
              ) : (
                <Sparkles className="h-7 w-7 text-white" />
              )}
            </span>
            <h1 className="text-3xl font-extrabold gradient-text-animated">
              Quiz terminé
            </h1>
            <p className="mt-1 text-sm text-zinc-400">{quiz.title}</p>
          </div>

          {me && (
            <div className="card border-glow p-6 text-center animate-pop-in">
              <p className="text-xs uppercase tracking-widest text-zinc-400">
                Ton score
              </p>
              <p className="my-2 text-6xl font-extrabold tabular-nums gradient-text animate-score-pop">
                {me.score}
              </p>
              <p className="text-sm text-zinc-400">
                Position {myRank} / {sorted.length}
              </p>
              {podium && (
                <p className="mt-3 inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-gold/20 to-accent-primary/20 px-4 py-1.5 text-sm font-semibold text-emerald-200">
                  <PartyPopper className="h-4 w-4" />
                  {myRank === 1
                    ? "Bravo, tu remportes ce quiz !"
                    : myRank === 2
                      ? "Excellent — médaille d'argent !"
                      : "Beau podium — médaille de bronze !"}
                </p>
              )}
            </div>
          )}

          <div className="card p-6 animate-slide-up delay-2">
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
      <main className="mx-auto min-h-screen max-w-md safe-px safe-pb py-10">
        <div className="space-y-6 text-center animate-slide-up">
          <span className="inline-flex h-16 w-16 items-center justify-center rounded-3xl bg-gradient-to-br from-accent-primary to-accent-secondary shadow-glow-lg animate-pulse-soft">
            <Sparkles className="h-7 w-7 text-white" />
          </span>
          <div>
            <h1 className="text-2xl font-extrabold gradient-text-animated">
              En attente du lancement…
            </h1>
            <p className="mt-1 text-sm text-zinc-400">{quiz.title}</p>
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
                .map((p, idx) => (
                  <li
                    key={p.id}
                    style={{ animationDelay: `${Math.min(idx, 8) * 50}ms` }}
                    className={cn(
                      "flex animate-slide-up items-center gap-2 rounded-lg border border-bg-border bg-bg-soft/30 px-3 py-2.5 text-sm",
                      p.id === session.participant_id &&
                        "border-accent-primary/60 bg-accent-primary/10",
                    )}
                  >
                    <span className="relative flex h-2.5 w-2.5">
                      <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400/70" />
                      <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-emerald-400" />
                    </span>
                    {p.username}
                    {p.id === session.participant_id && (
                      <span className="ml-auto text-xs text-accent-glow">
                        vous
                      </span>
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
        <Loader2 className="h-6 w-6 animate-spin text-accent-primary" />
      </main>
    );
  }

  const hasSubmitted = submittedFor === currentQuestion.id;
  const totalQuestions = questions.length;
  const progressPct = ((quiz.current_question_index + 1) / totalQuestions) * 100;

  return (
    <main className="mx-auto min-h-screen max-w-2xl safe-px safe-pb py-8">
      <div className="space-y-5">
        {/* En-tête + progression */}
        <div className="space-y-2 animate-fade-in">
          <div className="flex items-center justify-between text-xs text-zinc-500">
            <span className="font-medium">
              Question {quiz.current_question_index + 1} / {totalQuestions}
            </span>
            <span className="font-mono text-accent-glow">{session.username}</span>
          </div>
          <div className="h-1.5 w-full overflow-hidden rounded-full bg-bg-border">
            <div
              className="h-full rounded-full bg-gradient-to-r from-accent-glow via-accent-primary to-accent-secondary transition-all duration-500 ease-out"
              style={{ width: `${progressPct}%` }}
            />
          </div>
        </div>

        {/* Carte question (re-anime à chaque question grâce à la key) */}
        <div
          key={currentQuestion.id}
          className="card border-glow p-5 sm:p-6 space-y-5 animate-slide-up"
        >
          <div>
            <span className="chip border-accent-primary/30 bg-accent-primary/10 text-accent-glow">
              {questionTypeLabel(currentQuestion.type)}
            </span>
            <h1 className="mt-3 text-xl font-bold leading-snug sm:text-2xl">
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

          <div className="space-y-2.5">
            {currentQuestion.answers.map((a, idx) => {
              const checked = selected.includes(a.id);
              return (
                <button
                  key={a.id}
                  type="button"
                  disabled={hasSubmitted}
                  onClick={() => toggle(a.id)}
                  style={{ animationDelay: `${idx * 55}ms` }}
                  className={cn(
                    "group w-full animate-slide-up touch-manipulation rounded-2xl border px-4 py-4 text-left transition-all active:scale-[.98]",
                    checked
                      ? "border-accent-primary bg-accent-primary/15 text-white shadow-glow"
                      : "border-bg-border bg-bg-soft/40 hover:border-accent-primary/50 hover:bg-bg-soft",
                    hasSubmitted && "opacity-60",
                  )}
                >
                  <div className="flex items-center gap-3">
                    <span
                      className={cn(
                        "flex h-6 w-6 shrink-0 items-center justify-center border-2 transition-all",
                        currentQuestion.type === "multiple"
                          ? "rounded-md"
                          : "rounded-full",
                        checked
                          ? "scale-110 border-accent-glow bg-accent-glow"
                          : "border-zinc-500 group-hover:border-accent-primary/60",
                      )}
                    >
                      {checked && (
                        <CheckCircle2 className="h-4 w-4 animate-pop-in text-bg" />
                      )}
                    </span>
                    <span className="flex-1 text-base">{a.text}</span>
                  </div>
                </button>
              );
            })}
          </div>

          {!hasSubmitted ? (
            <button
              onClick={submit}
              disabled={selected.length === 0 || submitting}
              className="btn-primary w-full py-4 text-base"
            >
              {submitting ? (
                <Loader2 className="h-5 w-5 animate-spin" />
              ) : (
                "Valider ma réponse"
              )}
            </button>
          ) : (
            <div
              className={cn(
                "animate-pop-in rounded-2xl border p-4 text-center text-sm",
                feedback?.is_correct
                  ? "border-emerald-500/40 bg-emerald-500/10 text-emerald-200"
                  : feedback?.is_partial
                    ? "border-amber-500/40 bg-amber-500/10 text-amber-200"
                    : "border-bg-border bg-bg-soft/40 text-zinc-300",
              )}
            >
              {feedback ? (
                <>
                  <p className="flex items-center justify-center gap-2 text-base font-bold">
                    {feedback.is_correct ? (
                      <PartyPopper className="h-5 w-5" />
                    ) : null}
                    {feedback.is_correct
                      ? "Bonne réponse !"
                      : feedback.is_partial
                        ? "Presque ! Réponse partielle."
                        : "Pas tout à fait."}
                    {feedback.points > 0 && (
                      <span className="font-mono">+{feedback.points} pts</span>
                    )}
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
