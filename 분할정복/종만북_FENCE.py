import sys

def solution():
    global board, units
    N = int(input())
    while N > 0:
        N -= 1
        units = int(input())
        board = list(map(int,sys.stdin.readline().rstrip().split()))
        result = getMaxRect(0, len(board)-1)
        print(result)

def getMaxRect(left, right):
    if left == right:
        return board[left]
    
    half = (left + right) // 2
    # 얘들은 차피 너비 1임
    heightMax = max(getMaxRect(left, half), getMaxRect(half+1, right))

    # 걸쳐 있을 때
    midLeft = half
    midRight = half+1
    midHeight = min(board[midLeft], board[midRight])
    midSizeMax = max(heightMax, 2 * midHeight)
    while midLeft > left or midRight < right:
        if midRight < right and (midLeft == left or board[midLeft-1] < board[midRight+1]):
            midRight += 1
            midHeight = min(midHeight, board[midRight])
        else:
            midLeft -= 1
            midHeight = min(midHeight, board[midLeft])
        midSizeMax = max(midSizeMax, (midRight-midLeft+1) * midHeight)
        # midLeftHeight = min(board[midLeft-1], midHeight)
        # midRightHeight = min(board[midRight+1], midHeight)
        # if midLeftHeight <= midRightHeight:
        #     midRight += 1
        #     midHeight = midRightHeight
        # else:
        #     midLeft -= 1
        #     midHeight = midLeftHeight
        
        # midSizeMax = max(midSizeMax, (midRight-midLeft+1) * midHeight)

    return midSizeMax

solution()