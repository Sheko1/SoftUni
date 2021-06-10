function solve(matrix) {
    let rightDiagonal = 0;
    let leftDiagonal = 0;

    for (let i = 0; i < matrix.length; i ++) {
        rightDiagonal += matrix[i][i];
        leftDiagonal += matrix[i][matrix.length - i - 1];
    }

    return `${rightDiagonal} ${leftDiagonal}`
}


console.log(solve([[3, 5, 17],
    [-1, 7, 14],
    [1, -8, 89]]))
