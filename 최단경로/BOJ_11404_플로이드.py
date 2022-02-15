import sys

def solution():
    N = int(input())
    M = int(input())
    INF = int(1e9)
    graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        s, d, v = map(int, sys.stdin.readline().rstrip().split())
        if graph[s][d] >= INF or graph[s][d] > v:
            graph[s][d] = v
    
    for node_middle in range(1, N+1):
        for node_start in range(1, N+1):
            if node_start == node_middle:
                continue
            for node_end in range(1, N+1):
                if node_end == node_middle or node_end == node_start:
                    continue
                value = graph[node_start][node_middle] + graph[node_middle][node_end]
                if value < graph[node_start][node_end]:
                    graph[node_start][node_end] = value
    
    for arr in graph[1:]:
        for el in arr[1:]:
            if el >= INF:
                el = 0
            print(el, end=' ')
        print() 

solution()