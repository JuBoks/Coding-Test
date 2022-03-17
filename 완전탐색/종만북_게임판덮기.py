import sys
from unittest import result

def solution():
    global result, x, y
    result = 0

    N = int(input())
    x, y = map(int, input().split())
    graph = [[0 for _ in range(y)] for _ in range(x)]
    for i in range(x):
        box = list(sys.stdin.readline().rstrip())
        for k in range(y):
            if box[k] == '.':
                graph[i][k] = 1
    
    getAllCases(0, 0, graph)

    print(result)

def getNextPosition(row, col):
    next_row = 0
    next_col = 0

    if col + 1 == y:
        next_row = row + 1
        if next_row == x:
            next_row = -1
            next_col = -1
    else:
        next_row = row
        next_col = col + 1
    
    return next_row, next_col

def getAllCases(row, col, graph):
    # loop 다 돌고
    if row == -1:
        # 모든 칸이 채워졌는지
        print(graph)
        if isFull(graph) == True:
            result += 1
            return True
        else:
            return False
    
    # 빈칸이면
    if graph[row][col] == 1:
        if isCanBePlaced1(row, col, graph) == True:
            graph[row][col] = 0
            graph[row][col+1] = 0
            graph[row+1][col] = 0
            next_row, next_col = getNextPosition(row, col)
            getAllCases(next_row, next_col, graph)
            graph[row][col] = 1
            graph[row][col+1] = 1
            graph[row+1][col] = 1

        if isCanBePlaced2(row, col, graph) == True:
            graph[row][col] = 0
            graph[row][col+1] = 0
            graph[row+1][col+1] = 0
            next_row, next_col = getNextPosition(row, col)
            getAllCases(next_row, next_col, graph)
            graph[row][col] = 1
            graph[row][col+1] = 1
            graph[row+1][col+1] = 1
            
        if isCanBePlaced3(row, col, graph) == True:
            graph[row][col] = 0
            graph[row+1][col] = 0
            graph[row+1][col+1] = 0
            next_row, next_col = getNextPosition(row, col)
            getAllCases(next_row, next_col, graph)
            graph[row][col] = 1
            graph[row+1][col] = 1
            graph[row+1][col+1] = 1

        if isCanBePlaced4(row, col, graph) == True:
            graph[row][col] = 0
            graph[row+1][col] = 0
            graph[row+1][col-1] = 0
            next_row, next_col = getNextPosition(row, col)
            getAllCases(next_row, next_col, graph)
            graph[row][col] = 1
            graph[row+1][col] = 1
            graph[row+1][col-1] = 1
    else:
        next_row, next_col = getNextPosition(row, col)
        getAllCases(next_row, next_col, graph)
                
# ┌
def isCanBePlaced1(row, col, graph):
    if col + 1 == y or row + 1 == x:
        return False

    if graph[row][col] == 1 and graph[row][col+1] == 1 and graph[row+1][col] == 1:
        return True
    else:
        return False

# ┐
def isCanBePlaced2(row, col, graph):
    if col + 1 == y or row + 1 == x:
        return False

    if graph[row][col] == 1 and graph[row][col+1] == 1 and graph[row+1][col+1] == 1:
        return True
    else:
        return False

# └
def isCanBePlaced3(row, col, graph):
    if col + 1 == y or row + 1 == x:
        return False

    if graph[row][col] == 1 and graph[row+1][col] == 1 and graph[row+1][col+1] == 1:
        return True
    else:
        return False

# ┘
def isCanBePlaced4(row, col, graph):
    if col - 1 < 0 or row + 1 == x:
        return False

    if graph[row][col] == 1 and graph[row+1][col] == 1 and graph[row+1][col-1] == 1:
        return True
    else:
        return False

def isFull(graph):
    for row in range(x):
        for col in range(y):
            if graph[row][col] == 1:
                return False
    return True

solution()