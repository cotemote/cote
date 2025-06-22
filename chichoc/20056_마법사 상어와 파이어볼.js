const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const [N, M, K] = inputs[0].split(' ').map(Number);
const balls = inputs.slice(1).map((ball) => ball.split(' ').map(Number));
const dirs = [
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
  [0, -1],
  [-1, -1]
];

for (let turn = 0; turn < K; turn++) {
  const board = Array.from({ length: N }, () => Array.from({ length: N }, () => []));
  for (const [r, c, m, s, d] of balls) {
    const nr = (r + ((dirs[d][0] * s) % N) + N * 1000) % N;
    const nc = (c + ((dirs[d][1] * s) % N) + N * 1000) % N;
    board[nr][nc].push([nr, nc, m, s, d]);
  }

  balls.length = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const cell = board[i][j];
      if (cell.length === 0) continue;
      if (cell.length === 1) {
        balls.push(cell[0]);
      } else {
        let sumM = 0,
          sumS = 0,
          allEven = true,
          allOdd = true;
        for (const [r, c, m, s, d] of cell) {
          sumM += m;
          sumS += s;
          if (d % 2 === 0) allOdd = false;
          else allEven = false;
        }
        const nm = Math.floor(sumM / 5);
        if (nm === 0) continue;
        const ns = Math.floor(sumS / cell.length);
        const nds = allEven || allOdd ? [0, 2, 4, 6] : [1, 3, 5, 7];
        for (const nd of nds) {
          balls.push([i, j, nm, ns, nd]);
        }
      }
    }
  }
}

console.log(balls.reduce((sumM, ball) => sumM + ball[2], 0));
