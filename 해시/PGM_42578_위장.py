from itertools import combinations

def solution(clothes):
  answer = 0
  
  table = {}
  for name, kind in clothes:
    try:
      table[kind] += 1
    except:
      table[kind] = 2
  
  keys = list(table.keys())
  answer = table[keys[0]]
  for key in keys[1:]:
    answer *= table[key]
  
  answer -= 1

  return answer
  
  
  
ipt = [["A1", "headgear"], ["A3", "headgear"], ["A2", "headgear"], ["A1", "eyewear"], ["A2", "eyewear"], ["A1", "up"], ["A2", "up"], ["A3", "up"], ["A4", "up"], ["A1", "down"], ["A2", "down"], ["A1", "out"], ["A2", "out"], ["A3", "out"]]
print(solution(ipt))