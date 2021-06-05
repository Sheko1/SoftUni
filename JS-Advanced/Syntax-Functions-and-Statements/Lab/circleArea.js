function solve(num) {
    let inputType = typeof num;

    if (inputType !== "number") {
        console.log(`We can not calculate the circle area, because we receive a ${inputType}.`);
    }

    else {
        let result = num ** 2 * Math.PI;
        console.log(result.toFixed(2));
    }
}

solve(5);