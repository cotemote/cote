from itertools import combinations  
from collections import deque  
def bfs(group):  
    q = deque()  
    q.append(group[0])  
    visited = [False] * (N+1)  
    visited[group[0]] = True  
    cnt = population[group[0]]  
    while q:  
        now = q.popleft()  
        for k in region[now]:  
            if k in group and not visited[k]:  
                q.append(k)  
                visited[k] = 1  
                cnt += population[k]  

    for g in group:  
        if not visited[g]:  
            return 0  
    return cnt  

N = int(input())  
population = [0] + [*map(int, input().split())]  
region = [[] for _ in range(N+1)]  
for i in range(N):  
    query = [*map(int, input().split())]  
    region[i+1] = query[1:]  

result = float('inf')  
for i in range(1, N//2+1):  
    for comb in combinations(range(1, N+1), i):  
        A = list(comb)  
        B = []  
        for j in range(1, N+1):  
            if not j in A:  
                B.append(j)  
        val1, val2 = bfs(A), bfs(B)  

        if val1 and val2:  
            result = min(result, abs(val1 - val2))  

print(result if not result == float('inf') else -1)
