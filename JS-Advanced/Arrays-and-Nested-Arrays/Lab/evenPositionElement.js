function solve(input) {
    let result = [];

    for (let i = 0; i < input.length; i += 2) {
        result.push(input[i]);
    }

    return result.join(' ');
}

console.log(solve(['20', '30', '40', '50', '60']));
