class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(open, close):
            nonlocal n

            if open == close == n:
                res.append("".join(cur))
                return
            
            if close < open:
                cur.append(")")
                dfs(open, close + 1)
                cur.pop()
            
            if open < n:
                cur.append("(")
                dfs(open + 1, close)
                cur.pop()
        
        dfs(0, 0)
        return res