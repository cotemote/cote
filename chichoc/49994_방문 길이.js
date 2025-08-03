function solution(dirs) {
    let answer = 0;
    let currX = 5, currY = 5;
    const moving = {U: [1, 0], D: [-1, 0], R: [0, 1], L: [0, -1]}
    const visited = Array.from({length: 11}, () => Array.from({length: 11}, () => []));
    
    const checkLine = (x1, y1, x2, y2) => {
        for (const [y, x] of visited[y1][x1]) {
            if (x !== x2 || y !== y2) continue;
            return true;
        }
        visited[y1][x1].push([y2, x2])
        visited[y2][x2].push([y1, x1])
        return false;
    }
    
    for (const dir of dirs) {
        const nextX = currX + moving[dir][1]
        const nextY = currY + moving[dir][0];
        if (nextX < 0 || nextX > 10 || nextY < 0 || nextY > 10) continue;
        
        const isVisited = checkLine(nextX, nextY, currX, currY);
        currX = nextX, currY = nextY;
        if (isVisited) continue;
        answer++;
    }
    return answer;
}
