function carregaMapa(){

    var lat = document.getElementById('lat').value
    var lon = document.getElementById('lon').value

    if(lat == '' || lon == ''){
        lat = -22.728619
        lon = -47.646921
    }

    var map = L.map('map', 
                {center: [lat, lon], 
                zoom: 15});

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> - MAPA DAS FRUTAS'
        }).addTo(map);


    L.marker([lat,lon]).addTo(map);

}