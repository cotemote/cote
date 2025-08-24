function solution(users, emoticons) {
    const discountPercents = [10, 20, 30, 40];
    const answer = {plus: 0, notPlusPrice: 0}
    const m = emoticons.length;
    const n = users.length;
    
    const getPermutations = (arr, num) => {
        const results = [];
        if (num === 1) return arr.map((el) => [el]); 
        
        arr.forEach((fixed, index, origin) => {
            const rest = [...origin.slice(0, index), ...origin.slice(index)] 
            const permutations = getPermutations(rest, num - 1); 
            const attached = permutations.map((el) => [fixed, ...el]); 
            results.push(...attached); 
        });
        return results;
    }
    
    const discountCases = getPermutations(discountPercents, m);
    
    for (let i = 0; i < discountCases.length; i++) {
        const totalPrices = Array(n).fill(0)
        for (let j = 0; j < n; j++) {
            const [d, p] = users[j]
            for (let k = 0; k < m; k++) {
                if (discountCases[i][k] < d) continue;
                totalPrices[j] += emoticons[k] * (1 - discountCases[i][k]/100)
            }
        }
        let p = 0, np = 0;
        totalPrices.forEach((price, idx) => {
            if (price >= users[idx][1]) {
                p += 1
            } else {
                np += price;
            }
        })
        if (answer.plus < p) {
            answer.plus = p;
            answer.notPlusPrice = np;
        } else if (answer.plus === p) {
            answer.notPlusPrice = Math.max(answer.notPlusPrice, np)
        }
    }
    
    return Object.values(answer);
}
