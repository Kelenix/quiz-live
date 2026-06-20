"use client";

import { useEffect, useState } from "react";
import { cn } from "@/lib/utils";

export function Timer({
  seconds,
  onExpire,
  resetKey,
}: {
  seconds: number;
  onExpire?: () => void;
  resetKey?: string | number;
}) {
  const [remaining, setRemaining] = useState(seconds);

  useEffect(() => {
    setRemaining(seconds);
  }, [seconds, resetKey]);

  useEffect(() => {
    if (remaining <= 0) {
      onExpire?.();
      return;
    }
    const id = setTimeout(() => setRemaining((r) => r - 1), 1000);
    return () => clearTimeout(id);
  }, [remaining, onExpire]);

  const pct = Math.max(0, Math.min(100, (remaining / seconds) * 100));
  const danger = remaining <= Math.max(3, Math.floor(seconds * 0.25));

  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between text-xs uppercase tracking-wider text-zinc-400">
        <span>Temps restant</span>
        <span
          className={cn(
            "font-mono text-sm font-bold tabular-nums transition-colors",
            danger ? "scale-110 text-err animate-pulse-soft" : "text-zinc-200",
          )}
        >
          {remaining}s
        </span>
      </div>
      <div className="h-2.5 w-full overflow-hidden rounded-full bg-bg-border">
        <div
          className={cn(
            "h-full rounded-full transition-all duration-1000 ease-linear",
            danger
              ? "bg-gradient-to-r from-red-500 to-orange-500 shadow-[0_0_12px_-1px_rgba(239,68,68,.7)]"
              : "bg-gradient-to-r from-accent-glow via-accent-primary to-accent-secondary",
          )}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}
