import sys

sys.stdin = open('d:/projects/Coding-Test/SSAFY/input.txt', 'r')

def solution():
  T = int(input())
  for test_case in range(1, T + 1):
    len1, len2 = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    if len1 <= len2:
      result = getMaxResult(arr1, arr2, len2-len1+1)
    else:
      result = getMaxResult(arr2, arr1, len1-len2+1)
    
    print('#%d'%test_case, result)
    
def getMaxResult(shortArr, longArr, swing):
  maxResult = float('-inf')
  startIdx = 0
  nowIdx = 0
  while swing > 0:
    swing -= 1
    result = 0
    for sh in shortArr:
      result += sh * longArr[nowIdx]
      nowIdx += 1
    if result > maxResult:
      maxResult = result
    startIdx += 1
    nowIdx = startIdx
    
  return maxResult
  

solution()