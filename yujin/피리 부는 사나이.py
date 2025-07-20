n, m = map(int, input().split())
map = [input() for _ in range(n)]

def solution(n, m, map):
  dir_dict = {
      "D": (0, 1), # x, y
      "L": (-1, 0),
      "R": (1, 0),
      "U": (0, -1)
  }
  mark = [[-1 for _ in range(m)] for _ in range(n)]
  mark_num = 1
  answer = set()

  for y in range(n):
    for x in range(m):
      if mark[y][x] == -1:
        curr_x = x; curr_y = y;
        temp_mark = mark_num
        pos = [(curr_x, curr_y)]

        while True:
          move_x, move_y = dir_dict[map[curr_y][curr_x]]
          next_x = curr_x + move_x; next_y = curr_y + move_y;
          if not (next_x >= 0 and next_x < m and next_y >= 0 and next_y < n):
            break

          if mark[next_y][next_x] == -1:
            curr_x = next_x; curr_y = next_y;
            mark[curr_y][curr_x] = temp_mark
            pos.append((curr_x, curr_y))
          else:
            temp_mark = mark[next_y][next_x]
            break

        while pos:
          temp_x, temp_y = pos.pop()
          mark[temp_y][temp_x] = temp_mark
        answer.add(temp_mark)

      mark_num += 1

  return len(answer)

print(solution(n, m, map))
