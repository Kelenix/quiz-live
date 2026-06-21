"use client";

import { useEffect, useRef } from "react";
import { cn } from "@/lib/utils";
import type { Participant } from "@/types";
import { Trophy, Medal, Award, ChevronUp, ChevronDown } from "lucide-react";

const PODIUM = [
  { icon: Trophy, color: "text-amber-300", ring: "ring-amber-400/50" },
  { icon: Medal, color: "text-zinc-200", ring: "ring-zinc-300/40" },
  { icon: Award, color: "text-orange-400", ring: "ring-orange-400/40" },
];

function sortParticipants(participants: Participant[]) {
  return [...participants].sort(
    (a, b) => b.score - a.score || a.username.localeCompare(b.username),
  );
}

export function Leaderboard({
  participants,
  highlightId,
  limit = 10,
  compact = false,
  showDelta = false,
}: {
  participants: Participant[];
  highlightId?: string;
  limit?: number;
  compact?: boolean;
  /** Affiche la variation de rang (▲/▼) depuis le dernier rendu — utile pendant une partie en direct. */
  showDelta?: boolean;
}) {
  const fullSorted = sortParticipants(participants);
  const sorted = fullSorted.slice(0, limit);

  // Suivi des rangs précédents pour afficher les décalages en direct.
  const prevRanksRef = useRef<Map<string, number>>(new Map());
  const deltaByParticipant = new Map<string, number>();
  if (showDelta) {
    fullSorted.forEach((p, idx) => {
      const prevRank = prevRanksRef.current.get(p.id);
      if (prevRank !== undefined && prevRank !== idx) {
        deltaByParticipant.set(p.id, prevRank - idx); // > 0 = a gagné des places
      }
    });
  }

  useEffect(() => {
    if (!showDelta) return;
    const map = new Map<string, number>();
    sortParticipants(participants).forEach((p, idx) => map.set(p.id, idx));
    prevRanksRef.current = map;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [participants, showDelta]);

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
        const delta = deltaByParticipant.get(p.id);
        return (
          <li
            key={p.id}
            style={{ animationDelay: `${Math.min(idx, 9) * 60}ms` }}
            className={cn(
              "flex animate-slide-up items-center gap-3 rounded-xl border border-bg-border bg-bg-soft/40 px-4 transition",
              compact ? "py-2" : "py-3",
              isMe && "ring-2 ring-accent-primary/60 border-accent-primary/60",
              idx === 0 && "border-amber-400/40 bg-gradient-to-r from-amber-400/10 to-transparent",
              idx === 1 && "border-zinc-300/25 bg-gradient-to-r from-zinc-300/5 to-transparent",
              idx === 2 && "border-orange-400/25 bg-gradient-to-r from-orange-400/5 to-transparent",
            )}
          >
            <span
              className={cn(
                "flex h-9 w-9 shrink-0 items-center justify-center rounded-full font-bold tabular-nums",
                podium
                  ? `animate-pop-in ring-2 ${podium.ring} ${podium.color} bg-bg`
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
            {delta !== undefined && (
              <span
                key={`${p.id}-${delta}`}
                className={cn(
                  "flex animate-pop-in items-center gap-0.5 text-xs font-bold tabular-nums",
                  delta > 0 ? "text-emerald-400" : "text-red-400",
                )}
              >
                {delta > 0 ? (
                  <ChevronUp className="h-3.5 w-3.5" />
                ) : (
                  <ChevronDown className="h-3.5 w-3.5" />
                )}
                {Math.abs(delta)}
              </span>
            )}
            <span className="font-mono text-base font-bold tabular-nums text-accent-glow">
              {p.score}
            </span>
          </li>
        );
      })}
    </ol>
  );
}
