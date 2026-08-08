class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        visiting = set()
        res = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, word, node):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visiting or board[r][c] not in node.children:
                return
            
            char = board[r][c]
            visiting.add((r, c))
            word += char
            node = node.children[char]
            if node.endOfWord:
                res.append(word)
            
            dfs(r + 1, c, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r, c - 1, word, node)

            visiting.remove((r, c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", root)
        
        return list(set(res))
            
