def count(num) :
  cnt = 0
  binNum = bin(num)[2:]
  length = len(binNum)
  for i in range(length) :
    if binNum[i] == '1' :
      val = length - i - 1
      cnt += oneSum[val]
      cnt += (num - 2**val + 1)
      num = num -2 ** val
  return cnt
x, y = map(int, input().split())
oneSum = [0 for _ in range(60)]

for i in range(1, 60) :
  oneSum[i] = 2 ** (i-1) + 2 * oneSum[i-1]

print(count(y) - count(x-1))
