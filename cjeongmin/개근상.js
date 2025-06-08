const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();

const N = Number(input);
const MOD = 1000000;

const dp = Array.from({ length: N + 1 }, () => Array.from({ length: 2 }, () => Array(3).fill(0)));
dp[0][0][0] = 1;
for (let i = 0; i < N; i++) {
  for (let l = 0; l < 2; l++) {
    for (let a = 0; a < 3; a++) {
      const curr = dp[i][l][a];
      if (!curr) continue;
      dp[i + 1][l][0] = (dp[i + 1][l][0] + curr) % MOD;
      if (l < 1) dp[i + 1][1][0] = (dp[i + 1][1][0] + curr) % MOD;
      if (a < 2) dp[i + 1][l][a + 1] = (dp[i + 1][l][a + 1] + curr) % MOD;
    }
  }
}

let result = 0;
for (let l = 0; l < 2; l++) {
  for (let a = 0; a < 3; a++) {
    result = (result + dp[N][l][a]) % MOD;
  }
}
console.log(result);
