def solution(info, n, m):
    memo = {}

    def find_ans(idx, acc_a, acc_b):
        if acc_a >= n:
            return -1, acc_b
        if acc_b >= m:
            return acc_a, -1
        if idx == len(info):
            return acc_a, acc_b

        key = (idx, acc_a, acc_b)
        if key in memo:
            return memo[key]

        a1, b1 = find_ans(idx + 1, acc_a + info[idx][0], acc_b)
        a2, b2 = find_ans(idx + 1, acc_a, acc_b + info[idx][1])
        fail1 = a1 == -1 or b1 == -1
        fail2 = a2 == -1 or b2 == -1
        result = (-1, -1)
        if fail1 and fail2:
            result = (-1, -1)
        elif fail1:
            result = (a2, b2)
        elif fail2:
            result = (a1, b1)
        elif a1 < a2:
            result = (a1, b1)
        else:
            result = (a2, b2)
        memo[key] = result
        return result

    a, b = find_ans(0, 0, 0)
    if a == -1 and b == -1:
        return -1
    return a
