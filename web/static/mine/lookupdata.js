window.onload = function () {
  var osmlayer = L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution:
      'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
      '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery © <a href="http://mapbox.com">Mapbox</a>',
    id: "mapbox.streets",
  });
  var none_layer = L.tileLayer("", {
    maxZoom: 18,
    attribution: "Empty",
  });
  var map = L.map("map", {
    center: [-1.05, 37.0833],
    zoom: 10,
    minZoom: 2,
    maxZoom: 18,
    zoomControl: false,
    layers: [osmlayer],
  });

  var selectedItem = document.getElementById("selected-item");
  var originalContent = selectedItem.innerHTML;

  var county_map = L.geoJson(countydata, {
    onEachFeature: function (feature, layer) {
      var popupContent = "County Name: " + feature.properties.name_2;
      if (feature.properties && feature.properties.popupContent) {
        popupContent += feature.properties.popupContent;
      }
      layer.bindPopup(popupContent);
      layer.on({
        add: function (e) {
          map.fitBounds(e.target.getBounds());
        },
        remove: function (e) {
          selectedItem.innerHTML = originalContent;
        },
        click: function (e) {
          map.fitBounds(e.target.getBounds());
          selectedItem.innerHTML = `
					<h3>County</h3>
					<h3>Name: ${feature.properties.name_2}</h3>
				`;
        },
      });
    },
    style: function (feature) {
      return {
        fillColor: "#f2f2f2",
        weight: 1,
        opacity: 1,
        color: "#000000",
        fillOpacity: 0.7,
      };
    },
  });
  // map.fitBounds(county_map.getBounds());
  //Shambas Map and Styling
  const colors = {
    gte250: "#ff0000",
    gte1: "#6666ff",
    Null: "#00ff00",
    default: "#00ff00",
  };
  function getColor(d) {
    return d > 250
      ? colors.gte250
      : d > 1
      ? colors.gte1
      : d > "Null"
      ? colors.Null
      : colors.default;
  }
  var addingLayers = false;

  var shambas = L.geoJson(shambadata, {
    onEachFeature: function (feature, layer) {
      var name = feature.properties.owner;
      var htmlName = "";
      if (name) {
        htmlName = "Name: " + name + "<br>";
      }
      var popupContent =
        "Balance " +
        feature.properties.balance +
        "<br>" +
        htmlName +
        "Zone: " +
        feature.properties.zone +
        "<br>" +
        "Type Of Lease: " +
        feature.properties.type_of_lease +
        "<br>" +
        "Period Of Lease: " +
        feature.properties.period_of_lease +
        "<br>" +
        "Land Use: " +
        feature.properties.land_use +
        "<br>";
      if (feature.properties && feature.properties.popupContent) {
        popupContent += feature.properties.popupContent;
      }
      layer.bindPopup(popupContent);
      layer.on({
        remove: function (e) {
          selectedItem.innerHTML = originalContent;
        },
        click: function (e) {
          map.fitBounds(e.target.getBounds(), { padding: [100, 100] });
          selectedItem.innerHTML = `
          <h2>Shamba</h2>
          <h3>Owner: ${feature.properties.owner}</h3>
          <h3>Balance: ${feature.properties.balance}</h3>
          <h3>Zone: ${feature.properties.zone}</h3>
          <h3>Type Of Lease: ${feature.properties.type_of_lease}</h3>
          `;
        },
      });
    },
    style: function (feature) {
      return {
        fillColor: getColor(feature.properties.balance),
        weight: 0.5,
        opacity: 1,
        color: "#000000",
        fillOpacity: 0.7,
      };
    },
  });
  //   console.log(shambas);
  map.fitBounds(shambas.getBounds());
  shambas.addTo(map);
  //Constituencies Map
  // onEachFeature:function(feature, layer){
  // 	var popupContent = 'County Name: ' + feature.properties.name_2;
  // 	if (feature.properties && feature.properties.popupContent){
  // 		popupContent += feature.properties.popupContent;
  // 	}
  // 	layer.bindPopup(popupContent);
  // 	layer.on({
  // 		click:function(e){
  // 			map.fitBounds(e.target.getBounds())
  // 		}
  // 	});
  // },

  var constituencies_map = L.geoJson(constituenciesdata, {
    onEachFeature: function (feature, layer) {
      var popupContent = feature.properties.const_nam + " Constituency";
      if (feature.properties && feature.properties.popupContent) {
        popupContent += feature.properties.popupContent;
      }
      layer.bindPopup(popupContent);
      layer.on({
        click: function (e) {
          map.fitBounds(e.target.getBounds());
        },
      });
    },
    style: function (feature) {
      return {
        fillColor: "#ffff66",
        weight: 1,
        opacity: 1,
        color: "#000000",
        fillOpacity: 0.7,
      };
    },
  });
  //Layer Button
  var overlays = {
    Shambas: shambas,
    "County Map": county_map,
    Constituencies: constituencies_map,
  };
  //Baslayers button
  var baseLayers = {
    "Osm Layer": osmlayer,
    None: none_layer,
  };
  L.control.layers(baseLayers, overlays).addTo(map);
  var zoomHome = L.Control.zoomHome({
    position: "topleft",
    homeCoordinates: [-1.05, 37.0833],
    homeZoom: 10,
  }).addTo(map);

  L.control
    .Legend({
      position: "bottomleft",
      title: "Shamba Balance",
      symbolWidth: 10,
      legends: [
        {
          label: "Bal > 250",
          type: "rectangle",
          color: colors.gte250,
          fillColor: colors.gte250,
          weight: 1,
          opacity: 1,
          fillOpacity: 0.7,
          weight: 10,
        },
        {
          label: "Bal < 250",
          type: "rectangle",
          color: colors.gte1,
          fillColor: colors.gte1,
          weight: 1,
          opacity: 1,
          fillOpacity: 0.7,
          weight: 10,
        },
        {
          label: "Bal = Unknown",
          type: "rectangle",
          color: colors.Null,
          fillColor: colors.Null,
          weight: 1,
          opacity: 1,
          fillOpacity: 0.7,
          weight: 10,
        },
      ],
    })
    .addTo(map);
};
