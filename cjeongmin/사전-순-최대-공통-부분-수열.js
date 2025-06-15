const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const N = Number(input[0]);
const A = input[1].split(' ').map(Number);
const M = Number(input[2]);
const B = input[3].split(' ').map(Number);

function preprocess(arr) {
  const positions = new Map();
  for (let i = 0; i < arr.length; i++) {
    const num = arr[i];
    if (!positions.has(num)) {
      positions.set(num, []);
    }
    positions.get(num).push(i);
  }
  return positions;
}

const posA = preprocess(A);
const posB = preprocess(B);

function findNextIndex(positionsMap, num, minIndex) {
  if (!positionsMap.has(num)) {
    return null;
  }
  return positionsMap.get(num).find((idx) => idx >= minIndex);
}

function findLCS(currentAIdx, currentBIdx) {
  if (currentAIdx >= N || currentBIdx >= M) {
    return [];
  }

  for (let val = 100; val >= 1; val--) {
    const nextAIdx = findNextIndex(posA, val, currentAIdx);

    if (nextAIdx != null) {
      const nextBIdx = findNextIndex(posB, val, currentBIdx);

      if (nextBIdx != null) {
        const sub = findLCS(nextAIdx + 1, nextBIdx + 1);
        return [val, ...sub];
      }
    }
  }
  return [];
}

const result = findLCS(0, 0);

console.log(result.length);
if (result.length > 0) {
  console.log(result.join(' '));
}
