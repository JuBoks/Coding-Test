'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''

import sys
import heapq

def solution():
    case = int(input())
    for _ in range(case):
        N = int(input())
        graph = [[0 for _ in range(N+2)] for _ in range(N+2)]
        for x in range(1,N+1):
            arr = list(map(int, sys.stdin.readline().rstrip().split()))
            for y in range(1,N+1):
                graph[x][y] = arr[y-1]

        DFS(graph, N)
    
        
def DFS(graph, N):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    node_list = [(graph[N][N], N, N)]
    visited = [[False for _ in range(N+2)] for _ in range(N+2)]
    while node_list:
        value, x, y = heapq.heappop(node_list)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= 0 or nx > N or ny <= 0 or ny > N:
                continue
            
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny] += graph[x][y]
                heapq.heappush(node_list, (graph[nx][ny], nx, ny))

        # if x-1 > 0 and visited[x-1][y] == False:
        #     visited[x-1][y] = True
        #     graph[x-1][y] += graph[x][y]
        #     heapq.heappush(node_list, (graph[x-1][y], (x-1, y)))

        # if x+1 <= N and visited[x+1][y] == False:
        #     visited[x+1][y] = True
        #     graph[x+1][y] += graph[x][y]
        #     heapq.heappush(node_list, (graph[x+1][y], (x+1, y)))

        # if y-1 > 0 and visited[x][y-1] == False:
        #     visited[x][y-1] = True
        #     graph[x][y-1] += graph[x][y]
        #     heapq.heappush(node_list, (graph[x][y-1], (x, y-1)))

        # if y+1 <= N and visited[x][y+1] == False:
        #     visited[x][y+1] = True
        #     graph[x][y+1] += graph[x][y]
        #     heapq.heappush(node_list, (graph[x][y+1], (x, y+1)))
    
    print('answer', graph[1][1])

solution()
