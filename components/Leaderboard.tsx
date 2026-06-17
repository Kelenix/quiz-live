import { cn } from "@/lib/utils";
import type { Participant } from "@/types";
import { Trophy, Medal, Award } from "lucide-react";

const PODIUM = [
  { icon: Trophy, color: "text-amber-300", ring: "ring-amber-400/50" },
  { icon: Medal, color: "text-zinc-200", ring: "ring-zinc-300/40" },
  { icon: Award, color: "text-orange-400", ring: "ring-orange-400/40" },
];

export function Leaderboard({
  participants,
  highlightId,
  limit = 10,
  compact = false,
}: {
  participants: Participant[];
  highlightId?: string;
  limit?: number;
  compact?: boolean;
}) {
  const sorted = [...participants]
    .sort((a, b) => b.score - a.score || a.username.localeCompare(b.username))
    .slice(0, limit);

  if (sorted.length === 0) {
    return (
      <p className="py-6 text-center text-sm text-zinc-500">
        Aucun participant pour le moment.
      </p>
    );
  }

  return (
    <ol className="space-y-2">
      {sorted.map((p, idx) => {
        const podium = idx < 3 ? PODIUM[idx] : null;
        const Icon = podium?.icon;
        const isMe = highlightId === p.id;
        return (
          <li
            key={p.id}
            className={cn(
              "flex items-center gap-3 rounded-xl border border-bg-border bg-bg-soft/40 px-4 transition",
              compact ? "py-2" : "py-3",
              isMe && "ring-2 ring-accent-primary/60 border-accent-primary/60",
              idx === 0 && "bg-amber-400/5 border-amber-400/30",
            )}
          >
            <span
              className={cn(
                "flex h-9 w-9 shrink-0 items-center justify-center rounded-full font-bold",
                podium
                  ? `ring-2 ${podium.ring} ${podium.color} bg-bg`
                  : "bg-bg-border text-zinc-300",
              )}
            >
              {Icon ? <Icon className="h-4 w-4" /> : idx + 1}
            </span>
            <span className="flex-1 truncate font-medium">
              {p.username}
              {isMe && (
                <span className="ml-2 text-xs font-normal text-accent-glow">
                  (vous)
                </span>
              )}
            </span>
            <span className="font-mono text-base font-bold tabular-nums text-accent-glow">
              {p.score}
            </span>
          </li>
        );
      })}
    </ol>
  );
}
