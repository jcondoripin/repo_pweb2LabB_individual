function getNumbertoDay(Number) {
    let days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    return days[Number];
}

console.log(getNumbertoDay(0)); // Para dia cualquiera
console.log(getNumbertoDay(new Date().getDay())) // Dia actual