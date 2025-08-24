function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let deliverySum = 0;
    let pickupSum = 0;

    for (let i = n - 1; i >= 0; i--) {
        deliverySum += deliveries[i];
        pickupSum += pickups[i];
        
        while (deliverySum > 0 || pickupSum > 0) {
            deliverySum -= cap;
            pickupSum -= cap;
            answer += (i + 1) * 2;
        }
    }
    
    return answer;
}
