function diasFaltantesArequipa() {
    let diaArequipa = new Date("2023-07-15");
    let diaActual = new Date();
    
    let diasFaltantes = diaArequipa - diaActual; // ms
    diasFaltantes = diasFaltantes / 1000 / 60 / 60 / 24;
    diasFaltantes = Math.ceil(diasFaltantes);

    document.getElementById('result').innerHTML = diasFaltantes;
}

document.onload = diasFaltantesArequipa();