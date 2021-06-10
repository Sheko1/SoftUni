function solve(arr) {
    let result = [arr.shift()];

    for (const el of arr) {
        if (result[result.length - 1] <= el) {
            result.push(el);
        }
    }

    return result
}

console.log(solve(
    [1,
        3,
        8,
        4,
        10,
        12,
        12,
        3,
        2,
        24]
))
