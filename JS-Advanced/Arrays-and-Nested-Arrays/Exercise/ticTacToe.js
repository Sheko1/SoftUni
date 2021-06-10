function solve (commands) {
    function getCurrPlayer (players) {
        let currPlayer = players.shift();
        players.push(currPlayer);

        return currPlayer;
    }

    function checkHorizontalWin (player, board, rowIndex) {
        for (let i = 0; i < board[rowIndex].length; i ++) {
            if (board[rowIndex][i] !== player) {
                return false;
            }
        }

        return true;
    }

    function checkVerticalWin (player, board, colIndex) {
        for (let i = 0; i < board.length; i++) {
            if (board[i][colIndex] !== player) {
                return false;
            }
        }

        return true;
    }

    function checkRightDiagonalWin (player, board) {
        for (let i = 0; i < board.length; i ++) {
            if (board[i][i] !== player) {
                return false;
            }
        }

        return true;

    }

    function checkLeftDiagonalWin(player, board) {
        for (let i = 0; i < board.length; i ++) {
            if (board[i][board.length - i - 1] !== player) {
                return false;
            }
        }

        return true;
    }

    let players = ['X', 'O'];
    let board = [
        [false, false, false],
        [false, false, false],
        [false, false, false],

    ];
    let boardFreeSpace = 9;

    for (const el of commands) {
        let [row, col] = el.split(' ');
        row = Number(row);
        col = Number(col);

        if (board[row][col] !== false) {
            console.log('This place is already taken. Please choose another!');
            continue;
        }

        let player = getCurrPlayer(players);
        board[row][col] = player;
        boardFreeSpace -= 1;

        if (boardFreeSpace === 0) {
            console.log('The game ended! Nobody wins :(');
            board.forEach(x => console.log(x.join('\t')));
            return;
        }

        else if (checkHorizontalWin(player, board, row) || checkVerticalWin(player, board, col) ||
            checkRightDiagonalWin(player, board) || checkLeftDiagonalWin(player, board)) {

            console.log(`Player ${player} wins!`);
            board.forEach(x => console.log(x.join('\t')));
            return;
        }
    }

}

solve(["0 1", "0 0", "0 2", "2 0", "1 0", "1 1", "1 2", "2 2", "2 1", "0 0"]);
