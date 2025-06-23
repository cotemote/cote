n, m, k = map(int, input().split())

inputs = []
for _ in range(m):
    r, c, m_, s, d = map(int, input().split())
    inputs.append((r - 1, c - 1, m_, s, d))

from collections import deque, defaultdict

def solution(n, m, k, inputs):
  fireballs = deque(inputs)

  directions = [
      (-1, 0), (-1, 1), (0, 1), (1, 1),
      (1, 0), (1, -1), (0, -1), (-1, -1)
  ]

  def move(n, fireballs):
    new_dict = defaultdict(list)
    while fireballs:
      r, c, m, s, d = fireballs.popleft()
      dir_r, dir_c = directions[d]
      next_r = (r + dir_r * s) % n
      next_c = (c + dir_c * s) % n
      new_dict[(next_r, next_c)].append((m, s, d))
    return new_dict

  for _ in range(k):
    new_dict = move(n, fireballs)

    for (r, c), items in new_dict.items():
        if len(items) == 1: # 파이어볼이 1개일 때
            fireballs.append((r, c, *items[0]))
        else: # 파이어볼 여러 개가 겹쳤을 때
            total_m = sum(x[0] for x in items)
            total_s = sum(x[1] for x in items)

            new_m = total_m // 5
            if new_m == 0:
                continue
            avg_s = total_s // len(items)

            flags = []
            for item in items:
                direction = item[2]
                flags.append(direction % 2)

            new_dirs = []
            
            if len(set(flags)) == 1:
                new_dirs = [0, 2, 4, 6]
            else:
                new_dirs = [1, 3, 5, 7]

            for nd in new_dirs:
                fireballs.append((r, c, new_m, avg_s, nd))

  return sum(m for _, _, m, _, _ in fireballs)

print(solution(n, m, k, inputs))
