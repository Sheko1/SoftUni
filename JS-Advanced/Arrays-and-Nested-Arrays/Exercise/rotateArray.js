function solve(arr, n) {
    for (let i = 0; i < n; i ++) {
        arr.unshift(arr.pop());
    }

    return arr.join(' ');
}

console.log(solve(['1', '2', '3', '4'], 2));
