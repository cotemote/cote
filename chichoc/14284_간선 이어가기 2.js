const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const [n, m] = inputs[0].split(' ').map(Number);
const infos = inputs.slice(1, m + 1).map((info) => info.split(' ').map(Number));
const [s, t] = inputs[1 + m].split(' ').map(Number);

const graph = Array.from({ length: n + 1 }, () => []);
for (const [a, b, c] of infos) {
  graph[a].push([b, c]);
  graph[b].push([a, c]);
}

const dist = Array(n + 1).fill(Infinity);
const visited = Array(n + 1).fill(false);
dist[s] = 0;

const pq = [];
pq.push([0, s]);

while (pq.length) {
  pq.sort((a, b) => a[0] - b[0]);
  const [cost, node] = pq.shift();
  if (visited[node]) continue;
  visited[node] = true;

  for (const [next, weight] of graph[node]) {
    if (dist[next] > dist[node] + weight) {
      dist[next] = dist[node] + weight;
      pq.push([dist[next], next]);
    }
  }
}

console.log(dist[t]);
