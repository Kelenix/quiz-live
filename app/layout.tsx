import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Quiz Live",
  description: "Plateforme de quiz en temps réel",
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  viewportFit: "cover",
  themeColor: "#121212",
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
        {/* Fond animé : orbes colorés flottants */}
        <div className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
          <div className="absolute -top-40 -left-40 h-[34rem] w-[34rem] rounded-full bg-accent-primary/25 blur-3xl animate-float-slow" />
          <div className="absolute top-1/3 -right-40 h-[32rem] w-[32rem] rounded-full bg-sky/15 blur-3xl animate-float-slow [animation-delay:-5s]" />
          <div className="absolute -bottom-48 left-1/4 h-[36rem] w-[36rem] rounded-full bg-accent-secondary/20 blur-3xl animate-float-slow [animation-delay:-9s]" />
        </div>
        {children}
      </body>
    </html>
  );
}
