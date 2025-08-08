def make_num(str):
    result = 0
    for i in range(len(str)):
        result += pow(26, len(str) - 1 - i) * (ord(str[i]) - ord("a") + 1)
    return result


def make_str(num):
    result = ""
    while num > 0:
        result = chr((num - 1) % 26 + ord("a")) + result
        num = (num - 1) // 26
    return result


def solution(n, bans):
    ban_nums = sorted(make_num(ban) for ban in bans)
    for ban in ban_nums:
        if ban <= n:
            n += 1

    return make_str(n)
