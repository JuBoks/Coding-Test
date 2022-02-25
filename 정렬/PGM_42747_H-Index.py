def solution(citations):
    answer = 0
    units = len(citations)
    max_h = max(citations)
    table = [0] * (max_h + 1)
    for i in range(units):
      n = citations[i]
      for idx in range(n+1):
        table[idx] += 1
      
    for h in range(max_h + 1):
      x = table[h]
      y = units - x
      if x >= h and y <= h:
        answer = h
      else:
        break
      
    return answer
  
  
def test():
  ipt = [3, 0, 6, 1, 5]
  ipt.sort(reverse=True)
  print(list(enumerate(ipt, start=1)))
  print(list(map(min, enumerate(ipt, start=1))))
  
  
ipt = [3, 0, 6, 1, 5]
# print(solution(ipt))

test()