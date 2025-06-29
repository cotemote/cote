const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const N = +inputs[0];
const station = inputs[1].split(' ').map(Number);
const M = +inputs[2];
const users = inputs.slice(4 + M).map((input) => input.split(' ').map(Number));
let idx = 0;

const stationsIdx = Array.from({ length: N }, (_, i) => Array.from({ length: station[i] }, () => idx++));
const stationCount = idx;
const graph = Array.from({ length: stationCount }, () => []);

for (let i = 0; i < N; i++) {
  for (let j = 0; j < station[i] - 1; j++) {
    const a = stationsIdx[i][j];
    const b = stationsIdx[i][j + 1];
    graph[a].push([b, 1]);
    graph[b].push([a, 1]);
  }
}

const transferList = [];
for (const input of inputs.slice(3, 3 + M)) {
  const [p1, p2, q1, q2] = input.split(' ').map(Number);
  transferList.push([stationsIdx[p1 - 1][p2 - 1], stationsIdx[q1 - 1][q2 - 1]]);
}

function dijkstra(start, end, transferCost) {
  const dist = Array(stationCount).fill(Infinity);
  dist[start] = 0;
  const pq = [[0, start]];

  while (pq.length) {
    pq.sort((a, b) => a[0] - b[0]);
    const [cost, node] = pq.shift();
    if (dist[node] < cost) continue;
    for (const [next, weight] of graph[node]) {
      if (dist[next] <= dist[node] + weight) continue;
      dist[next] = dist[node] + weight;
      pq.push([dist[next], next]);
    }

    for (const [a, b] of transferList) {
      if (node === a && dist[b] > dist[a] + transferCost) {
        dist[b] = dist[a] + transferCost;
        pq.push([dist[b], b]);
      }
      if (node === b && dist[a] > dist[b] + transferCost) {
        dist[a] = dist[b] + transferCost;
        pq.push([dist[a], a]);
      }
    }
  }
  return dist[end];
}

for (const [t, u1, u2, v1, v2] of users) {
  const start = stationsIdx[u1 - 1][u2 - 1];
  const end = stationsIdx[v1 - 1][v2 - 1];
  const answer = dijkstra(start, end, t);
  console.log(answer);
}
