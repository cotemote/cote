function solution(A, B) {
    let answer = 0;
    let i = 0, j = 0;
    
    A.sort((a, b) => a - b)
    B.sort((a, b) => a - b)
    
    while (i < A.length && j < B.length) {
        if (B[j] > A[i]) {
            answer++;
            i++
        }
        j++
    }
    
    return answer;
}
