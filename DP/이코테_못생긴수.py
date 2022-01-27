
def solution():
    N = int(input())

    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5

    ugly = [0 for _ in range(N)]
    # 첫 번째 수는 1
    ugly[0] = 1 

    for idx in range(1, N):
        ugly[idx] = min(next2, next3, next5)

        if ugly[idx] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[idx] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[idx] == next5:
            i5 += 1
            next5 = ugly[i5] * 5
    
    print(ugly[N-1])

# 시간 초과
# def solution():
#     N = int(input())
#     arr = [1]
#     num = 2
#     check_table = [0 for _ in range(10000000)]
#     check_table[1] = 1
#     while len(arr) < 1000:
#         divide = -1
#         if num % 2 == 0:
#             divide = num // 2
#         elif num % 3 == 0:
#             divide = num // 3
#         elif num % 5 == 0:
#             divide = num // 5
        
#         if divide > 0 and check_table[divide] == 1:
#             arr.append(num)
#             check_table[num] = 1
        
#         num += 1
    
#     print(arr[N-1])

solution()