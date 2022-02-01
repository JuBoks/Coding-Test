'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''

def solution():
    N, M = map(int, input().split())
    
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        s, d = map(int, input().split())
        graph[s][d] = 1
    
    result = 0
    for node in range(1, N+1):
        visited = simulate(node, graph, N)
        isAllVisited = checkAll(visited)
        if isAllVisited:
            result += 1

    print(result)

def simulate(node, graph, N):
    visited = [False] * (N+1)
    # 해당 노드가 시작점일경우
    visit_list = [node]
    while visit_list:
        node_next = visit_list.pop()
        if visited[node_next] == True:
            continue
        visited[node_next] = True
        for node_end in range(1, N+1):
            if graph[node_next][node_end] == 1:
                visit_list.append(node_end)

    # 해당 노드가 도착점일경우
    visited[node] = False #초기화
    visit_list.append(node)
    while visit_list:
        node_before = visit_list.pop()
        if visited[node_before] == True:
            continue
        visited[node_before] = True
        for node_start in range(1, N+1):
            if graph[node_start][node_before] == 1:
                visit_list.append(node_start)

    return visited

def checkAll(visited):
    for el in visited[1:]:
        if el == False:
            return False
    return True

solution()