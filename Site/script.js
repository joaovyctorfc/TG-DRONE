let h2 = document.querySelector('h2');
let map;

function initializeMap(latitude, longitude) {
    if (map) {
        map.remove();
    }
    map = L.map('map').setView([latitude, longitude], 1000);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([latitude, longitude]).addTo(map)
        .bindPopup('Sua localização está aqui')
        .openPopup();
}

function updateLocation(pos) {
    console.log(pos);
    h2.textContent = `Latitude: ${pos.coords.latitude}, Longitude: ${pos.coords.longitude}`;

    if (!map) {
        initializeMap(pos.coords.latitude, pos.coords.longitude);
    }
}

function handleGeolocationSuccess(pos) {
    updateLocation(pos);
}

function handleGeolocationError(error) {
    console.log(error);
}

navigator.geolocation.getCurrentPosition(handleGeolocationSuccess, handleGeolocationError, {
    enableHighAccuracy: true,
    timeout: 5000
});