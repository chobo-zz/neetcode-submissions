class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visit = [False] * len(nums)
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if visit[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not visit[i - 1]:
                    continue
                visit[i] = True
                cur.append(nums[i])
                dfs(cur)
                visit[i] = False
                cur.pop()
        
        dfs([])
        return res
