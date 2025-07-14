n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
  arr.sort()

  min_sum = float('inf')
  result = (0, 0, 0)

  for i in range(n - 2):
    left, right = i + 1, n - 1
    
    while left < right:
      sum = arr[i] + arr[left] + arr[right]
      if abs(sum) < min_sum:
        min_sum = abs(sum)
        result = (arr[i], arr[left], arr[right])
      
      if sum > 0:
        right -= 1
      elif sum < 0:
        left += 1
      else:
        return result

  return result

print(*solution(n, arr))
