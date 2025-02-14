# combinations로 가능한 모든 컬럼 조합을 만들고,
# 모든 조합에 대해 유일성 검사를 하고, 이를 통과한 조합에 대해 최소성 검사 진행

from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combinations(range(col), i))
    
    unique = []
    for candidate in candidates:
        tmp = [tuple(relation[i][j] for j in candidate) for i in range(row)]
        if len(set(tmp)) == row:
            unique.append(candidate)
    
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(set(unique[i])) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])
    
    return len(answer)