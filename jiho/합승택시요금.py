import heapq


def solution(n, s, a, b, fares):
    INF = float("inf")
    graph = [[] for _ in range(n + 1)]
    for [c, d, f] in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def dijkstra(start, end):
        distance = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                if dist + i[1] < distance[i[0]]:
                    distance[i[0]] = dist + i[1]
                    heapq.heappush(q, (dist + i[1], i[0]))
        return distance[end]

    answer = INF
    for k in range(1, n + 1):
        answer = min(answer, dijkstra(s, k) + dijkstra(k, a) + dijkstra(k, b))
    return answer
