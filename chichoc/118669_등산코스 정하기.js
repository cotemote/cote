function solution(n, paths, gates, summits) {
    const graph = Array.from({length: n + 1}, () => []);
    const isSummit = new Set(summits);
    const isGate = new Set(gates);
    
    paths.forEach(([a, b, w]) => {
        graph[a].push([b, w]);
        graph[b].push([a, w]);
    });
    
    const intensity = Array(n + 1).fill(Infinity);
    let queue = [...gates];
    
    gates.forEach(gate => intensity[gate] = 0);
    
    while (queue.length > 0) {
        const nextQueue = [];
        
        for (const current of queue) {
            for (const [next, weight] of graph[current]) {
                if (isGate.has(next)) continue;
                
                const newIntensity = Math.max(intensity[current], weight);
                
                if (newIntensity < intensity[next]) {
                    intensity[next] = newIntensity;
                    
                    if (!isSummit.has(next)) {
                        nextQueue.push(next);
                    }
                }
            }
        }
        
        queue = [...new Set(nextQueue)];
    }
    
    return summits
        .map(s => [s, intensity[s]])
        .sort((a, b) => a[1] === b[1] ? a[0] - b[0] : a[1] - b[1])[0];
}
