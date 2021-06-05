function solve(num) {
    let star = '* ';
    let result = '';

    for (let i = 1; i <= num; i++) {
        result += star.repeat(num) + '\n'
    }
    return result
}

console.log(solve(5))
