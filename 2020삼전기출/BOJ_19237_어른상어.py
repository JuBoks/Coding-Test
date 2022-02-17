import sys
import heapq

def solution():
    global dx, dy
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    # 입력받기
    N, M, k = map(int, sys.stdin.readline().rstrip().split())
    # 상어번호, 상어방향, 냄새남은시간
    graph = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    # 상어냄새정보 테이블
    odor = [[] for _ in range(M+1)]
    for i in range(N):
        arr = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(N):
            shark_num = arr[j]
            if shark_num > 0:
                heapq.heappush(odor[shark_num], [k * -1, i, j])
                graph[i][j][2] = k
            graph[i][j][0] = shark_num

    # 방향 읽고 방향테이블에 업데이트
    direction = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(M):
        shark_num = i+1
        v, x, y = odor[shark_num][0]
        graph[x][y][1] = direction[i]
    # 방향 우선순위 정보 테이블
    direction = {i: [[0 for _ in range(5)] for _ in range(5)] for i in range(M+1)}
    for shark_num in range(1, M+1):
        for i in range(1, 5):
            a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
            direction[shark_num][i][1] = a
            direction[shark_num][i][2] = b
            direction[shark_num][i][3] = c
            direction[shark_num][i][4] = d

    # 현재 남아있는 shark 수
    remain = M
    # shark 생존여부 테이블
    shark_alive = [True for _ in range(M+1)]
    time = 0
    while True:
        time += 1
        # 상어 방향 우선순위에 따라 각자 가는 방 리스트 구함
        next_list = checkEmptyOrOdorRoom(graph, direction, odor, shark_alive, M, N)
        # 상어끼리 충돌여부확인
        for shark_a in range(1, M+1):
            if shark_alive[shark_a] == False:
                continue
            if not next_list[shark_a]:
                continue
            for shark_b in range(shark_a+1, M+1):
                if shark_alive[shark_b] == False:
                    continue
                # 충돌일 경우 큰 숫자의 상어는 소멸
                if next_list[shark_a][0] == next_list[shark_b][0] and next_list[shark_a][1] == next_list[shark_b][1]:
                    next_list[shark_b] = (-1, -1, -1)
                    shark_alive[shark_b] = False
                    remain -= 1

        # 상어를 이동 후 odor 갱신
        moveShark(next_list, graph, odor, shark_alive, k, M)

        if remain == 1:
            break
        # 1000 넘어도 안끝나면 -1 
        if time == 1000:
            time = -1
            break
    
    print(time)

def checkEmptyOrOdorRoom(graph, direction, odor, shark_alive, M, N):
    next_list = [0 for _ in range(M+1)]

    for shark_num in range(1, M+1):
        if shark_alive[shark_num] == False:
            continue
        v, x, y = odor[shark_num][0]
        shark_dir = graph[x][y][1]
        # 현재 방향의 우선순위에 따라 빈칸이 있는지 확인
        dir_table = direction[shark_num]
        # 빈칸 방 체크
        new_room = checkRoom(x, y, 0, dir_table, shark_dir, graph, N)
        if not new_room:
            # 본인의 냄새가 있는 방을 체크
            new_room = checkRoom(x, y, shark_num, dir_table, shark_dir, graph, N)

        next_list[shark_num] = new_room
    
    return next_list

def checkRoom(x, y, room, dir_table, shark_dir, graph, N):
    # (x, y, 방향)
    new_room = ()
    for i in range(1, 5):
        dir_check = dir_table[shark_dir][i]
        x_next = x + dx[dir_check]
        y_next = y + dy[dir_check]
        if x_next < 0 or y_next < 0 or x_next == N or y_next == N:
            continue
        if graph[x_next][y_next][0] == room:
            new_room = (x_next, y_next, dir_check)
            break
    return new_room

def moveShark(next_list, graph, odor, shark_alive, k, M):
    for shark_num in range(1, M+1):
        # 죽은 shark 거나 shark 가 아무곳도 갈 수 없는 상황일 때 -> 남아있는 냄새만 odor 감소
        if shark_alive[shark_num] == False or not next_list[shark_num]:
            odor_new = []
            while odor[shark_num]:
                v_odor, x_odor, y_odor = heapq.heappop(odor[shark_num])
                graph[x_odor][y_odor][2] = (v_odor + 1) * -1
                if graph[x_odor][y_odor][2] == 0:
                    graph[x_odor][y_odor][0] = 0
                    graph[x_odor][y_odor][1] = 0
                else:
                    heapq.heappush(odor_new, [v_odor + 1, x_odor, y_odor])
            odor[shark_num] = odor_new
            continue
        # 살아있는 shark 의 경우
        x_next, y_next, dir_next = next_list[shark_num]
        if x_next != -1:
            graph[x_next][y_next][0] = shark_num
            graph[x_next][y_next][1] = dir_next
            graph[x_next][y_next][2] = k
            # odor 업데이트
            odor_new = []
            flag = True
            while odor[shark_num]:
                v_odor, x_odor, y_odor = heapq.heappop(odor[shark_num])
                # 빈 칸이 아니라 냄새 갱신일 때
                if x_odor == x_next and y_odor == y_next:
                    heapq.heappush(odor_new, [k * -1, x_odor, y_odor])
                    flag = False
                else:
                    graph[x_odor][y_odor][2] = (v_odor + 1) * -1
                    if graph[x_odor][y_odor][2] == 0:
                        graph[x_odor][y_odor][0] = 0
                        graph[x_odor][y_odor][1] = 0
                    else:
                        heapq.heappush(odor_new, [v_odor + 1, x_odor, y_odor])
            # 빈 칸으로 움직였을 때
            if flag:
                heapq.heappush(odor_new, [k * -1, x_next, y_next])
            odor[shark_num] = odor_new

solution()