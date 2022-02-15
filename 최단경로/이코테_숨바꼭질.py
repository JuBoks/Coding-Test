'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''

import heapq

def solution():
    N, M = map(int, input().split())

    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    visited = [False] * (N+1)
    dist = [int(1e9)] * (N+1)
    dist[1] = 0
    node_list = [(0, 1)]
    while node_list:
        val, node_start = heapq.heappop(node_list)
        if visited[node_start] == True:
            continue
        visited[node_start] = True
        
        for node_end in range(1, N+1):
            if graph[node_start][node_end] > 0:
                dist_total = dist[node_start] + graph[node_start][node_end]
                if dist_total < dist[node_end]:
                    dist[node_end] = dist_total
                    heapq.heappush(node_list, (dist[node_end], node_end))
    dist[0] = -1
    value_max = max(dist)
    node_num = dist.index(value_max)
    count = 0
    for el in dist:
        if el == value_max:
            count += 1

    print('{0} {1} {2}'.format(node_num, value_max, count))

solution()