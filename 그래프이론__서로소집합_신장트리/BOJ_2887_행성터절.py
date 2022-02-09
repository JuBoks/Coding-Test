import sys
import heapq

def solution():
    N = int(input())

    coords = []
    for node in range(N):
        el = [node] + list(map(int, sys.stdin.readline().rstrip().split()))
        coords.append(el)
    
    q = []
    step = 1
    while step <= 3:
        coords.sort(key=lambda x: x[step])
        for x in range(N-1):
            v = abs(coords[x][step]-coords[x+1][step])
            heapq.heappush(q, (v, coords[x][0], coords[x+1][0]))

        step += 1
        # for x in range(N):
        #     for y in range(x+1, N):
        #         v = min(abs(coords[x][0]-coords[y][0]), abs(coords[x][1]-coords[y][1]), abs(coords[x][2]-coords[y][2]))
        #         heapq.heappush(q, (v, x, y))

    parent = [0] * N
    for i in range(N):
        parent[i] = i
    
    result = 0
    while q:
        value, x, y = heapq.heappop(q)
        if findParent(x, parent) != findParent(y, parent):
            unionParent(x, y, parent)
            result += value
            findParent(x, parent)
            findParent(y, parent)
    
    print(result)

def findParent(x, parent):
    if x != parent[x]:
        parent[x] = findParent(parent[x], parent)
    return parent[x]

def unionParent(x, y, parent):
    x = findParent(x, parent)
    y = findParent(y, parent)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

solution()