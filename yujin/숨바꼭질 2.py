start, end = map(int, input().split())

from collections import deque 

def solution(start, end):
  SIZE = 1000000
  memory = [float('inf') for _ in range(SIZE + 1)]
  result = 0
  count = 0
  found = False
  queue = deque([])
  queue.append((start, 0))

  while queue:
    curr, step = queue.popleft()
    if found and result < step:
      break

    if curr == end:
        found = True
        result = step
        count += 1
      
    nexts = [curr + 1, curr - 1, curr * 2]
    for next in nexts:
      if next >= 0 and next <= SIZE and memory[next] >= step + 1:
        memory[next] = step + 1
        queue.append((next, step + 1))
  return (result, count)

step, count = solution(start, end)
print(step)
print(count)
