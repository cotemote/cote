import heapq

N = int(input())
station_cnt = list(map(int, input().split()))

M = int(input())
transfer = dict()
for i in range(M):
    P1, P2, Q1, Q2 = map(int, input().split())
    transfer[(P1, P2)] = (Q1, Q2)
    transfer[(Q1, Q2)] = (P1, P2)


def dijkstra(start, end, T):
    global transfer, N, station_cnt
    distance = dict()
    for line in range(N):
        cnt = station_cnt[line]
        for c in range(1, cnt + 1):
            distance[(line + 1, c)] = float("inf")

    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, pos = heapq.heappop(q)
        if cost > distance[pos]:
            continue
        next_positions = []
        if pos[1] > 1:
            next_positions.append(((pos[0], pos[1] - 1), 1))
        if pos[1] < station_cnt[pos[0] - 1]:
            next_positions.append(((pos[0], pos[1] + 1), 1))
        if pos in transfer:
            next_pos = transfer[pos]
            next_positions.append(((next_pos[0], next_pos[1]), T))

        for next_node, next_cost in next_positions:
            dist = cost + next_cost
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(q, (dist, next_node))

    return distance[end]


def solution(T, U1, U2, V1, V2):
    return dijkstra((U1, U2), (V1, V2), T)


K = int(input())
for i in range(K):
    transfer_time = list(map(int, input().split()))
    print(solution(*transfer_time))
