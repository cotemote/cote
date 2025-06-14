import sys

strs = list(sys.stdin.readline().strip())
boom = list(sys.stdin.readline().strip())

stack = []
for s in strs:
    stack.append(s)
    if stack[-len(boom) :] == boom:
        for _ in range(len(boom)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
