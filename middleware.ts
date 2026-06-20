import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { ADMIN_COOKIE, expectedAdminToken } from "@/lib/admin-auth";

// Protège l'espace admin et les routes API d'administration.
// Les routes participant (/api/join, /api/responses) restent publiques.
export async function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl;

  // Laisse passer la page de login et son API.
  if (pathname === "/admin/login" || pathname.startsWith("/api/admin/")) {
    return NextResponse.next();
  }

  const expected = await expectedAdminToken();
  const token = req.cookies.get(ADMIN_COOKIE)?.value;
  const authorized = Boolean(expected && token && token === expected);

  if (!authorized) {
    // Pour une route API : 401 JSON.
    if (pathname.startsWith("/api/")) {
      return NextResponse.json({ error: "Non autorisé" }, { status: 401 });
    }
    // Pour une page admin : redirige vers le login.
    const url = req.nextUrl.clone();
    url.pathname = "/admin/login";
    url.search = "";
    url.searchParams.set("from", pathname);
    return NextResponse.redirect(url);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/admin/:path*", "/api/quizzes/:path*"],
};
