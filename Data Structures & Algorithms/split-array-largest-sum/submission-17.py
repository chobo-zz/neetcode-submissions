class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(m):
            subarrays = 1
            curSum = 0
            for n in nums:
                if curSum + n > m:
                    curSum = 0
                    subarrays += 1
                    if subarrays > k:
                        return False
                curSum += n
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