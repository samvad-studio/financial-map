<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import { supabase } from '$lib/supabaseClient';
	import type { Map } from 'leaflet';

	let mapElement: HTMLDivElement;
	let countryData = new Map();

	onMount(() => {
		if (browser) {
			const initializeMap = async () => {
				const L = (await import('leaflet')).default;
				await import('leaflet/dist/leaflet.css');

				// 1. Fetch data from Supabase
				const { data: supabaseData } = await supabase.from('country_data').select('*');
				if (supabaseData) {
					supabaseData.forEach((country) => {
						countryData.set(country.CountryCode_ISO2, country);
					});
				}

				// 2. Initialize the map
				const map: Map = L.map(mapElement).setView([20, 0], 2);
				L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
					attribution: '&copy; OpenStreetMap &copy; CARTO'
				}).addTo(map);

				// 3. Load the GeoJSON and apply styles and popups
				const response = await fetch('/countries.geojson');
				const geoJsonData = await response.json();

				L.geoJSON(geoJsonData, {
					style: (feature) => {
						// Style countries differently based on whether we have data for them
						if (countryData.has(feature.properties.ISO_A2)) {
							return { color: '#2563eb', weight: 1, fillColor: '#3b82f6', fillOpacity: 0.5 }; // Active style
						}
						return { color: '#9ca3af', weight: 1, fillColor: '#e5e7eb', fillOpacity: 0.5 }; // Inactive style
					},
					onEachFeature: (feature, layer) => {
						// Only add a click event if we have data for the country
						if (countryData.has(feature.properties.ISO_A2)) {
							layer.on('click', () => {
								const data = countryData.get(feature.properties.ISO_A2);
								let popupContent = `<b>${data.CountryName}</b><br>`;
                                // Dynamically add whatever data is available
                                if (data.PolicyRate_UpperBound) popupContent += `Policy Rate: ${data.PolicyRate_UpperBound}%<br>`;
                                if (data.GDP_Growth_YoY) popupContent += `GDP Growth (YoY): ${data.GDP_Growth_YoY}%<br>`;
                                if (data.Inflation_CPI_YoY) popupContent += `Inflation (YoY): ${data.Inflation_CPI_YoY}%<br>`;
								
								layer.bindPopup(popupContent).openPopup();
							});
						}
					}
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