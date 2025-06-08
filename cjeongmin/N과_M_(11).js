const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

const unique = [...new Set(arr)].sort((a, b) => a - b);
const result = [];

const dfs = (comb) => {
  if (comb.length === M) {
    result.push(comb.join(' '));
    return;
  }

  for (let i = 0; i < unique.length; i++) {
    comb.push(unique[i]);
    dfs(comb);
    comb.pop();
  }
};

dfs([]);
console.log(result.join('\n'));
