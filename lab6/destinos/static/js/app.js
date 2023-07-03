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