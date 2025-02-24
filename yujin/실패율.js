function solution(N, stages) {
    stages.sort((a,b) => a - b)
    let remain = stages.length;
    let pointer = 0;
    const fails = [];
    for (let i = 1; i <= N; i++){
        let failer = 0;
        while(stages[pointer] <= i) {
            failer++;
            pointer++;
        }
        fails.push(failer / remain);
        remain -= failer;
    }
    const answer = fails.map((value, index) => [value, index + 1]);
    answer.sort((a, b) => b[0] - a[0])
    
    return answer.map(val => val[1]);
}
