function solve(numbers) {
    let sumResult = 0;
    let sumResult1 = 0;
    let concat = '';

    for (let i = 0; i < numbers.length; i++) {
        sumResult += numbers[i]
        sumResult1 += 1 / numbers[i]
        concat += numbers[i]
    }

    return `${sumResult}\n${sumResult1}\n${concat}`
}

console.log(solve([2, 4, 8, 16]))
