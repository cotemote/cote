from itertools import combinations

def checkUnique(relation, cols):
    keys = set()
    for row in relation:
        key = ()
        for col in cols:
            key = key + (row[col],)
        keys.add(key)
    return len(relation) == len(keys)

def solution(relation):
    M = len(relation[0])
    arr = [i for i in range(M)]
    comb = [combinations(arr, i + 1) for i in range(M)]
    
    candidates = set()
    for c in comb:
        for e in c:
            if any(set(x).issubset(set(e)) for x in candidates):
                continue
            if checkUnique(relation, e):
                candidates.add(e)
    
    return len(candidates)