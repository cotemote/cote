n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
    
for _ in range(m):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))
  graph[v].append((u, w))

s, t = map(int, input().split())

import heapq

def solution(n, m, graph, s, t):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    queue = [(0, s)]

    while queue:
        curr_dist, v = heapq.heappop(queue)
        if curr_dist > dist[v]:
            continue
        if v == t:
            return curr_dist
        for nei, w in graph[v]:
            new_dist = curr_dist + w
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(queue, (new_dist, nei))

print(solution(n, m, graph, s, t))
