class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        
        used = [False] * len(nums)
        target = total // k
        nums.sort(reverse=True)

        def dfs(i, curSum, k):
            if k == 0:
                return True

            if curSum == target:
                return dfs(0, 0, k - 1)
            
            if i == len(nums):
                return False
            
            for j in range(i, len(nums)):
                if used[j] or nums[j] + curSum > target:
                    continue
                used[j] = True
                if dfs(j + 1, curSum + nums[j], k):
                    return True
                used[j] = False


            
            return False
        
        return dfs(0, 0, k)
