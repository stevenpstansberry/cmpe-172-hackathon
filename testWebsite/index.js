// Initialize the map
var map = L.map('map').setView([0, 0], 2);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Dummy GeoJSON data - replace this with your real data
var geojsonData = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [0, 0] // Example coordinates
      },
      "properties": {
        "name": "Area 1"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [10, 10] // Example coordinates
      },
      "properties": {
        "name": "Area 2"
      }
    }
    // Add more features as needed
  ]
};

// Add GeoJSON layer with click event handling
L.geoJSON(geojsonData, {
  onEachFeature: function (feature, layer) {
    layer.on('mouseover', function () {
      var areaName = feature.properties.name;
      var question = prompt('Ask a question about ' + areaName + ':');

      // Call OpenAI API with the question and process the response
      if (question) {
        // Example: Fetch from OpenAI API
        fetch('YOUR_OPENAI_API_ENDPOINT', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_OPENAI_API_KEY'
          },
          body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
          alert('Answer: ' + data.answer);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
      }
    });
  }
}).addTo(map);
