class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:  
                    continue 
                cur.append(nums[i])
                used[i] = True
                dfs(cur)
                cur.pop()
                used[i] = False
        
        dfs([])
        return res