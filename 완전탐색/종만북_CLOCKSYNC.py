import sys

def solution():
    global linkedSwitches, SWITCHES, CLOCKS
    SWITCHES = 10
    CLOCKS = 16
    linkedSwitches = [
        [0, 1, 2],
        [3, 7, 9 , 11],
        [4, 10, 14, 15],
        [0, 4, 5, 6, 7],
        [6, 7, 8, 10, 12],
        [0, 2, 14, 15],
        [3, 14, 15],
        [4, 5, 7, 14, 15],
        [1, 2, 3, 4, 5],
        [3, 4, 5, 9, 13]
    ]

    N = int(input())
    while N > 0:
        N -= 1
        board = list(map(int, sys.stdin.readline().rstrip().split()))
        result = simulator(0, board)
        if result >= 1e9:
            result = -1
        print(result)

def areAligned(board):
    for clock in board:
        if clock != 12:
            return False
    return True

def pushClock(switch, board):
    for linked in linkedSwitches[switch]:
        board[linked] += 3
        if board[linked] == 15:
            board[linked] = 3

def simulator(switch, board):
    if areAligned(board):
        return 0
    if switch == SWITCHES:
        return 1e9
    
    result = 1e9
    for count in range(4):
        result = min(result, count + simulator(switch+1, board))
        pushClock(switch, board)
    
    return result

solution()