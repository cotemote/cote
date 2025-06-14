from collections import deque

N, K = map(int, input().split())
max_size = 100_000
visited = [-1] * (max_size * 2 + 1)
cnt = [0] * (max_size * 2 + 1)

queue = deque()
queue.append(N)
visited[N] = 0
cnt[N] = 1

while len(queue) != 0:
    x = queue.popleft()
    next = [x - 1, x + 1, x * 2]
    for n in next:
        if n < 0 or n >= len(visited):
            continue
        if visited[n] == -1:
            visited[n] = visited[x] + 1
            cnt[n] = cnt[x]
            queue.append(n)
        elif visited[n] == visited[x] + 1:
            cnt[n] = cnt[n] + cnt[x]

print(visited[K])
print(cnt[K])
