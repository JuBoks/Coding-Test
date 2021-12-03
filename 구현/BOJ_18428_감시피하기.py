from itertools import combinations

def solution():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(input().split(' '))

    S = []
    T = []
    for y in range(N):
        for x in range(N):
            if graph[y][x] == 'S':
                S.append((y, x))
            elif graph[y][x] == 'T':
                if y > 0 and graph[y-1][x] == 'S' \
                    or y < N-1 and graph[y+1][x] == 'S' \
                    or x > 0 and graph[y][x-1] == 'S' \
                    or x < N-1 and graph[y][x+1] == 'S':
                    return "NO" 
                T.append((y, x))

    if len(T) == 0:
        return "YES"

    X = set()
    check = []
    for y1, x1 in S:
        for y2, x2 in T:
            flag = 1
            if y1 == y2 and x1 > x2:
                start = x2
                end = x1
                fixed = y1
                flag = 0
                check.append((flag, fixed, start, end))
            elif y1 == y2 and x1 < x2:
                start = x1
                end = x2
                fixed = y1
                flag = 0
                check.append((flag, fixed, start, end))
            elif x1 == x2 and y1 > y2:
                start = y2
                end = y1
                fixed = x1
                check.append((flag, fixed, start, end))
            elif x1 == x2 and y1 < y2:
                start = y1
                end = y2
                fixed = x1
                check.append((flag, fixed, start, end))
            else:
                continue

            start += 1
            while start < end:
                if flag == 0:
                    X.add((fixed, start))
                else:
                    X.add((start, fixed))
                start += 1

    check_flag = [False for _ in range(len(check))]
    if len(X) < 3:
        return "YES"
    for elm in list(combinations(X, 3)):
        for x, y in elm:
            idx = 0
            for axis, fixed_value, start, end in check:
                if axis == 0 and fixed_value == x:
                    if y > start and y < end:
                        check_flag[idx] = True
                elif axis == 1 and fixed_value == y:
                    if x > start and x < end:
                        check_flag[idx] = True
                idx += 1
        if checkFlag(check_flag):
            return "YES"
        else:
            for i in range(len(check_flag)):
                check_flag[i] = False
        
    return "NO"

def checkFlag(arr):
    for flag in arr:
        if flag == False:
            return False
    return True

print(solution())