var homes = ['castle', 'apartment', 'house', 'condo', 'palace', 'mansion', 'citadel', 'flat', 'suite', 'home']

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