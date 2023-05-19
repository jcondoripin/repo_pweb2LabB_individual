function extraerGuiones() {
    let url = document.getElementById('urlMeet').value;
    let exp = /https:\/\/meet.google.com\/(.+)-(.+)-(.+)/;
    if(exp.test(url)){ // Si cumple con la expresión
        let result = url.match(exp);
        let res1 = result[1];
        let res2 = result[2];
        let res3 = result[3];
        let string = res1+res2+res3;
        insertCode(string);
    }else {
        console.log("Link de meet no valido");
    }
}
function insertCode(url) {
    let div = document.getElementById('result');
    div.innerHTML = url;
}