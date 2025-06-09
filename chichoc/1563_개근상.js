const N = +require('fs').readFileSync(0).toString().trim();
const MOD = 1000000;

const dp = Array.from({ length: N + 1 }, () => Array.from({ length: 2 }, () => Array(3).fill(-1)));

function solve(day, late, absent) {
  if (late >= 2 || absent >= 3) return 0;
  if (day === N) return 1;
  if (dp[day][late][absent] !== -1) return dp[day][late][absent];

  let ret = 0;
  ret = (ret + solve(day + 1, late, 0)) % MOD;
  ret = (ret + solve(day + 1, late, absent + 1)) % MOD;
  ret = (ret + solve(day + 1, late + 1, 0)) % MOD;

  dp[day][late][absent] = ret;
  return ret;
}

console.log(solve(0, 0, 0));
