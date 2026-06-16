"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { Edit2, Trash2, Play, Settings, ExternalLink } from "lucide-react";
import type { Quiz } from "@/types";

export function AdminQuizRowActions({ quiz }: { quiz: Quiz }) {
  const router = useRouter();
  const [busy, setBusy] = useState(false);

  const remove = async () => {
    if (!confirm(`Supprimer "${quiz.title}" ? Cette action est irréversible.`)) return;
    setBusy(true);
    try {
      const res = await fetch(`/api/quizzes/${quiz.id}`, { method: "DELETE" });
      if (!res.ok) throw new Error("Erreur suppression");
      router.refresh();
    } catch (e: any) {
      alert(e.message);
    } finally {
      setBusy(false);
    }
  };

  const launch = async () => {
    setBusy(true);
    try {
      const res = await fetch(`/api/quizzes/${quiz.id}/start`, { method: "POST" });
      if (!res.ok) throw new Error("Erreur lancement");
      router.push(`/admin/quiz/${quiz.id}/manage`);
    } catch (e: any) {
      alert(e.message);
      setBusy(false);
    }
  };

  return (
    <div className="flex flex-wrap items-center gap-2">
      <Link
        href={`/live/${quiz.join_code}`}
        target="_blank"
        className="btn-ghost !px-3"
        title="Ouvrir le lien participant"
      >
        <ExternalLink className="h-4 w-4" />
      </Link>
      <Link
        href={`/admin/quiz/${quiz.id}/edit`}
        className="btn-ghost !px-3"
        title="Modifier"
      >
        <Edit2 className="h-4 w-4" />
      </Link>
      <button
        onClick={remove}
        disabled={busy}
        className="btn-danger !px-3"
        title="Supprimer"
      >
        <Trash2 className="h-4 w-4" />
      </button>
      {quiz.status === "draft" && (
        <button onClick={launch} disabled={busy} className="btn-primary !px-3">
          <Play className="h-4 w-4" /> Lancer
        </button>
      )}
      {quiz.status !== "draft" && (
        <Link
          href={`/admin/quiz/${quiz.id}/manage`}
          className="btn-primary !px-3"
        >
          <Settings className="h-4 w-4" /> Gérer
        </Link>
      )}
    </div>
  );
}
