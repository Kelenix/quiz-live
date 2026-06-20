import { createClient, SupabaseClient } from "@supabase/supabase-js";

const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL ?? "";
const SUPABASE_ANON_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ?? "";

/**
 * Client public (lecture publique + Realtime + insertions autorisées par RLS).
 * Utilisable côté browser et côté serveur.
 */
export function createPublicClient(): SupabaseClient {
  if (!SUPABASE_URL || !SUPABASE_ANON_KEY) {
    throw new Error(
      "Supabase: variables NEXT_PUBLIC_SUPABASE_URL / NEXT_PUBLIC_SUPABASE_ANON_KEY manquantes.",
    );
  }
  return createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    auth: { persistSession: false },
    realtime: { params: { eventsPerSecond: 20 } },
  });
}

/**
 * Client admin (service role). UNIQUEMENT côté serveur (API routes).
 * Bypasse RLS.
 */
export function createAdminClient(): SupabaseClient {
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!SUPABASE_URL || !key) {
    throw new Error(
      "Supabase admin: variables NEXT_PUBLIC_SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY manquantes.",
    );
  }
  return createClient(SUPABASE_URL, key, {
    auth: { persistSession: false },
    global: {
      // Empêche Next.js de mettre en cache les lectures Supabase côté serveur.
      // Sans ça, une page rendue alors que la table était vide peut continuer
      // à servir un résultat vide en cache même après l'ajout de données.
      fetch: (input, init) =>
        fetch(input as RequestInfo, { ...init, cache: "no-store" }),
    },
  });
}

// Singleton browser (évite plusieurs WebSocket Realtime).
let browserClient: SupabaseClient | null = null;
export function getBrowserClient(): SupabaseClient {
  if (!browserClient) browserClient = createPublicClient();
  return browserClient;
}
