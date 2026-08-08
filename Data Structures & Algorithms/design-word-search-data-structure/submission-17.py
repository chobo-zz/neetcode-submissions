class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, cur):
            if i >= len(word):
                return cur.endOfWord
            char = word[i]
            if char == ".":
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if char in cur.children:
                    return dfs(i + 1, cur.children[char])
                return False


        return dfs(0, self.root)
