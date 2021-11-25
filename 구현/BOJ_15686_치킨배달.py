from itertools import combinations

def solution():
    n, m = map(int, input().split(' '))
    table = []
    home_list = []
    store_list = []
    for i in range(n):
        arr = list(map(int, input().split(' ')))
        table.append(arr)
        for k in range(n):
            if arr[k] == 1:
                home_list.append([i, k])
            elif arr[k] == 2:
                store_list.append([i, k])

    store_unit = len(store_list)

    # store 조합 구하기
    store_name_list = []
    for i in range(store_unit):
        store_name_list.append(i)

    store_combinations = list(combinations(store_name_list, m))

    # 각 집마다 치킨집 거리 갱신
    table_length = []

    for home in home_list:
        arr = []
        for store in store_list:
            arr.append(abs(home[0] - store[0]) + abs(home[1] - store[1]))

        table_length.append(arr)

    result = float('inf')

    for comb in store_combinations:
        value = getLengthSum(comb, table_length)
        if result > value:
            result = value
    
    return result

def getLengthSum(comb, table):
    result = 0
    for home_info in table:
        home_min_length = float("inf")
        for store in comb:
            if home_min_length > home_info[store]:
                home_min_length = home_info[store]
        result += home_min_length
    return result

print(solution())