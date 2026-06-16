import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";

export const dynamic = "force-dynamic";

/**
 * Question suivante. Si déjà à la dernière question, passe en "finished".
 */
export async function POST(_req: Request, { params }: { params: { id: string } }) {
  try {
    const admin = createAdminClient();

    const { data: quiz, error: e1 } = await admin
      .from("quizzes")
      .select("id, current_question_index, status")
      .eq("id", params.id)
      .single();
    if (e1) throw e1;

    const { count, error: e2 } = await admin
      .from("questions")
      .select("id", { count: "exact", head: true })
      .eq("quiz_id", params.id);
    if (e2) throw e2;

    const total = count ?? 0;
    const nextIdx = quiz.current_question_index + 1;

    if (nextIdx >= total) {
      const { error } = await admin
        .from("quizzes")
        .update({ status: "finished" })
        .eq("id", params.id);
      if (error) throw error;
      return NextResponse.json({ ok: true, finished: true });
    }

    const { error } = await admin
      .from("quizzes")
      .update({ current_question_index: nextIdx, status: "live" })
      .eq("id", params.id);
    if (error) throw error;
    return NextResponse.json({ ok: true, current_question_index: nextIdx });
  } catch (e: any) {
    return NextResponse.json({ error: e.message }, { status: 500 });
  }
}
