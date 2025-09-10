<script lang="ts">
    import { onMount } from 'svelte';
    import { browser } from '$app/environment';
    import { supabase } from '$lib/supabaseClient';

    let mapElement: HTMLDivElement;

    onMount(() => {
        if (browser) {
            const initializeMap = async () => {
                const L = (await import('leaflet')).default;
                await import('leaflet/dist/leaflet.css');
                const map = L.map(mapElement).setView([20, 0], 2);
                L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
                    attribution: '&copy; OpenStreetMap &copy; CARTO'
                }).addTo(map);

                const { data } = await supabase.from('country_data').select('*');
                console.log('Fetched data:', data);
            };
            initializeMap();
        }
    });
</script>

<main class="w-full h-screen p-4">
    <h1 class="text-2xl font-bold text-center mb-4">Global Financial Metrics</h1>
    <div bind:this={mapElement} class="w-full h-[80vh] rounded-lg shadow-md" />
</main>