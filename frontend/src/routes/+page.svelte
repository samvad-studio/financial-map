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

				// --- 1. Fetch data from Supabase ---
				// ... (data fetching code remains the same) ...
				const { data: supabaseData } = await supabase.from('country_data').select('*');
				if (supabaseData) {
					supabaseData.forEach((country) => {
						countryData.set(country.CountryCode_ISO2, country);
					});
				}

				// --- 2. Initialize the map with new options ---
				const map: Map = L.map(mapElement, {
					center: [20, 0],
					zoom: 2,
					maxBounds: L.latLngBounds(L.latLng(-90, -180), L.latLng(90, 180)), // Set map boundaries
					maxBoundsViscosity: 1.0 // Make the boundaries "bouncy"
				});

				L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
					attribution: '&copy; OpenStreetMap &copy; CARTO',
					noWrap: true // <-- STOPS THE MAP FROM REPEATING
				}).addTo(map);
				
				// --- 3. Load the GeoJSON (code remains the same) ---
				const response = await fetch('/countries.geojson');
				const geoJsonData = await response.json();

				L.geoJSON(geoJsonData, {
					// ... (style and onEachFeature logic remains the same) ...
				}).addTo(map);
			};
			initializeMap();
		}
	});
</script>