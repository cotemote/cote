from collections import deque
def solution(numbers):
    answer = []
    
    for nums in numbers :
        num = bin(nums)[2:]

        n = 0
        for i in range(10000) :
            if i < 2 ** i :
                n = i
                break
                
        while len(num) != 2 ** n - 1 :
            num = '0' + num
        
        root = len(num) // 2
        deq = deque([root])
        flag = True
        while n != 0 and flag :
            gap = 2 ** (n-2) 
            if n == 1 :
                break
            nextDeq = deque()
            while deq :
                root = deq.popleft()
                left = root - gap
                right = root + gap
                if num[root] == "0" :
                    if num[left] == "1" or num[right] == "1" :
                        answer.append(0)
                        flag = False
                        break
                
                nextDeq.append(right)
                nextDeq.append(left)
            deq = nextDeq
            n -= 1
        if flag == True :
            answer.append(1)
            
    return answer