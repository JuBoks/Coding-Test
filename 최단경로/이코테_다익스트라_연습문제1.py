'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

from re import I
import sys
import heapq

def solution():
    N, V = map(int, input().split())
    node_start = int(input())
    
    # visited 배열 :: 노드 방문 여부 배열
    visited = [False for _ in range(N+1)]
    # graph 배열 :: 노드간의 거리 정보 테이블
    graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    # dikstra 배열 :: 시작노드에서 각 노드들까지의 최소 거리 정보 테이블
    dikstra = [int(1e9) for _ in range(N+1)]

    # 노드들의 간선 정보 업데이트
    for _ in range(V):
        s, d, v = map(int, sys.stdin.readline().rstrip().split())
        graph[s][d] = v

    # 시작할 노드들의 리스트
    # 초기에는 자기 자신과의 거리이므로 0임
    node_list = []
    heapq.heappush(node_list, (0, node_start))
    dikstra[node_start] = 0

    while node_list:
        # distance : node_start 에서 시작점 노드와의 거리
        # node_num : 시작점 노드 번호
        distance, node_num = heapq.heappop(node_list)
        
        # 이미 방문한 적이 있는 거면 스킵
        if visited[node_num] == True:
            continue
    
        visited[node_num] = True

        for idx in range(1, N+1):
            # 두 노드간에 거리 정보가 있다면,
            if graph[node_num][idx] > 0:
                # 시작 노드로부터 해당 노드까지의 총 거리를 구함
                total_distance = graph[node_num][idx] + dikstra[node_num]
                # 총 거리 값이 기존 최소값 보다 작으면 갱신
                if dikstra[idx] > total_distance:
                    dikstra[idx] = total_distance

            node_list.append((dikstra[idx], idx))

    for idx in range(1, N+1):
        print(dikstra[idx])

solution()