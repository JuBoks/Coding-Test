import sys

def solution():
    global dx, dy
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    score = [0, 0, 0, 1, 1, 2, 3, 5, 11]

    N = int(input())
    word_list = []
    for i in range(N):
        word_list.append(sys.stdin.readline().rstrip())
    input()

    games = int(input())
    while games > 0:
        games -= 1
        graph = []
        for _ in range(4):
            graph.append(list(sys.stdin.readline().rstrip()))

        if games > 0:
            input()
        
        count = 0
        total_score = 0
        find_list = []

        for word in word_list:
            if findWords(graph, word) == True:
                count += 1
                total_score += score[len(word)]
                find_list.append(word)

        if len(find_list) == 0:
            print(0, 0)
        else:
            find_list.sort(key=lambda x:(-len(x), x))
            print(total_score, find_list[0], count)

def findWords(graph, word):
    flag = [
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True],
        [True, True, True, True]
    ]
    for x in range(4):
        for y in range(4):
            if graph[x][y] == word[0]:
                flag[x][y] = False
                if findAlphabets(graph, flag, x, y, list(word[1:])) == True:
                    return True
    return False

def findAlphabets(graph, flag, now_x, now_y, word):
    if len(word) == 0:
        return True
    for i in range(8):
        x = now_x + dx[i]
        y = now_y + dy[i]
        if x < 0 or y < 0 or x == 4 or y == 4:
            continue

        for alphabet in word:
            if graph[x][y] == alphabet and flag[x][y] == True:
                word.remove(alphabet)
                flag[x][y] = False
                if findAlphabets(graph, flag, x, y, word) == True:
                    return True

    return False
            
solution()