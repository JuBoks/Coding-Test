def solution(p):
    answer = ''
    
    if p == '':
        return ''
    if isCorrectStr(p):
        return p
    
    answer = getFixedStr(p)
            
    return answer

def getFixedStr(str):
    if str == '':
        return str
    u, v = getBalancedString(str)
    if isCorrectStr(u):
        return u + getFixedStr(v)
    else:
        # v에 대한 재귀값 호출
        v_recurv = getFixedStr(v)
        # 4-1 ~ 4-3
        str_new = '('
        str_new += v_recurv
        str_new += ')'
        # 4-4 ~ 4-5
        len_u = len(u)
        u = u[1:len_u-1]
        u_reverse = reverseStr(u)
        str_new += u_reverse
        return str_new

def getBalancedString(str):
    if len(str) < 2:
        return str, ''
    
    result = str[0]
    result_rest = ''
    balance = getCharValue(str[0])

    str = str[1:]
    for idx in range(len(str)):
        balance += getCharValue(str[idx])
        result += str[idx]
        if balance == 0:
            result_rest = str[idx+1:]
            break
    
    return result, result_rest
        
def getCharValue(char):
    if char == '(':
        return 1
    else:
        return -1
        
def isCorrectStr(str):
    value = getCharValue(str[0])
    if value < 0:
        return False
    str = str[1:]
    for char in str:
        value += getCharValue(char)
        if value < 0 :
            return False
    return True
    
def reverseStr(str):
    result = ''
    for char in str:
        if getCharValue(char) == 1:
            result += ')'
        else:
            result += '('
    return result