class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        used = [False] * len(nums)
        nums.sort(reverse=True)

        def backtrack(k, subsetSum):
            if k == 0:
                return True
            
            if subsetSum == target:
                return backtrack(k - 1, 0)
            
            for j in range(len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                
                used[j] = True
                if backtrack(k, subsetSum + nums[j]):
                    return True
                used[j] = False

                if subsetSum == 0:
                    return False
            
            return False
        
        return backtrack(k, 0)