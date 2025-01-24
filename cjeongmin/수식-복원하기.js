const isNumeric = (str) => !isNaN(Number(str));

const parseExpression = (exp) => {
    const [num1, operator, num2, _, result] = exp.split(" ");
    return { num1, operator, num2, result };
};

const calculateInBase = (num1, num2, operator, base) => {
    const n1 = parseInt(num1, base);
    const n2 = parseInt(num2, base);
    return operator === "+" ? n1 + n2 : n1 - n2;
};

const findMaxDigit = (expressions) => {
    let maxDigit = 0;
    expressions.forEach((exp) => {
        const { num1, num2, result } = parseExpression(exp);
        [num1, num2, result].forEach((num) => {
            if (isNumeric(num)) {
                maxDigit = Math.max(maxDigit, ...num.split("").map(Number));
            }
        });
    });
    return maxDigit;
};

const getPossibleBases = (expressions) => {
    const maxDigit = findMaxDigit(expressions);
    const candidates = new Set([...Array(10)].map((_, i) => i).slice(maxDigit + 1));

    return Array.from(candidates).filter((base) =>
        expressions.every((exp) => {
            const { num1, operator, num2, result } = parseExpression(exp);
            if (result === "X") return true;

            const calculated = calculateInBase(num1, num2, operator, base);
            return calculated.toString(base) === result;
        })
    );
};

function solution(expressions) {
    const bases = getPossibleBases(expressions);

    return expressions
        .map(parseExpression)
        .filter(({ result }) => result === "X")
        .map(({ num1, operator, num2 }) => {
            const results = new Set(bases.map((base) => calculateInBase(num1, num2, operator, base).toString(base)));
            return results.size === 1
                ? `${num1} ${operator} ${num2} = ${results.values().next().value}`
                : `${num1} ${operator} ${num2} = ?`;
        });
}
