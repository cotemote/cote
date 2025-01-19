const BONUS_TYPES = {
    S: 1,
    D: 2,
    T: 3,
};

const OPTION_TYPES = {
    "*": 2,
    "#": -1,
};

const parseGameResults = (dartResult) => {
    const regex = /(\d+)([SDT])([*#])?/g;
    const rounds = [];
    let match;

    while ((match = regex.exec(dartResult)) !== null) {
        rounds.push({
            score: parseInt(match[1]),
            bonus: match[2],
            option: match[3] || null,
        });
    }

    return rounds;
};

const calculateScore = (rounds) => {
    const scores = [];

    rounds.forEach(({ score, bonus, option }, index) => {
        let roundScore = Math.pow(score, BONUS_TYPES[bonus]);

        if (option === "#") {
            roundScore *= OPTION_TYPES["#"];
        } else if (option === "*") {
            roundScore *= OPTION_TYPES["*"];
            if (index > 0) {
                scores[index - 1] *= OPTION_TYPES["*"];
            }
        }

        scores.push(roundScore);
    });

    return scores.reduce((sum, score) => sum + score, 0);
};

function solution(dartResult) {
    const rounds = parseGameResults(dartResult);
    return calculateScore(rounds);
}
