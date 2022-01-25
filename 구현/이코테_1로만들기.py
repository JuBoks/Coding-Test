def solution(X):
    dp = [0 for _ in range(X+1)]

    # Creating Table
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, X+1):
        value = float("inf")
        if i % 2 == 0 and dp[i//2] < value:
            value = dp[i//2]
        if i % 3 == 0 and dp[i//3] < value:
            value = dp[i//3]
        if i % 5 == 0 and dp[i//5] < value:
            value = dp[i//5]
        if dp[i-1] < value:
            value = dp[i-1]

        dp[i] = value + 1

    print(dp[X])

solution(26)