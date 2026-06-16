"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export function JoinByCodeInline() {
  const router = useRouter();
  const [code, setCode] = useState("");

  const go = () => {
    const c = code.trim().toUpperCase();
    if (!c) return;
    router.push(`/live/${c}`);
  };

  return (
    <div className="flex items-stretch gap-2">
      <input
        type="text"
        placeholder="CODE"
        maxLength={8}
        value={code}
        onChange={(e) => setCode(e.target.value.toUpperCase())}
        onKeyDown={(e) => e.key === "Enter" && go()}
        className="input w-32 text-center font-mono tracking-[0.4em]"
      />
      <button onClick={go} className="btn-ghost">
        Rejoindre
      </button>
    </div>
  );
}
