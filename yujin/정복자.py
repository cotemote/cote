n, m, t = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

from collections import defaultdict

def solution(n, t, roads):
  roots = [i for i in range(n + 1)]

  def find(x):
    if roots[x] != x:
      roots[x] = find(roots[x])
    return roots[x]

  def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root == b_root:
      return False

    roots[b_root] = a
    return True
  
  roads.sort(key=lambda x:x[2])

  total = 0
  cnt = 0

  for road in roads:
    a, b, c = road
    if union(a, b):
      total += (c + t * cnt)
      cnt += 1

  return total

print(solution(n, t, roads))
