import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { computeScore, correctAnswerIds } from "@/lib/utils";

export const dynamic = "force-dynamic";

interface Body {
  participant_id: string;
  question_id: string;
  answer_ids: string[];
  elapsed_ms?: number | null;
}

export async function POST(req: Request) {
  try {
    const body = (await req.json()) as Body;
    if (!body.participant_id || !body.question_id) {
      return NextResponse.json(
        { error: "participant_id / question_id requis" },
        { status: 400 },
      );
    }
    const admin = createAdminClient();

    // Charge la question + ses réponses pour calculer le score
    const { data: question, error: eq } = await admin
      .from("questions")
      .select("id, type, time_limit, answers(id, is_correct)")
      .eq("id", body.question_id)
      .single();
    if (eq) throw eq;

    const allAnswers = (question as any).answers as { id: string; is_correct: boolean }[];
    const correct = correctAnswerIds(allAnswers as any);

    const score = computeScore({
      question: { type: question.type as any, time_limit: question.time_limit },
      correctAnswerIds: correct,
      selectedAnswerIds: body.answer_ids ?? [],
      elapsedMs: body.elapsed_ms ?? null,
    });

    // Insère la réponse (unique sur (participant_id, question_id)).
    // En cas de doublon on renvoie 409 sans toucher le score.
    const { error: er } = await admin.from("responses").insert({
      participant_id: body.participant_id,
      question_id: body.question_id,
      answer_ids: body.answer_ids ?? [],
      is_correct: score.isCorrect,
    });
    if (er) {
      if (er.code === "23505") {
        return NextResponse.json(
          { error: "Réponse déjà enregistrée" },
          { status: 409 },
        );
      }
      throw er;
    }

    // Met à jour le score du participant
    if (score.points > 0) {
      const { data: p, error: ep } = await admin
        .from("participants")
        .select("score")
        .eq("id", body.participant_id)
        .single();
      if (ep) throw ep;
      const { error: eu } = await admin
        .from("participants")
        .update({ score: (p?.score ?? 0) + score.points })
        .eq("id", body.participant_id);
      if (eu) throw eu;
    }

    return NextResponse.json({
      ok: true,
      points: score.points,
      is_correct: score.isCorrect,
      is_partial: score.isPartial,
    });
  } catch (e: any) {
    return NextResponse.json(
      { error: e.message ?? "Erreur serveur" },
      { status: 500 },
    );
  }
}
