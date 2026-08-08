class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, cur):
            if open == close == n:
                res.append("".join(cur))
                return
            
            if open < n:
                cur.append("(")
                dfs(open + 1, close, cur)
                cur.pop()
            
            if close < open:
                cur.append(")")
                dfs(open, close + 1, cur)
                cur.pop()
            
        dfs(0, 0, [])
        return res