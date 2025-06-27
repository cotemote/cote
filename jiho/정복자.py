import heapq

N, M, t = map(int, input().split())
q = []
for i in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(q, [c, a, b])


def find_parent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    X = find_parent(parent, x)
    Y = find_parent(parent, y)
    if X == Y:
        return False
    parent[X] = Y
    return True


def solution():
    global N, M, t, q
    parent = [i for i in range(N + 1)]

    result, cnt = 0, 0
    while cnt < N - 1:
        c, x, y = heapq.heappop(q)
        if union(parent, x, y):
            result += c + t * cnt
            cnt += 1

    return result


print(solution())
