
var osmlayer =  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
	id: 'mapbox.streets'
});
var none_layer =  L.tileLayer('', {
	maxZoom: 18,
	attribution: 'Empty'
});
var map = L.map('map', {
    center: [-1.0500, 37.0833],
    zoom: 10,
    minZoom:2,
    maxZoom:18,
    zoomControl: false,
    layers:[osmlayer,]
});

var county_map = L.geoJson(countydata,{
	onEachFeature:function(feature, layer){
		var popupContent = 'County Name: ' + feature.properties.name_2;
		if (feature.properties && feature.properties.popupContent){
			popupContent += feature.properties.popupContent;
		}
		layer.bindPopup(popupContent);
		layer.on({
			click:function(e){
				map.fitBounds(e.target.getBounds())
			}
		});
	},
	style:function(feature){
		return{
			fillColor:'#f2f2f2',
			weight:1,
			opacity:1,
			color:'#000000',
			fillOpacity:0.7
		}
	}
}).addTo(map);
map.fitBounds(county_map.getBounds());
//Shambas Map and Styling
function getColor(d) {
    return d > 250	? '#ff0000' :
           d > 1  	? '#6666ff' :
           d > 'Null' ? '#00ff00' :           
                      '#00ff00';
}
var shambas = L.geoJson(shambadata,{
	onEachFeature:onEachFeature,
	style:function(feature){
		return {
			fillColor:getColor(feature.properties.balance),
			weight:0.5,
			opacity:1,
			color:'#000000',
			fillOpacity:0.7
		}
	}
});
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

var constituencies_map = L.geoJson(constituenciesdata,{
	onEachFeature:function(feature, layer) {
		var popupContent = feature.properties.const_nam + ' Constituency';
		if (feature.properties && feature.properties.popupContent){
			popupContent += feature.properties.popupContent;
		}
		layer.bindPopup(popupContent);
		layer.on({
			click:function(e){
				map.fitBounds(e.target.getBounds())
			}
		});
	},	
	style:function(feature){
		return{
			fillColor:'#ffff66',
			weight: 1,
			opacity: 1,
			color: '#000000',
			fillOpacity: 0.7
		}
	}
});
//Layer Button
var overlays = {
	"County Map":county_map,
	"Constituencies":constituencies_map,	
	"Shambas": shambas
};
//Baslayers button
var baseLayers = {
	"Osm Layer": osmlayer,
	"None":none_layer
};
L.control.layers(baseLayers, overlays).addTo(map);
var zoomHome = L.Control.zoomHome({
	position: 'topleft',
	homeCoordinates:[-1.0500, 37.0833],
	homeZoom:10
}).addTo(map);