const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const N = +inputs[0];
const A = inputs.slice(1).map((input) => input.split(' ').map(Number));
const total = A.reduce((acc, cur) => acc + cur.reduce((a, c) => a + c, 0), 0);
let minDiff = Infinity;

function find5(board, x, y, d1, d2) {
  for (let i = 0; i <= d1; i++) {
    board[x + i][y - i] = 5;
    board[x + d2 + i][y + d2 - i] = 5;
  }

  for (let i = 0; i <= d2; i++) {
    board[x + i][y + i] = 5;
    board[x + d1 + i][y - d1 + i] = 5;
  }
}

for (let x = 0; x < N; x++) {
  for (let y = 0; y < N; y++) {
    for (let d1 = 1; d1 < N; d1++) {
      for (let d2 = 1; d2 < N; d2++) {
        if (x + d1 + d2 >= N) continue;
        if (y - d1 < 0 || y + d2 >= N) continue;

        const board = Array.from({ length: N }, () => Array(N).fill(0));
        find5(board, x, y, d1, d2);
        const sum = Array(5).fill(0);
        sum[4] = total;

        for (let i = 0; i < x + d1; i++) {
          for (let j = 0; j <= y; j++) {
            if (board[i][j]) break;
            sum[0] += A[i][j];
          }
        }
        for (let i = 0; i <= x + d2; i++) {
          for (let j = N - 1; j > y; j--) {
            if (board[i][j]) break;
            sum[1] += A[i][j];
          }
        }
        for (let i = x + d1; i < N; i++) {
          for (let j = 0; j < y - d1 + d2; j++) {
            if (board[i][j]) break;
            sum[2] += A[i][j];
          }
        }
        for (let i = x + d2 + 1; i < N; i++) {
          for (let j = N - 1; j >= y - d1 + d2; j--) {
            if (board[i][j]) break;
            sum[3] += A[i][j];
          }
        }

        for (let i = 0; i < 4; i++) {
          sum[4] -= sum[i];
        }
        minDiff = Math.min(minDiff, Math.max(...sum) - Math.min(...sum));
      }
    }
  }
}

console.log(minDiff);
