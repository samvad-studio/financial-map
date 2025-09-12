<script lang="ts">
	import { onMount, tick } from 'svelte'; // <-- Import 'tick'
	import { browser } from '$app/environment';
	import { supabase } from '$lib/supabaseClient';
	import type { Map } from 'leaflet';

	let mapElement: HTMLDivElement;

	onMount(() => {
		if (browser) {
			const initializeMap = async () => {
                // --- Wait for the DOM to be updated ---
				await tick(); // <-- The Fix: Wait for bind:this to complete

				const L = (await import('leaflet')).default;
				await import('leaflet/dist/leaflet.css');
				
				// Fetch data... (logic remains the same)
				const { data: supabaseData } = await supabase.from('country_data').select('*');
				const countryData = new Map();
				if (supabaseData) {
					supabaseData.forEach((country) => {
						countryData.set(country.CountryCode_ISO2, country);
					});
				}

				// Initialize map... (logic remains the same)
				const map: Map = L.map(mapElement).setView([20, 0], 2);
				L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
					attribution: '&copy; OpenStreetMap &copy; CARTO'
				}).addTo(map);

				// Fetch GeoJSON and add layers... (logic remains the same)
				const response = await fetch('/countries.geojson');
				const geoJsonData = await response.json();
				L.geoJSON(geoJsonData, {
                    // ... (your style and onEachFeature logic)
                }).addTo(map);
			};

			initializeMap();
		}
	});
</script>