class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        
        def dfs(cur):
            if len(nums) == len(cur):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue
                
                used[i] = True
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                used[i] = False

        dfs([])
        return res
