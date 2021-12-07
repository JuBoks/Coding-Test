def solution(board):
    global dx, dy, graph, graph_check, N, INF, answer
    N = len(board[0])
    graph = [item[:] for item in board]
    INF = float("inf")
    graph_check = [[INF for _ in range(N)] for _ in range(N)]
    graph_check[0][0] = 0
    graph_check[0][1] = 0
    ##### D, R, U, L
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    answer = INF
    dfs([0,0], [0,1], "H", 1, False)

    return answer

def dfs(x1, x2, axis, val, r_flag):
    # print(x1, x2, axis, val)
    # for elm in graph_check:
    #     print(elm)
    global answer
    if x1 == [N-1, N-1] or x2 == [N-1, N-1]:
        if answer > val - 1:
            answer = val - 1
        # for elm in graph_check:
        #     print(elm)
        # print()
        return answer
    if answer < val - 1:
        return answer
    # can move ?
    if canMove(x1, x2, "up", val):
        now1, now2 = move(x1, x2, "up")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, axis, val, False)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    if canMove(x1, x2, "down", val):
        now1, now2 = move(x1, x2, "down")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, axis, val, False)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    if canMove(x1, x2, "right", val):
        now1, now2 = move(x1, x2, "right")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, axis, val, False)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    if canMove(x1, x2, "left", val):
        now1, now2 = move(x1, x2, "left")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, axis, val, False)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    # can rotate?
    if canRotate(x1, x2, axis, "upClock", r_flag):
        now1, now2, now_axis = rotate(x1, x2, axis, "upClock")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, now_axis, val, True)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    if canRotate(x1, x2, axis, "downClock", r_flag):
        now1, now2, now_axis = rotate(x1, x2, axis, "downClock")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, now_axis, val, True)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    if canRotate(x1, x2, axis, "upCounterClock", r_flag):
        now1, now2, now_axis = rotate(x1, x2, axis, "upCounterClock")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, now_axis, val, True)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    if canRotate(x1, x2, axis, "downCounterClock", r_flag):
        now1, now2, now_axis = rotate(x1, x2, axis, "downCounterClock")
        before_1 = graph_check[now1[0]][now1[1]]
        before_2 = graph_check[now2[0]][now2[1]]
        graph_check[now1[0]][now1[1]] = val
        graph_check[now2[0]][now2[1]] = val
        val += 1
        dfs(now1, now2, now_axis, val, True)
        val -= 1
        graph_check[now1[0]][now1[1]] = before_1
        graph_check[now2[0]][now2[1]] = before_2
    

def canRotate(x1, x2, axis, direction, r_flag):
    # 이미 한 번 rotate 한 상황이면 False
    if r_flag:
        return False
    x1_new, x2_new, box = rotate(x1, x2, axis, direction)
    x1x = x1_new[0]
    x1y = x1_new[1]
    x2x = x2_new[0]
    x2y = x2_new[1]
    # 이동 후 범위에 속하는지
    if x1x < 0 or x1x >= N or x2x < 0 or x2x >= N or x1y < 0 or x1y >= N or x2y < 0 or x2y >= N:
        return False
    # rotate 가 가능한지
    if axis == "V":
        if direction == "upClock" and graph[x2[0]][x2[1] - 1] == 1:
            return False
        elif direction == "downClock" and graph[x1[0]][x1[1] + 1] == 1:
            return False
        elif direction == "upCounterClock" and graph[x2[0]][x2[1] + 1] == 1:
            return False
        elif direction == "downCounterClock" and graph[x1[0]][x1[1] - 1] == 1:
            return False
    elif axis == "H":
        if direction == "upClock" and graph[x1[0] - 1][x1[1]] == 1:
            return False
        elif direction == "downClock" and graph[x2[0] + 1][x2[1]] == 1:
            return False
        elif direction == "upCounterClock" and graph[x2[0] - 1][x2[1]] == 1:
            return False
        elif direction == "downCounterClock" and graph[x1[0] + 1][x1[1]] == 1:
            return False
    return True

def rotate(x1, x2, axis, direction):
    # x2 가 무조건 x1보다 x든 y든 값이 큼
    if axis == "V":
        if direction == "upClock":
            return x1, [x1[0], x1[1] - 1], "H"
        elif direction == "downClock":
            return x2, [x2[0], x2[1] + 1], "H"
        elif direction == "upCounterClock":
            return x1, [x1[0], x1[1] + 1], "H"
        elif direction == "downCounterClock":
            return x2, [x2[0], x2[1] - 1], "H"
    elif axis == "H":
        if direction == "upClock":
            return [x2[0] - 1, x2[1]], x2, "V"
        elif direction == "downClock":
            return x1, [x1[0] + 1, x1[1]], "V"
        elif direction == "upCounterClock":
            return [x1[0] - 1, x1[1]], x1, "V"
        elif direction == "downCounterClock":
            return x2, [x2[0] + 1, x2[1]], "V"

def canMove(x1, x2, direction, val):
    x1, x2 = move(x1, x2, direction)
    x1x = x1[0]
    x1y = x1[1]
    x2x = x2[0]
    x2y = x2[1]
    # 이동 후 범위에 속하는지
    if x1x < 0 or x1x >= N or x2x < 0 or x2x >= N or x1y < 0 or x1y >= N or x2y < 0 or x2y >= N:
        return False
    # 이동 후 이동할 수 있는 범위인지
    if graph[x1x][x1y] == 1 or graph[x2x][x2y] == 1:
        return False
    # 이동한 곳이 다 방문했던 곳인지
    if graph_check[x1x][x1y] < val and graph_check[x2x][x2y] < val:
        return False
    return True

def move(x1, x2, direction):
    # move along to direction
    x1x = x1[0]
    x1y = x1[1]
    x2x = x2[0]
    x2y = x2[1]
    idx = 0
    if direction == "down":
        idx = 0
    elif direction == "right":
        idx = 1
    elif direction == "up":
        idx = 2
    else:
        idx = 3
    x1x += dx[idx]
    x2x += dx[idx]
    x1y += dy[idx]
    x2y += dy[idx]
    
    return [x1x, x1y], [x2x, x2y]


ipt = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(ipt))