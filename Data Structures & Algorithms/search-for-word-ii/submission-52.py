class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
    
    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = TrieNode()
        visited = set()
        for word in set(words):
            trie.addWord(word)

        res = []
        def dfs(r, c, cur):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or board[r][c] not in cur.children:
                return
            
            char = board[r][c]
            visited.add((r, c))
            cur = cur.children[char]
            if cur.word:
                res.append(cur.word)
            
            dfs(r, c - 1, cur)
            dfs(r, c + 1, cur)
            dfs(r + 1, c, cur)
            dfs(r - 1, c, cur)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)
        return list(set(res))

            


