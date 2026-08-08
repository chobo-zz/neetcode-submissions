class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closeN, n, cur):
            if openN == closeN == n:
                res.append("".join(cur))

            if openN < n:
                cur.append("(")
                dfs(openN + 1, closeN, n, cur)
                cur.pop()
            
            if closeN < openN:
                cur.append(")")
                dfs(openN, closeN + 1, n, cur)
                cur.pop()
        
        dfs(0, 0, n, [])
        return res