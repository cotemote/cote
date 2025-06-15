n = int(input())
bridges = [list(map(int, input().split())) for _ in range(n-2)]

def solution(n, bridges):
  parent = [i for i in range(n + 1)]

  def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
  
  def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root

  for bridge in bridges:
    l1, l2 = bridge
    union(l1, l2)
  
  for i in range(2,n+1):
    if find(1) != find(i):
        return f"{1} {i}"  

print(solution(n, bridges))
