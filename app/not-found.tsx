import Link from "next/link";

export default function NotFound() {
  return (
    <main className="mx-auto flex min-h-screen max-w-md flex-col items-center justify-center px-6 text-center">
      <div className="card p-8 space-y-3">
        <p className="font-mono text-xs text-zinc-500">404</p>
        <h1 className="text-xl font-bold">Page introuvable</h1>
        <p className="text-sm text-zinc-400">
          Le lien que tu as suivi n'existe plus ou n'est pas valide.
        </p>
        <Link href="/" className="btn-primary mt-2">
          Retour à l'accueil
        </Link>
      </div>
    </main>
  );
}
