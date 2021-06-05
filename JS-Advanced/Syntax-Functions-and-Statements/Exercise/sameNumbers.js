function solve(number) {
    number = String(number);
    let firstNumber = number[0];
    let sumResult = 0;
    let result = true;

    for (let i = 0; i < number.length; i++) {
        if (number[i] !== firstNumber && result) {
            result = false;
        }
        sumResult += Number(number[i]);
    }

    return `${result}\n${sumResult}`;
}

console.log(solve(1234))
