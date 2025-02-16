function solution(relation) {
    const N = relation.length;
    const M = relation[0].length;
    return Array.from({ length: (1 << M) - 1 }, (_, idx) => idx + 1).reduce((acc, bit) => {
        const keys = relation.map((row) => row.filter((_, j) => bit & (1 << j)).join("|"));
        if (new Set(keys).size !== N) return acc;
        if (acc.some((candidate) => (candidate & bit) === candidate)) return acc;
        return [...acc, bit];
    }, []).length;
}
