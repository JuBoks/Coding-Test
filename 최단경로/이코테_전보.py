'''
3 2 1
1 2 4
1 3 2
'''

import sys
import heapq

def solution():
    N, M, C = map(int, sys.stdin.readline().rstrip().split())
    
    graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    for idx in range(N+1):
        graph[idx][idx] = 0
    
    for _ in range(M):
        s, d, v = map(int, sys.stdin.readline().rstrip().split())
        graph[s][d] = v
    
    dikstra_list = dikstra(C, graph, N)

    INF = int(1e9)
    time = 0
    count = 0
    for el in dikstra_list:
        if el < INF and el > 0:
            count += 1
            if el > time:
                time = el
    
    print(count, time)




def dikstra(node_s, graph, N):
    visited = [False for _ in range(N+1)]
    
    dikstra_list = [int(1e9) for _ in range(N+1)]
    dikstra_list[node_s] = 0

    node_list = []
    heapq.heappush(node_list, (0, node_s))

    while node_list:
        v, node_middle = heapq.heappop(node_list)
        
        if visited[node_middle] == True:
            continue
        visited[node_middle] = True

        for node_end in range(1, N+1):
            if graph[node_middle][node_end] > 0:
                value = dikstra_list[node_middle] + graph[node_middle][node_end]
                if value < dikstra_list[node_end]:
                    dikstra_list[node_end] = value
                    heapq.heappush(node_list, (value, node_end))

        return dikstra_list

solution()