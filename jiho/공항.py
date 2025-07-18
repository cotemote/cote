G = int(input())
P = int(input())
gates = [int(input()) for _ in range(P)]


def solution():
    ans = 0
    memo = [0] * (G + 1)
    result = [False] * (G + 1)
    for g in gates:
        i = g
        if memo[g] != 0:
            i = memo[i]
        while i > 0 and result[i]:
            i -= 1
        if i == 0:
            return ans
        result[i] = True

        memo[g] = i
        ans += 1

    return ans


print(solution())
