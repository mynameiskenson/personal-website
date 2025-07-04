import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import tsconfigPaths from "vite-tsconfig-paths"

// https://vite.dev/config/
export default defineConfig({
  server : {
    proxy: { '/api': 'http://localhost:5000' }
  },
  plugins: [react(),tailwindcss(),tsconfigPaths()],
})
