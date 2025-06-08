const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const [n, m] = inputs[0].split(' ').map(Number);
const numbers = inputs[1].split(' ').map(Number);
const sortedNumbers = [...new Set(numbers)].sort((a, b) => a - b);
const answer = [];

function permutation(permu, rests) {
  if (permu.length === m) {
    return answer.push(permu.join(' '));
  }

  rests.forEach((num) => {
    permutation([...permu, num], rests);
  });
}

permutation([], sortedNumbers);

console.log(answer.join('\n'));
