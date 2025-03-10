const directions = {
    d: [1, 0],
    l: [0, -1],
    r: [0, 1],
    u: [-1, 0],
};

function solution(n, m, x, y, r, c, k) {
    let answer = '';
    let found = false;

    function dfs(row, col, steps, path) {
        if (found) return;
        if (steps === k) {
            if (row === r && col === c) {
                answer = path;
                found = true;
            }
            return;
        }

        const remain = k - steps;
        const dist = Math.abs(row - r) + Math.abs(col - c);
        if (dist > remain || (remain - dist) % 2 !== 0) return;

        for (const d of ['d', 'l', 'r', 'u']) {
            const newRow = row + directions[d][0];
            const newCol = col + directions[d][1];

            if (newRow < 1 || newRow > n || newCol < 1 || newCol > m) continue;

            dfs(newRow, newCol, steps + 1, path + d);
        }
    }

    const initialDist = Math.abs(x - r) + Math.abs(y - c);
    if (initialDist > k || (k - initialDist) % 2 !== 0) return 'impossible';

    dfs(x, y, 0, '');
    return found ? answer : 'impossible';
}
