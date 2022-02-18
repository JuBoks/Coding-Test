def solution():
  N = int(input())
  print(convert(N))
  
def convert(N):
  quotient = N // 2
  remainder = N % 2
  if quotient != 1:
    quotient = convert(quotient)
  return str(quotient) + str(remainder)

solution()