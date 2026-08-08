class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(max):
            subarrays = 1
            curSum = 0
            
            for num in nums:
                curSum += num
                if curSum > max:
                    subarrays += 1
                    curSum = num
                    if subarrays > k:
                        return False
            return True


        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2

            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res