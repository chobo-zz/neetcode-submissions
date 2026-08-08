class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or remaining < 0:
                return
            
            cur.append(nums[i])
            dfs(i, cur, remaining - nums[i])

            cur.pop()
            dfs(i + 1, cur, remaining)

        dfs(0, [], target)
        return res