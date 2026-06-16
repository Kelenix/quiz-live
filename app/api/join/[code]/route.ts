import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";

export const dynamic = "force-dynamic";

/**
 * Inscrit un participant à un quiz via son join_code.
 * Vérifie unicité du username dans le quiz.
 */
export async function POST(req: Request, { params }: { params: { code: string } }) {
  try {
    const { username } = (await req.json()) as { username?: string };
    const clean = (username ?? "").trim();
    if (!clean) {
      return NextResponse.json({ error: "Pseudo requis" }, { status: 400 });
    }
    if (clean.length > 24) {
      return NextResponse.json(
        { error: "Pseudo trop long (max 24)" },
        { status: 400 },
      );
    }

    const admin = createAdminClient();
    const code = params.code.toUpperCase();

    const { data: quiz, error: eq } = await admin
      .from("quizzes")
      .select("id, status")
      .eq("join_code", code)
      .maybeSingle();
    if (eq) throw eq;
    if (!quiz) {
      return NextResponse.json({ error: "Quiz introuvable" }, { status: 404 });
    }
    if (quiz.status === "finished") {
      return NextResponse.json({ error: "Quiz terminé" }, { status: 410 });
    }
    if (quiz.status === "draft") {
      return NextResponse.json(
        { error: "Quiz pas encore disponible" },
        { status: 423 },
      );
    }

    // Unicité du username dans ce quiz
    const { data: exists, error: ex } = await admin
      .from("participants")
      .select("id")
      .eq("quiz_id", quiz.id)
      .eq("username", clean)
      .maybeSingle();
    if (ex) throw ex;
    if (exists) {
      return NextResponse.json(
        { error: "Ce pseudo est déjà pris" },
        { status: 409 },
      );
    }

    const { data: p, error: ei } = await admin
      .from("participants")
      .insert({ quiz_id: quiz.id, username: clean })
      .select("id, quiz_id, username, score, joined_at")
      .single();
    if (ei) throw ei;

    return NextResponse.json({ participant: p, quiz_id: quiz.id });
  } catch (e: any) {
    return NextResponse.json(
      { error: e.message ?? "Erreur serveur" },
      { status: 500 },
    );
  }
}
