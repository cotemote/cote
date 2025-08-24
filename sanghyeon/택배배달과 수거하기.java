import java.util.*;
class Pair implements Comparable<Pair> {
    int idx;
    int cnt;
    public Pair(int idx, int cnt) {
        this.idx = idx;
        this.cnt = cnt;
    }
    
    @Override
    public int compareTo(Pair o) {
        return o.idx - this.idx;
    }
}
class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        PriorityQueue<Pair> deli = new PriorityQueue<>();
        ArrayList<Pair> pick = new ArrayList<>();
        
        int lastPickIndex = 0;
        for(int i = 0; i < n; i++) {
            if(deliveries[i] > 0) deli.offer(new Pair(i+1, deliveries[i]));
            if(pickups[i] > 0) {pick.add(new Pair(i+1, pickups[i])); lastPickIndex = i;}
        }
        
        int deliverySum = 0;
        int buf = 0;
        int far = 0;
        
        while(!deli.isEmpty()) {
            Pair pair = deli.poll();
            if(far == 0) far = pair.idx;
            buf += pair.cnt;
            if(buf > cap) {
                answer += (long)far * 2;
                deliverySum += cap;
                deli.offer(new Pair(pair.idx, buf - cap));
                buf = 0;
                far = 0;
            }
            else if(buf == cap) {
                answer += (long)far * 2;
                deliverySum += cap;
                far = 0;
                buf = 0;
            }
        }
        if(buf > 0) {
            answer += (long) far * 2;
            deliverySum += buf;
        }
        
        Collections.sort(pick, Collections.reverseOrder());
        
        int pickSum = 0;
        for(int i = 0; i < pick.size(); i++) {
            if(pick.get(i).cnt <= deliverySum) {
                deliverySum -= pick.get(i).cnt;
                pick.remove(0);
            }
            else {
                pick.get(i).cnt -= deliverySum;
                deliverySum = 0;
                pickSum += pick.get(i).cnt;
                if(pickSum > cap) {
                    answer += (long) pick.get(i).idx * 2;
                    pickSum = pick.get(i).cnt - pickSum;
                }
                else if(pickSum == cap) {
                    answer += (long) pick.get(i).idx * 2;
                    pickSum = 0;
                }
                pick.remove(0);
            }
        }
        if(pickSum > 0) {
            answer += (long) lastPickIndex * 2;
        }

        return answer;
    }
}
