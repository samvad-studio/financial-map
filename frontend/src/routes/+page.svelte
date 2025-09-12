<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import { supabase } from '$lib/supabaseClient';
	import { base } from '$app/paths'; // Import 'base' for correct asset path
	import type { Map as LeafletMap } from 'leaflet';

	let mapElement: HTMLDivElement;

	onMount(() => {
		if (browser) {
			const initializeMap = async () => {
				const L = (await import('leaflet')).default;
				await import('leaflet/dist/leaflet.css');

				const map: LeafletMap = L.map(mapElement).setView([20, 0], 2);
				L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
					attribution: '&copy; OpenStreetMap &copy; CARTO'
				}).addTo(map);

				const [geoJsonResponse, { data: supabaseData }] = await Promise.all([
					fetch(`${base}/countries.geojson`), // Use 'base' for the correct path
					supabase.from('country_data').select('*')
				]);

				const geoJsonData = await geoJsonResponse.json();
				const countryData = new Map();
				if (supabaseData) {
					supabaseData.forEach((country) => {
						countryData.set(country.CountryCode_ISO2, country);
					});
				}

				L.geoJSON(geoJsonData, {
					// ... (Your style and onEachFeature logic) ...
				}).addTo(map);
			};
			initializeMap();
		}
	});
</script>

<main class="w-full h-screen p-4">
	<h1 class="text-2xl font-bold text-center mb-4">Global Financial Metrics</h1>
	<div bind:this={mapElement} class="w-full h-[80vh] rounded-lg shadow-md border" />
</main>