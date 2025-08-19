def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx, p_idx = n - 1, n - 1
    while d_idx >= 0 or p_idx >= 0:
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        while p_idx >= 0 and pickups[p_idx] == 0:
            p_idx -= 1
        answer += (max(d_idx, p_idx) + 1) * 2
        d_cnt = 0
        while d_cnt < cap and d_idx >= 0:
            can_deliver = min(cap - d_cnt, deliveries[d_idx])
            deliveries[d_idx] -= can_deliver
            d_cnt += can_deliver
            if deliveries[d_idx] == 0:
                d_idx -= 1
        p_cnt = 0
        while p_cnt < cap and p_idx >= 0:
            can_pickup = min(cap - p_cnt, pickups[p_idx])
            pickups[p_idx] -= can_pickup
            p_cnt += can_pickup
            if pickups[p_idx] == 0:
                p_idx -= 1
    return answer
