function solve(arr) {
    let result = [];
    let arrLength = arr.length;
    arr.sort((a, b) => a - b);

    for (let i = 0; i < arrLength / 2; i ++) {
        result.push(arr[i]);
        result.push(arr[arrLength - 1 - i]);
    }

    return result.slice(0, arrLength);
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
