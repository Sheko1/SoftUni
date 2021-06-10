function solve(numbers) {
    let firstNumber = Number(numbers[0]);
    let lastNumber = Number(numbers[numbers.length - 1]);

    return firstNumber + lastNumber
}

console.log(solve(['20', '30', '40']))
