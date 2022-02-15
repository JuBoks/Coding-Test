'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
import sys
import heapq

def solution():
    N, M = map(int, input().split())

    # parent 생성과 초기화
    parent = [0] * (N+1)
    for i in range(N+1):
        parent[i] = i
    
    # 간선 최소정렬을 위해 minheap 사용
    graph = []
    for _ in range(M):
        A, B, cost = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(graph, (cost, A, B))

    result = 0
    while graph:
        cost, A, B = heapq.heappop(graph)
        pA = findParent(parent, A)
        pB = findParent(parent, B)
        if pA == pB:
            continue
        unionParent(parent, A, B, N)
        result += cost

    print(result)

def findParent(parent, X):
    if parent[X] != X:
        parent[X] = findParent(parent, parent[X])
    return parent[X]


def unionParent(parent, X, Y, N):
    # 현재 비교대상 X, Y의 값의 부모를 가져와서 
    # 부모끼리 비교한뒤 해당 "부모"의 부모를 갱신하는 것임
    pX = findParent(parent, X)
    pY = findParent(parent, Y)
    if pX < pY:
        # 비교대상 Y의 부모가 아니라
        # Y의 부모인 pY 의 부모를 갱신하는 것임.(제일 최상위 부모를 갱신함)
        parent[pY] = pX
    else:
        parent[pX] = pY 

    # 틀림
    # if pX < pY:
    #     parent[Y] = pX
    # else:
    #     parent[X] = pY


solution()