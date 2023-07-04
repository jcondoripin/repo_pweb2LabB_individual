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
function deleteDestiny(e) {
    e.stopPropagation();
    let row = e.target.parentNode.parentNode;
    let id = row.childNodes[1].textContent;
    let token = document.querySelector('#token').value;
    fetch(`/delete/${id}`, { 
        method: 'DELETE',
        headers: {
            'X-CSRFToken': token
        }
    })
    .then(res => res.text())
    .then(data => {

        row.remove();

        // Crear el elemento del toast
        const toast = document.createElement('div');
        toast.classList.add('toast');
        toast.classList.add('show');
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');
        toast.setAttribute('data-bs-autohide', 'true');
        toast.setAttribute('data-bs-delay', '3000');

        // Crear el encabezado del toast
        const toastHeader = document.createElement('div');
        toastHeader.classList.add('toast-header');
        toastHeader.classList.add('bg-primary');
        toast.appendChild(toastHeader);

        // Agregar el título al encabezado
        const title = document.createElement('strong');
        title.classList.add('me-auto');
        title.classList.add('text-white');
        title.textContent = 'DestinyApp';
        toastHeader.appendChild(title);

        // Agregar el botón de cierre al encabezado
        const closeButton = document.createElement('button');
        closeButton.setAttribute('type', 'button');
        closeButton.classList.add('btn-close');
        closeButton.setAttribute('data-bs-dismiss', 'toast');
        closeButton.setAttribute('aria-label', 'Cerrar');
        toastHeader.appendChild(closeButton);

        // Agregar el contenido al cuerpo del toast
        const toastBody = document.createElement('div');
        toastBody.classList.add('toast-body');
        toastBody.textContent = data;
        toast.appendChild(toastBody);

        // Agregar el toast al contenedor
        const toastContainer = document.getElementById('toast-container');
        toastContainer.appendChild(toast);

        // Mostrar el toast
        const bsToast = new bootstrap.Toast(toast, { autohide: true, delay: 3300 });
        bsToast.show();

        toast.addEventListener('hidden.bs.toast', () => {
            toast.remove();
        });
    })
    .catch(err => {
        // Crear el elemento del toast
        const toast = document.createElement('div');
        toast.classList.add('toast');
        toast.classList.add('show');
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');
        toast.setAttribute('data-bs-autohide', 'true');
        toast.setAttribute('data-bs-delay', '3000');

        // Crear el encabezado del toast
        const toastHeader = document.createElement('div');
        toastHeader.classList.add('toast-header');
        toastHeader.classList.add('bg-primary');
        toast.appendChild(toastHeader);

        // Agregar el título al encabezado
        const title = document.createElement('strong');
        title.classList.add('me-auto');
        title.classList.add('text-white');
        title.textContent = 'DestinyApp';
        toastHeader.appendChild(title);

        // Agregar el botón de cierre al encabezado
        const closeButton = document.createElement('button');
        closeButton.setAttribute('type', 'button');
        closeButton.classList.add('btn-close');
        closeButton.setAttribute('data-bs-dismiss', 'toast');
        closeButton.setAttribute('aria-label', 'Cerrar');
        toastHeader.appendChild(closeButton);

        // Agregar el contenido al cuerpo del toast
        const toastBody = document.createElement('div');
        toastBody.classList.add('toast-body');
        toastBody.textContent = err;
        toast.appendChild(toastBody);

        // Agregar el toast al contenedor
        const toastContainer = document.getElementById('toast-container');
        toastContainer.appendChild(toast);

        // Mostrar el toast
        const bsToast = new bootstrap.Toast(toast, { autohide: true, delay: 3300 });
        bsToast.show();

        toast.addEventListener('hidden.bs.toast', () => {
            toast.remove();
        });
    });
}

// function deleteDestiny(e) {
//     e.stopPropagation();
//     let row = e.target.parentNode.parentNode;
//     let id = row.childNodes[1].textContent;
//     let token = document.querySelector('#token').value;
//     fetch(`/delete/${id}`, { 
//         method: 'DELETE',
//         headers: {
//             'X-CSRFToken': token
//         }
//     })
//     .then(res => res.text())
//     .then(data => {
//         // Crear el elemento del toast
//         const toast = document.createElement('div');
//         toast.classList.add('toast');
//         toast.classList.add('show');
//         toast.setAttribute('role', 'alert');
//         toast.setAttribute('aria-live', 'assertive');
//         toast.setAttribute('aria-atomic', 'true');
//         toast.setAttribute('data-bs-autohide', 'true');
//         toast.setAttribute('data-bs-delay', '3000');

//         // Agregar el contenido al toast
//         toast.innerHTML = `
//         <div class="toast-header bg-success">
//             <strong class="me-auto text-white">Confirmación</strong>
//             <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Cerrar"></button>
//         </div>
//         <div class="toast-body">${data}</div>
//         `;

//         // Agregar el toast al contenedor
//         const toastContainer = document.getElementById('toast-container');
//         toastContainer.appendChild(toast);

//         // Mostrar el toast
//         const bsToast = new bootstrap.Toast(toast, { autohide: true, delay: 3300 });
//         bsToast.show();

//         toast.addEventListener('hidden.bs.toast', () => {
//             toast.remove();
//         });
//     })
//     .catch(err => {
//         // Crear el elemento del toast
//         const toast = document.createElement('div');
//         toast.classList.add('toast');
//         toast.classList.add('show');
//         toast.setAttribute('role', 'alert');
//         toast.setAttribute('aria-live', 'assertive');
//         toast.setAttribute('aria-atomic', 'true');
//         toast.setAttribute('data-bs-autohide', 'true');
//         toast.setAttribute('data-bs-delay', '3000');

//         // Agregar el contenido al toast
//         toast.innerHTML = `
//         <div class="toast-header bg-danger">
//             <strong class="me-auto text-white">Error</strong>
//             <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Cerrar"></button>
//         </div>
//         <div class="toast-body">${err}</div>
//         `;

//         // Agregar el toast al contenedor
//         const toastContainer = document.getElementById('toast-container');
//         toastContainer.appendChild(toast);

//         // Mostrar el toast
//         const bsToast = new bootstrap.Toast(toast, { autohide: true, delay: 3300 });
//         bsToast.show();

//         toast.addEventListener('hidden.bs.toast', () => {
//             toast.remove();
//         });
//     })
// }

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
const inputPrecio = document.getElementById('precioTour'); 
const precioInicial = inputPrecio != null ? inputPrecio.value : 0;
function descontar() {

    let precio = document.getElementById('precioTour');
    let descuento = document.getElementById('inDescuento').value;
    
    precio.value = precioInicial * (1 - descuento / 100);

}