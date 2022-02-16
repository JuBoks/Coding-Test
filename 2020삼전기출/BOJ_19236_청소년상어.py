import sys

global dx, dy

# 처음 한 칸은 공백으로 방향에 따라 인덱스 접근하도록 설정
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def solution():
    graph = [[(0, 0) for _ in range(4)] for _ in range(4)]
    # 물고기들의 번호에 따라 현재 위치를 가지는 테이블 생성
    # 0 인덱스는 상어
    fish_position = [[0, 0] for _ in range(17)]
    # 살아있는 물고기
    fish_alive = [True for _ in range(17)]

    for i in range(4):
        ipt = list(map(int, sys.stdin.readline().rstrip().split()))
        for k in range(0, 8, 2):
            fish_num = ipt[k]
            fish_direction = ipt[k+1]
            j = int(k/2)
            graph[i][j] = [fish_num, fish_direction]
            fish_position[fish_num] = [i, j]
    
    # 처음 상어가 (0, 0)에 들어옴
    fish = graph[0][0][0]
    fish_alive[fish] = False
    fish_position[0] = [0, 0]
    graph[0][0][0] = -1

    result = moveShark(fish, graph, fish_position, fish_alive)

    print(result)

def moveFish(graph, fish_position, fish_alive):
    for now_fish in range(1, 17):
        # 이미 먹힌 고기는 진행하지 않음
        if fish_alive[now_fish] == False:
            continue
        now_x, now_y = fish_position[now_fish]
        now_direction = graph[now_x][now_y][1]
        while True:
            dir_x = now_x + dx[now_direction]
            dir_y = now_y + dy[now_direction]
            # 방향이 가리키는 곳에 상어가 있거나 해당 방향이 out of range 일 때
            if dir_x < 0 or dir_y < 0 or dir_x == 4 or dir_y == 4 or graph[dir_x][dir_y][0] < 0:
                now_direction += 1
                if now_direction > 8:
                    now_direction = 1
            else:
                next_fish, next_direction = graph[dir_x][dir_y]
                next_x, next_y = dir_x, dir_y
                break
        # graph 바꾸기
        graph[next_x][next_y] = [now_fish, now_direction]
        graph[now_x][now_y] = [next_fish, next_direction]
        # fish porision 업데이트
        fish_position[now_fish] = [next_x, next_y]
        if next_fish > 0:
            fish_position[next_fish] = [now_x, now_y]

def moveShark(now, graph, fish_position, fish_alive):
    # 물고기 시뮬레이션
    moveFish(graph, fish_position, fish_alive)
    # 상어 현재 위치
    now_x, now_y = fish_position[0]
    direction = graph[now_x][now_y][1]
    # 상어의 방향에서 먹을 수 있는 먹이 리스트 구하기
    copy_x = now_x
    copy_y = now_y
    fish_list = []
    while True:
        next_x = copy_x + dx[direction]
        next_y = copy_y + dy[direction]
        # 범위 밖이면 그만
        if next_x < 0 or next_y < 0 or next_x == 4 or next_y == 4:
            break
        # 물고기가 있는 경우에만 fish_list에 추가
        if graph[next_x][next_y][0] > 0:
            fish_list.append(graph[next_x][next_y][0])
        copy_x = next_x
        copy_y = next_y

    max = now
    while fish_list:
        # 먹이가 있을 때
        fish = fish_list.pop()
        fish_x, fish_y = fish_position[fish]
        # graph 사본에 업데이트
        graph_c = [[item[:] for item in items] for items in graph]
        graph_c[fish_x][fish_y][0] = -1
        graph_c[now_x][now_y] = [0, 0]
        # fish_alive 사본에 업데이트
        fish_alive_c = fish_alive[:]
        fish_alive_c[fish] = False
        # fish_position 사본에 업데이트
        fish_position_c = fish_position[:]
        fish_position_c[0] = [fish_x, fish_y]

        value = now + moveShark(fish, graph_c, fish_position_c, fish_alive_c)
        if value > max:
            max = value

    return max

solution()