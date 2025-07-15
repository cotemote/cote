n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
  nums = list(map(int, input().split()))
  a.append(nums[0])
  b.append(nums[1])
  c.append(nums[2])
  d.append(nums[3])

from collections import defaultdict

def solution(n, a, b, c, d):
  count = 0
  cnt = defaultdict(int)

  for i in a:
    for j in b:
      cnt[i + j] += 1
  
  for i in c:
    for j in d:
      count += cnt.get(-(i + j), 0)
      
  return count

print(solution(n, a, b, c, d))
