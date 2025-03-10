function solution(commands) {
    const answer = [];
    const N = 50;
    const size = N * N;
    const idx = (r, c) => (r - 1) * N + (c - 1);
    const p = Array(size).fill(0).map((_, i) => i);
    const table = Array(size).fill(null);
    const groupMembers = Array(size).fill(null).map((_, i) => new Set([i]));
    
    const find = (x) => {
        if (p[x] === x) return x;
        return p[x] = find(p[x]);
    }
    
    const union = (x, y, r1c1Priority = false) => {
        const root1 = find(x);
        const root2 = find(y);
        if (root1 === root2) return;
        
        let newRoot, otherRoot;
        if (r1c1Priority) {
            newRoot = root1;
            otherRoot = root2;
        } else {
            newRoot = root1;
            otherRoot = root2;
        }
        
        for (const member of groupMembers[otherRoot]) {
            groupMembers[newRoot].add(member);
        }
        groupMembers[otherRoot].clear();
        
        p[otherRoot] = newRoot;
        
        if (table[newRoot] === null && table[otherRoot] !== null) {
            table[newRoot] = table[otherRoot];
        }
    }
    
    for (const command of commands) {
        const parts = command.split(' ');
        const cmd = parts[0];
        
        if (cmd === 'UPDATE') {
            if (parts.length === 4) {
                const r = Number(parts[1]), c = Number(parts[2]);
                const value = parts[3];
                const index = idx(r, c);
                const root = find(index);
                table[root] = value;
            } else if (parts.length === 3) {
                const value1 = parts[1], value2 = parts[2];
                for (let i = 0; i < size; i++) {
                    if (find(i) === i && table[i] === value1) {
                        table[i] = value2;
                    }
                }
            }
        } else if (cmd === 'MERGE') {
            const r1 = Number(parts[1]), c1 = Number(parts[2]);
            const r2 = Number(parts[3]), c2 = Number(parts[4]);
            const index1 = idx(r1, c1);
            const index2 = idx(r2, c2);
            
            if (index1 === index2) continue;
            
            const root1 = find(index1);
            const root2 = find(index2);
            if (root1 === root2) continue;
            
            union(root1, root2, true);
        } else if (cmd === 'UNMERGE') {
            const r = Number(parts[1]), c = Number(parts[2]);
            const index = idx(r, c);
            const root = find(index);
            const temp = table[root];
            
            const members = Array.from(groupMembers[root]);
            for (const member of members) {
                p[member] = member;
                table[member] = null;
                groupMembers[member] = new Set([member]);
            }
            table[index] = temp;
        } else if (cmd === 'PRINT') {
            const r = Number(parts[1]), c = Number(parts[2]);
            const index = idx(r, c);
            const root = find(index);
            answer.push(table[root] !== null ? table[root] : 'EMPTY');
        }
    }
    
    return answer;
}
