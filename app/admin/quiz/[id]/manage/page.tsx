import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import { createAdminClient } from "@/lib/supabase";
import { ManageClient } from "./ManageClient";
import type { Quiz, QuestionWithAnswers } from "@/types";

export const dynamic = "force-dynamic";

async function load(id: string) {
  const admin = createAdminClient();
  const { data: quiz } = await admin
    .from("quizzes")
    .select("*")
    .eq("id", id)
    .maybeSingle();
  if (!quiz) return null;
  const { data: questions } = await admin
    .from("questions")
    .select("*, answers(*)")
    .eq("quiz_id", id)
    .order("order_index", { ascending: true });
  return { quiz: quiz as Quiz, questions: (questions ?? []) as QuestionWithAnswers[] };
}

export default async function ManagePage({ params }: { params: { id: string } }) {
  const data = await load(params.id);
  if (!data) notFound();
  return (
    <div className="space-y-6">
      <Link
        href="/admin"
        className="inline-flex items-center gap-2 text-sm text-zinc-400 hover:text-zinc-200"
      >
        <ArrowLeft className="h-4 w-4" /> Retour aux quiz
      </Link>
      <ManageClient quiz={data.quiz} questions={data.questions} />
    </div>
  );
}
