import Link from "next/link";
import { ArrowRight, Sparkles, Users, Zap, Trophy } from "lucide-react";
import { JoinByCodeInline } from "./JoinByCodeInline";

export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-screen max-w-5xl flex-col px-6 py-12">
      <nav className="mb-12 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 font-semibold">
          <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-accent-primary to-accent-secondary shadow-glow">
            <Sparkles className="h-4 w-4 text-white" />
          </span>
          Quiz Live
        </Link>
        <Link href="/admin" className="text-sm text-zinc-400 hover:text-zinc-200">
          Espace admin
        </Link>
      </nav>

      <section className="flex flex-1 flex-col items-center justify-center text-center">
        <span className="chip border-accent-primary/40 bg-accent-primary/10 text-accent-glow">
          <span className="h-1.5 w-1.5 rounded-full bg-accent-glow animate-pulse-soft" />
          Quiz en temps réel, sans inscription
        </span>
        <h1 className="mt-6 max-w-3xl bg-gradient-to-r from-white via-accent-glow to-white bg-clip-text text-4xl font-bold leading-tight text-transparent sm:text-6xl">
          Anime tes quiz comme un live, depuis ton navigateur.
        </h1>
        <p className="mt-5 max-w-2xl text-base text-zinc-400">
          Crée un quiz, partage un code à six caractères ou un QR, et lance la
          partie. Les participants jouent depuis leur mobile, en temps réel.
        </p>

        <div className="mt-8 flex flex-col gap-3 sm:flex-row">
          <Link href="/admin" className="btn-primary">
            Créer un quiz <ArrowRight className="h-4 w-4" />
          </Link>
          <JoinByCodeInline />
        </div>

        <div className="mt-16 grid w-full grid-cols-1 gap-4 sm:grid-cols-3">
          <Feature
            icon={Zap}
            title="Temps réel"
            text="Diffusion instantanée des questions et du classement grâce à Supabase Realtime."
          />
          <Feature
            icon={Users}
            title="Aucune inscription"
            text="Un pseudo, un code, et c'est parti. Idéal pour des sessions ouvertes."
          />
          <Feature
            icon={Trophy}
            title="Score & podium"
            text="Bonus rapidité, podium animé et classement final pour récompenser les meilleurs."
          />
        </div>
      </section>
    </main>
  );
}

function Feature({
  icon: Icon,
  title,
  text,
}: {
  icon: typeof Sparkles;
  title: string;
  text: string;
}) {
  return (
    <div className="card p-5 text-left">
      <span className="mb-3 inline-flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-accent-primary/30 to-accent-secondary/30 text-accent-glow">
        <Icon className="h-4 w-4" />
      </span>
      <h3 className="text-sm font-semibold">{title}</h3>
      <p className="mt-1 text-sm text-zinc-400">{text}</p>
    </div>
  );
}
