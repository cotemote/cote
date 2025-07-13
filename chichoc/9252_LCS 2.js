const [s1, s2] = require('fs').readFileSync(0).toString().trim().split('\n');
const len1 = s1.length,
  len2 = s2.length;

function lcs(s1, s2) {
  const dp = Array.from({ length: len1 + 1 }, () => Array(len2 + 1).fill(0));
  const result = [];

  for (let i = 1; i <= len1; i++) {
    for (let j = 1; j <= len2; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  let i1 = len1,
    i2 = len2;
  while (i1 > 0 && i2 > 0) {
    if (dp[i1][i2] === 0) break;
    if (s1[i1 - 1] === s2[i2 - 1]) {
      result.push(s1[i1 - 1]);
      i1--;
      i2--;
    } else if (dp[i1 - 1][i2] > dp[i1][i2 - 1]) {
      i1--;
    } else {
      i2--;
    }
  }
  return [dp[len1][len2], result.reverse().join('')];
}

const [length, lcsStr] = lcs(s1, s2);
console.log(length);
if (length > 0) console.log(lcsStr);
