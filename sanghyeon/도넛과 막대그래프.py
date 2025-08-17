from collections import defaultdict

def solution(edges):
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    nodes = set()

    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1
        nodes.add(a)
        nodes.add(b)

    gen = -1
    for v in nodes:
        if indeg[v] == 0 and outdeg[v] >= 2:
            gen = v
            break
    bars = 0
    eights = 0
    for v in nodes:
        if v == gen:
            continue
        if outdeg[v] == 0:
            bars += 1
        if indeg[v] >= 2 and outdeg[v] >= 2:
            eights += 1

    donuts = outdeg[gen] - bars - eights
    return [gen, donuts, bars, eights]
