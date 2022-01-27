steps = int(input())

sum_arr = [0]
for units in range(1, steps + 1):
    nums = list(map(int, input().split()))
    for i in range(units):
        if i == 0:
            nums[0] += sum_arr[0]
        elif i == units - 1:
            nums[i] += sum_arr[i-1]
        else:
            if sum_arr[i] > sum_arr[i-1]:
                nums[i] += sum_arr[i]
            else:
                nums[i] += sum_arr[i-1]
    sum_arr = nums[:]

print(max(sum_arr))