<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/environment'; // Imports the browser guard
	import { supabase } from '$lib/supabaseClient';
	import type { Map } from 'leaflet'; // Import only the type definitions

	let mapElement: HTMLDivElement; // A reference to the div element for the map

	onMount(() => {
		// This 'if' statement is the key. It ensures this code ONLY runs in a browser.
		if (browser) {
			const initializeMap = async () => {
				// 1. Dynamically import Leaflet only when we are in the browser
				const L = (await import('leaflet')).default;
				await import('leaflet/dist/leaflet.css');

				// 2. Fetch all data needed for the map
				const geoJsonResponse = await fetch('/countries.geojson');
				const geoJsonData = await geoJsonResponse.json();

				const { data: supabaseData } = await supabase.from('country_data').select('*');
				const countryData = new Map();
				if (supabaseData) {
					supabaseData.forEach((country) => {
						countryData.set(country.CountryCode_ISO2, country);
					});
				}

				// 3. Now, initialize the map and add layers
				const map: Map = L.map(mapElement).setView([20, 0], 2);
				L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
					attribution:
						'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
				}).addTo(map);

				L.geoJSON(geoJsonData, {
					onEachFeature: (feature, layer) => {
						layer.on('click', () => {
							const data = countryData.get(feature.properties.ISO_A2);
							let popupContent = `<b>${feature.properties.ADMIN}</b><br>Data not available.`;
							if (data) {
								popupContent = `
                                    <b>${data.CountryName}</b><br>
                                    Policy Rate: ${data.PolicyRate_UpperBound}%
                                `;
							}
							layer.bindPopup(popupContent).openPopup();
						});
					}
				}).addTo(map);
			};

			initializeMap();
		}
	});
</script>

<main class="w-full h-screen p-4">
	<h1 class="text-2xl font-bold text-center mb-4">Global Financial Metrics</h1>

	<div bind:this={mapElement} class="w-full h-[80vh] rounded-lg shadow-md" />
</main>