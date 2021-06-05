function solve(num1, num2) {
    let small;
    let result;

    if (num1 > num2) {
        small = num2;
    }
    else {
        small = num1;
    }

    for (let i = 0; i <=small; i++) {
        if (num1 % i === 0 && num2 % i === 0) {
            result = i
        }
    }

    return result
}

console.log(solve(15, 5))