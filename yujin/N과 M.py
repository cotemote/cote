a, b = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def solution(nums, b):
    stack = []

    def backtrack():
        if len(stack) == b:
            print(" ".join(map(str, stack)))
            return

        temp = 0
        for i in range(len(nums)):
            if temp != nums[i]:
                stack.append(nums[i])
                temp = nums[i]
                backtrack()
                stack.pop()

    backtrack()

solution(nums, b)
