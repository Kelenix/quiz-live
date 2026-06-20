import { notFound } from "next/navigation";
import { createAdminClient } from "@/lib/supabase";
import { JoinClient } from "./JoinClient";
import type { Quiz } from "@/types";

export const dynamic = "force-dynamic";

async function getQuiz(code: string): Promise<Quiz | null> {
  const admin = createAdminClient();
  const { data } = await admin
    .from("quizzes")
    .select("*")
    .eq("join_code", code.toUpperCase())
    .maybeSingle();
  return (data as Quiz) ?? null;
}

export default async function JoinPage({
  params,
}: {
  params: { code: string };
}) {
  const quiz = await getQuiz(params.code);
  if (!quiz) {
    return (
      <main className="mx-auto flex min-h-screen max-w-md flex-col items-center justify-center safe-px py-10">
        <div className="card w-full p-8 text-center space-y-3 animate-pop-in">
          <h1 className="text-xl font-bold">Quiz introuvable</h1>
          <p className="text-sm text-zinc-400">
            Le code <span className="font-mono">{params.code}</span> ne correspond à aucun quiz.
            Vérifie le code auprès de l'organisateur.
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="mx-auto flex min-h-screen max-w-md flex-col items-center justify-center safe-px py-10">
      <JoinClient quiz={quiz} code={params.code.toUpperCase()} />
    </main>
  );
}
