n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())
INF = float("inf")


def dijkstra(graph, start, end):
    global n, INF
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)

    distance[start] = 0
    visited[start] = True
    for b, c in graph[start]:
        distance[b] = c

    for _ in range(n - 1):
        now = get_smallest_node(distance, visited)
        visited[now] = True
        for b, c in graph[now]:
            distance[b] = min(distance[b], distance[now] + c)

    return distance[end]


def get_smallest_node(distance, visited):
    global INF
    min_val = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index


def solution():
    global n, edges, s, t
    graph = [[] for _ in range(n + 1)]
    for [a, b, c] in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    return dijkstra(graph, s, t)


print(solution())
