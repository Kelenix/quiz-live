import { NextResponse } from "next/server";
import { ADMIN_COOKIE, ADMIN_MAX_AGE, expectedAdminToken } from "@/lib/admin-auth";

export const dynamic = "force-dynamic";

// POST : connexion. Body { password }
export async function POST(req: Request) {
  const pw = process.env.ADMIN_PASSWORD;
  if (!pw) {
    return NextResponse.json(
      {
        error:
          "ADMIN_PASSWORD n'est pas configuré côté serveur. Ajoute la variable d'environnement.",
      },
      { status: 500 },
    );
  }

  let password = "";
  try {
    const body = await req.json();
    password = String(body?.password ?? "");
  } catch {
    return NextResponse.json({ error: "Requête invalide." }, { status: 400 });
  }

  if (password !== pw) {
    return NextResponse.json({ error: "Mot de passe incorrect." }, { status: 401 });
  }

  const token = await expectedAdminToken();
  const res = NextResponse.json({ ok: true });
  res.cookies.set(ADMIN_COOKIE, token!, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    path: "/",
    maxAge: ADMIN_MAX_AGE,
  });
  return res;
}

// DELETE : déconnexion.
export async function DELETE() {
  const res = NextResponse.json({ ok: true });
  res.cookies.set(ADMIN_COOKIE, "", {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    path: "/",
    maxAge: 0,
  });
  return res;
}
