class TrieNode:
    def __init__(self):
        self.children = {} # key -> character, value -> TrieNode
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                child = TrieNode()
                cur.children[c] = child
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.endOfWord
            
            char = word[i]
            if char == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if char in node.children:
                    return dfs(i + 1, node.children[char])
                return False
        
        return dfs(0, self.root)
