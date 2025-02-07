# 아스키코드를 활용해서 초기 사전 만들기
# 문자열을 순회하면서 현재 위치에서 시작하는 가능한 가장 긴 문자열 찾기
# 찾은 문자열의 색인 번호를 answer 배열에 추가하고, 그 다음 문자를 포함한 새로운 문자열을 사전에 추가
# 처리된 문자열 길이만큼 인덱스를 이동


def solution(msg):
    answer = []
    dictionary = {}
    for i in range(26):
        dictionary[chr(65+i)] = i+1
        
    idx = 27
    
    i = 0
    while i < len(msg):
        length = 1
        while i + length <= len(msg) and msg[i:i+length] in dictionary:
            length += 1
        
        answer.append(dictionary[msg[i:i+length-1]])
        
        if i + length <= len(msg):
            dictionary[msg[i:i+length]] = idx
            idx += 1
            
        i += length-1
        
    return answer