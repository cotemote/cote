Max = 1000000
n = int(input())
dp = [[[0]* 3 for _ in range(2)]for _ in range(n+1)]
dp[1][0][0] = dp[1][1][0] = dp[1][0][1] = 1
for i in range(2, n+1) :
  dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % Max
  dp[i][1][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2] + dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % Max
  dp[i][1][1] = (dp[i-1][1][0]) % Max
  dp[i][1][2] = (dp[i-1][1][1]) % Max
  dp[i][0][1] = (dp[i-1][0][0]) % Max
  dp[i][0][2] = (dp[i-1][0][1]) % Max

answer = (dp[n][0][0] + dp[n][0][1] + dp[n][0][2] + dp[n][1][0] + dp[n][1][1] + dp[n][1][2]) % Max
print(answer)
