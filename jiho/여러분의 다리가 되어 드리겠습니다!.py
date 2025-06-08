import sys

n = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 2)]
parent = [i for i in range(n + 1)]


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    px = find(parent, x)
    py = find(parent, y)
    if px == py:
        return
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


def solution(n, parent):
    for i in range(1, n):
        if find(parent, i) != find(parent, n):
            return [i, n]
    return [0, 0]


for [i, j] in edges:
    union(parent, i, j)
[a, b] = solution(n, parent)
print(a, b)
