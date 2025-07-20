g = int(input())
p = int(input())
roots = [i for i in range(g + 1)]

def find(x):
  if roots[x] != x:
    roots[x] = find(roots[x])
  return roots[x]


def union(a, b):
  root_a = find(a)
  root_b = find(b)

  if root_a == root_b:
    return

  roots[root_a] = root_b

answer = 0

for x in range(p):
  gate = int(input())
  root = find(gate)

  if root == 0:
    break
  
  answer += 1
  union(root, root - 1)

print(answer)
