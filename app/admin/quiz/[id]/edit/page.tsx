import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import { createAdminClient } from "@/lib/supabase";
import { QuizForm } from "@/components/QuizForm";
import type { QuizDraft } from "@/types";

export const dynamic = "force-dynamic";

async function loadDraft(id: string): Promise<QuizDraft | null> {
  const admin = createAdminClient();
  const { data: quiz } = await admin
    .from("quizzes")
    .select("*, questions(*, answers(*))")
    .eq("id", id)
    .maybeSingle();
  if (!quiz) return null;
  const questions = (quiz.questions ?? [])
    .sort((a: any, b: any) => a.order_index - b.order_index)
    .map((q: any, i: number) => ({
      id: q.id,
      statement: q.statement,
      type: q.type,
      time_limit: q.time_limit,
      order_index: i,
      answers: (q.answers ?? []).map((a: any) => ({
        id: a.id,
        text: a.text,
        is_correct: a.is_correct,
      })),
    }));
  return {
    title: quiz.title,
    category: quiz.category,
    description: quiz.description ?? "",
    questions,
  };
}

export default async function EditQuizPage({ params }: { params: { id: string } }) {
  const draft = await loadDraft(params.id);
  if (!draft) notFound();
  return (
    <div className="space-y-6">
      <Link href="/admin" className="inline-flex items-center gap-2 text-sm text-zinc-400 hover:text-zinc-200">
        <ArrowLeft className="h-4 w-4" /> Retour aux quiz
      </Link>
      <div>
        <h1 className="text-2xl font-bold">Modifier le quiz</h1>
        <p className="text-sm text-zinc-400">
          Tu modifies « {draft.title} ». Les questions seront remplacées par la nouvelle version.
        </p>
      </div>
      <QuizForm initial={draft} quizId={params.id} />
    </div>
  );
}
