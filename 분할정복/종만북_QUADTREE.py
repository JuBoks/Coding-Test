import sys

def solution():
    N = int(input())
    global quadtree
    while N > 0:
        N -= 1
        quadtree = list(list(sys.stdin.readline().rstrip()))

        if len(quadtree) == 1:
            print(quadtree[0])
            continue

        result = reverse(0)
        print(result[1])
        

def reverse(idx):
    value = quadtree[idx]
    if value == 'b' or value == 'w':
        return idx, value

    # x인 경우
    idx, upLeft = reverse(idx+1)
    idx, upRight = reverse(idx+1)
    idx, downLeft = reverse(idx+1)
    idx, downRight = reverse(idx+1)

    return idx, 'x' + downLeft + downRight + upLeft + upRight


solution()