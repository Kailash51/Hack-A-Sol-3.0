function initMap() {
  var mapOptions = {
    zoom: 8,
    center: { lat: 20.5937, lng: 78.9629 },
  };
  var map = new google.maps.Map(document.getElementById("map"), mapOptions);

  document.getElementById("latitude").addEventListener("input", function () {
    var lat = parseFloat(document.getElementById("latitude").value);
    var lng = parseFloat(document.getElementById("longitude").value);
    var marker = new google.maps.Marker({
      position: { lat: lat, lng: lng },
      map: map,
    });
    map.setCenter({ lat: lat, lng: lng });
  });
}
