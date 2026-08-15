class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    part = s[i:j + 1]
                    cur.append(part)
                    dfs(j + 1, cur)
                    cur.pop()
        
        dfs(0, [])
        return res