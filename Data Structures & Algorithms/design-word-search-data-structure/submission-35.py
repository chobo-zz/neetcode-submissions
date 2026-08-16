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
        def dfs(i, cur): # returns if word exists starting from word[i:]
            if i == len(word):
                return cur.endOfWord

            char = word[i]
            if word[i] == ".":
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if char not in cur.children:
                    return False
                cur = cur.children[char]
                return dfs(i + 1, cur)

        return dfs(0, self.root)
