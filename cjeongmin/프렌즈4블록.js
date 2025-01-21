const EMPTY = "";

const isBlockMatch = (board, row, col) => {
    const current = board[row][col];
    return (
        current &&
        current === board[row + 1][col] &&
        current === board[row][col + 1] &&
        current === board[row + 1][col + 1]
    );
};

const findMatchingBlocks = (m, n, board) => {
    const matched = Array.from({ length: m }, () => Array(n).fill(false));
    let matchCount = 0;

    for (let i = 0; i + 1 < m; i++) {
        for (let j = 0; j + 1 < n; j++) {
            if (isBlockMatch(board, i, j)) {
                matched[i][j] = matched[i + 1][j] = matched[i][j + 1] = matched[i + 1][j + 1] = true;
            }
        }
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (matched[i][j]) {
                board[i][j] = EMPTY;
                matchCount++;
            }
        }
    }

    return matchCount;
};

const down = (m, n, board) => {
    for (let col = 0; col < n; col++) {
        let bottomRow = m - 1;
        for (let row = m - 1; row >= 0; row--) {
            if (board[row][col] !== EMPTY) {
                if (bottomRow !== row) {
                    board[bottomRow][col] = board[row][col];
                    board[row][col] = EMPTY;
                }
                bottomRow--;
            }
        }
    }
};

function solution(m, n, board) {
    const gameBoard = board.map((row) => Array.from(row));
    let ans = 0;

    while (true) {
        const removedBlocks = findMatchingBlocks(m, n, gameBoard);
        if (removedBlocks === 0) break;

        ans += removedBlocks;
        down(m, n, gameBoard);
    }

    return ans;
}
