function solve(matrix) {
    let biggestNumber = -Infinity;

    for (const row of matrix) {
        for (const el of row) {
            if (biggestNumber < el) {
                biggestNumber = el;
            }
        }
    }

    return biggestNumber
}

console.log(solve([[3, 5, 7, 12],
    [-1, 4, 33, 2],
    [8, 3, 0, 4]]))
