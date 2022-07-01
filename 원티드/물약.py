import sys

def solution():
  global discountsInfo, N, result
  
  result = 1e9
  N = int(input())  
  priceInfo = list(map(int, sys.stdin.readline().rstrip().split()))
  priceInfo.insert(0, 0)

  buyInfo = [False for _ in range(N+1)]
  discountsInfo = dict()
  for unit in range(1, N+1):
    discounts = int(input())
    discountsInfo[unit] = []
    for __ in range(discounts):
      i, discounted = map(int, sys.stdin.readline().rstrip().split())
      discountsInfo[unit].append((i, discounted))
      
  # 각 물약을 처음으로 모두 시작해봄
  simulate(priceInfo, buyInfo, 0)
  print(result)


# 현재 물약 번호(medicine), 물약 가격정보, 현재 지불한 누적금액(money)
# 물약을 사면 할인 정보에 따라 물약 가격정보가 바뀜
def simulate(priceInfo, buyInfo, money):
  global result
  
  if isSoldOut(buyInfo) == True:
    result = min(result, money)
    
  for unit in range(1, N+1):
    # 이미 산 물약은 패스
    if buyInfo[unit] == True:
      continue
    
    value = priceInfo[unit]
    if value <= 0:
      value = 1
      
    # 물약 구매
    money += value
    buyMedicine(unit, priceInfo, buyInfo)
    
    result = min(result, simulate(priceInfo, buyInfo, money))

    # 원상복귀
    undoBuyMedicine(unit, priceInfo, buyInfo)
    money -= value
  
  return result

def isSoldOut(buyInfo):
  for el in buyInfo[1:]:
    if el == False:
      return False
  return True

def buyMedicine(medicine, priceInfo, buyInfo):
  updatePriceInfo(medicine, priceInfo, 'update')
  buyInfo[medicine] = True

def undoBuyMedicine(medicine, priceInfo, buyInfo):
  updatePriceInfo(medicine, priceInfo, 'rollback')
  buyInfo[medicine] = False

# 현재 물약(medicine)을 구입 시, priceInfo 를 업데이트 하는 함수
# mode - update(할인가격적용), rollback(할인적용전가격)
def updatePriceInfo(medicine, priceInfo, mode):
  for unit, discount in discountsInfo[medicine]:
    if mode == 'update':
      priceInfo[unit] -= discount
    elif mode == 'rollback':
      priceInfo[unit] += discount
  
solution()