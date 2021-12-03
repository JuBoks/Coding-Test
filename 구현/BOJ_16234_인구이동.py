import sys
from collections import deque

def solution():
    global graph_visited, graph, N, L, R
    N, L, R = map(int, input().split(' '))
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

    graph_visited = [[False] * N for _ in range(N)]
    land_list = []
    day = 0
    while True:
        for y in range(N):
            for x in range(N):
                if not graph_visited[y][x]:
                    land = bfs_getUnion(y, x)
                    if len(land) > 1:
                        land_list.append(land)
        
        if len(land_list) == 0:
            break

        for land in land_list:
            value = 0
            unit = len(land)
            for y, x in land:
                value += graph[y][x]
            value = int(value / unit)
            for y, x in land:
                graph[y][x] = value

        # initialize
        graph_visited = [[False] * N for _ in range(N)]
        land_list = []

        day += 1

    for elm in graph:
        print(elm)
    print(day)

def bfs_getUnion(y, x):
    union = [(y, x)]
    queue = deque()
    queue.append((y, x))
    graph_visited[y][x] = True
    while queue:
        node_now = queue.popleft()
        y = node_now[0]
        x = node_now[1]

        if y > 0 and not graph_visited[y-1][x] and isUnion(y, x, y-1, x):
            queue.append((y-1, x))
            union.append((y-1, x))
            graph_visited[y-1][x] = True
        if y < N-1 and not graph_visited[y+1][x] and isUnion(y, x, y+1, x):
            queue.append((y+1, x))
            union.append((y+1, x))
            graph_visited[y+1][x] = True
        if x > 0 and not graph_visited[y][x-1] and isUnion(y, x, y, x-1):
            queue.append((y, x-1))
            union.append((y, x-1))
            graph_visited[y][x-1] = True
        if x < N-1 and not graph_visited[y][x+1] and isUnion(y, x, y, x+1):
            queue.append((y, x+1))
            union.append((y, x+1))
            graph_visited[y][x+1] = True
    
    return union

def isUnion(y1, x1, y2, x2):
    value = abs(graph[y1][x1] - graph[y2][x2])
    if value >= L and value <= R:
        return True
    else:
        return False

solution()