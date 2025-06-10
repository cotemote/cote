from collections import deque
n, k = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append((n, 0))

minTime = int(1e9)
count = 0

while q :
    cur, time = q.popleft()
    if cur == k :
        if minTime > time :
            minTime = time
            count = 1
        elif minTime == time :
            count += 1
        continue

    for next in [cur-1, cur+1, cur*2] :
        if 0 <= next <= 100000 and (visited[next] == -1 or visited[next] == time + 1) :
            visited[next] = time + 1
            q.append((next, time+1))

print(minTime)
print(count)