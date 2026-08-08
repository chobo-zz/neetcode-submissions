class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, cur):
            if i > n:
                if len(cur) == k:
                    res.append(cur.copy())
                return
            
            cur.append(i)
            dfs(i + 1, cur)

            cur.pop()
            dfs(i + 1, cur)
        
        dfs(1, [])
        return res