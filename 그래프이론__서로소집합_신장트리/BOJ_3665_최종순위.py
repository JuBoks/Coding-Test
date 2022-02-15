import sys
from collections import deque

def solution():
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        rank = list(map(int, sys.stdin.readline().rstrip().split()))

        graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
        for i in range(N):
            x = rank[i]
            for j in range(i+1, N):
                y = rank[j]
                graph[x][y] = 1

        K = int(input())
        for __ in range(K):
            x, y = map(int, sys.stdin.readline().rstrip().split())
            if graph[x][y] == 1:
                graph[x][y] = 0
                graph[y][x] = 1
            else:
                graph[x][y] = 1
                graph[y][x] = 0

        indegree = [0] * (N+1)
        for y in range(1, N+1):
            degree = 0
            for x in range(1, N+1):
                if graph[x][y] == 1:
                    degree += 1
            indegree[y] = degree
        
        q = deque()
        for i in range(1, N+1):
            if indegree[i] == 0:
                q.append(i)
        if len(q) > 1:
            print("?")
            continue
        elif len(q) == 0:
            print("IMPOSSIBLE")
            continue
        result = []
        flag = False
        while q:
            node = deque.popleft(q)
            indegree[node] = -1 # visited
            result.append(node)
            for x in range(1, N+1):
                if graph[node][x] == 1:
                    graph[node][x] = 0
                    indegree[x] -= 1
                    if indegree[x] == 0:
                        q.append(x)

            if len(q) > 1:
                flag = True
                break
        
        if len(result) == N:
            print(*result)
        else:
            if flag == True:
                print("?")
            else:
                print("IMPOSSIBLE")
                
def checkAndUpdateQueue(q, N, indegree):
    count = 0
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            count += 1
    if count > 1:
        return False
    else:
        return True
        
solution()