function solve(numbers) {
    let result = [];

    numbers.forEach((x, i) => {
        if (i % 2 !== 0) {
            result.push(x * 2)
        }
    })
    result.reverse()
    return result
}

console.log(solve([10, 15, 20, 25]))
