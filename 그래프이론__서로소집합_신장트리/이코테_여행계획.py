'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''
'''
서로소 집합 알고리즘으로 풀어야 함
'''
import sys

def solution2():
    N, M = map(int, input().split())
    parent = [0] * (N+1)
    for i in range(N+1):
        parent[i] = i
    for node_start in range(1, N+1):
        arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
        for node_end in range(1, N+1):
            if arr[node_end] == 1:
                unionParent(node_start, node_end, parent)
        
    plan = list(map(int, sys.stdin.readline().rstrip().split()))

    result = "YES"
    for i in range(M-1):
        if findParent(plan[i], parent) != findParent(plan[i+1], parent):
            result = "NO"
            break

    print(result)

def unionParent(x, y, parent):
    x = findParent(x, parent)
    y = findParent(y, parent)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def findParent(x, parent):
    if x != parent[x]:
        parent[x] = findParent(parent[x], parent)
    return parent[x]

def solution():
    N, M = map(int, input().split())
    table = [[0 for _ in range(N+1)]]
    for _ in range(N):
        i = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
        table.append(i)
    quest = list(map(int, sys.stdin.readline().rstrip().split()))

    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                continue
            if table[a][b] == 0:
                isReachable = isReach(a, b, N, table)
                if isReachable:
                    table[a][b] = 1
                    table[b][a] = 1

    for i in range(M-1):
        s = quest[i]
        e = quest[i+1]
        if table[s][e] == 0:
            print("NO")
            return False
    
    print("YES")
    return True

def isReach(x, y, N, table):
    for a in range(1, N+1):
        if table[a][y] == 1 and table[x][a] == 1:
            return True
    return False

solution2()