import sys
input = sys.stdin.readline

def tracking(k) :
    if k == m :
        for i in range(m) :
            print(answer[i], end = ' ')
        print()
        return
    temp = 0
    for i in range(n) :
        if temp != arr[i] :
            answer[k] = arr[i]
            temp = arr[i]
            tracking(k+1)
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = [-1] * n
    tracking(0)
