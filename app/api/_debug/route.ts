import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";

export const dynamic = "force-dynamic";

// Route de diagnostic temporaire : http://localhost:3000/api/_debug
// Montre ce que le SERVEUR Next voit réellement (même client que la page admin).
export async function GET() {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL ?? "(manquant)";
  const ref = url.match(/https:\/\/([^.]+)/)?.[1] ?? "(introuvable)";
  const svc = process.env.SUPABASE_SERVICE_ROLE_KEY ?? "";

  let role = "(illisible)";
  try {
    role = JSON.parse(
      Buffer.from(svc.split(".")[1], "base64").toString(),
    ).role;
  } catch {}

  try {
    const admin = createAdminClient();
    const { count, error } = await admin
      .from("quizzes")
      .select("*", { count: "exact", head: true });
    return NextResponse.json({
      projet: ref,
      url_propre: !/\s/.test(url),
      role_cle: role,
      quiz_count: count,
      erreur: error?.message ?? null,
    });
  } catch (e) {
    return NextResponse.json({
      projet: ref,
      role_cle: role,
      erreur: (e as Error).message,
    });
  }
}
