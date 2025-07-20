const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = inputs[0].split(' ').map(Number);
const board = inputs.slice(1);
const directs = { D: [1, 0], U: [-1, 0], L: [0, -1], R: [0, 1] };
const visited = Array.from({ length: N }, () => Array(M).fill(0));
let answer = 0;

function dfs(row, col) {
  visited[row][col] = 1;

  const direct = directs[board[row][col]];
  const nr = row + direct[0];
  const nc = col + direct[1];

  if (visited[nr][nc] === 0) {
    if (dfs(nr, nc)) {
      visited[row][col] = 2;
      return true;
    }
  } else if (visited[nr][nc] === 1) {
    visited[row][col] = 2;
    return true;
  }

  visited[row][col] = 2;
  return false;
}

for (let r = 0; r < N; r++) {
  for (let c = 0; c < M; c++) {
    if (visited[r][c]) continue;
    if (dfs(r, c)) answer++;
  }
}

console.log(answer);
