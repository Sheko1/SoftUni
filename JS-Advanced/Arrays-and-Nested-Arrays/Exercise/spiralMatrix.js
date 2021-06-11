function solve(rows, cols) {
    function isValid (row, col, matrix) {
        if (row >= 0 && row < matrix.length && col >= 0 && col < matrix[0].length) {
            if (matrix[row][col] === false) {
                return true
            }
        }
        return false

    }

    function generateMatrix () {
        let result = [];
        for (let row = 0; row < rows; row ++) {
            result.push([]);

            for (let col = 0; col < cols; col ++) {
                result[row].push(false);
            }

        }

        return result
    }

    let matrix = generateMatrix();
    let mapper = [[0, +1], [+1, 0], [0, -1], [-1, 0]];
    let value = 2;

    let row = 0;
    let col = 0;
    let size = (rows * cols) - 1;
    matrix[0][0] = 1;

    while (size > 0) {
        for (let move of mapper) {
            let currRow = row + move[0];
            let currCol = col + move[1];

            while (isValid(currRow, currCol, matrix)) {
                row = currRow;
                col = currCol;
                matrix[currRow][currCol] = value;
                value ++;
                size --;

                currRow += move[0];
                currCol += move[1];
            }
        }
    }

    let result = matrix.map(x => x.join(' '));

    return result.join('\n')
}

console.log(solve(3, 3))
