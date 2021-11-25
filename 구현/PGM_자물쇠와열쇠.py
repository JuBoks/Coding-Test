def solution(key, lock):
    # lock 확장
    key_dim = len(key[0])
    lock_dim = len(lock[0])
    lock_extended = []
    lock_extended_dim = 2 * key_dim + lock_dim
    key_dim = key_dim - 1
    lock_extended_dim = lock_extended_dim - 2
    for i in range(key_dim):
        lock_extended.append([0] * lock_extended_dim)
    for elm in lock:
        lock_extended.append([0] * key_dim + elm + [0] * key_dim)
    for i in range(key_dim):
        lock_extended.append([0] * lock_extended_dim)
    key_dim = key_dim + 1
    
    # key 90도 회전
    key_90 = []
    for idx1 in range(key_dim):
        row = []
        for idx2 in reversed(range(key_dim)):
            row.append(key[idx2][idx1])
        key_90.append(row)
    
    # key 180도 회전
    key_180 = []
    for idx1 in reversed(range(key_dim)):
        row = []
        for idx2 in reversed(range(key_dim)):
            row.append(key[idx1][idx2])
        key_180.append(row)

    # key 270도 회전
    key_270 = []
    for idx1 in reversed(range(key_dim)):
        row = []
        for idx2 in range(key_dim):
            row.append(key[idx2][idx1])
        key_270.append(row)
        
    if is_solution(key, lock_extended, lock_dim):
        return True
    
    if is_solution(key_90, lock_extended, lock_dim):
        return True

    if is_solution(key_180, lock_extended, lock_dim):
        return True
    
    if is_solution(key_270, lock_extended, lock_dim):
        return True
    
    return False

def is_solution(key, lock_extended, lock_dim):
    # add key matrix on lock matrix
    key_dim = len(key[0])
    lock_extended_dim = len(lock_extended[0])
    upto = lock_extended_dim - key_dim + 1
    for start_y in range(upto):
        for start_x in range(upto):
            # add matrix
            if add_matrix(key, lock_extended, start_y, start_x, lock_dim):
                return True
    return False
        
def add_matrix(key, lock, start_y, start_x, lock_dim):
    key_dim = len(key[0])
    # sum matrix
    for y in range(key_dim):
        for x in range(key_dim):
            lock[start_y + y][start_x + x] += key[y][x]
            
    # check matrix
    lock_start_x = key_dim - 1
    lock_start_y = key_dim - 1
    for y in range(lock_dim):
        for x in range(lock_dim):
            if lock[lock_start_y + y][lock_start_x + x] != 1:
                # lock 원상복구
                # deepcopy시 너무 많은 시간이 소요됨
                for y2 in range(key_dim):
                    for x2 in range(key_dim):
                        lock[start_y + y2][start_x + x2] -= key[y2][x2]
                return False
    return True
    