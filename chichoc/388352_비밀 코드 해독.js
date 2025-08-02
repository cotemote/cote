function solution(n, q, ans) {
    const m = ans.length;
    const never = new Set();
    const numbers = Array.from({length: n}, (_, idx) => idx + 1);
    let answer = 0;
    
    const combination = (nArray, k, idx = 0, path = []) => {
        if (path.length === k) {
            for (let i = 0; i < m; i++) {
                const count = path.filter(num => q[i].includes(num)).length;
                if (count !== ans[i]) return;
            }
            answer++;
            return;
        }
        for (let i = idx; i < nArray.length; i++) {
            path.push(nArray[i]);
            combination(nArray, k, i + 1, path);
            path.pop();
        }
      
    };
    
    for (let i = 0; i < m; i++) {
        if (ans[i] > 0) continue;
        q[i].forEach(num => never.add(num))        
    }
    
    const available = numbers.filter(num => !never.has(num));
    combination(available, 5)
    
    return answer;
}
