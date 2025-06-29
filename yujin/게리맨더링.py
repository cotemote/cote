n = int(input())
pop = list(map(int, input().split()))
graph = {}
for i in range(1, n + 1):
  a, *neis = list(map(int, input().split()))
  graph[i] = neis if a != 0 else []

from itertools import combinations
from collections import deque

def get_combs(arr):
  result = []
  for size in range(1, n // 2 + 1):
    for comb in combinations(arr, size):
      result.append((comb, tuple(set(arr) - set(comb))))
  return result

def bfs(graph, arr):
  visited = set()

  queue = deque([arr[0]])
  visited.add(arr[0])
  count = 1

  while queue:
    curr = queue.popleft()
    for next in graph[curr]:
      if next in set(arr) and next not in visited:
        visited.add(next)
        queue.append(next)
        count += 1
  
  return len(arr) == count

def pop_total(pdict, arr):
  answer = 0
  for el in arr:
    answer += pdict[el]
  return answer

def solution(n, pop, graph):
  pop_dict = {}
  for idx, p in enumerate(pop):
    pop_dict[idx + 1] = p

  arr = [i for i in range(1, 1 + n)]
  combs = get_combs(arr)
  answer = float('inf')

  for a, b in combs:
    if bfs(graph, a) and bfs(graph, b):
      ap = pop_total(pop_dict, a)
      bp = pop_total(pop_dict, b)
      if abs(ap - bp) < answer:
        answer = abs(ap - bp)
  return answer if answer < float('inf') else -1

print(solution(n, pop, graph))
