import Link from "next/link";
import { Sparkles } from "lucide-react";

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-20 border-b border-bg-border bg-bg/80 backdrop-blur-md">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <Link href="/admin" className="flex items-center gap-2 font-semibold">
            <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-accent-violet to-accent-blue shadow-glow">
              <Sparkles className="h-4 w-4 text-white" />
            </span>
            <span>Quiz Live · Admin</span>
          </Link>
          <Link href="/" className="text-sm text-zinc-400 hover:text-zinc-200">
            Accueil
          </Link>
        </div>
      </header>
      <main className="mx-auto max-w-6xl px-6 py-8">{children}</main>
    </div>
  );
}
