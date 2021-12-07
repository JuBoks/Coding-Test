import sys
N = int(input())
arr = []
for _ in range(N):
    elm = sys.stdin.readline().rstrip().split(' ')
    elm[1:] = map(int, elm[1:])
    arr.append(tuple(elm))

e = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for elm in e:
    print(elm[0])