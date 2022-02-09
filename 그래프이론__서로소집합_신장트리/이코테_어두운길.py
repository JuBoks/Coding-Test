'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
import sys
import heapq

def solution():
    N, M = map(int, input().split())
    
    parent = [0] * N
    for i in range(N):
        parent[i] = i
    
    total_cost = 0
    q = []
    for _ in range(M):
        s, d, v = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(q, (v, s, d))
        total_cost += v
    
    cost = 0
    while q:
        value, s, d = heapq.heappop(q)
        if findParent(s, parent) != findParent(d, parent):
            unionParent(s, d, parent)
            cost += value

    print(total_cost - cost)
        
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