def solution(record):
    answer = []
    # 최종 닉네임만 따지기
    #user actions -> 최종 행동(leave제외)에서 이름
    #history -> id, 행동
    userActions = {}
    history = []
    for rc in record :
        info = rc.split(' ')
        if info[0] != 'Leave' :
            userActions[info[1]] = info[2] # uid = nickname
        history.append([info[1], info[0]]) # uid, action
    for hs in history :
        uid, action = hs
        nickname = userActions[uid]
        if action == 'Enter' :
            answer.append(nickname + '님이 들어왔습니다.')
        elif action == 'Leave' :
            answer.append(nickname + '님이 나갔습니다.')
    return answer