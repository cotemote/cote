function solution(A, B) {
    const rev = (a, b) => (b - a)
    A.sort(rev)
    B.sort(rev)
    console.log(A)
    console.log(B)
    
    let ans = 0
    let s = 0, e = B.length - 1
    for(const a of A) {
        if(B[s] > a) {
            ans += 1
            s += 1
        } else {
            if(B[e] > a) {
                ans += 1
            }
            e -= 1
        }
    }
    return ans
}