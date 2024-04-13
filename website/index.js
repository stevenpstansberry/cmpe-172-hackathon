
// Initialize the map
var map = L.map('map').setView([51.505, -0.09], 2);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Dummy GeoJSON data - get from scrapper
var geojsonData = {

// inset data here

};

// Add GeoJSON layer
L.geoJSON(geojsonData, {
  onEachFeature: function (feature, layer) {
    layer.on('click', function () {
      // Add your click event logic here
      alert('Clicked on ' + feature.properties.name);
    });
  }
}).addTo(map);
