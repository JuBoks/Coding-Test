'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
from operator import indexOf
import sys
from collections import deque

def solution():
    N = int(input())
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    indegree = [0] * (N+1)
    result = [0] * (N+1)
    table = {i: [] for i in range(1, N+1)}
    for node in range(1, N+1):
        ipt = list(map(int, sys.stdin.readline().rstrip().split()))
        cost = ipt[0]
        
        graph[node][node] = cost
        for el in ipt[1:-1]:
            graph[el][node] = -1
            indegree[node] += 1
            table[node].append(el)
    
    # graph 에서 중복 선행 노드는 제거
    for key in table.keys():
        for node in table[key]:
            for el in table[node]:
                try:
                    i = table[key].index(el)
                    del table[key][i]
                    graph[el][key] = 0
                    indegree[key] -= 1
                except:
                    continue
    
    

    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        # result 구하기
        for i in range(1, N+1):
            result[node] += graph[i][node]

        # 간선부분을 값으로 업데이트하기
        for i in range(1, N+1):
            if graph[node][i] < 0:
                graph[node][i] = result[node]
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    for el in result[1:]:
        print(el)

solution()