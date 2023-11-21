function removeAcento (text){       
    text = text.toLowerCase();                                                         
    text = text.replace(new RegExp('[ÁÀÂÃ]','gi'), 'a');
    text = text.replace(new RegExp('[ÉÈÊ]','gi'), 'e');
    text = text.replace(new RegExp('[ÍÌÎ]','gi'), 'i');
    text = text.replace(new RegExp('[ÓÒÔÕ]','gi'), 'o');
    text = text.replace(new RegExp('[ÚÙÛ]','gi'), 'u');
    text = text.replace(new RegExp('[Ç]','gi'), 'c');
    return text;                 
}


function carregaMapa(){

    var lat = window.localStorage.getItem("lat")//document.getElementById('lat').value
    var lon = window.localStorage.getItem("lon")//document.getElementById('lon').value

    if(lat == '' || lon == ''){
        lat = -22.728619
        lon = -47.646921
    }

    document.getElementById('carregando').innerHTML = '';

    var map = L.map('map', 
                {center: [lat, lon], 
                zoom: 15});

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> - MAPA DAS FRUTAS'
        }).addTo(map);


    L.marker([lat,lon]).addTo(map);


    var greenIcon = L.icon({
        iconUrl: 'leaf-green.png',
        shadowUrl: 'leaf-shadow.png',
    
        iconSize:     [38, 95], // size of the icon
        shadowSize:   [50, 64], // size of the shadow
        iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
        shadowAnchor: [4, 62],  // the same for the shadow
        popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
    });

    
    for (var a = 0; a<pontos.length; a++){
        ar = pontos[a]
        var lat1 = ar[0]
        var lon1 = ar[1]
        var pop = ar[2] 
        var id = ar[3]
        var iconeUrl = "../static/imgs/icones/"+removeAcento(pop.toLowerCase())+".png"

        var icone = L.icon({
            iconUrl: iconeUrl,
            shadowUrl: '../static/imgs/icones/sombra.png',
        
            iconSize:     [50, 50], // size of the icon
            shadowSize:   [50, 50], // size of the shadow
            iconAnchor:   [22, 38], // point of the icon which will correspond to marker's location
            shadowAnchor: [15, 33],  // the same for the shadow
            popupAnchor:  [-3, -25] // point from which the popup should open relative to the iconAnchor
        });

        texto = "<span style='font-size: 20px; font-weight: bold'>"+pop+"</span>"
        texto += "<br>Confirmado: 1"
        texto += "<br><a href='/verFruta/"+id+"'>Ver Fruta</a>"
        texto += "<br>latitude: " +lat1
        texto += "<br>longitude: " +lon1

        L.marker([lat1, lon1], {icon: icone}).addTo(map)
            .bindPopup(texto);

        // L.circleMarker([lat1+0.0001, lon1], {radius: 20}).addTo(map);
    }


}