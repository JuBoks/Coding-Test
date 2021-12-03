import sys
from collections import deque

def solution():
    INF = float("inf")
    N, K = map(int, sys.stdin.readline().rstrip().split(' '))
    graph_input = []
    for _ in range(N):
        graph_input.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    S, X, Y = map(int, sys.stdin.readline().rstrip().split(' '))
    X -= 1
    Y -= 1

    queue_empty = deque()
    graph = []
    for y in range(N):
        row = []
        for x in range(N):
            row.append(list([graph_input[y][x]] * 2))
            if graph_input[y][x] == 0:
                queue_empty.append([y, x])
        graph.append(row)

    step = 0
    queue_filled = []
    while True:
        # 시간이 S초일 때 0초일 수도 있으므로
        if step == S:
            break
        queue_len = len(queue_empty)
        for _ in range(queue_len):
            node_now_y, node_now_x = queue_empty.popleft()

            value = INF
            if node_now_y+1 < N and graph[node_now_y+1][node_now_x][0] > 0 and graph[node_now_y+1][node_now_x][0] < value:
                value = graph[node_now_y+1][node_now_x][0]
            if node_now_y > 0 and graph[node_now_y-1][node_now_x][0] > 0 and graph[node_now_y-1][node_now_x][0] < value:
                value = graph[node_now_y-1][node_now_x][0]
            if node_now_x > 0 and graph[node_now_y][node_now_x-1][0] > 0 and graph[node_now_y][node_now_x-1][0] < value:
                value = graph[node_now_y][node_now_x-1][0]
            if node_now_x+1 < N and graph[node_now_y][node_now_x+1][0] > 0 and graph[node_now_y][node_now_x+1][0] < value:
                value = graph[node_now_y][node_now_x+1][0]

            if value == INF or value == 0:
                queue_empty.append([node_now_y, node_now_x])
            else:
                graph[node_now_y][node_now_x][1] = value
                queue_filled.append([node_now_y, node_now_x])

        step += 1
        # queue 가 empty일 때
        if not queue_empty:
            break
        # S초의 X,Y가 0이 아닐 때
        if graph[X][Y][1] != 0:
            break

        for elm in queue_filled:
            graph[elm[0]][elm[1]][0] = graph[elm[0]][elm[1]][1]
        queue_filled = []

    print(graph[X][Y][1])

solution()