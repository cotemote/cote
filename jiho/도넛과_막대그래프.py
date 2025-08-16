def solution(edges):
    answer = [0, 0, 0, 0]
    n = 1_000_001
    in_cnt = [0] * n
    out_cnt = [0] * n
    for a, b in edges:
        out_cnt[a] += 1
        in_cnt[b] += 1

    for i in range(1, n):
        if in_cnt[i] == 0 and out_cnt[i] >= 2:
            answer[0] = i
        elif in_cnt[i] >= 1 and out_cnt[i] == 0:
            answer[2] += 1
        elif in_cnt[i] >= 2 and out_cnt[i] == 2:
            answer[3] += 1
    total_graph_cnt = out_cnt[answer[0]]
    answer[1] = total_graph_cnt - sum(answer[2:])

    return answer
