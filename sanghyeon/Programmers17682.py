def solution(dartResult):
    answer = 0
    result = 0
    scores = []
    bonus = {'S':1, 'D':2, 'T':3}
    for i in range(len(dartResult)) :
        c = dartResult[i] 
        if c == 'S' or c == 'D' or c == 'T' :
            if dartResult[i-2] == '1' and dartResult[i-1] == '0' :
                result = 10
            else :
                result = int(dartResult[i-1])
            
            result = result ** bonus[c]
            
            ok = False
            if len(dartResult)-1 >= i+1 :
                ok = True
            
            if ok and dartResult[i+1] == '*' :
                if scores :
                    scores[-1] = scores[-1] * 2
                    result *= 2
                else :
                    result *= 2
            if ok and dartResult[i+1] == '#' :
                result = result * (-1)
                
            scores.append(result)

    answer = sum(scores)
    return answer
