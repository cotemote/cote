const isDigit = (c) => "0" <= c && c <= "9";

const parseFilename = (file, index) => {
    const extractUntil = (str, startIdx, condition) => {
        let temp = "";
        let i = startIdx;
        while (i < str.length && condition(str[i])) {
            temp += str[i];
            i += 1;
        }
        return [temp, i];
    };

    const [head, numberStart] = extractUntil(file, 0, (c) => !isDigit(c));
    const [number, tailStart] = extractUntil(file, numberStart, isDigit);
    const tail = file.slice(tailStart);

    return {
        head,
        number,
        tail,
        originalIndex: index,
    };
};

const compareFilenames = (a, b) => {
    const headA = a.head.toUpperCase();
    const headB = b.head.toUpperCase();
    if (headA < headB) return -1;
    if (headA > headB) return 1;
    const numA = parseInt(a.number, 10);
    const numB = parseInt(b.number, 10);
    if (numA < numB) return -1;
    if (numA > numB) return 1;
    return a.originalIndex - b.originalIndex;
};

function solution(files) {
    return files
        .map((file, i) => parseFilename(file, i))
        .sort(compareFilenames)
        .map(({ head, number, tail }) => `${head}${number}${tail}`);
}
