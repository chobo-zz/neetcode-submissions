class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def dfs(openN, closeN, n):
            if openN == closeN == n:
                res.append("".join(cur))

            if openN < n:
                cur.append("(")
                dfs(openN + 1, closeN, n)
                cur.pop()
            
            if closeN < openN:
                cur.append(")")
                dfs(openN, closeN + 1, n)
                cur.pop()
        
        dfs(0, 0, n)
        return res