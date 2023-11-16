function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    var x = document.getElementById("demo");
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
  
function showPosition(position) {
  document.getElementById('lat').value = position.coords.latitude
  document.getElementById('lon').value = position.coords.longitude

  localStorage.setItem("lat",position.coords.latitude)
  localStorage.setItem("lon",position.coords.longitude)
}
