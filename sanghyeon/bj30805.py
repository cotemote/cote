a = int(input())
arrA = list(map(int, input().split()))
b = int(input())
arrB = list(map(int, input().split()))

def solution(arrA, arrB, res = []) :
    if (not arrA) or (not arrB) :
        return res
    maxA = max(arrA)
    maxB = max(arrB)
    idxA = arrA.index(maxA)
    idxB = arrB.index(maxB)
    if maxA == maxB :
        res.append(maxA)
        return solution(arrA[idxA+1:], arrB[idxB+1:], res)
    elif maxA > maxB :
        arrA.pop(idxA)
        return solution(arrA, arrB, res)
    else :
        arrB.pop(idxB)
        return solution(arrA, arrB, res)
answer = solution(arrA, arrB)
print(len(answer))
print(*answer)