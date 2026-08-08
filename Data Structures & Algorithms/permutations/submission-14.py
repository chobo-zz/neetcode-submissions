class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
            
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    dfs(i + 1, cur)
                    cur.pop()
            
        dfs(0, [])
        return res