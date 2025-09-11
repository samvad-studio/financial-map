import adapter from '@sveltejs/adapter-static'; // <-- Import the static adapter
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    preprocess: vitePreprocess(),

    kit: {
        adapter: adapter({
            // default options are fine for Vercel
            pages: 'build',
            assets: 'build',
            fallback: 'index.html',
            precompress: false
        })
    }
};

export default config;