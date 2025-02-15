const upperBound = (arr) => (x) => {
    let left = 0;
    let right = arr.length;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] <= x) left = mid + 1;
        else right = mid;
    }
    return left;
};

function solution(N, stages) {
    stages.sort((a, b) => a - b);
    const upper = upperBound(stages);
    let curr = 0;
    return Array.from({ length: N }, (_, i) => i + 1)
        .map((stage) => [upper(stage), stage])
        .map((v) => {
            const x = (v[0] - curr) / (stages.length - curr);
            curr = v[0];
            return [x, v[1]];
        })
        .sort((a, b) => b[0] - a[0])
        .map((v) => v[1]);
}
