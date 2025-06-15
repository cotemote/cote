arr1_len = int(input())
arr1 = list(map(int, input().split()))
arr2_len = int(input())
arr2 = list(map(int, input().split()))

commons = set(arr1) & set(arr2)

if not commons:
  print(0)
  exit()

result = []

while commons:
  max_val = max(commons)
  result.append(max_val)

  idx1 = arr1.index(max_val)
  idx2 = arr2.index(max_val)
  arr1 = arr1[idx1 + 1:]
  arr2 = arr2[idx2 + 1:]

  commons = set(arr1) & set(arr2)

print(len(result))
print(*result)
