const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const directions = [
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
  [0, -1],
  [-1, -1],
];

const [N, M, K] = input[0].split(' ').map(Number);
const fireballs = input.slice(1).map((line) => line.split(' ').map(Number));

const moveFireballs = () => {
  const newMap = Array.from({ length: N }, () => Array.from({ length: N }, () => []));

  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (map[r][c].length === 0) continue;

      for (const [m, s, d] of map[r][c]) {
        const [dr, dc] = directions[d];
        const nr = (r + dr * s + N * 1000) % N;
        const nc = (c + dc * s + N * 1000) % N;
        newMap[nr][nc].push([m, s, d]);
      }
    }
  }

  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      if (newMap[r][c].length < 2) continue;

      let totalM = 0;
      let totalS = 0;

      for (const [m, s, d] of newMap[r][c]) {
        totalM += m;
        totalS += s;
      }

      const newM = Math.floor(totalM / 5);
      const newS = Math.floor(totalS / newMap[r][c].length);
      const isEvenOrOdd =
        Array.prototype.every.call(newMap[r][c], ([_, __, d]) => d % 2 === 0) ||
        Array.prototype.every.call(newMap[r][c], ([_, __, d]) => d % 2 === 1);

      newMap[r][c] = [];
      if (newM > 0) {
        for (let i = 0; i < 4; i++) {
          newMap[r][c].push([newM, newS, isEvenOrOdd ? 2 * i : 2 * i + 1]);
        }
      }
    }
  }

  return newMap;
};

let map = Array.from({ length: N }, () => Array.from({ length: N }, () => []));
for (const [r, c, m, s, d] of fireballs) {
  map[r - 1][c - 1].push([m, s, d]);
}

for (let i = 0; i < K; i++) {
  map = moveFireballs();
}

let result = 0;
for (let r = 0; r < N; r++) {
  for (let c = 0; c < N; c++) {
    if (map[r][c].length === 0) continue;

    for (const [m, s, d] of map[r][c]) {
      result += m;
    }
  }
}
console.log(result);
