from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    
    table = [[] for _ in range(10001)]
    table_reversed = [[] for _ in range(10001)]
    
    for word in words:
        table[len(word)].append(word)
        table_reversed[len(word)].append(word[::-1])
    
    for arr in table:
        arr.sort()
        
    for arr in table_reversed:
        arr.sort()
        
    for query in queries:
        if query[0] == '?':
            count = getCount(query[::-1], table_reversed[len(query)])
        else:
            count = getCount(query, table[len(query)])
        
        answer.append(count)

    return answer

def getCount(query, words):
    return bisect_right(words, query.replace('?', 'z')) - bisect_left(words, query.replace('?', 'a'))