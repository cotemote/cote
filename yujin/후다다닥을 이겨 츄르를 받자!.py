n = int(input())
stations = list(map(int, input().split()))
m = int(input())
trans = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
inputs = [list(map(int, input().split())) for _ in range(k)]

from collections import defaultdict
import heapq

def solution(stations, trans, input_val):
  t, u1, u2, v1, v2 = input_val
  INF = float('inf')
  
  trans_dict = defaultdict(list)

  for tran in trans:
    p1, p2, q1, q2 = tran
    trans_dict[p1, p2].append((q1, q2))
    trans_dict[q1, q2].append((p1, p2))

  dist = []
  dist.append([])
  for count in stations:
    dist.append([INF for _ in range(count + 1)])

  heap = [(0, u1, u2)]

  while heap:
    time, cu1, cu2 = heapq.heappop(heap)

    if time > dist[cu1][cu2]:
      continue

    # 목적지인지 확인
    if (cu1, cu2) == (v1, v2):
      return time
    
    # 이전역
    if cu2 - 1 >= 1 and time + 1 < dist[cu1][cu2 - 1]:
      dist[cu1][cu2 - 1] = time + 1
      heapq.heappush(heap, (time + 1, cu1, cu2 - 1))

    # 다음역
    if cu2 + 1 <= stations[cu1 - 1] and time + 1 < dist[cu1][cu2 +1]:
      dist[cu1][cu2 +1] = time + 1
      heapq.heappush(heap, (time + 1, cu1, cu2 + 1))

    # 환승하기
    for tran in trans_dict[cu1, cu2]:
      q1, q2 = tran
      if time + t < dist[q1][q2]:
        dist[q1][q2] = time + t
        heapq.heappush(heap, (time + t, q1, q2))

for input_val in inputs:
  print(solution(stations, trans, input_val))
