import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))


def solution(A, B):
    if len(A) == 0 or len(B) == 0:
        return []

    Amax, Bmax = max(A), max(B)
    Aidx, Bidx = A.index(Amax), B.index(Bmax)

    if Amax == Bmax:
        return [Amax] + solution(A[Aidx + 1 :], B[Bidx + 1 :])
    elif Amax < Bmax:
        B.pop(Bidx)
        return solution(A, B)
    else:
        A.pop(Aidx)
        return solution(A, B)


ans = solution(A, B)
print(len(ans))
print(" ".join(map(str, ans)))
