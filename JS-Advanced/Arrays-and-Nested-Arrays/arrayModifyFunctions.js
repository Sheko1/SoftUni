function pop(arr) {
    const lastElement = arr[arr.length - 1];
    arr.length --;
    return lastElement;

}

function push(arr, ...elements) {
    let index = arr.length;
    arr.length += elements.length;

    for (const el of elements) {
        arr[index] = el;
        index ++;
    }
}

function shift(arr) {
    let [...elements] = arr;
    arr.length --;

    for (let i = 0; i < arr.length; i++) {
        arr[i] = elements[i+1];
    }
    return elements[0];
}

function unshift(arr, ...elements) {
    const [...arrElements] = arr;
    arr.length += elements.length;
    const length = elements.length;

    for (let i = 0; i < arr.length; i++) {
        if (i < length) {
            arr[i] = elements[i];
            continue;
        }
        arr[i] = arrElements[i - length];
    }
}

let arr = [1, 2, 3, 4, 5];
let el = pop(arr);
console.log(arr, el);

arr = [1, 2, 3, 4, 5];
push(arr, 6, 7, 8, 9, 10);
console.log(arr);

arr = [1, 2, 3, 4, 5];
el = shift(arr);
console.log(arr, el);

arr = [1, 2, 3, 4, 5];
unshift(arr, -2, -1, 0);
console.log(arr);
