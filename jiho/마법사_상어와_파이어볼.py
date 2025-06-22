N, M, K = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(M)]


def addDict(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]


def move(balls):
    global N
    move = dict()
    dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    for pos, infos in balls.items():
        for info in infos:
            s, d = info[1], info[2]
            i = pos[0] + dirs[d][0] * s
            j = pos[1] + dirs[d][1] * s
            while i <= 0:
                i += N
            while j <= 0:
                j += N
            while i > N:
                i -= N
            while j > N:
                j -= N
            addDict(move, (i, j), info)
    return move


def getSum(tupArr, idx):
    result = 0
    for tup in tupArr:
        result += tup[idx]
    return result


def checkAll(tupArr, idx, checkFunc):
    for tup in tupArr:
        if checkFunc(tup[idx]) == False:
            return False
    return True


def merge(moved):
    result = dict()
    for pos, infos in moved.items():
        cnt = len(infos)
        if cnt == 1:
            addDict(result, pos, infos[0])
            continue
        totalm = getSum(infos, 0)
        totals = getSum(infos, 1)
        totald = checkAll(infos, 2, lambda x: x % 2 == 0) or checkAll(
            infos, 2, lambda x: x % 2 == 1
        )

        m = totalm // 5
        s = totals // cnt
        d = [0, 2, 4, 6] if totald else [1, 3, 5, 7]

        if m == 0:
            continue

        for i in range(4):
            addDict(result, pos, (m, s, d[i]))
    return result


def solution():
    balls = dict()
    for [r, c, m, s, d] in inputs:
        pos = (r, c)
        value = (m, s, d)
        addDict(balls, pos, value)

    global K
    for _ in range(K):
        moved = move(balls)
        balls = merge(moved)

    return sum(getSum(v, 0) for v in balls.values())


print(solution())
