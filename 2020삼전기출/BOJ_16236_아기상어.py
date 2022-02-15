import sys
import heapq

global dx, dy
# 12부터 반시계방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def solution():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # 현재 아기상어 위치 초기화
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 9:
                loc_x = x
                loc_y = y
            
    # 현재 아기상어 크기, 레벨업 초기화
    size = 2
    q = [(loc_x, loc_y, 0)]
    graph[loc_x][loc_y] = 0
    # 걸리는 시간
    fishes = checkFishes(size, graph)
    if fishes == 0:
        result = 0
    else:
        result = findFishes(q, N, size, graph)

    print(result)

def checkFishes(size, graph):
    count = 0
    for arr in graph:
        for el in arr:
            if el > 0 and el < size:
                count += 1
    return count

def findFishes(q_step, N, size, graph):
    result = 0
    level = size
    q_fish = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    while True:
        q_step_next = []
        while q_step:
            x, y, step = q_step.pop()
            # 1. 현재 상어 위치에서 갈 수 있는 곳들 찾아내기
            for i in range(4):
                now_x = x + dx[i]
                now_y = y + dy[i]
                # 범위에서 벗어나는 것은 제외
                if now_x < 0 or now_x == N or now_y < 0 or now_y == N:
                    continue
                fish_size = graph[now_x][now_y]
                # 현재 상어의 사이즈보다 작은 경우 먹을 수 있다
                if fish_size < size and fish_size > 0:
                    heapq.heappush(q_fish, (now_x, now_y, step+1))
                # 현재 상어의 사이즈보다 같거나 0인 경우 통과할 수 있다
                elif visited[now_x][now_y] == False and (fish_size == size or fish_size == 0):
                    q_step_next.append((now_x, now_y, step+1))
                    visited[now_x][now_y] = True

        # 먹을 수 있는 물고기가 있는지 확인
        # - 있다
        # 먹이가 한마리라도 있으면 그만하고 여러마리일 경우 우선순위부여 하고 1순위를 리턴 후 초기화
        if len(q_fish) > 0:
            fish_x, fish_y, step = heapq.heappop(q_fish)
            result = step
            graph[fish_x][fish_y] = 0
            level -= 1
            # size 만큼 먹으면 size up 
            if level == 0:
                size += 1
                level = size
            if checkFishes(size, graph) == 0:
                break
            # 초기화 (처음부터)
            q_fish = []
            q_step = [(fish_x, fish_y, step)]
            visited = [[False for _ in range(N)] for _ in range(N)]
        # - 없다
        # 먹이가 한마리도 없으면 step 진행
        else:
            q_step = q_step_next[:]
        
        # 막혔을 경우
        if len(q_step) == 0:
            break

    return result

solution()