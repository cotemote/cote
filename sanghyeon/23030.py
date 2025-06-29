import heapq
n = int(input())
station = [map(int, input().split())]
stations = list(map(int, input().split()))

for i in range(n) :
    for j in range(station[i]) :
        stations[i][j].append(i, j)

m = int(input())
for i in range(m) :
    p1, p2, q1, q2 = map(int, input().split())
    stations[p1][p2].append((q1, q2))
    stations[q1][q2].append((p1, p2))

for _ in range(int(input())) :
    s = [[1e9] * station[i] for i in range(n)]
    t, u1, u2, v1, v2 = map(int, input().split())
    q = []
    heapq.heappush(q, (u1, u2))
    s[u1][u2] = 0
    while q :
        x, y = heapq.heappop(q)
        for nx, ny in stations[x][y]:
            if x == nx and s[nx][ny] > s[x][y] + 1:
                s[nx][ny] = s[x][y] + 1
                heapq.heappush(q, (nx, ny))
            elif x != nx and s[nx][ny] > s[x][y] + t:
                s[nx][ny] = s[x][y] + t
                heapq.heappush(q, (nx, ny))
    print(s[v1][v2])
