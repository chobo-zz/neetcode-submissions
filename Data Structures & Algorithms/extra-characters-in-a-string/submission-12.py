class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(set(dictionary))
        memo = {}

        def dfs(i):
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]

            res = 1 + dfs(i + 1)
            cur = trie.root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.endOfWord:
                    res = min(res, dfs(j + 1))
            memo[i] = res
            return res
        return dfs(0)
                

        