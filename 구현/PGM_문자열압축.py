def solution(s):
    answer = float("inf")
    length = len(s)
    if length == 1:
        return 1
    halfLength = length // 2 + 1
    for unit in range(1, halfLength):
        newStr = []
        count = 1
        idx1 = 0
        idx2 = 0
        compare = ''
        nextString = ''
        while idx2 < length:
            # 1. get compare string
            while len(compare) != unit:
                compare += s[idx1]
                idx1 = idx1 + 1
                idx2 = idx1
            # 2. get next string
            while len(nextString) != unit:
                if idx2 == length:
                    break
                nextString += s[idx2]
                idx2 = idx2 + 1
            # 3. compare them
            if idx2 < length:
                if compare == nextString:
                   count = count + 1
                else:
                    if count > 1:
                        newStr.append(str(count))
                    newStr.append(compare)
                    idx1 = idx2 - unit
                    compare = ''
                    count = 1
            else:
                if compare == nextString:
                    count = count + 1
                    nextString = ''
                if count > 1:
                    newStr.append(str(count))
                newStr.append(compare)
                newStr.append(nextString)

            nextString = ''
        
        newStr = ''.join(newStr)
        if answer > len(newStr):
            answer = len(newStr)
            
    return answer

print('답: ', solution(input()))