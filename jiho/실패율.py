def solution(N, stages):
    counter = [0 for i in range(N + 2)]
    for stage in stages:
        counter[stage]+=1
    
    fail = []
    total = len(stages)
    for i, c in enumerate(counter[1:-1]):
        fail.append((i+1, 0 if total == 0 else c/total))
        total -= c
    
    fail.sort(key= lambda f: (-f[1], f[0]))
    return [idx for (idx, _) in fail]