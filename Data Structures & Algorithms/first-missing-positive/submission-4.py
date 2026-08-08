class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Replace negative numbers with 0 since they cannot affect
        # the answer (the first missing positive is always >= 1).
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # Use the array itself as a hash set.
        # If value x exists and 1 <= x <= n, mark index (x - 1)
        # as visited by making nums[x - 1] negative.
        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    # Use a special negative sentinel because
                    # negating 0 would still be 0.
                    nums[val - 1] = -1 * (len(nums) + 1)
            
        # The first index that was never marked corresponds
        # to the smallest missing positive integer.
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1