class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)

        if totalSum % k != 0:
            return False

        targetSum = totalSum // k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        
        def dfs(i, k, subsetSum):
            if k == 0:
                return True
            
            if subsetSum == targetSum:
                return dfs(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > targetSum:
                    continue
                used[j] = True

                if dfs(j, k, subsetSum + nums[j]):
                    return True
                
                used[j] = False

                if subsetSum == 0:
                    return False
            return False

        return dfs(0, k, 0)
            