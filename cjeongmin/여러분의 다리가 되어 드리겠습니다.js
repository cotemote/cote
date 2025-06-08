const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const N = Number(input[0]);

const graph = Array.from({ length: N + 1 }, () => []);
for (let i = 0; i < N - 2; i++) {
  const [a, b] = input[i + 1].split(' ').map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

const parents = Array.from({ length: N + 1 }, (_, i) => i);

const find = (x) => {
  if (parents[x] === x) return x;
  return (parents[x] = find(parents[x]));
};

const union = (x, y) => {
  const rootX = find(x);
  const rootY = find(y);
  if (rootX !== rootY) {
    parents[rootY] = rootX;
  }
};

for (let i = 1; i <= N; i++) {
  for (const node of graph[i]) {
    union(i, node);
  }
}

for (let i = 1; i <= N; i++) {
  find(i);
}

console.log([...new Set(parents.slice(1))].join(' '));
