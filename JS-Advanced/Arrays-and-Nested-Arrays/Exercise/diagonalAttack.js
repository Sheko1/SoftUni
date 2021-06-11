function solve(arr) {
    let diagonalIndexes = [];

    function getDiagonalSum(matrix) {
        let firstDiagonal = 0;
        let secondDiagonal = 0;

        for (let i = 0; i < matrix.length; i ++) {
            firstDiagonal += matrix[i][i];
            secondDiagonal += matrix[i][matrix[i].length - i - 1];
            diagonalIndexes.push(`${i} ${i}`, `${i} ${matrix[i].length - i - 1}`)
        }

        return [firstDiagonal, secondDiagonal];
    }

    let matrix = arr.map(x => x.split(' '));
    matrix = matrix.map(x => x.map(y => parseInt(y)));
    let [firstDiagonal, secondDiagonal] = getDiagonalSum(matrix);

    if (firstDiagonal === secondDiagonal) {
        for (let row = 0; row < matrix.length; row ++) {
            for (let col = 0; col < matrix[row].length; col ++) {
                if (diagonalIndexes.includes(`${row} ${col}`)) {
                    continue;

                }
                matrix[row][col] = firstDiagonal;
            }
        }
    }
    let result = matrix.map(x => x.join(' '));
    return result.join('\n');
}

console.log(solve(['5 3 12 3 1', '11 4 23 2 5', '101 12 3 21 10', '1 4 5 2 2', '5 22 33 11 1']))
