N = input()
sum = 0
newStr = []

# 1. 아스키코드 값을 통해 숫자인지 알파벳인지 구분
# for i in N:
#     if ord(i) >= 48 and ord(i) <= 57:
#         sum += int(i)
#     else:
#         newStr.append(i)

# 2. 💖isalpha() 함수를통해 알파벳을 구분💖 
for i in N:
    if i.isalpha():
        newStr.append(i)
    else:
        sum += int(i)

newStr.sort()
newStr = ''.join(newStr)
print(newStr + str(sum))
