import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa'

const manifestForPlugin = {
  registerType: "prompt",
  includeAssets: ["favicon.ico", "apple-touch-icon.png", "masked-icon.svg"],
  manifest: {
    name: "Ecommerce django react",
    short_name: "Sirekom",
    description: "Ecommerce django react.",
    icons: [
      {
        src: "/assets/192x192 logo_sirekom-01.png",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "/assets/512x512_logo_sirekom-02.png",
        sizes: "512x512",
        type: "image/png",
      },
      {
        src: "/assets/180x180_logo_sirekom-03.png",
        sizes: "180x180",
        type: "image/png",
        purpose: "apple touch icon",
      },
      {
        src: "/assets/225x225_logo_sirekom-04.png",
        sizes: "225x225",
        type: "image/png",
        purpose: "any maskable",
      },
    ],

    display: "standalone",
    scope: "/",
    start_url: "/",
    orientation: "portrait",
  },
};


// https://vitejs.dev/config/
export default defineConfig({
  server: {

    port: 3000,
  },
  plugins: [react(), VitePWA(manifestForPlugin)],
});
