'''
숫자 a, b, c 가 있다고 할 때, 이 숫자들이 섞인다는 걸 합한다면
-> 2a + 2b + c
숫자 a, b, c, c 가 있다고 할 때, 이 숫자들이 섞인다는 걸 합한다면
-> 3a + 3b + 2c + d

틀림
틀린 이유 : a + b 에서 새로운 카드뭉치가 나왔고 해당 카드에 대해서도 정렬을 다시 해야 하기 때문임

'''
# import sys

# def solution():
#     N = int(input())
#     num_arr = []
#     for _ in range(N):
#         num_arr.append(int(sys.stdin.readline().rstrip()))
#     num_arr.sort()

#     length = N
#     N -= 1
#     result = num_arr[0] * N
#     for idx in range(1, length):
#         result += num_arr[idx] * N
#         N -= 1

#     return result

'''
우선순위 큐를 통해 풀이
https://www.daleseo.com/python-priority-queue/
우선순위 큐
- 데이터 추가는 어떤 순서로 해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 독특한 특성을 지닌 자료구조
- 내부적으로 데이터를 정렬된 상태로 보관함
'''
import sys
from queue import PriorityQueue

def solution():
    N = int(input())
    queue = PriorityQueue()
    for _ in range(N):
        queue.put(int(sys.stdin.readline().rstrip()))

    num1 = queue.get()
    result = 0
    while not queue.empty():
        num2 = queue.get()
        value = num1 + num2
        result += value
        queue.put(value)
        num1 = queue.get()

    return result

answer = solution()
print(answer)