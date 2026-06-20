"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { Loader2, Sparkles, ArrowRight, Hand } from "lucide-react";
import { StatusBadge } from "@/components/StatusBadge";
import type { Quiz } from "@/types";

export function JoinClient({ quiz, code }: { quiz: Quiz; code: string }) {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  if (quiz.status === "finished") {
    return (
      <div className="card w-full p-8 text-center space-y-3 animate-pop-in">
        <span className="mx-auto mb-1 flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-grape to-sky shadow-glow">
          <Sparkles className="h-6 w-6 text-white" />
        </span>
        <h1 className="text-xl font-bold">Quiz terminé</h1>
        <p className="text-sm text-zinc-400">
          Ce quiz s'est déjà terminé. Reviens lors du prochain.
        </p>
      </div>
    );
  }

  if (quiz.status === "draft") {
    return (
      <div className="card w-full p-8 text-center space-y-3 animate-pop-in">
        <span className="mx-auto mb-1 flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-primary to-accent-secondary shadow-glow animate-pulse-soft">
          <Sparkles className="h-6 w-6 text-white" />
        </span>
        <h1 className="text-xl font-bold">Quiz pas encore disponible</h1>
        <p className="text-sm text-zinc-400">
          L'organisateur n'a pas encore lancé ce quiz. Reste sur cette page et
          réessaye dans quelques instants.
        </p>
      </div>
    );
  }

  const submit = async () => {
    setError(null);
    const clean = username.trim();
    if (!clean) {
      setError("Choisis un pseudo");
      return;
    }
    setBusy(true);
    try {
      const res = await fetch(`/api/join/${code}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: clean }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error ?? "Erreur");
      sessionStorage.setItem(
        `quizlive:${code}`,
        JSON.stringify({
          participant_id: data.participant.id,
          username: clean,
        }),
      );
      router.push(`/live/${code}/play`);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="w-full space-y-7">
      <div className="text-center animate-slide-up">
        <span className="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-3xl bg-gradient-to-br from-accent-primary to-accent-secondary shadow-glow-lg animate-float">
          <Sparkles className="h-7 w-7 text-white" />
        </span>
        <h1 className="flex items-center justify-center gap-2 text-3xl font-extrabold leading-tight gradient-text-animated">
          <Hand className="h-7 w-7 shrink-0 text-accent-glow" /> Bienvenue&nbsp;!
        </h1>
        <p className="mt-2 text-sm text-zinc-400">
          Tu es sur le point de rejoindre un quiz en direct.
        </p>
        <div className="mt-4 flex justify-center">
          <StatusBadge status={quiz.status} />
        </div>
      </div>

      <div className="card border-glow p-6 space-y-4 animate-slide-up delay-1">
        <div className="text-center">
          <h2 className="text-lg font-bold">Prêt à jouer&nbsp;?</h2>
          <p className="mt-1 text-sm text-zinc-400">
            Choisis ton pseudo pour rejoindre la partie. Le quiz démarrera dès que
            l'organisateur le lancera.
          </p>
        </div>
        <div>
          <label className="label">Ton pseudo</label>
          <input
            className="input text-center text-lg font-medium tracking-wide"
            placeholder="ex. Léa"
            value={username}
            maxLength={24}
            autoFocus
            inputMode="text"
            enterKeyHint="go"
            onChange={(e) => setUsername(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && submit()}
          />
        </div>
        {error && (
          <div className="animate-shake rounded-xl border border-red-500/40 bg-red-500/10 p-3 text-sm text-red-300">
            {error}
          </div>
        )}
        <button
          onClick={submit}
          disabled={busy}
          className="btn-primary w-full py-3.5 text-base"
        >
          {busy ? (
            <Loader2 className="h-5 w-5 animate-spin" />
          ) : (
            <>
              Rejoindre le quiz <ArrowRight className="h-5 w-5" />
            </>
          )}
        </button>
        <p className="text-center text-xs text-zinc-500">
          Code :{" "}
          <span className="font-mono tracking-[0.3em] text-accent-glow">
            {code}
          </span>
        </p>
      </div>
    </div>
  );
}
