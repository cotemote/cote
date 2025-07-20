n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

visited = [[0] for _ in range(m) for _ in range(n)]
safeZone = 0

def dfs(x, y) :
    global safeZone
    visited[y][x] = True
    cycle.append([x, y])
    
    if maps[y][x] == 'U' and y > 0 :
        y -= 1
    elif maps[y][x] == 'D' and y < N-1 :
        y += 1
    elif maps[y][x] == 'L' and x > 0 :
        x -= 1
    elif maps[y][x] == 'R' and x < m-1 :
        x += 1
    if visited[y][x] :
        if [x, y] in cycle :
            safeZone += 1
    else :
        dfs(x, y)
for x in range(m) :
    for y in range(n) :
        if not visited[y][x] :
            cycle = []
            dfs(x, y)
print(safeZone)
