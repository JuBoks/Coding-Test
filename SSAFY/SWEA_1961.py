import sys

sys.stdin = open("d:/projects/Coding-Test/SSAFY/input.txt", "r")

def rotateGraph90Degree(N, graph):
    graph_new = []
    for y in range(N):
        el = []
        for x in range(N-1, -1, -1):
            el.append(graph[x][y])
        graph_new.append(el)
    return graph_new

def rotateGraph180Degree(N, graph):
    graph_new = []
    for y in range(N-1, -1, -1):
        el = []
        for x in range(N-1, -1, -1):
            el.append(graph[y][x])
        graph_new.append(el)
    return graph_new
            
def rotateGraph270Degree(N, graph):
    graph_new = []
    for y in range(N-1, -1, -1):
        el = []
        for x in range(N):
            el.append(graph[x][y])
        graph_new.append(el)
    return graph_new

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    # 90도 회전
    graph_90 = rotateGraph90Degree(N, graph)
    
    # 180도 회전
    graph_180 = rotateGraph180Degree(N, graph)
    
    # 270도 회전
    graph_270 = rotateGraph270Degree(N, graph)

    print('#%d' % test_case)
    for x in range(N):
        for y in range(N):
            print(graph_90[x][y], end='')
        print(' ', end='')
        for y in range(N):
            print(graph_180[x][y], end='')
        print(' ', end='')
        for y in range(N):
            print(graph_270[x][y], end='')
        print()
