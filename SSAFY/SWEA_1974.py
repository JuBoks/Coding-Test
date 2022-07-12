import sys

sys.stdin = open("d:/projects/Coding-Test/SSAFY/input.txt", "r")

def checkSquares(graph):
  for x in range(0, 9, 3):
    for y in range(0, 9, 3):
      check = [0 for _ in range(10)]
      for i in range(x, x+3):
        for j in range(y, y+3):
          if check[graph[i][j]] == 0:
            check[graph[i][j]] = 1
          else:
            return False
    return True
  

def checkHorizon(graph):
  for x in range(9):
    check = [0 for _ in range(10)]
    for y in range(9):
      if check[graph[x][y]] == 0:
        check[graph[x][y]] = 1
      else:
        return False
  return True

def checkVertical(graph):
  for y in range(9):
    check = [0 for _ in range(10)]
    for x in range(9):
      if check[graph[x][y]] == 0:
        check[graph[x][y]] = 1
      else:
        return False
  return True

T = int(input())
for test_case in range(1, T + 1):
  graph = [list(map(int, input().split())) for _ in range(9)]
  
  # print('#%d' % test_case)
  # for el in graph:
  #   print(el)
  # print()
  
  # 1. 3x3 네모 확인
  if checkSquares(graph) == False:
    print('#%d 0' % test_case)
    continue
  
  # 2. 가로확인
  if checkHorizon(graph) == False:
    print('#%d 0' % test_case)
    continue
  
  # 3. 세로확인
  if checkVertical(graph) == False:
    print('#%d 0' % test_case)
    continue
  else:
    print('#%d 1' % test_case)
