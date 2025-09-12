<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import { supabase } from '$lib/supabaseClient';
	import type { Map as LeafletMap } from 'leaflet';

	let mapElement: HTMLDivElement;
	let mapInstance: LeafletMap | null = null;

	onMount(() => {
		const initializeMap = async () => {
			if (browser && mapElement && !mapInstance) {
				const L = (await import('leaflet')).default;
				await import('leaflet/dist/leaflet.css');

				// 1. Initialize the map
				mapInstance = L.map(mapElement).setView([20, 0], 2);
				L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
					attribution: '&copy; OpenStreetMap &copy; CARTO'
				}).addTo(mapInstance);

				// 2. Fetch both data files at the same time
				const [geoJsonResponse, { data: supabaseData }] = await Promise.all([
					fetch('/countries.geojson'),
					supabase.from('country_data').select('*')
				]);

				const geoJsonData = await geoJsonResponse.json();
				const countryData = new Map();
				if (supabaseData) {
					supabaseData.forEach((country) => {
						countryData.set(country.CountryCode_ISO2, country);
					});
				}

				// 3. Add the interactive layer
				L.geoJSON(geoJsonData, {
					style: (feature) => {
						return countryData.has(feature?.properties.ISO_A2)
							? { color: '#2563eb', weight: 1, fillColor: '#3b82f6', fillOpacity: 0.5 }
							: { color: '#9ca3af', weight: 1, fillColor: '#e5e7eb', fillOpacity: 0.5 };
					},
					onEachFeature: (feature, layer) => {
						if (countryData.has(feature?.properties.ISO_A2)) {
							layer.on('click', () => {
								const data = countryData.get(feature.properties.ISO_A2);
								let popupContent = `<b>${data.CountryName}</b><br>`;
								if (data.PolicyRate_UpperBound) popupContent += `Policy Rate: ${data.PolicyRate_UpperBound}%<br>`;
                                if (data.GDP_Growth_YoY) popupContent += `GDP Growth (YoY): ${data.GDP_Growth_YoY}%<br>`;
                                if (data.Inflation_CPI_YoY) popupContent += `Inflation (YoY): ${data.Inflation_CPI_YoY}%<br>`;
								layer.bindPopup(popupContent).openPopup();
							});
						}
					}
				}).addTo(mapInstance);
			}
		};
		initializeMap();
	});
</script>

<main class="w-full h-screen p-4">
	<h1 class="text-2xl font-bold text-center mb-4">Global Financial Metrics</h1>
	<div bind:this={mapElement} class="w-full h-[80vh] rounded-lg shadow-md border" />
</main>