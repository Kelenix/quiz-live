import Link from "next/link";
import { createAdminClient } from "@/lib/supabase";
import { StatusBadge } from "@/components/StatusBadge";
import { Plus } from "lucide-react";
import { AdminQuizRowActions } from "./AdminQuizRowActions";
import type { Quiz } from "@/types";

export const dynamic = "force-dynamic";

async function getQuizzes(): Promise<Quiz[]> {
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("quizzes")
    .select("*")
    .order("created_at", { ascending: false });
  if (error) throw error;
  return data as Quiz[];
}

export default async function AdminHome() {
  const quizzes = await getQuizzes();

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Mes quiz</h1>
          <p className="text-sm text-zinc-400">
            {quizzes.length} quiz au total
          </p>
        </div>
        <Link href="/admin/quiz/new" className="btn-primary">
          <Plus className="h-4 w-4" /> Créer un quiz
        </Link>
      </div>

      {quizzes.length === 0 ? (
        <div className="card flex flex-col items-center gap-3 p-12 text-center">
          <p className="text-zinc-300">Aucun quiz pour le moment.</p>
          <Link href="/admin/quiz/new" className="btn-primary">
            <Plus className="h-4 w-4" /> Créer ton premier quiz
          </Link>
        </div>
      ) : (
        <div className="card divide-y divide-bg-border">
          {quizzes.map((q) => (
            <div
              key={q.id}
              className="flex flex-col gap-3 px-5 py-4 sm:flex-row sm:items-center sm:justify-between"
            >
              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-3">
                  <h3 className="truncate text-base font-semibold">{q.title}</h3>
                  <StatusBadge status={q.status} />
                </div>
                <p className="mt-1 flex items-center gap-3 text-xs text-zinc-500">
                  <span className="chip border-bg-border bg-bg-soft text-zinc-300">
                    {q.category}
                  </span>
                  <span>
                    Code :{" "}
                    <span className="font-mono text-accent-glow">
                      {q.join_code}
                    </span>
                  </span>
                  <span className="hidden sm:inline">
                    {new Date(q.created_at).toLocaleDateString("fr-FR")}
                  </span>
                </p>
              </div>
              <AdminQuizRowActions quiz={q} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
