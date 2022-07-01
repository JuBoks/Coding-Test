import sys

sys.stdin = open("d:/projects/Coding-Test/SSAFY/1979_input.txt", "r")

T = int(input())

# 검은 블록 or 범위 밖인지 체크
def checkIfBlack(x, y, graph, N):
  if x == N or x < 0 or y == N or y < 0:
    return True
  elif graph[x][y] == 0:
    return True
  else:
    return False

def howManyBlocksVertical(x, y, graph, N):
  whites = 0
  for i in range(x, N):
    if graph[i][y] == 1:
      whites += 1
    else:
      break
  return whites

def howManyBlocksHorizon(x, y, graph, N):
  whites = 0
  for i in range(y, N):
    if graph[x][i] == 1:
      whites += 1
    else:
      break
  return whites

for test_case in range(1, T + 1):
  # ///////////////////////////////////////////////////////////////////////////////////
  N, K = map(int, input().split())
  graph = [list(map(int, input().split())) for _ in range(N)]
  result = 0
  # 위에서 아래로 체크
  for x in range(N):
    for y in range(N):
      # 현재보다 위쪽 블록이 Black 이면 수직으로 빈칸개수 체크
      if graph[x][y] == 1 and checkIfBlack(x-1, y, graph, N):
        whites = howManyBlocksVertical(x, y, graph, N)
        if whites == K:
          result += 1

  # 왼쪽에서 오른쪽으로 체크
  for x in range(N):
    for y in range(N):
      # 현재보다 위쪽 블록이 Black 이면 수직으로 빈칸개수 체크
      if graph[x][y] == 1 and checkIfBlack(x, y-1, graph, N):
        whites = howManyBlocksHorizon(x, y, graph, N)
        if whites == K:
          result += 1
          
  print('#%d' % test_case, result)
  # ///////////////////////////////////////////////////////////////////////////////////
