'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
from collections import deque

def solution():
    N, M = map(int, input().split())
    indegree = [0] * (N+1)

    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    # 진입차수 테이블 초기화
    for x in range(1, N+1):
        count = 0
        for y in range(1, N+1):
            if graph[y][x] > 0:
                count += 1
        indegree[x] = count

    result = []

    start = -1
    for i in range(1, N+1):
        if indegree[i] == 0:
            start = i
            break

    if start < 0:
        print("Cycle 존재")
        return False

    # 큐 초기화
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        
        # 간선 제거후 진입차수 업데이트
        for i in range(1, N+1):
            if graph[node][i] > 0:
                graph[node][i] = 0
                indegree[i] -= 1
                # 새롭게 진입차수가 0이 되는 원소를 큐에 추가
                if indegree[i] == 0:
                    q.append(i)

        result.append(node)

    # q는 비었는데 모든 노드를 방문 못한경우 -> 사이클 존재함
    if len(result) < N:
        print("Cycle 존재")
    else:
        print(result)

solution()