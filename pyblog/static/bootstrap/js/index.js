
var map = L.map('map').setView([13.22, -5.16], 10);

var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreet map</a> OMB 2021',
    });
        osm.addTo(map);

var watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        subdomains: 'abcd',
        minZoom: 1,
        maxZoom: 16,
        ext: 'jpg'
    });
       watercolor.addTo(map);

var darkLayer = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 19
    });
      darkLayer.addTo(map);


var esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: ''
        // 'Tiles &copy; Esri &mdash; Source: Esri'
    });
        esri_WorldImagery.addTo(map);


var baseLayers = {
        "water color": watercolor,
        "esri Imagery": esri_WorldImagery,
        "dark layer map": darkLayer,
         osm : osm,
    };
       L.control.layers(baseLayers).addTo(map);


var marker = L.marker([13.22, -5.16], {
        draggable :true,
        title: 'REPERE',
        opacity: 0.5,
    })
        .addTo(map)
        .bindPopup('<h1>Marker</h1><p>This is the marker text</p>');

    // GEOSERVER REQUEST

var wmsLayer = L.Geoserver.wms("http://localhost:8080/geoserver/wms", {
        layers: 'tiger:tiger_roads',
      });
        wmsLayer.addTo(map);




    // $( "p" ).click(function() {
    //   $( this ).slideUp()
    //   });




