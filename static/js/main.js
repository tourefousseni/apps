
var map = L.map('map').setView([27.2, 83.95], 10);

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreet map</a> DNGR 2021'
});

osm.addTo(map);

var marker = L.marker([27.2, 83.95].addTo(map));


