function solution(n, q, ans) {
    let answer = 0
    
    function check(comb) {
        for(let i=0;i<ans.length;i++){
            query = q[i]
            cnt = ans[i]
            let queryCnt = 0
            for(const qq of query) {
                if(comb.includes(qq)) queryCnt++
            }
            if(queryCnt !== cnt) return false
        }
        return true
    }
    
    function findCombs(comb, prev) {
        if(comb.length == 5) {
            if(check(comb))
                answer += 1
            return;
        }
        for(let i = prev + 1; i <= n; i++) {
            comb.push(i)
            findCombs(comb, i)
            comb.pop()
        }
    }
    
    findCombs([], 0)
    
    return answer;
}