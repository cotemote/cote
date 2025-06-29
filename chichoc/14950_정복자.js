const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const [N, M, t] = inputs[0].split(' ').map(Number);
const cities = inputs.slice(1).map((input) => {
  const [a, b, c] = input.split(' ').map(Number);
  return { a, b, c };
});
const parent = Array(N + 1)
  .fill(0)
  .map((_, i) => i);
let minCost = 0;
let count = 1;

cities.sort((e1, e2) => e1.c - e2.c);

function find(x) {
  if (parent[x] !== x) parent[x] = find(parent[x]);
  return parent[x];
}

function union(x, y) {
  x = find(x);
  y = find(y);
  if (x === y) return false;
  parent[y] = x;
  return true;
}

for (const { a, b, c } of cities) {
  if (!union(a, b)) continue;

  minCost += c + (count - 1) * t;
  if (++count === N) break;
}
console.log(minCost);
