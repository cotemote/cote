str1 = list(input())
str2 = list(input())

dp = [[0] * (len(str1)+1) for _ in range(len(str2) + 1)]
for i in range(1, len(str2)+1) :
  for j in range(1, len(str1)+1) :
    if str2[i-1] == str1[j-1] :
      dp[i][j] = dp[i-1][j-1] + 1
    else :
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i, j = len(str1), len(str2)
while i > 0 and j > 0 :
  if str1[i-1] == str2[j-1] :
    answer = str2[j-1] + answer
    i -= 1
    j -= 1
  elif str1[i-1] >= str2[j-1] :
    i -= 1
  else :
    j -= 1
    
print(answer)
print(max(max(dp)))
