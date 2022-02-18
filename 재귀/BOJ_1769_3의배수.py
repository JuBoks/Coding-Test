def solution():
  N = list(map(int,input()))
  N, result = convert(N, 0)
  print(result)
  if N[0] % 3 == 0:
    print("YES")
  else:
    print("NO")
  
def convert(N, count):
  if len(N) != 1:
    N = sumInput(N)
    N, count = convert(N, count+1)
  return N, count
  
def sumInput(N):
  total = 0
  for el in N:
    total += el
  return list(map(int, str(total)))

solution()