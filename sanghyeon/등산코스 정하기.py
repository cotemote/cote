from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    MAX = 10000001
    answer = [0, MAX]

    set_summits = set(summits)

    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    min_dis = [MAX for _ in range(n+1)] # ! (n+1) 주의
    pq = [(0, gate) for gate in gates]
    while pq:
        intensity, cur_v = heapq.heappop(pq)
        if min_dis[cur_v] > intensity:
            min_dis[cur_v] = intensity
        else: 
            continue
        for cost, next_v in graph[cur_v]:
            next_cost = max(intensity, cost)
            if min_dis[next_v] <= next_cost:
                continue
            if cur_v in set_summits: 
                continue
            heapq.heappush(pq, (next_cost, next_v))

    for summit in summits:
        if answer[1] > min_dis[summit]:
            answer = [summit, min_dis[summit]]
        elif answer[1] == min_dis[summit] and summit < answer[0]:
            answer[0] = summit
    return answer
