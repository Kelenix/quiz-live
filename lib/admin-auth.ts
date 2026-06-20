// Authentification admin légère par mot de passe (cookie httpOnly).
// Le mot de passe vit dans la variable d'environnement ADMIN_PASSWORD (jamais en dur).

export const ADMIN_COOKIE = "admin_session";
export const ADMIN_MAX_AGE = 60 * 60 * 12; // 12 heures

// SHA-256 hex via Web Crypto (compatible Edge middleware + Node).
export async function sha256Hex(input: string): Promise<string> {
  const data = new TextEncoder().encode(input);
  const digest = await crypto.subtle.digest("SHA-256", data);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

// Jeton attendu dans le cookie = hash du mot de passe configuré.
// Renvoie null si aucun mot de passe n'est configuré côté serveur.
export async function expectedAdminToken(): Promise<string | null> {
  const pw = process.env.ADMIN_PASSWORD;
  if (!pw) return null;
  return sha256Hex(`quizlive::${pw}`);
}
