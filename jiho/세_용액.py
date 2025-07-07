N = int(input())
arr = list(map(int, input().split()))
arr.sort()


def solution():
    global arr, N

    min_sum = abs(arr[0] + arr[1] + arr[2])
    min_nums = [arr[0], arr[1], arr[2]]
    for i in range(N - 2):
        start, end = i + 1, N - 1
        while start < end:
            nums = [arr[i], arr[start], arr[end]]
            s = sum(nums)
            if abs(s) < min_sum:
                min_sum = abs(s)
                min_nums = nums

            if s < 0:
                start += 1
            else:
                end -= 1
    return min_nums


ans = solution()
print(" ".join(map(str, ans)))
