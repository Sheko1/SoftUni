function solve(n, k) {
    let arr = [1];

    for (let i = 1; i < n; i++) {
        let subArr = arr.slice(-k);
        let number = subArr.reduce((a, x) => a + x, 0)
        arr.push(number)
    }

    return arr
}

console.log(solve(6, 3));
