from itertools import combinations, product
from collections import Counter
import bisect

def solution(dice):
    n = len(dice)
    half = n // 2
    max_win = -1
    answer = []

    for a_dice_indices in combinations(range(n), half):
        b_dice_indices = [i for i in range(n) if i not in a_dice_indices]
        
        a_sums = [sum(p) for p in product(*[dice[i] for i in a_dice_indices])]
        b_sums = [sum(p) for p in product(*[dice[i] for i in b_dice_indices])]
        
        b_sums.sort()
        win = 0
      
        for a_sum in a_sums:
            win += bisect.bisect_left(b_sums, a_sum)
        
        if win > max_win:
            max_win = win
            answer = sorted([i + 1 for i in a_dice_indices]

    return answer
