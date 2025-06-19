from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def checkLeftRight(A, B, C):
    result1 = (A[0] * B[1]) + (B[0] * C[1]) + (C[0] * A[1])
    result2 = (B[0] * A[1]) + (C[0] * B[1]) + (A[0] * C[1])
    result = result1 - result2
    if result > 0:
        return "L"
    elif result < 0:
        return "R"
    else:
        return "S"


def checkInRect(A, B, C, D, pos):
    if checkLeftRight(A, B, pos) == "R":
        return False
    if checkLeftRight(B, C, pos) == "R":
        return False
    if checkLeftRight(C, D, pos) == "R":
        return False
    if checkLeftRight(D, A, pos) == "R":
        return False
    return True


def counter(x, y, d1, d2):
    global arr, n
    cnt = [0] * 5
    areaResult = [[0] * (n + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            area = 5
            if checkInRect(
                [x, y],
                [x + d1, y - d1],
                [x + d1 + d2, y - d1 + d2],
                [x + d2, y + d2],
                [r, c],
            ):
                areaResult[r][c] = 5

    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if areaResult[r][c] == 5:
                break
            areaResult[r][c] = 1

    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if areaResult[r][c] == 5:
                break
            areaResult[r][c] = 2

    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if areaResult[r][c] == 5:
                break
            areaResult[r][c] = 3

    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 - 1, -1):
            if areaResult[r][c] == 5:
                break
            areaResult[r][c] = 4

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            area = areaResult[r][c]
            cnt[area - 1] += arr[r - 1][c - 1]

    return cnt


def solution():
    ans = float("inf")
    global arr, n

    for x in range(1, n):
        for y in range(1, n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    if x + d1 + d2 > n:
                        continue
                    if y - d1 < 1:
                        continue
                    if y + d2 > n:
                        continue
                    result = counter(x, y, d1, d2)
                    maxCnt = max(result)
                    minCnt = min(result)
                    ans = min(maxCnt - minCnt, ans)

    return ans


print(solution())
