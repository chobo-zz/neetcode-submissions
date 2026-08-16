class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(i, cur):
            if i >= len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word in wordDict:
                    cur.append(word)
                    dfs(j + 1, cur)
                    cur.pop()
        
        dfs(0, [])
        return res