import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Quiz Live",
  description: "Plateforme de quiz en temps réel",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="fr" className="dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-screen bg-bg text-zinc-100 font-sans antialiased">
        <div className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
          <div className="absolute -top-40 -left-40 h-[40rem] w-[40rem] rounded-full bg-accent-primary/20 blur-3xl" />
          <div className="absolute -bottom-40 -right-40 h-[40rem] w-[40rem] rounded-full bg-accent-secondary/20 blur-3xl" />
        </div>
        {children}
      </body>
    </html>
  );
}
