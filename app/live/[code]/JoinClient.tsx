"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { Loader2, Sparkles } from "lucide-react";
import { StatusBadge } from "@/components/StatusBadge";
import type { Quiz } from "@/types";

export function JoinClient({ quiz, code }: { quiz: Quiz; code: string }) {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  if (quiz.status === "finished") {
    return (
      <div className="card w-full p-8 text-center space-y-3 animate-fade-in">
        <h1 className="text-xl font-bold">Quiz terminé</h1>
        <p className="text-sm text-zinc-400">
          Ce quiz s'est déjà terminé. Reviens lors du prochain.
        </p>
      </div>
    );
  }

  if (quiz.status === "draft") {
    return (
      <div className="card w-full p-8 text-center space-y-3 animate-fade-in">
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
      // Stocke localement (par code) pour reconnecter sur la page play.
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
    <div className="w-full space-y-6 animate-fade-in">
      <div className="text-center">
        <span className="mb-3 inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-violet to-accent-blue shadow-glow">
          <Sparkles className="h-5 w-5 text-white" />
        </span>
        <h1 className="text-2xl font-bold">{quiz.title}</h1>
        {quiz.description && (
          <p className="mt-1 text-sm text-zinc-400">{quiz.description}</p>
        )}
        <div className="mt-3 flex justify-center">
          <StatusBadge status={quiz.status} />
        </div>
      </div>

      <div className="card p-6 space-y-4">
        <div>
          <label className="label">Ton pseudo</label>
          <input
            className="input text-center text-base"
            placeholder="ex. Léa"
            value={username}
            maxLength={24}
            autoFocus
            onChange={(e) => setUsername(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && submit()}
          />
        </div>
        {error && (
          <div className="rounded-xl border border-red-500/40 bg-red-500/10 p-3 text-sm text-red-300">
            {error}
          </div>
        )}
        <button onClick={submit} disabled={busy} className="btn-primary w-full">
          {busy ? <Loader2 className="h-4 w-4 animate-spin" /> : "Rejoindre le quiz"}
        </button>
        <p className="text-center text-xs text-zinc-500">
          Code :{" "}
          <span className="font-mono tracking-widest text-accent-glow">{code}</span>
        </p>
      </div>
    </div>
  );
}
