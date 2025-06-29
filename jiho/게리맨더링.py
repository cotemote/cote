from collections import deque

N = int(input())
people = list(map(int, input().split()))
graph = [list(map(int, input().split()))[1:] for _ in range(N)]


def bfs(start, subset, subset_type):
    global people, graph, N
    visited = [False] * (N + 1)
    q = deque()

    visited[start] = True
    q.append(start)
    total_people = people[start - 1]

    while q:
        x = q.popleft()
        for next_node in graph[x - 1]:
            if visited[next_node] or subset[next_node] != subset_type:
                continue
            visited[next_node] = True
            q.append(next_node)
            total_people += people[next_node - 1]

    for i in range(1, N + 1):
        if subset[i] == subset_type:
            if not visited[i]:
                return -1

    return total_people


def make_subsets(N, subset, prev):
    true_cnt, false_cnt = 0, 0
    for i in range(1, N + 1):
        if true_cnt == 0 and subset[i] == True:
            true_cnt = bfs(i, subset, True)
        if false_cnt == 0 and subset[i] == False:
            false_cnt = bfs(i, subset, False)

    current_ans = 10000
    if true_cnt > 0 and false_cnt > 0:
        current_ans = abs(true_cnt - false_cnt)

    if prev == N:
        return current_ans

    subset[prev + 1] = True
    ans1 = make_subsets(N, subset, prev + 1)

    subset[prev + 1] = False
    ans2 = make_subsets(N, subset, prev + 1)

    return min(current_ans, ans1, ans2)


def solution():
    global N, people, graph

    ans = make_subsets(
        N,
        [False] * (N + 1),
        0,
    )
    if ans == 10000:
        return -1
    return ans


print(solution())
