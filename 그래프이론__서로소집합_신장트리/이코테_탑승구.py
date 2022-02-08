'''
4
6
2
2
3
3
4
4
'''
'''
바로 왼쪽의 집합과 합침으로써 서로소 알고리즘으로도 풀 수 있음
'''
def solution():
    N = int(input())
    M = int(input())
    empty = [0] * (N+1)
    for i in range(N+1):
        empty[i] = i
    result = 0
    for _ in range(M):
        p = int(input())
        if empty[p] == 0:
            break
        empty[p] -= 1
        # p 보다 큰 것
        for i in range(p+1, N+1):
            empty[i] -= 1
        # p 보다 작은 것
        for i in range(empty[p], p):
            empty[i] = empty[p]
        print(empty)
        result += 1

    print(result)

# def solution():
#     N = int(input())
#     M = int(input())
#     visited = [False] * N
#     result = 0
#     for _ in range(M):
#         p = int(input()) - 1
#         flag = True
#         for i in range(p, -1, -1):
#             if visited[i] == False:
#                 visited[i] = True
#                 result += 1
#                 flag = False
#                 break
#         if flag:
#             break

#     print(result)

solution()