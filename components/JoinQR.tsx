"use client";

import { QRCodeCanvas } from "qrcode.react";
import { useEffect, useState } from "react";
import { Copy, Check } from "lucide-react";
import { joinUrl } from "@/lib/utils";

export function JoinQR({ code }: { code: string }) {
  const [url, setUrl] = useState("");
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    setUrl(joinUrl(code));
  }, [code]);

  const copy = async () => {
    if (!url) return;
    await navigator.clipboard.writeText(url);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="rounded-2xl bg-white p-4 shadow-glow">
        {url ? (
          <QRCodeCanvas value={url} size={196} bgColor="#ffffff" fgColor="#0f0f1a" includeMargin={false} />
        ) : (
          <div className="h-[196px] w-[196px] animate-pulse bg-zinc-200" />
        )}
      </div>
      <div className="w-full space-y-2">
        <p className="text-center text-xs uppercase tracking-widest text-zinc-400">
          Code à saisir
        </p>
        <p className="text-center font-mono text-3xl font-bold tracking-[0.4em] text-accent-glow">
          {code}
        </p>
      </div>
      <button onClick={copy} className="btn-ghost w-full">
        {copied ? (
          <>
            <Check className="h-4 w-4" /> Lien copié
          </>
        ) : (
          <>
            <Copy className="h-4 w-4" /> Copier le lien
          </>
        )}
      </button>
      {url && (
        <p className="break-all text-center text-xs text-zinc-500">{url}</p>
      )}
    </div>
  );
}
