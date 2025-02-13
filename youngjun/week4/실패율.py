# for 문으로 1~N 스테이지에 대해 도달한 사람 수를 나타내는 딕셔너리 생성
# stages의 각 수에 대해 for문으로 딕셔너리 value 값 +1 
# 실패율 : 해당 스테이지 value - 다음 스테이지 value / 해당 스테이지 value

def sort_key(item):
        return (-item[1], item[0])

def solution(N, stages):
    reached = {}
    for i in range(1, N+1):
        reached[i] = 0
    
    fRate = {}
    for i in range(1, N+1):
        fRate[i] = 0
        
    total_players = len(stages)
    for stage in stages:
        if stage <= N:  
            reached[stage] += 1
            
    players = total_players
    for stage in range(1, N+1):
        if players == 0: 
            fRate[stage] = 0
        else:
            fRate[stage] = reached[stage] / players
            players -= reached[stage]
    
    fail_list = []
    for stage in range(1, N+1):
        fail_list.append((stage, fRate[stage]))
    
    fail_list.sort(key=sort_key)
    
    answer = []
    for stage, rate in fail_list:
        answer.append(stage)
        
    return answer