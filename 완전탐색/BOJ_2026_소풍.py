import sys

def solution():
    K, N, F = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for x in range(1, N+1):
        graph[x][x] = 1

    while F > 0:
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x][y] = 1
        graph[y][x] = 1
        F -= 1

    set_list = []
    for x in range(1, N+1):
        set_list.append(set([x]))

    for x in range(1, N+1):
        for el_set in set_list:
            if isAbleToBeSet(x, el_set, graph) == True:
                el_set.add(x)
            
    result_list = []
    for el_set in set_list:
        if len(el_set) >= K:
            result_list.append(list(el_set))
    
    if len(result_list) == 0:
        print(-1)
    else:
        # result_list 가 빈 리스트일 경우에는 sort가 안되니까 있는 경우에만 해야했음....
        result_list.sort(key=lambda x: x)
        # sort 를 해야 했었음;;;;
        result_list[0].sort()
        for i in range(K):
            print(result_list[0][i])

def isAbleToBeSet(x, el_set, graph):
    for el in el_set:
        if graph[x][el] == 0:
            return False
    return True
            
solution()