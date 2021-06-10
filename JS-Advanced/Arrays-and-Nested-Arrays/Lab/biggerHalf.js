function solve(numbers) {
    numbers.sort((a, b) => a - b);

    let result = numbers.slice(numbers.length / 2);

    return result;
}

solve([3, 19, 14, 7, 2, 19, 6]);
