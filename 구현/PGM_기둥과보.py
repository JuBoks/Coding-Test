from collections import OrderedDict

table = {}
def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x = int(frame[0])
        y = int(frame[1])
        material = int(frame[2])
        isToInstall = int(frame[3])
        if material == 0: # 기둥
            if y == n:
                continue
            if isToInstall == 1: # 설치
                if isColumnAbleToInstall(x, y):
                    installMaterial(x, y, 0)
            else:
                if isColumnAbleToRemove(x, y):
                    removeMaterial(x, y, 0)
        else: # 보
            if x == n or y == 0:
                continue
            if isToInstall == 1: # 설치
                if isBeamAbleToInstall(x, y):
                    installMaterial(x, y, 1)
            else:
                if isBeamAbleToRemove(x, y):
                    removeMaterial(x, y, 1)
    
    table_sorted = sorted(table.items(), key = lambda x: (int(x[0].split(',')[0]) + 1) * 1000 + (int(x[0].split(',')[1]) + 1) * 10)

    for elm in table_sorted:
        arr = []
        x, y = elm[0].split(',')
        arr.append(int(x))
        arr.append(int(y))
        elm[1].sort()
        for m in elm[1]:
            arr_copied = arr[:]
            arr_copied.append(m)
            answer.append(arr_copied)
    
    if len(answer) == 0:
        answer.append([])
        
    return answer

def isKeyExist(x, y):
    if table.get(f'{x},{y}') == None:
        return False
    return True

def installMaterial(x, y, material):
    if isKeyExist(x, y) == False:
        table[f'{x},{y}'] = []

    table[f'{x},{y}'].append(material)

def removeMaterial(x, y, material):
    table[f'{x},{y}'].remove(material)

def isThisBeam(x, y):
    if not isKeyExist(x, y):
        return False
    
    for elm in table[f'{x},{y}']:
        if elm == 1:
            return True
    return False

def isThisColumn(x, y):
    if not isKeyExist(x, y):
        return False
    
    for elm in table[f'{x},{y}']:
        if elm == 0:
            return True
    return False

def isBeamAbleToInstall(x, y):
    if isThisBeam(x-1, y) and isThisBeam(x+1, y):
        return True
    elif isThisColumn(x, y-1):
        return True
    elif isThisColumn(x+1, y-1):
        return True
    return False

def isColumnAbleToInstall(x, y):
    if y == 0:
        return True
    elif isThisColumn(x, y-1):
        return True
    elif isThisBeam(x, y):
        return True
    elif isThisBeam(x-1, y):
        return True
    return False

def isBeamAbleToRemove(x, y):
    removeMaterial(x, y, 1)
    if isThisBeam(x-1, y):
        if not isBeamAbleToInstall(x-1, y):
            installMaterial(x, y, 1)
            return False
    if isThisBeam(x+1, y):
        if not isBeamAbleToInstall(x+1, y):
            installMaterial(x, y, 1)
            return False
    if isThisColumn(x+1, y):
        if not isColumnAbleToInstall(x+1, y):
            installMaterial(x, y, 1)
            return False
    if isThisColumn(x, y):
        if not isColumnAbleToInstall(x, y):
            installMaterial(x, y, 1)
            return False
    installMaterial(x, y, 1)
    return True

def isColumnAbleToRemove(x, y):
    removeMaterial(x, y, 0)
    if isThisBeam(x, y+1):
        if not isBeamAbleToInstall(x, y+1):
            installMaterial(x, y, 0)
            return False
    if isThisColumn(x, y+1):
        if not isColumnAbleToInstall(x, y+1):
            installMaterial(x, y, 0)
            return False
    if isThisBeam(x-1, y+1):
        if not isBeamAbleToInstall(x-1, y+1):
            installMaterial(x, y, 0)
            return False
    installMaterial(x, y, 0)
    return True


a = solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
print(a)