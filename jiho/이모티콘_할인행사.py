def get_discount_rate(m):
    result = []

    def make_permutations(perm):
        if len(perm) == m:
            result.append(perm[:])
            return
        for rate in [10, 20, 30, 40]:
            perm.append(rate)
            make_permutations(perm)
            perm.pop()

    make_permutations([])
    return result


def solution(users, emoticons):
    answer = [0, 0]
    m = len(emoticons)
    types = get_discount_rate(len(emoticons))
    for rates in types:
        prices = [0] * m
        for i in range(m):
            prices[i] = emoticons[i] * (100 - rates[i]) / 100

        total_costs, join_cnt = 0, 0
        for user in users:
            costs = 0
            joined = False
            for i in range(m):
                if rates[i] >= user[0]:
                    costs += prices[i]
                if costs >= user[1]:
                    costs = 0
                    joined = True
                    break
            if joined:
                join_cnt += 1
            total_costs += costs
        if join_cnt > answer[0]:
            answer[0] = join_cnt
            answer[1] = total_costs
        elif join_cnt == answer[0] and total_costs > answer[1]:
            answer[1] = total_costs
    return answer
