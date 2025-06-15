const input = require('fs').readFileSync(0).toString().trim().split('\n');
let A = input[1].split(' ').map(Number);
let B = input[3].split(' ').map(Number);

const result = [];

while (true) {
  const setA = new Set(A);
  const setB = new Set(B);
  const common = [...setA].filter((x) => setB.has(x));
  if (common.length === 0) break;

  const maxVal = Math.max(...common);
  result.push(maxVal);

  const idxA = A.indexOf(maxVal);
  const idxB = B.indexOf(maxVal);
  A = A.slice(idxA + 1);
  B = B.slice(idxB + 1);
}

console.log(result.length);
if (result.length > 0) console.log(result.join(' '));
