N = int(input())
A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N
for i in range(N):
    a, b, c, d = map(int, input().split())
    A[i] = a
    B[i] = b
    C[i] = c
    D[i] = d

nums = dict()
for a in A:
    for b in B:
        s = a + b
        if s in nums:
            nums[s] += 1
        else:
            nums[s] = 1

ans = 0
for c in C:
    for d in D:
        s = c + d
        if -s in nums:
            ans += nums[-s]

print(ans)
