'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''
'''
1 에서 K 까지의 최단거리 + K 에서 X 까지의 최단거리 로 접근하여 풀이
다익스트라와 플로이드 워셜 알고리즘을 통해 풀 수 있음
'''
# 다익스트라
import sys
import heapq

def solution():
    N, M = map(int, input().split())
    
    graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    for idx in range(N+1):
        graph[idx][idx] = 0
    
    for _ in range(M):
        s, d = map(int, sys.stdin.readline().rstrip().split())
        graph[s][d] = 1
        graph[d][s] = 1

    X, K = map(int, input().split())

    d1X = dikstra(1, K, graph, N)
    dXK = dikstra(K, X, graph, N)

    result = d1X + dXK
    if result >= int(1e9):
        result = -1
    
    print(result)
    

def dikstra(node_s, node_d, graph, N):
    visited = [False for _ in range(N+1)]
    dikstra_list = [int(1e9) for _ in range(N+1)]
    dikstra_list[node_s] = 0
    node_list = []
    heapq.heappush(node_list, (0, node_s))

    while node_list:
        v, node_start = heapq.heappop(node_list)
        if visited[node_start] == True:
            continue
        visited[node_start] = True
        for idx in range(N+1):
            if graph[node_start][idx] > 0:
                value = dikstra_list[node_start] + graph[node_start][idx]
                if value < dikstra_list[idx]:
                    dikstra_list[idx] = value
                    heapq.heappush(node_list, (value, idx))
    
    return dikstra_list[node_d]
    

solution()