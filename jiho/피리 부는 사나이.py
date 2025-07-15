N, M = map(int, input().split())
arr = [input() for _ in range(N)]


def check_new_cycle(startI, startJ, visited, now):
    global N, M, arr
    i, j = startI, startJ

    dir = dict()
    dir["D"] = [1, 0]
    dir["L"] = [0, -1]
    dir["U"] = [-1, 0]
    dir["R"] = [0, 1]

    while i >= 0 and j >= 0 and i < N and j < M:
        if visited[i][j] > 0 and visited[i][j] < now:
            return False
        if visited[i][j] == now:
            return True

        visited[i][j] = now
        d = dir[arr[i][j]]
        i += d[0]
        j += d[1]

    return True


ans = 0
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if visited[i][j] > 0:
            continue
        if check_new_cycle(i, j, visited, i * N + j + 1):
            ans += 1

print(ans)
