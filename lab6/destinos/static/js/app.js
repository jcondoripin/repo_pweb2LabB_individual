function search() {
    let input = document.getElementById('inputSearch').value;
    
    let rows = Array.from(document.getElementsByClassName('trow'));

    rows.forEach(row => {
        let nameCity = row.childNodes.item(3).textContent;
        if (nameCity.toLowerCase().includes(input.toLowerCase())) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    })
}

function changeForm() {
    
}