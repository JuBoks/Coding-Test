N = list(input())
length = len(N) // 2
left = N[:length]
right = N[length:]

sum = 0
for i in left:
    sum += int(i)
for i in right:
    sum -= int(i)

if sum == 0:
    print('LUCKY')
else:
    print('READY')