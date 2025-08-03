function solution(dirs) {
    const directions = {
        'U': [-1,0],
        'L': [0,-1],
        'D': [1, 0],
        'R': [0, 1]
    }
    
    let answer = new Set();
    let pos = [0, 0]
    for(const d of dirs) {
        let next = [0, 0]
        next[0] = pos[0] + directions[d][0]
        next[1] = pos[1] + directions[d][1]
        if(next[0] < -5 || next[1] < -5 || next[0] > 5 || next[1] > 5)
            continue
        const [start, end] = pos[0] < next[0] || (pos[0] === next[0] && pos[1] < next[1]) 
            ? [pos, next] : [next, pos];
        const roadKey = [...start, ...end].join(",")
        answer.add(roadKey);
        pos = [...next]
    }
    return answer.size
}