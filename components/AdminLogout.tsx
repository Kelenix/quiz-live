"use client";

import { useRouter, usePathname } from "next/navigation";
import { useState } from "react";
import { LogOut, Loader2 } from "lucide-react";

export function AdminLogout() {
  const router = useRouter();
  const pathname = usePathname();
  const [busy, setBusy] = useState(false);

  // Pas de bouton de déconnexion sur la page de login.
  if (pathname === "/admin/login") return null;

  const logout = async () => {
    setBusy(true);
    try {
      await fetch("/api/admin/login", { method: "DELETE" });
      router.replace("/admin/login");
      router.refresh();
    } finally {
      setBusy(false);
    }
  };

  return (
    <button
      onClick={logout}
      disabled={busy}
      className="inline-flex items-center gap-1.5 text-sm text-zinc-400 transition-colors hover:text-zinc-200"
      title="Se déconnecter"
    >
      {busy ? (
        <Loader2 className="h-4 w-4 animate-spin" />
      ) : (
        <LogOut className="h-4 w-4" />
      )}
      <span className="hidden sm:inline">Déconnexion</span>
    </button>
  );
}
