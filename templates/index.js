var map = L.map('map').setView([13.22, -5.16], 10);
var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreet map</a> OMB 2021',
});
osm.addTo(map);
var marker = L.marker([13.22, -5.16], {
    draggable :true,
    title: 'REPERE',
    opacity: 0.5,
})
    .addTo(map)
    .bindPopup('<h1>Marker</h1><p>This is the marker text</p>');
var watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	subdomains: 'abcd',
	minZoom: 1,
	maxZoom: 16,
	ext: 'jpg'
});
   watercolor.addTo(map);
var esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	attribution: ''
    // 'Tiles &copy; Esri &mdash; Source: Esri'
});
    esri_WorldImagery.addTo(map);
var baseLayers = {
    osm : osm,
    "water color": watercolor,
    "esri Imagery": esri_WorldImagery,
};
L.control.Layers(baseLayers).addTo(map);



$( "p" ).click(function() {
  $( this ).slideUp();
});
