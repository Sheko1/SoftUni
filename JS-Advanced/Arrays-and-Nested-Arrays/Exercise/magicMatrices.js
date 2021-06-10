function solve(matrix) {
    function checkRow (index) {
        return matrix[index].reduce((a, x) => a + x, 0);
    }

    function checkCol (index) {
        let result = 0;

        for (let i = 0; i < matrix.length; i ++) {
            result += matrix[i][index];
        }

        return result
    }

    const sumOfFirstRow = checkRow(0);

    for (let i = 0; i < matrix.length; i ++){
        if (checkRow(i) !== sumOfFirstRow || checkCol(i) !== sumOfFirstRow) {
            return false
        }
    }

    return true
}

console.log(solve([[1, 0, 0],
    [0, 0, 1],
    [0, 1, 0]]))
