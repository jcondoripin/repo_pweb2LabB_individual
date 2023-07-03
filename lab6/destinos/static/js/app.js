function search() {
    let input = document.getElementById('inputSearch').value;
    
    let rows = Array.from(document.getElementsByClassName('trow'));

    rows.forEach(row => {
        let nameCity = row.childNodes.item(5).textContent;
        if (nameCity.toLowerCase().includes(input.toLowerCase())) {
            row.style.display = ''; 
        } else {
            row.style.display = 'none';
        }
    })
}

function changeEdit(row) {
    let id = row.childNodes.item(1).textContent;
    window.location.pathname = `/show/${id}`;
}

function displaySale(check) {
    let input = document.getElementById('inDescuento');
    let option = document.getElementById('opDescuento');

    if (check.checked) {
        input.removeAttribute('disabled');
        option.removeAttribute('disabled');
    } else {
        input.setAttribute('disabled', true);
        option.setAttribute('disabled', true);
    }
}

// Para no borrar el precio inicial
const precioInicial = document.getElementById('precioTour').value; 
function descontar() {

    let precio = document.getElementById('precioTour');
    let descuento = document.getElementById('inDescuento').value;
    
    precio.value = precioInicial * (1 - descuento / 100);

}