const [A, B] = require('fs').readFileSync('example.txt').toString().trim().split(' ').map(BigInt);

function countOnes(x) {
  let total = 0n;
  for (let i = 0n; i < 61n; i++) {
    const bitLen = 1n << (i + 1n);
    const full = (x + 1n) / bitLen;
    const remain = (x + 1n) % bitLen;

    total += full * (bitLen >> 1n);
    if (remain > bitLen >> 1n) {
      total += remain - (bitLen >> 1n);
    }
  }
  return total;
}

console.log((countOnes(B) - countOnes(A - 1n)).toString());

// 01 10 11 100
// 101 110 111 1000
