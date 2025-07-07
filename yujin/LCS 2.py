str1 = input()
str2 = input()

def solution(s1, s2):
  dp = [[""] * (len(s2) + 1) for _ in range(len(s1) + 1)]

  for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
      if s1[i - 1] == s2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
      else:
        if len(dp[i][j - 1]) > len(dp[i - 1][j]):
          dp[i][j] = dp[i][j - 1]
        else:
          dp[i][j] = dp[i - 1][j]
  
  return dp[len(s1)][len(s2)]

result = solution(str1, str2)
print(len(result))
if len(result) > 0:
  print(result)
