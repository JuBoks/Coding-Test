import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

print(arr[(N-1) // 2])
# table = {}
# for elm in arr:
#     if not elm in table:
#         table[elm] = 1
#     else:
#         table[elm] += 1

# table = sorted(table.items())
# result = [1e9, 1e9]
# units = len(table)
# for idx in range(units):
#     value = table[idx][0]
#     sum_value = 0
#     for left_idx in range(idx):
#         sum_value += (value - table[left_idx][0]) * table[left_idx][1]
#     for right_idx in range(idx, units):
#         sum_value += (table[right_idx][0] - value) * table[right_idx][1]
#     if result[1] > sum_value:
#         result[1] = sum_value
#         result[0] = value
#     elif result[1] == sum_value and result[0] > value:
#         result[0] = value

# print(result[0])