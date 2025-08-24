def solution(users, emoticons):
    emoticonCnt = len(emoticons)
    answer = []
    def find(depth, emos) :
        nonlocal answer
        if emoticonCnt == depth :
            subscribe, total = 0, 0
            for user in users :
                cost = 0
                pTarget, cTarget = user
                for i in range(len(emos)) :
                    emo = emos[i]
                    if emo >= pTarget :
                        cost += (emoticons[i] * (100-emo) / 100) 
                if cost >= cTarget :
                    subscribe += 1
                else :
                    total += cost
            answer.append([subscribe, total])
            return
        for percentage in [10, 20, 30, 40] :
            emos.append(percentage)
            find(depth+1, emos)
            emos.pop()
    find(0, [])
    answer.sort(key = lambda x : (-x[0], -x[1]))
    return answer[0]
