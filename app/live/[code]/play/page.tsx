import { notFound } from "next/navigation";
import { createAdminClient } from "@/lib/supabase";
import { PlayClient } from "./PlayClient";
import type { Quiz, QuestionWithAnswers } from "@/types";

export const dynamic = "force-dynamic";

async function load(code: string) {
  const admin = createAdminClient();
  const { data: quiz } = await admin
    .from("quizzes")
    .select("*")
    .eq("join_code", code.toUpperCase())
    .maybeSingle();
  if (!quiz) return null;
  const { data: questions } = await admin
    .from("questions")
    .select("id, quiz_id, statement, type, time_limit, order_index, answers(id, question_id, text)")
    .eq("quiz_id", quiz.id)
    .order("order_index", { ascending: true });
  // Note : on n'expose pas is_correct aux participants (sécurité).
  const safeQuestions = (questions ?? []).map((q: any) => ({
    id: q.id,
    quiz_id: q.quiz_id,
    statement: q.statement,
    type: q.type,
    time_limit: q.time_limit,
    order_index: q.order_index,
    answers: (q.answers ?? []).map((a: any) => ({
      id: a.id,
      question_id: a.question_id,
      text: a.text,
      is_correct: false,
    })),
  })) as QuestionWithAnswers[];
  return { quiz: quiz as Quiz, questions: safeQuestions };
}

export default async function PlayPage({
  params,
}: {
  params: { code: string };
}) {
  const data = await load(params.code);
  if (!data) notFound();
  return (
    <PlayClient
      quiz={data.quiz}
      questions={data.questions}
      code={params.code.toUpperCase()}
    />
  );
}
