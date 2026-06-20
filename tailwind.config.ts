import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./lib/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        bg: {
          DEFAULT: "#121212",
          soft: "#1a1a1a",
          card: "#1f1f1f",
          border: "#2e2e2e",
        },
        accent: {
          primary: "#3ecf8e",
          secondary: "#1f9d63",
          glow: "#7ffbc4",
        },
        // Palette d'accents secondaires pour des touches de couleur vives
        grape: "#a855f7",
        sky: "#38bdf8",
        rose: "#fb7185",
        gold: "#fbbf24",
        ok: "#22c55e",
        warn: "#f59e0b",
        err: "#ef4444",
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"],
      },
      boxShadow: {
        glow: "0 0 32px -8px rgba(62,207,142,.5)",
        "glow-lg": "0 0 60px -10px rgba(62,207,142,.65)",
        card: "0 8px 24px -12px rgba(0,0,0,.6)",
      },
      keyframes: {
        "fade-in": {
          "0%": { opacity: "0", transform: "translateY(8px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        "slide-up": {
          "0%": { opacity: "0", transform: "translateY(24px) scale(.98)" },
          "100%": { opacity: "1", transform: "translateY(0) scale(1)" },
        },
        "pop-in": {
          "0%": { opacity: "0", transform: "scale(.85)" },
          "60%": { opacity: "1", transform: "scale(1.04)" },
          "100%": { transform: "scale(1)" },
        },
        "pulse-soft": {
          "0%,100%": { opacity: "1" },
          "50%": { opacity: ".6" },
        },
        float: {
          "0%,100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-10px)" },
        },
        "float-slow": {
          "0%,100%": { transform: "translate(0,0) scale(1)" },
          "50%": { transform: "translate(20px,-20px) scale(1.08)" },
        },
        shake: {
          "0%,100%": { transform: "translateX(0)" },
          "20%,60%": { transform: "translateX(-7px)" },
          "40%,80%": { transform: "translateX(7px)" },
        },
        "score-pop": {
          "0%": { transform: "scale(.4)", opacity: "0" },
          "55%": { transform: "scale(1.18)", opacity: "1" },
          "100%": { transform: "scale(1)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
        "gradient-x": {
          "0%,100%": { backgroundPosition: "0% 50%" },
          "50%": { backgroundPosition: "100% 50%" },
        },
        "spin-slow": {
          to: { transform: "rotate(360deg)" },
        },
      },
      animation: {
        "fade-in": "fade-in .35s ease-out both",
        "slide-up": "slide-up .45s cubic-bezier(.21,1.02,.73,1) both",
        "pop-in": "pop-in .4s cubic-bezier(.34,1.56,.64,1) both",
        "pulse-soft": "pulse-soft 2.2s ease-in-out infinite",
        float: "float 4s ease-in-out infinite",
        "float-slow": "float-slow 14s ease-in-out infinite",
        shake: "shake .4s ease-in-out both",
        "score-pop": "score-pop .6s cubic-bezier(.34,1.56,.64,1) both",
        shimmer: "shimmer 2.5s linear infinite",
        "gradient-x": "gradient-x 6s ease infinite",
        "spin-slow": "spin-slow 9s linear infinite",
      },
    },
  },
  plugins: [],
};

export default config;
