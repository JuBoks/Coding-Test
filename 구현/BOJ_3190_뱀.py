f = open(r'BOJ_3190_뱀4.txt')

N = int(f.readline().rstrip())
matrix = [[0] * N for _ in range(N)]
apple_unit = int(f.readline().rstrip())
# matrix 사과 표시
for i in range(apple_unit):
    x, y = map(int, f.readline().rstrip().split(' '))
    matrix[x-1][y-1] = 1
# 회전 횟수
rotate_unit = int(f.readline().rstrip())
now = 1
direction_list = ['R', 'D', 'L', 'U']
location_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_now_idx = 0
queue = []
for i in range(rotate_unit):
    time, direction = f.readline().rstrip().split(' ')
    time = int(time)
    while now <= time:
        queue.append(location_list[direction_now_idx])
        now += 1
    if direction == 'D':
        direction_now_idx += 1
        if direction_now_idx == 4:
            direction_now_idx = 0
    else:
        direction_now_idx -= 1
        if direction_now_idx < 0:
            direction_now_idx = 3

# 시뮬레이션 시작
sneak = [(0, 0)]
head = [0, 0]
count = 0
queue = list(reversed(queue))
while True:
    # queue 에서 방향 정보 얻기
    try:
        command = queue.pop()
    except:
        command = location_list[direction_now_idx]
    head[0] += command[0]
    head[1] += command[1]
    # head 위치가 out of matrix 인지 판별
    if head[0] == N or head[0] < 0 or head[1] == N or head[1] < 0:
        count += 1
        break
    # head 위치가 sneak 에 속하는지 판별
    flag = False
    for elm in sneak:
        if elm[0] == head[0] and elm[1] == head[1]:
            count += 1
            flag = True
            break
    if flag:
        break
    # 사과 없음
    if matrix[head[0]][head[1]] != 1:
        sneak = sneak[1:]
    else: # 사과 먹고 지워줌
        matrix[head[0]][head[1]] = 0
    sneak.append((head[0], head[1]))
    count += 1
print(count)

f.close()
