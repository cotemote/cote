const isAlphabet = (char) => /[a-z]/.test(char);

const createMultiSet = (str) => {
    const pairs = [];
    const lower = str.toLowerCase();

    for (let i = 0; i < lower.length - 1; i++) {
        if (isAlphabet(lower[i]) && isAlphabet(lower[i + 1])) {
            pairs.push(lower.slice(i, i + 2));
        }
    }

    return pairs;
};

const getFrequencyMap = (arr) => {
    const freqMap = new Map();
    arr.forEach((item) => {
        freqMap.set(item, (freqMap.get(item) ?? 0) + 1);
    });
    return freqMap;
};

const expandMapToArray = (map) => {
    return Array.from(map.entries()).flatMap(([item, count]) => Array(count).fill(item));
};

const getUnion = (set1, set2) => {
    const freq1 = getFrequencyMap(set1);
    const freq2 = getFrequencyMap(set2);

    const unionMap = new Map(freq1);
    for (const [key, count] of freq2) {
        unionMap.set(key, Math.max(unionMap.get(key) ?? 0, count));
    }

    return expandMapToArray(unionMap);
};

const getIntersection = (set1, set2) => {
    const freq1 = getFrequencyMap(set1);
    const freq2 = getFrequencyMap(set2);

    const intersectionMap = new Map();
    for (const [key, count] of freq1) {
        if (freq2.has(key)) {
            intersectionMap.set(key, Math.min(count, freq2.get(key)));
        }
    }

    return expandMapToArray(intersectionMap);
};

function solution(str1, str2) {
    const set1 = createMultiSet(str1);
    const set2 = createMultiSet(str2);

    const unionSet = getUnion(set1, set2);
    const intersectionSet = getIntersection(set1, set2);

    if (unionSet.length === 0) return 65536;
    return Math.floor((intersectionSet.length / unionSet.length) * 65536);
}
