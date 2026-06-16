import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";

export const dynamic = "force-dynamic";

/**
 * Ouvre la salle d'attente (status -> waiting). Les participants peuvent rejoindre.
 */
export async function POST(_req: Request, { params }: { params: { id: string } }) {
  try {
    const admin = createAdminClient();
    const { error } = await admin
      .from("quizzes")
      .update({ status: "waiting", current_question_index: 0 })
      .eq("id", params.id);
    if (error) throw error;
    return NextResponse.json({ ok: true });
  } catch (e: any) {
    return NextResponse.json({ error: e.message }, { status: 500 });
  }
}
