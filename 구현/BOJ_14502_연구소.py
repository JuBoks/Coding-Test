# combinations
# bfs 로 시뮬레이션
from itertools import combinations
from collections import deque
import sys

def solution():
    result = -1
    N, M = map(int, sys.stdin.readline().rstrip().split(' '))
    graph = []
    for _ in range(N):
         graph.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

    # 바이러스가 있는 방 deque
    queue = deque()
    queue_empty = list()
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 2:
                queue.append([y, x])
            elif graph[y][x] == 0:
                queue_empty.append([y, x])
    
    # 빈 벽들에 대해 combination
    list_comb = list(combinations(queue_empty, 3))
    for comb in list_comb:
        graph_copied = [item[:] for item in graph]
        queue_copied = deque(item[:] for item in queue)
        for y, x in comb:
            graph_copied[y][x] = 1

        count = bfs_simulation(graph_copied, queue_copied, N-1, M-1)
        if result < count:
            result = count
            if result == 14:
                for elm in graph_copied:
                    print(elm)

    print(result)

def bfs_simulation(graph, queue, N, M):
    while queue:
        y, x = queue.popleft()
        if y < N and graph[y+1][x] == 0:
            graph[y+1][x] = 2
            queue.append([y+1, x])
        if y > 0 and graph[y-1][x] == 0:
            graph[y-1][x] = 2
            queue.append([y-1, x])
        if x < M and graph[y][x+1] == 0:
            graph[y][x+1] = 2
            queue.append([y, x+1])
        if x > 0 and graph[y][x-1] == 0:
            graph[y][x-1] = 2
            queue.append([y, x-1])
    
    count = 0
    for row in graph:
        for elm in row:
            if elm == 0:
                count += 1

    return count

solution()