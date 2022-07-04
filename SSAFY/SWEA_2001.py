import sys

sys.stdin = open("C:\Github\Coding-Test\SSAFY\input.txt", "r")

T = int(input())

def getSum(start_x, start_y, M, graph):
    sum = 0
    for x in range(start_x, start_x + M):
        for y in range(start_y, start_y + M):
            sum += graph[x][y]
    return sum

def getMaxResult(N, M, graph):
    maxSum = float("-inf")
    for x in range(0, N - M + 1):
        for y in range(0, N - M + 1):
            sum = getSum(x, y, M, graph)
            if sum > maxSum:
                maxSum = sum
    return maxSum

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    result = getMaxResult(N, M, graph)

    print('#%d' % test_case, result)
