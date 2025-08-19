import heapq


def dijkstra(graph, gates, summits):
    INF = float("inf")
    distance = [INF] * len(graph)
    q = []

    for g in gates:
        heapq.heappush(q, (0, g))
        distance[g] = 0

    summit_set = set(summits)
    while len(q) > 0:
        dist, now = heapq.heappop(q)
        if now in summit_set or distance[now] < dist:
            continue
        for node, cost in graph[now]:
            through = max(dist, cost)
            if through < distance[node]:
                distance[node] = through
                heapq.heappush(q, (through, node))

    summit, intensity = INF, INF
    for s in summits:
        if distance[s] < intensity:
            summit = s
            intensity = distance[s]
    return summit, intensity


def solution(n, paths, gates, summits):
    summits.sort()
    graph = [[] for _ in range(n + 1)]
    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))
    s, intensity = dijkstra(graph, gates, summits)
    return [s, intensity]
