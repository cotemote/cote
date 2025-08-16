def get_combs(dice):
    combs = []

    def backtrack(arr, idx):
        if len(arr) == len(dice) // 2:
            A = arr[:]
            B = [i for i in range(len(dice)) if i not in A]
            combs.append([A, B])
            return
        for i in range(idx, len(dice)):
            arr.append(i)
            backtrack(arr, i + 1)
            arr.pop()

    backtrack([], 0)
    return combs


num_types_memo = {}


def get_sum_result(dice, dice_types):
    key = tuple(dice_types)
    if key in num_types_memo:
        return num_types_memo[key]
    num_types = dict()

    def make_sum(idx, acc):
        if idx == len(dice_types):
            if acc in num_types:
                num_types[acc] += 1
            else:
                num_types[acc] = 1
            return
        dice_type = dice_types[idx]
        for num in dice[dice_type]:
            make_sum(idx + 1, acc + num)

    make_sum(0, 0)
    num_types_memo[key] = num_types
    return num_types


def make_acc_dict(d):
    acc = dict()
    prev = 0
    for num in sorted(d.keys()):
        acc[num] = prev + d[num]
        prev = acc[num]
    return acc


def find_max_in(d, num):
    prev = 0
    for key in sorted(d.keys()):
        if key < num:
            prev = key
        elif key > num:
            return prev
    return prev


def count_win(A, B):
    win = 0
    acc_a = make_acc_dict(A)
    acc_b = make_acc_dict(B)
    for key in A:
        b_key = find_max_in(B, key)
        if b_key == 0:
            continue
        win += A[key] * acc_b[b_key]
    return win


def solution(dice):
    combs = get_combs(dice)
    max_win = 0
    answer = []
    for a_types, b_types in combs:
        a_nums = get_sum_result(dice, a_types)
        b_nums = get_sum_result(dice, b_types)
        win = count_win(a_nums, b_nums)
        if win > max_win:
            answer = [i + 1 for i in a_types]
            max_win = win
    return answer
