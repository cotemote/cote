const insert = (trie, text) => {
    let curr = trie;
    curr.count = (curr.count ?? 0) + 1;
    for (const c of text) {
        if (!(c in curr.nodes)) curr.nodes[c] = { nodes: {} };
        curr = curr.nodes[c];
        curr.count = (curr.count ?? 0) + 1;
    }
};

const calc = (trie, word) => {
    let depth = 0;
    let curr = trie;
    for (const c of word) {
        depth += 1;
        curr = curr.nodes[c];
        if (curr.count === 1) break;
    }
    return depth;
};

function solution(words) {
    const trie = { nodes: {} };
    words.forEach((word) => insert(trie, word));
    return words.reduce((acc, word) => acc + calc(trie, word), 0);
}
