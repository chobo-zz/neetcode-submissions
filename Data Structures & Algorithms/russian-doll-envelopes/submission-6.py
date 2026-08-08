class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            dp.append(nums[0])

            LIS = 1
            for i in range(1, len(nums)):
                if dp[-1] < nums[i]:
                    dp.append(nums[i])
                    LIS += 1
                    continue

                idx = bisect_left(dp, nums[i])
                dp[idx] = nums[i]

            return LIS

        return lis([e[1] for e in envelopes])