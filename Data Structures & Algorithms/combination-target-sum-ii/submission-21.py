class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res = []

        def dfs(i, cur, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            
            if remaining < 0 or i == len(nums):
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur, remaining - nums[i])

            cur.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, cur, remaining)

        dfs(0, [], target)
        return res