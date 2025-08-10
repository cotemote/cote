function solution(info, n, m) {
    let minA = Infinity;
    const infoLen = info.length;
    const visited = new Set();
    
    const sumB = info.reduce((sum, arr) => sum + arr[1], 0);
    if (sumB < m) return 0;
    
    const dfs = (sumA, sumB, i) => {
        console.log(sumA, sumB, i)
        if (sumA >= n || sumB >= m || sumA >= minA) return;
        if (i === infoLen) {
            minA = Math.min(minA, sumA)
            return;
        }
        
        const key = `${sumA},${sumB},${i}`;
        if (visited.has(key)) return;
        visited.add(key);
        
        dfs(sumA + info[i][0], sumB, i + 1)
        dfs(sumA, sumB + info[i][1], i + 1)
    }
    
    dfs(0, 0, 0);
    
    return minA === Infinity ? -1 : minA;
}
