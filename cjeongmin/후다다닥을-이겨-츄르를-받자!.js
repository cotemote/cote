const Heap = (() => {
  const shiftDown = (heap, idx, compare) => {
    let smallest = idx;
    const left = 2 * idx + 1;
    const right = 2 * idx + 2;

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
    let parent = Math.floor((idx - 1) / 2);

    if (parent >= 0 && compare(heap[idx], heap[parent])) {
      [heap[idx], heap[parent]] = [heap[parent], heap[idx]];
      shiftUp(heap, parent, compare);
    }
  };

  const push = (heap, value, compare) => {
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
    push,
    pop,
  };
})();

const input = require('fs').readFileSync(0, 'utf8').trim().split('\n');
let idx = 0;

const N = parseInt(input[idx++]);
const stations = input[idx++].split(' ').map(Number);
const M = parseInt(input[idx++]);

const graph = new Map();

for (let line = 0; line < N; line++) {
  for (let station = 1; station <= stations[line]; station++) {
    const key = `${line},${station}`;
    if (!graph.has(key)) graph.set(key, []);

    if (station > 1) {
      const prevKey = `${line},${station - 1}`;
      graph.get(key).push([prevKey, 1]);
      if (!graph.has(prevKey)) graph.set(prevKey, []);
      graph.get(prevKey).push([key, 1]);
    }
  }
}

const transfers = [];
for (let i = 0; i < M; i++) {
  const [P1, P2, Q1, Q2] = input[idx++].split(' ').map(Number);
  transfers.push([`${P1 - 1},${P2}`, `${Q1 - 1},${Q2}`]);
}

const K = parseInt(input[idx++]);

const dijkstra = (start, end, transferTime) => {
  const dist = new Map();
  const heap = [];
  const compare = (a, b) => a[0] < b[0];

  dist.set(start, 0);
  Heap.push(heap, [0, start], compare);

  while (heap.length > 0) {
    const [d, current] = Heap.pop(heap, compare);

    if (current === end) return d;
    if (dist.has(current) && dist.get(current) < d) continue;

    if (graph.has(current)) {
      for (const [next, cost] of graph.get(current)) {
        const newDist = d + cost;
        if (!dist.has(next) || dist.get(next) > newDist) {
          dist.set(next, newDist);
          Heap.push(heap, [newDist, next], compare);
        }
      }
    }

    for (const [station1, station2] of transfers) {
      if (current === station1) {
        const newDist = d + transferTime;
        if (!dist.has(station2) || dist.get(station2) > newDist) {
          dist.set(station2, newDist);
          Heap.push(heap, [newDist, station2], compare);
        }
      } else if (current === station2) {
        const newDist = d + transferTime;
        if (!dist.has(station1) || dist.get(station1) > newDist) {
          dist.set(station1, newDist);
          Heap.push(heap, [newDist, station1], compare);
        }
      }
    }
  }

  return -1;
};

const results = [];
for (let i = 0; i < K; i++) {
  const [T, U1, U2, V1, V2] = input[idx++].split(' ').map(Number);
  const start = `${U1 - 1},${U2}`;
  const end = `${V1 - 1},${V2}`;

  results.push(dijkstra(start, end, T));
}

console.log(results.join('\n'));
