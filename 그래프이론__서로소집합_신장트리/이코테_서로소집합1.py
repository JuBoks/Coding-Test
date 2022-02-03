'''
6 4
1 4
2 3
2 4
5 6
'''
def solution():
    N, M = map(int, input().split())
    
    # 부모정보 테이블 초기화는 노드 본인
    parent = [0] * (N+1)
    for idx in range(N+1):
        parent[idx] = idx
    
    for _ in range(M):
        A, B = map(int, input().split())
        unionParent(parent, A, B)

    # find 함수의 개선을 위해 각 원소에 대하여 find 함수를 수행
    for node in range(1, N+1):
        findParent(parent, node)

    print(parent[1:])

def unionParent(parent, A, B):
    pA = findParent(parent, A)
    pB = findParent(parent, B)
    if pA > pB:
        parent[pA] = pB
    else:
        parent[pB] = pA

def findParent(parent, A):
    if parent[A] != A:
        parent[A] = findParent(parent, parent[A])

    return parent[A]

solution()