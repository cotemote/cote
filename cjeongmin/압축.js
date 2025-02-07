function solution(msg) {
    const answer = [];
    const dict = new Map();
    for (let i = "A".charCodeAt(); i <= "Z".charCodeAt(); i++) {
        dict.set(String.fromCharCode(i), dict.size + 1);
    }

    let i = 0;
    while (i < msg.length) {
        let j = i + 1;
        while (j <= msg.length && dict.has(msg.slice(i, j))) {
            j++;
        }
        const current = msg.slice(i, j - 1);
        answer.push(dict.get(current));
        if (j <= msg.length) {
            dict.set(msg.slice(i, j), dict.size + 1);
        }
        i = j - 1;
    }

    return answer;
}
