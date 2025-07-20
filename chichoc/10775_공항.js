const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const G = +inputs[0];
const planes = inputs.slice(2).map(Number);
const parent = Array(G + 1)
  .fill(0)
  .map((_, i) => i);

function find(x) {
  if (parent[x] === x) return x;
  return (parent[x] = find(parent[x]));
}

function union(a, b) {
  a = find(a);
  b = find(b);
  parent[a] = b;
}

let answer = 0;

for (let plane of planes) {
  const dockGate = find(plane);

  if (dockGate === 0) break;

  union(dockGate, dockGate - 1);
  answer++;
}

console.log(answer);
