import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import type { QuizDraft } from "@/types";

export const dynamic = "force-dynamic";

export async function PUT(req: Request, { params }: { params: { id: string } }) {
  try {
    const body = (await req.json()) as QuizDraft;
    const admin = createAdminClient();

    const { error: eu } = await admin
      .from("quizzes")
      .update({
        title: body.title.trim(),
        category: body.category,
        description: body.description?.trim() || null,
      })
      .eq("id", params.id);
    if (eu) throw eu;

    // Stratégie simple : on supprime les questions (cascade supprime les answers/responses)
    // et on réinsère. C'est sain pour un éditeur de quiz.
    const { error: ed } = await admin
      .from("questions")
      .delete()
      .eq("quiz_id", params.id);
    if (ed) throw ed;

    for (let i = 0; i < body.questions.length; i++) {
      const q = body.questions[i];
      const { data: qRow, error: eq } = await admin
        .from("questions")
        .insert({
          quiz_id: params.id,
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

    return NextResponse.json({ ok: true });
  } catch (e: any) {
    return NextResponse.json(
      { error: e.message ?? "Erreur serveur" },
      { status: 500 },
    );
  }
}

export async function DELETE(_req: Request, { params }: { params: { id: string } }) {
  try {
    const admin = createAdminClient();
    const { error } = await admin.from("quizzes").delete().eq("id", params.id);
    if (error) throw error;
    return NextResponse.json({ ok: true });
  } catch (e: any) {
    return NextResponse.json(
      { error: e.message ?? "Erreur serveur" },
      { status: 500 },
    );
  }
}
