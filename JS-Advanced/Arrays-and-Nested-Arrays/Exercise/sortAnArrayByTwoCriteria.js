function solve(arr) {
    arr.sort((a, b) => {
        if (a.length - b.length === 0) {
            return a.localeCompare(b);
        }
        return a.length - b.length;
    })

    let result = '';
    arr.forEach(x => result += `${x}\n`);

    return result;
}

console.log(solve(['Isacc', 'Theodor', 'Jack', 'Harrison', 'George']));

