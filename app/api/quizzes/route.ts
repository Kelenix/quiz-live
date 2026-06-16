import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { generateJoinCode } from "@/lib/utils";
import type { QuizDraft } from "@/types";

export const dynamic = "force-dynamic";

async function uniqueJoinCode(admin: ReturnType<typeof createAdminClient>) {
  for (let i = 0; i < 8; i++) {
    const code = generateJoinCode();
    const { data, error } = await admin
      .from("quizzes")
      .select("id")
      .eq("join_code", code)
      .maybeSingle();
    if (error) throw error;
    if (!data) return code;
  }
  throw new Error("Impossible de générer un code unique");
}

export async function POST(req: Request) {
  try {
    const body = (await req.json()) as QuizDraft;
    if (!body?.title?.trim()) {
      return NextResponse.json({ error: "Titre requis" }, { status: 400 });
    }
    const admin = createAdminClient();
    const code = await uniqueJoinCode(admin);

    const { data: quiz, error: e1 } = await admin
      .from("quizzes")
      .insert({
        title: body.title.trim(),
        category: body.category,
        description: body.description?.trim() || null,
        join_code: code,
        status: "draft",
      })
      .select("*")
      .single();
    if (e1) throw e1;

    // Insère les questions une par une pour récupérer les ids, puis les réponses
    for (let i = 0; i < body.questions.length; i++) {
      const q = body.questions[i];
      const { data: qRow, error: eq } = await admin
        .from("questions")
        .insert({
          quiz_id: quiz.id,
          statement: q.statement.trim(),
          type: q.type,
          time_limit: q.time_limit,
          order_index: i,
        })
        .select("id")
        .single();
      if (eq) throw eq;

      const answersPayload = q.answers.map((a) => ({
        question_id: qRow.id,
        text: a.text.trim(),
        is_correct: !!a.is_correct,
      }));
      const { error: ea } = await admin.from("answers").insert(answersPayload);
      if (ea) throw ea;
    }

    return NextResponse.json({ id: quiz.id, join_code: quiz.join_code });
  } catch (e: any) {
    return NextResponse.json(
      { error: e.message ?? "Erreur serveur" },
      { status: 500 },
    );
  }
}
