'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
from gettext import find
import sys
import heapq

def solution():
    N, M = map(int, input().split())

    parent = [0] * (N+1)
    for i in range(N+1):
        parent[i] = i

    q = []
    for _ in range(M):
        x, y, v = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(q, (v, x, y))

    result_list = []
    while q:
        cost, a, b = heapq.heappop(q)
        a = findParent(parent, a)
        b = findParent(parent, b)
        
        if a == b:
            continue # 사이클이므로

        unionParent(parent, a, b)

        result_list.append(cost)

    value = 0
    for cost in result_list[:-1]:
        value += cost
    print(value)


def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, x, y):
    x = findParent(parent, x)
    y = findParent(parent, y)
    if x < y:
        parent[y] = x
    else: 
        parent[x] = y

solution()