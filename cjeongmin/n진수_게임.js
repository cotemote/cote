function solution(n, t, m, p) {
    let result = [];

    let currentIndex = 0;
    let currentNumber = 0;
    while (result.length < t) {
        const convertedNumber = currentNumber.toString(n);

        for (let j = 0; j < convertedNumber.length && result.length < t; j++) {
            if (currentIndex + 1 === p) {
                result.push(convertedNumber[j].toUpperCase());
            }

            currentIndex = (currentIndex + 1) % m;
        }

        currentNumber += 1;
    }

    return result.join("");
}
