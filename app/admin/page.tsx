import Link from "next/link";
import { createAdminClient } from "@/lib/supabase";
import { StatusBadge } from "@/components/StatusBadge";
import { Plus, ChevronLeft, ChevronRight } from "lucide-react";
import { AdminQuizRowActions } from "./AdminQuizRowActions";
import type { Quiz, QuizCategory } from "@/types";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";
export const revalidate = 0;

const CATEGORIES: QuizCategory[] = ["HTML", "CSS", "JS", "Java", "Python", "SQL"];
const PAGE_SIZE = 25;

type SearchParams = { category?: string; page?: string };

async function getCategoryCounts(): Promise<Record<string, number>> {
  const admin = createAdminClient();
  const { data, error } = await admin.from("quizzes").select("category");
  if (error) throw error;
  const counts: Record<string, number> = {};
  for (const row of data as { category: string }[]) {
    counts[row.category] = (counts[row.category] ?? 0) + 1;
  }
  counts.all = (data as unknown[]).length;
  return counts;
}

async function getQuizzes(
  category: string,
  page: number,
): Promise<{ quizzes: Quiz[]; total: number }> {
  const admin = createAdminClient();
  let query = admin
    .from("quizzes")
    .select("*", { count: "exact" })
    .order("created_at", { ascending: false });

  if (category !== "all") query = query.eq("category", category);

  const from = (page - 1) * PAGE_SIZE;
  const { data, error, count } = await query.range(from, from + PAGE_SIZE - 1);
  if (error) throw error;
  return { quizzes: data as Quiz[], total: count ?? 0 };
}

function buildHref(category: string, page: number): string {
  const params = new URLSearchParams();
  if (category !== "all") params.set("category", category);
  if (page > 1) params.set("page", String(page));
  const qs = params.toString();
  return qs ? `/admin?${qs}` : "/admin";
}

export default async function AdminHome({
  searchParams,
}: {
  searchParams: SearchParams;
}) {
  const category =
    searchParams.category && CATEGORIES.includes(searchParams.category as QuizCategory)
      ? searchParams.category
      : "all";
  const page = Math.max(1, parseInt(searchParams.page ?? "1", 10) || 1);

  const [counts, { quizzes, total }] = await Promise.all([
    getCategoryCounts(),
    getQuizzes(category, page),
  ]);

  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));
  const start = total === 0 ? 0 : (page - 1) * PAGE_SIZE + 1;
  const end = Math.min(page * PAGE_SIZE, total);

  const tabs: { key: string; label: string }[] = [
    { key: "all", label: "Tous" },
    ...CATEGORIES.map((c) => ({ key: c, label: c })),
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold">Mes quiz</h1>
          <p className="text-sm text-zinc-400">{counts.all ?? 0} quiz au total</p>
        </div>
        <Link href="/admin/quiz/new" className="btn-primary">
          <Plus className="h-4 w-4" /> Créer un quiz
        </Link>
      </div>

      {/* Filtres par catégorie */}
      <div className="flex flex-wrap gap-2">
        {tabs.map((tab) => {
          const active = category === tab.key;
          return (
            <Link
              key={tab.key}
              href={buildHref(tab.key, 1)}
              className={`chip border transition-colors ${
                active
                  ? "border-accent-primary bg-accent-primary/15 text-accent-glow"
                  : "border-bg-border bg-bg-soft text-zinc-300 hover:border-zinc-600"
              }`}
            >
              {tab.label}
              <span className="ml-1.5 text-xs text-zinc-500">
                {counts[tab.key] ?? 0}
              </span>
            </Link>
          );
        })}
      </div>

      {quizzes.length === 0 ? (
        <div className="card flex flex-col items-center gap-3 p-12 text-center">
          <p className="text-zinc-300">Aucun quiz dans cette catégorie.</p>
          <Link href="/admin/quiz/new" className="btn-primary">
            <Plus className="h-4 w-4" /> Créer ton premier quiz
          </Link>
        </div>
      ) : (
        <>
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
                      <span className="font-mono text-accent-glow">{q.join_code}</span>
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

          {/* Pagination */}
          <div className="flex flex-col items-center justify-between gap-3 sm:flex-row">
            <p className="text-sm text-zinc-500">
              {start}–{end} sur {total} quiz
            </p>
            <div className="flex items-center gap-2">
              {page > 1 ? (
                <Link
                  href={buildHref(category, page - 1)}
                  className="chip border border-bg-border bg-bg-soft text-zinc-300 hover:border-zinc-600"
                >
                  <ChevronLeft className="h-4 w-4" /> Précédent
                </Link>
              ) : (
                <span className="chip border border-bg-border bg-bg-soft text-zinc-600 opacity-50">
                  <ChevronLeft className="h-4 w-4" /> Précédent
                </span>
              )}
              <span className="text-sm text-zinc-400">
                Page {page} / {totalPages}
              </span>
              {page < totalPages ? (
                <Link
                  href={buildHref(category, page + 1)}
                  className="chip border border-bg-border bg-bg-soft text-zinc-300 hover:border-zinc-600"
                >
                  Suivant <ChevronRight className="h-4 w-4" />
                </Link>
              ) : (
                <span className="chip border border-bg-border bg-bg-soft text-zinc-600 opacity-50">
                  Suivant <ChevronRight className="h-4 w-4" />
                </span>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
}
