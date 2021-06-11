function solve(arr) {
    let [rows, cols] = [arr.shift(), arr.shift()];
    let [startRow, startCol] = [arr.shift(), arr.shift()];
    let matrix = [];

    for (let row = 0; row < rows; row ++) {
        matrix.push([]);

        for (let col = 0; col < cols; col ++) {
            matrix[row][col] = Math.max(Math.abs(row - startRow), Math.abs(col - startCol)) + 1;
        }
    }

    let result = matrix.map(x => x.join(' '));
    return result.join('\n')

}

console.log(solve([5, 5, 2, 2]))
