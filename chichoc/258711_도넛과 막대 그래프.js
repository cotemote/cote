function solution(edges) {
    const map = {};
    let addedNode = 0;
    let bar = 0, eight = 0;
    
    for (const [a, b] of edges) {
        if (!(a in map)) map[a] = {in: 0, out: 0};
        if (!(b in map)) map[b] = {in: 0, out: 0};
        map[a].out++;
        map[b].in++;
    }

    for (const [node, degree] of Object.entries(map)) {
        if (degree.in === 0 && degree.out >= 2) addedNode = +node;
        else if (degree.out === 0) bar++;
        else if (degree.in >= 2 && degree.out === 2) eight++;
    }

    const donut = map[addedNode].out - bar - eight;
    return [addedNode, donut, bar, eight];
}
