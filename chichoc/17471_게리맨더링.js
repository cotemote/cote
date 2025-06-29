const inputs = require('fs').readFileSync(0).toString().trim().split('\n');
const N = +inputs[0];
const populations = inputs[1].split(' ').map(Number);
const sumPop = populations.reduce((sum, curr) => sum + curr, 0);
const graph = [];
let minDiff = Infinity;

function getCombinations(arr, k) {
  const result = [];

  function backtrack(start, path) {
    if (path.length === k) {
      result.push([...path]);
      return;
    }
    for (let i = start; i < arr.length; i++) {
      path.push(arr[i]);
      backtrack(i + 1, path);
      path.pop();
    }
  }

  backtrack(0, []);
  return result;
}

function isConnected(group) {
  if (group.length === 0) return false;
  const queue = [group[0]];
  const visited = new Array(N).fill(false);
  visited[group[0]] = true;
  let count = 1;

  while (queue.length > 0) {
    const currNode = queue.shift();
    for (const neighbor of graph[currNode]) {
      if (!group.includes(neighbor) || visited[neighbor]) continue;
      visited[neighbor] = true;
      queue.push(neighbor);
      count++;
    }
  }
  return count === group.length;
}

for (let i = 2; i < 2 + N; i++) {
  const [_, ...connects] = inputs[i].split(' ').map(Number);
  graph.push(connects.map((n) => n - 1));
}

const allNodesIdx = [...Array(N).keys()];

for (let countA = 1; countA < N; countA++) {
  const combinations = getCombinations(allNodesIdx, countA);

  for (const groupA of combinations) {
    const groupB = allNodesIdx.filter((node) => !groupA.includes(node));

    if (!isConnected(groupA) || !isConnected(groupB)) continue;
    const sumA = groupA.reduce((sum, node) => sum + populations[node], 0);
    const sumB = sumPop - sumA;
    minDiff = Math.min(minDiff, Math.abs(sumA - sumB));
  }
}

console.log(minDiff === Infinity ? -1 : minDiff);
