function solve(numbers) {
    numbers.sort((a, b) => a - b);
    let result = numbers.slice(0, 2);

    return result.join(' ')
}

console.log(solve([3, 0, 10, 4, 7, 3]))
