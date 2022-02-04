'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
import sys

def solution():
    N, M = map(int, input().split())

    parent = [0] * (N+1)
    for i in range(N+1):
        parent[i] = i

    quest = []
    for _ in range(M):
        q, x, y  = map(int, sys.stdin.readline().rstrip().split())
        if q == 0:
            unionParent(parent, x, y)
        else:
            x = findParent(parent, x)
            y = findParent(parent, y)
            if x == y:
                print("YES")
            else:
                print("NO")

    
    # union 을 다 끝마친 뒤, 각 원소에 findParent()를 해줌으로써
    # 전부 루트노드 데이터로 변경
    # for i in range(1, N+1):
    #     findParent(parent, i)

    # for x, y in quest:
    #     x = findParent(parent, x)
    #     y = findParent(parent, y)
    #     if x == y:
    #         print("YES")
    #     else:
    #         print("NO")


def unionParent(parent, x, y):
    x = findParent(parent, x)
    y = findParent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

solution()