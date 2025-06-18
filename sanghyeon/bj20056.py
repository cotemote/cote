N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K) :
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] != [] :
                for m, s, d in arr[i][j] :
                    r = (i + dir[d][0] * s) % N
                    c = (j + dir[d][1] * s) % N
                    board[r][c].append([m, s, d])
                    
    for i in range(N) :
        for j in range(N) :
            if len(board[i][j]) >= 2 :
                mass = 0
                speed = 0
                check1 = 0
                check2 = 0
                
                for m, s, d in board[i][j] :
                    mass += m
                    speed += s
                    if (d % 2) == 0 : check1 += 1
                    if (d % 2) : check += 1
                mass //= 5
                if mass == 0 :
                    board[i][j] = []
                    continue
                speed //= len(board[i][j])
                if check1 == len(board[i][j]) or check2 == len(board[i][j]) :
                    board[i][j] = []
                    for d in [0, 2, 4, 6] :
                        board[i][j].append([mass, speed, d])
                else :
                    board[i][j] = []
                    for d in [1, 3, 5, 7] :
                        board[i][j].append([mass, speed, d])
    
    arr = [lst[:] for lst in board]
ans = 0
for i in range(N) :
    for j in range(N) :
        if arr[i][j] != []:
            for m, s, d, in arr[i][j] :
                ans += m
print(ans)