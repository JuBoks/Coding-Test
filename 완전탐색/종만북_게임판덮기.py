import sys

def solution():
    global x, y, coverType

    coverType = [
        [(0, 0), (0, 1), (1, 0)], # ┌
        [(0, 0), (0, 1), (1, 1)], # ┐
        [(0, 0), (1, 0), (1, 1)], # └
        [(0, 0), (1, -1), (1, 0)] # ┘
    ]

    N = int(input())
    while N > 0:
        N -= 1
        x, y = map(int, input().split())
        blankCount = 0
        graph = [[1 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            box = list(sys.stdin.readline().rstrip())
            for k in range(y):
                if box[k] == '.':
                    # 덮인 곳은 1, 안 덮인 곳은 0
                    graph[i][k] = 0
                    blankCount += 1
        
        # 빈칸의 개수가 3의 배수가 아니면 무조건 다 덮을 수 없음
        if blankCount % 3 != 0:
            print(0)
            continue

        # printGraph(graph)
        result = getAllCases(graph)
        print(result)


def printGraph(graph):
    print("################")
    for el in graph:
        print(el)

def isInBoard(row, col):
    if row < x and row >= 0 and col < y and col >= 0:
        return True
    else:
        return False

def setBoard(row, col, type, graph, value):
    isOk = True
    for x_delta, y_delta in coverType[type]:
        row_next = row + x_delta
        col_next = col + y_delta
        if isInBoard(row_next, col_next) == False:
            isOk = False
            continue
        graph[row_next][col_next] += value
        if graph[row_next][col_next] > 1:
            isOk = False
    return isOk


def getAllCases(graph):
    # 맨 위, 왼쪽부터 빈칸을 찾는다.
    row, col = isFull(graph)

    # 다 채워졌다면 개수를 센다
    if row == -1:
        return 1

    result = 0
    for i in range(4):
        # 각 coverType 에 따라 덮어보기
        if setBoard(row, col, i, graph, 1):
            # 덮어지면 재귀호출로 계속 덮어본다
            result += getAllCases(graph)
        # 덮었던 것을 다시 뗴어낸다
        setBoard(row, col, i, graph, -1)

    # 부모에게 값을 전달함
    return result

def isFull(graph):
    for row in range(x):
        for col in range(y):
            if graph[row][col] == 0:
                return (row, col)
    return (-1, -1)

solution()