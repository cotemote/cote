const input = require('fs').readFileSync(0, 'utf-8').toString().trim().split('\n');

const N = parseInt(input[0]);
const population = [0, ...input[1].split(' ').map(Number)];
const graph = Array.from({ length: N + 1 }, () => []);

for (let i = 1; i <= N; i++) {
  const line = input[i + 1].split(' ').map(Number);
  const count = line[0];
  for (let j = 1; j <= count; j++) {
    graph[i].push(line[j]);
  }
}

let result = Infinity;

const bfs = (districts) => {
  if (districts.length === 0) return -1;

  const visited = new Array(N + 1).fill(false);
  const queue = [districts[0]];
  visited[districts[0]] = true;
  let totalPopulation = population[districts[0]];
  let visitedCount = 1;

  while (queue.length > 0) {
    const current = queue.shift();

    for (const next of graph[current]) {
      if (!visited[next] && districts.includes(next)) {
        visited[next] = true;
        queue.push(next);
        totalPopulation += population[next];
        visitedCount++;
      }
    }
  }

  return visitedCount === districts.length ? totalPopulation : -1;
};

const solution = () => {
  for (let r = 1; r < N; r++) {
    dfs([], 1, r);
  }
};

const dfs = (current, start, r) => {
  if (current.length === r) {
    const groupA = [...current];
    const groupB = [];

    for (let i = 1; i <= N; i++) {
      if (!groupA.includes(i)) {
        groupB.push(i);
      }
    }

    const popA = bfs(groupA);
    const popB = bfs(groupB);

    if (popA !== -1 && popB !== -1) {
      result = Math.min(result, Math.abs(popA - popB));
    }
    return;
  }

  for (let i = start; i <= N; i++) {
    current.push(i);
    dfs(current, i + 1, r);
    current.pop();
  }
};

solution();

console.log(result === Infinity ? -1 : result);
