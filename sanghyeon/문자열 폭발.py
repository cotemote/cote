original = input()
boom = list(input())

stack = []
for alpa in original :
    stack.append(alpa)
    if stack[len(stack)-len(boom) : len(stack)] == boom :
        for _ in range(len(boom)) :
            stack.pop()
if stack :
    print(''.join(stack))
else :
    print("FRULA")