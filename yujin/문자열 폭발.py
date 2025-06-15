string = input()
bomb = input()

def solution(string, bomb):
  stack = []
  bomb_len = len(bomb)

  for ch in string:
    stack.append(ch)
    if len(stack) >= bomb_len and "".join(stack[-bomb_len:]) == bomb:
      for _ in range(bomb_len):
        stack.pop()
  
  return "".join(stack) if stack else "FRULA"

print(solution(string, bomb))
