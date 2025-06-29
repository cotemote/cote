import heapq
n, m, t = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x) :
    if x != parent[x] :
        return find(parent[x])
    return x
def union(a, b) :
    parentA = find(a)
    parentB = find(b)
    if parentA < parentB :
        parent[b] = parentA
        return 1
    elif parentA > parentB :
        parent[a] = parentB
        return 1
    return 0
        

heap = []
heapq.heapify(heap)
for i in range(m) :
    a, b, c = map(int, input().split())
    heapq.heappush(heap, [c, a, b])
count = 0
ans = 0

while count < n - 1 :
    c, a, b = heapq.heappop(heap)
    if union(a, b) :
        count += 1
        ans += c
print(ans + (((n-2) * (n-1)) // 2 ) * t)
