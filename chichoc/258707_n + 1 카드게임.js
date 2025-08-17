function solution(coin, cards) {
    const cardLen = cards.length;
    const targetNum = cardLen + 1;
    const map = new Map();
    const cost = [0, 0, 0];
    let answer = 1;
    
    for(let i = 0; i < cardLen / 3; i++) {
        const a = map.get(targetNum - cards[i]);
        if(a !== undefined) {
            cost[0]++;
        }
        else{
            map.set(cards[i], 0);
        }
    }
    
    for(let i = cardLen / 3; i < cardLen; i++){
        const a = map.get(targetNum-cards[i]);
        if(a !== undefined) cost[a+1]++;
        else map.set(cards[i], 1);
        
        if(i % 2 === 0) continue;
        
        if(cost[0] !== 0) { 
            answer++; 
            cost[0]--; 
            continue; 
        }
        if(cost[1] !== 0) { 
            if(coin < 1) break;
            answer++; 
            coin--; 
            cost[1]--; 
            continue; 
        }
        if(cost[2] !== 0) { 
            if(coin < 2) break;
            answer++;
            coin -= 2;
            cost[2]--;
            continue;
        }
        break;
    }
    return answer;
}
