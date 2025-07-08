n = int(input())
arr = sorted(list(map(int, input().split())))

standard = 1e9 * 4

find = False
for i in range(n - 2) :
  left = i + 1
  right = n - 1
  while left < right :
    cal = arr[left] + arr[right] + arr[i]
    if abs(cal) <= abs(standard) :
      standard = cal
      solCandidate = [arr[i], arr[left], arr[right]]

    if cal < 0 :
      left += 1
    elif cal > 0 :
      right -= 1
    else :
      find = True
      print(*solCandidate)
      break
    if find :
      break
print(*solCandidate)
