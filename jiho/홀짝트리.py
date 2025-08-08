import sys

sys.setrecursionlimit(400_000)


def check_orderd_tree(idx, child_cnt):
    return idx % 2 == child_cnt % 2


def check_unorderd_tree(idx, child_cnt):
    return idx % 2 != child_cnt % 2


def check_tree(graph, idx, is_root, visited, check):
    visited.add(idx)
    child_cnt = len(graph[idx]) - 1
    if is_root:
        child_cnt += 1
    if not check(idx, child_cnt):
        return False
    for child in graph[idx]:
        if child in visited:
            continue
        if not check_tree(graph, child, False, visited, check):
            return False
    return True


def solution(nodes, edges):
    graph = [[] for _ in range(1_000_001)]
    for [a, b] in edges:
        graph[a].append(b)
        graph[b].append(a)

    answer = [0, 0]
    visited1 = set()
    visited2 = set()
    for idx in nodes:
        if not idx in visited1:
            s = set()
            if check_tree(graph, idx, True, s, check_orderd_tree):
                answer[0] += 1
                visited1 = visited1 | s
        if not idx in visited2:
            s = set()
            if check_tree(graph, idx, True, s, check_unorderd_tree):
                answer[1] += 1
                visited2 = visited2 | s
    return answer
