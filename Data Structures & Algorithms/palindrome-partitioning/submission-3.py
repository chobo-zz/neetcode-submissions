class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(i):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    cur.append(s[i:j + 1])
                    dfs(j + 1)
                    cur.pop()
            
        dfs(0)
        return res
    
    def isPalindrome(self, s, i, j):
        l, r = i, j

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    