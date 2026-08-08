class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, cur):
            if i >= len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    cur.append(s[i:j + 1])
                    dfs(j + 1, cur)
                    cur.pop()
            
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        dfs(0, [])
        return res
