def solution(words, queries):
    answer = []
    
    # 1. words Trie 생성
    trie = Trie()
    for word in words:
        trie.insert(word)
        
    # 2. reversed words Trie 생성
    trie_reversed = Trie()
    for word in words:
        trie_reversed.insert(word[::-1])
    
    # 2. queries 찾기
    table = {}
    for query in queries:
        matched = 0

        try:
            matched = table[query]
        except:
            # 모두 ?인 쿼리
            if query[0] == '?' and query[-1] == '?':
                length = len(query)
                for word in words:
                    if len(word) == length:
                        matched = matched + 1
            else:
                if query[0] == '?': # reversed Trie에서 검색
                    matched = trie_reversed.getChildren(query[::-1])
                else: # Trie에서 검색
                    matched = trie.getChildren(query)
                    
            table[query] = matched

        answer.append(matched)
        
    return answer


class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.lengthCount = {}
        
class Trie(object):
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        
        length = len(string)
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            try:
                curr_node.lengthCount[length] = curr_node.lengthCount[length] + 1
            except:
                curr_node.lengthCount[length] = 1
        
    def getChildren(self, query):
        result = 0
        curr_node = self.head
        
        for char in query:
            if char == '?':
                break
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return result
                
        try:
            result = curr_node.lengthCount[len(query)]
        except:
            result = 0

        return result