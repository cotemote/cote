[n, m] = list(map(int, input().split()))
nums = sorted([x for x in set(list(map(int, input().split())))])


def solution(stack):
    global m, nums

    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return

    for num in nums:
        stack.append(num)
        solution(stack)
        stack.pop()


solution([])
