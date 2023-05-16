function invertirText() {
    let string = "";
    let text = document.getElementById('text').value;
    for(let i = 0; i < text.length; i++) {
        string = text[i] + string;
    }
    document.getElementById('result').innerHTML = string;
}