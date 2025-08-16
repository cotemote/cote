def check(deck1, deck2, target):
    for c in deck1:
        if target - c in deck2:
            deck1.remove(c)
            deck2.remove(target - c)
            return True
    return False


def solution(coin, cards):
    n = len(cards)
    hand = set()
    for i in range(0, n // 3):
        hand.add(cards[i])

    answer = 1
    idx = n // 3
    pending = set()
    while coin >= 0 and idx < n:
        pending.add(cards[idx])
        pending.add(cards[idx + 1])

        if check(hand, hand, n + 1):
            pass
        elif coin >= 1 and check(hand, pending, n + 1):
            coin -= 1
        elif coin >= 2 and check(pending, pending, n + 1):
            coin -= 2
        else:
            break
        idx += 2
        answer += 1
    return answer
