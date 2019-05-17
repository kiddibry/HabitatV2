var homes = ['Castle', 'Apartment', 'Galaxy', 'Condo', 'Palace', 'Mansion', 'Citadel', 'Flat', 'Suite', 'Home',]

function randomWholeNumber() {
    return Math.floor(Math.random() * 10);
}

function change() {
    document.getElementById("ran_hom").innerHTML = homes[randomWholeNumber()]
}

window.onload = function() {
    change();
}

document.getElementById("ran_hom").addEventListener("click", change);