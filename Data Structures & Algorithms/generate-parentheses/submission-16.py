class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(openN, close, n):
            if openN == close == n:
                res.append("".join(cur))
                return
            
            if openN < n:
                cur.append("(")
                dfs(openN + 1, close, n)
                cur.pop()
            
            if close < openN:
                cur.append(")")
                dfs(openN, close + 1, n)
                cur.pop()
            


        dfs(0, 0, n)
        return res