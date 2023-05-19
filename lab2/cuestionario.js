function arrayGenerator1(n, min, max) {
    let a = [];
    let x;
    for (x = 0; x < n; x += 1) {
        a.push(Math.ceil(Math.random() * (max - min) + min));
    }
    return a;
}

function arrayGenerator2(n, min, max) {
    let i;
    let arr = new Array(n);
    for (i = 0; i < n; i += 1) {
        arr[i] = 1;
    }
    arr = arr.map(function (x) {
        return x * Math.ceil(Math.random() * (max - min) + min);
    });
    return arr;
}

let array1 = arrayGenerator1(5,0,10);
console.log(array1);

let array2 = arrayGenerator2(5,0,10);
console.log(array2);
