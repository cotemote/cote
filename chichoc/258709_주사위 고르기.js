function solution(dice) {
    const n = dice.length;
    let maxWins = 0;
    let bestCombination = [];
    
    const combinations = (arr, size) => {
        if (size === 1) return arr.map(v => [v]);
        const result = [];
        arr.forEach((fixed, index) => {
            const rest = arr.slice(index + 1);
            const combs = combinations(rest, size - 1);
            combs.forEach(comb => result.push([fixed, ...comb]));
        });
        return result;
    }
    
    const calculateSums = (diceIndices) => {
        const sums = [];
        const selectedDice = diceIndices.map(i => dice[i]);
        
        function roll(depth, sum) {
            if (depth === selectedDice.length) {
                sums.push(sum);
                return;
            }
            
            selectedDice[depth].forEach(face => {
                roll(depth + 1, sum + face);
            });
        }
        
        roll(0, 0);
        return sums.sort((a, b) => a - b);
    }
    
    const countWins = (aScores, bScores) => {
        let winCount = 0;
        
        for (let aScore of aScores) {
            let left = 0, right = bScores.length - 1;
            let count = 0;
            
            while (left <= right) {
                let mid = Math.floor((left + right) / 2);
                if (bScores[mid] < aScore) {
                    count = mid + 1;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            winCount += count;
        }
        return winCount;
    }
    
    const allCombinations = combinations([...Array(n).keys()], n / 2);
    
    for (let i = 0; i < allCombinations.length / 2; i++) {
        const aComb = allCombinations[i];
        const bComb = [...Array(n).keys()].filter(x => !aComb.includes(x));
        
        const aSums = calculateSums(aComb);
        const bSums = calculateSums(bComb);
        
        const aWins = countWins(aSums, bSums);
        const bWins = countWins(bSums, aSums);
        
        if (aWins > maxWins) {
            maxWins = aWins;
            bestCombination = aComb.map(x => x + 1);
        }
        
        if (bWins > maxWins) {
            maxWins = bWins;
            bestCombination = bComb.map(x => x + 1);
        }
    }
    
    return bestCombination.sort((a, b) => a - b);
}
