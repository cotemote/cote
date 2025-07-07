A = input()
B = input()

N, M = len(A), len(B)
dp = [[0] * (M + 1) for _ in range(N + 1)]
A = " " + A
B = " " + B

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[N][M])

if dp[N][M] != 0:
    ans = ""
    i, j = N, M
    while dp[i][j] != 0:
        if dp[i - 1][j] == dp[i][j - 1]:
            if dp[i - 1][j] == dp[i][j]:
                i -= 1
            else:
                ans = A[i] + ans
                i -= 1
                j -= 1
        elif dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1

    print(ans)
