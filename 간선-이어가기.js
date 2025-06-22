const Heap = (() => {
  const shiftDown = (heap, idx, compare) => {
    let smallest = idx;
    const left = idx * 2 + 1;
    const right = idx * 2 + 2;

    if (left < heap.length && compare(heap[left], heap[smallest])) {
      smallest = left;
    }

    if (right < heap.length && compare(heap[right], heap[smallest])) {
      smallest = right;
    }

    if (smallest !== idx) {
      [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
      shiftDown(heap, smallest, compare);
    }
  };

  const shiftUp = (heap, idx, compare) => {
    const parent = Math.floor((idx - 1) / 2);

    if (parent >= 0 && compare(heap[parent], heap[idx])) {
      [heap[idx], heap[parent]] = [heap[parent], heap[idx]];
      shiftUp(heap, parent, compare);
    }
  };

  const insert = (heap, value, compare) => {
    heap.push(value);
    shiftUp(heap, heap.length - 1, compare);
  };

  const pop = (heap, compare) => {
    const result = heap[0];
    heap[0] = heap[heap.length - 1];
    heap.pop();
    shiftDown(heap, 0, compare);
    return result;
  };

  return {
    insert,
    pop,
  };
})();

const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const graph = Array.from({ length: N + 1 }, () => []);
input
  .slice(1, M + 1)
  .map((line) => line.split(' ').map(Number))
  .forEach(([a, b, c]) => {
    graph[a].push([b, c]);
    graph[b].push([a, c]);
  });
const [S, T] = input[M + 1].split(' ').map(Number);

const dijkstra = (start, end) => {
  const pq = [];
  const dist = Array(N + 1).fill(Infinity);
  dist[start] = 0;
  Heap.insert(pq, [0, start], (a, b) => a[0] < b[0]);

  while (pq.length) {
    const [cost, node] = Heap.pop(pq, (a, b) => a[0] < b[0]);
    if (dist[node] < cost) continue;

    for (const [next, nextCost] of graph[node]) {
      if (dist[next] > cost + nextCost) {
        dist[next] = cost + nextCost;
        Heap.insert(pq, [dist[next], next], (a, b) => a[0] < b[0]);
      }
    }
  }

  return dist[end];
};

console.log(dijkstra(S, T));
