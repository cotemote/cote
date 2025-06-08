const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const n = +inputs[0];

if (n === 2) {
  return console.log('1 2');
}

const connects = inputs.slice(1).map((input) => input.split(' ').map(Number));
const roots = {};

function find(num) {
  if (num !== roots[num]) {
    roots[num] = find(roots[num]);
  }
  return roots[num];
}

function union(num1, num2) {
  const root1 = find(num1);
  const root2 = find(num2);

  if (root1 === root2) return;
  else if (root2 > root1) roots[root2] = root1;
  else roots[root1] = root2;
}

for (let i = 1; i <= n; i++) {
  roots[i] = i;
}

connects.forEach(([num1, num2]) => union(num1, num2));

for (let i = 1; i <= n; i++) {
  for (let j = i + 1; j <= n; j++) {
    if (find(i) === find(j)) continue;
    return console.log(i, j);
  }
}
