const [N, K] = require('fs').readFileSync(0).toString().trim().split(' ').map(Number);
const MAX = 100001;
const visited = Array(MAX).fill(-1);
const queue = Array(MAX * 2);
let head = 0,
  tail = 0;
let minTime = Infinity;
let count = 0;

queue[tail++] = [N, 0];
visited[N] = 0;

while (head < tail) {
  const [pos, time] = queue[head++];

  if (minTime < time) break;

  if (pos === K) {
    if (minTime > time) {
      minTime = time;
      count = 1;
    } else if (minTime === time) {
      count++;
    }
    continue;
  }

  for (const next of [pos - 1, pos + 1, pos * 2]) {
    if (next >= 0 && next < MAX) {
      if (visited[next] === -1 || visited[next] === time + 1) {
        queue[tail++] = [next, time + 1];
        visited[next] = time + 1;
      }
    }
  }
}

console.log(minTime + '\n' + count);
