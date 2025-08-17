from itertools import combinations

def solution(coin, cards):
    n = len(cards)
    target = n + 1
    max_round = 0
    start_cards = set(cards[:n // 3])

    def dfs(idx, coin, hand, round_count):
        nonlocal max_round

        max_round = max(max_round, round_count)

        if idx >= n:
            return

        new1 = cards[idx]
        new2 = cards[idx + 1]
        next_idx = idx + 2

        options = []

        options.append((coin, hand.copy()))  # 둘 다 안 삼

        if coin >= 1:
            options.append((coin - 1, hand | {new1}))
            options.append((coin - 1, hand | {new2}))
        if coin >= 2:
            options.append((coin - 2, hand | {new1, new2}))

        for next_coin, next_hand in options:
            found = False
            for a, b in combinations(next_hand, 2):
                if a + b == target:
                    new_hand = next_hand.copy()
                    new_hand.remove(a)
                    new_hand.remove(b)
                    dfs(next_idx, next_coin, new_hand, round_count + 1)
                    found = True
                    break
    dfs(n // 3, coin, start_cards, 0)
    return max_round
