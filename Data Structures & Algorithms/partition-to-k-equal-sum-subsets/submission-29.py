class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        
        used = [False] * len(nums)
        target = total // k
        nums.sort(reverse=True)

        def dfs(curSum, k):
            if k == 0:
                return True

            if curSum == target:
                return dfs(0, k - 1)
            
            for j in range(len(nums)):
                if used[j] or nums[j] + curSum > target:
                    continue
                used[j] = True
                if dfs(curSum + nums[j], k):
                    return True
                used[j] = False

                if curSum == 0:
                    return False
            
            return False
        
        return dfs(0, k)
