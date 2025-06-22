const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const N = Number(input[0]);
const A = input.slice(1).map((line) => line.split(' ').map(Number));

const isValid = (y, x, d1, d2) => y + d1 + d2 < N && x - d1 >= 0 && x + d2 < N;

const getPopulation = (y, x, d1, d2) => {
  const population = Array(5).fill(0);
  const district = Array.from({ length: N }, () => Array(N).fill(0));

  for (let i = 0; i <= d1; i++) {
    district[y + i][x - i] = 5;
  }

  for (let i = 0; i <= d2; i++) {
    district[y + i][x + i] = 5;
  }

  for (let i = 0; i <= d2; i++) {
    district[y + d1 + i][x - d1 + i] = 5;
  }

  for (let i = 0; i <= d1; i++) {
    district[y + d2 + i][x + d2 - i] = 5;
  }

  for (let r = y + 1; r < y + d1 + d2; r++) {
    for (let c = 0; c < N; c++) {
      if (district[r][c] === 5) {
        for (let right = c + 1; right < N; right++) {
          if (district[r][right] === 5) break;
          district[r][right] = 5;
        }
        break;
      }
    }
  }

  for (let r = 0; r < y + d1; r++) {
    for (let c = 0; c <= x; c++) {
      if (district[r][c] === 5) break;
      district[r][c] = 1;
    }
  }

  for (let r = 0; r <= y + d2; r++) {
    for (let c = N - 1; c > x; c--) {
      if (district[r][c] === 5) break;
      district[r][c] = 2;
    }
  }

  for (let r = y + d1; r < N; r++) {
    for (let c = 0; c < x + d2 - d1; c++) {
      if (district[r][c] === 5) break;
      district[r][c] = 3;
    }
  }

  for (let r = y + d2 + 1; r < N; r++) {
    for (let c = N - 1; c >= x + d2 - d1; c--) {
      if (district[r][c] === 5) break;
      district[r][c] = 4;
    }
  }

  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      population[district[r][c] - 1] += A[r][c];
    }
  }

  return population;
};

let diff = Infinity;
for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    for (let d1 = 1; d1 < N; d1++) {
      for (let d2 = 1; d2 < N; d2++) {
        if (isValid(y, x, d1, d2)) {
          const population = getPopulation(y, x, d1, d2);
          diff = Math.min(diff, Math.max(...population) - Math.min(...population));
        }
      }
    }
  }
}
console.log(diff);
