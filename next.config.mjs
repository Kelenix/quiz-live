/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    serverActions: {
      bodySizeLimit: "2mb",
    },
  },
  // Le lint ne doit pas bloquer le déploiement Vercel (apostrophes en français, etc.).
  // Lancez `npm run lint` localement pour vérifier la qualité du code.
  eslint: {
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;
