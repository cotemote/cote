def find(x) :
    if x == nums[x] :
        return x
    return find(nums[x])
def union(a, b) :
    parentA = find(a)
    parentB = find(b)
    if parentA < parentB :
        nums[parentB] = parentA
    else :
        nums[parentA] = parentB
        
n = int(input())
nums = [i for i in range(n+1)]
for _ in range(n-2) :
    a, b = map(int, input().split())
    union(a, b)

for i in range(2, n+1) :
    if find(1) != find(i) :
        print(1, i)
        break