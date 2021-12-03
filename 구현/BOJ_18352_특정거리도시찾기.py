import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().rstrip().split(' '))

table_info = [[] for _ in range(N+1)]
table_length = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    table_info[a].append(b)

# BFS
queue = deque([X])
table_length[X] = 0

while queue:
    node_now = queue.popleft()
    for node in table_info[node_now]:
        if table_length[node] == -1:
            table_length[node] = table_length[node_now] + 1
            queue.append(node)

flag = True
for i in range(M+1):
    if table_length[i] == K:
        flag = False
        print(i)

if (flag):
    print(-1)