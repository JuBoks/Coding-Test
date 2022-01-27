def solution():
    days = int(input())
    dp = []
    for _ in range(days):
       dp.append(list(map(int, input().split())))
    dp.reverse()

    for day in range(days):
        if dp[day][0] > day+1:
            dp[day][0] = 0
            dp[day][1] = 0

    profit = [0 for _ in range(days)]
    profit[0] = dp[0][1]
    for day in range(1, days):
        sum1 = dp[day][1] + profit[day-dp[day][0]]
        sum2 = profit[day-1]
        if sum1 > sum2:
            sum_big = sum1
        else:
            sum_big = sum2
        profit[day] = sum_big

    print(profit[-1])

solution()