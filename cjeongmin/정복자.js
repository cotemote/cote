const input = require('fs').readFileSync(0, 'utf-8').toString().trim().split('\n');

const [N, M, T] = input[0].split(' ').map(Number);

const edges = [];
for (let i = 1; i <= M; i++) {
  const [a, b, c] = input[i].split(' ').map(Number);
  edges.push([c, a, b]);
}

edges.sort((a, b) => a[0] - b[0]);
const parent = Array.from({ length: N + 1 }, (_, i) => i);

const find = (x) => {
  if (parent[x] === x) return x;
  return (parent[x] = find(parent[x]));
};

const union = (a, b) => {
  const rootA = find(a);
  const rootB = find(b);

  if (rootA !== rootB) {
    if (rootA < rootB) {
      parent[rootB] = rootA;
    } else {
      parent[rootA] = rootB;
    }
    return true;
  }
  return false;
};

let result = 0;
let cnt = 0;

for (const [cost, a, b] of edges) {
  if (union(a, b)) {
    result += cost + cnt * T;
    cnt++;

    if (cnt === N - 1) {
      break;
    }
  }
}

console.log(result);
