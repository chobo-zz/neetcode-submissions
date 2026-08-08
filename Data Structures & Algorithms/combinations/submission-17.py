class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            nonlocal n, k

            if len(cur) == k:
                res.append(cur.copy())
                return
            
            for num in range(i, n + 1):
                cur.append(num)
                dfs(num + 1, cur)
                cur.pop()
            
        dfs(1, [])
        return res
