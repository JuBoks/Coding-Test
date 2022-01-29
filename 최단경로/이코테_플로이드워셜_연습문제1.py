'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
import sys

def solution():
    N = int(input())
    V = int(input())
    D = [[int(1e9) for _ in range(N+1)] for _ in range(N+1)]
    
    # 그래프 업데이트
    for _ in range(V):
        s, d, v = map(int, sys.stdin.readline().rstrip().split())
        D[s][d] = v
    
    # 자기 자신과의 거리는 0
    for idx in range(N+1):
        D[idx][idx] = 0

    # 해당 노드가 중간지점 노드인 경우의 수를 구함 (모든 노드에 대해서)
    for node_middle in range(1, N+1):
        for node_start in range(1, N+1):
            if node_start == node_middle:
                continue
            for node_end in range(1, N+1):
                if node_end == node_start or node_end == node_middle:
                    continue
                
                value = D[node_start][node_middle] + D[node_middle][node_end]
                if value < D[node_start][node_end]:
                    D[node_start][node_end] = value
    
    for idx1 in range(1, N+1):
        print(D[idx1][1:])


solution()








