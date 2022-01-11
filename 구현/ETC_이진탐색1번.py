from bisect import bisect_right, bisect_left

def solution():
    N, x = map(int, input().split())
    arr = list(map(int, input().split()))

    left = bisect_left(arr, x)
    right = bisect_right(arr, x)
    print(left, right)
    if left == right:
        result = -1
    else:
        result = right - left
    print(result)

solution()