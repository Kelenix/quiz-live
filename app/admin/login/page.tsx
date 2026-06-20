"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Lock, ArrowRight } from "lucide-react";

export default function AdminLoginPage() {
  const router = useRouter();
  const [password, setPassword] = useState("");
  const [from, setFrom] = useState("/admin");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    const p = new URLSearchParams(window.location.search).get("from");
    if (p && p.startsWith("/admin")) setFrom(p);
  }, []);

  const submit = async () => {
    setError(null);
    if (!password) {
      setError("Saisis le mot de passe");
      return;
    }
    setBusy(true);
    try {
      const res = await fetch("/api/admin/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error ?? "Erreur");
      router.replace(from);
      router.refresh();
    } catch (e: any) {
      setError(e.message);
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="mx-auto flex min-h-[70vh] max-w-sm flex-col items-center justify-center">
      <div className="w-full space-y-6 animate-slide-up">
        <div className="text-center">
          <span className="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-3xl bg-gradient-to-br from-accent-primary to-accent-secondary shadow-glow-lg animate-float">
            <Lock className="h-7 w-7 text-white" />
          </span>
          <h1 className="text-2xl font-extrabold gradient-text-animated">
            Espace administrateur
          </h1>
          <p className="mt-2 text-sm text-zinc-400">
            Accès réservé. Saisis le mot de passe pour continuer.
          </p>
        </div>

        <div className="card border-glow p-6 space-y-4">
          <div>
            <label className="label">Mot de passe</label>
            <input
              type="password"
              className="input"
              placeholder="••••••••"
              value={password}
              autoFocus
              enterKeyHint="go"
              onChange={(e) => setPassword(e.target.value)}
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
                Se connecter <ArrowRight className="h-5 w-5" />
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
