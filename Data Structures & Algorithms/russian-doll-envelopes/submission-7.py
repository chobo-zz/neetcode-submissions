class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]):
        # Sort by:
        #   1. width increasing
        #   2. if widths tie, height decreasing
        #
        # Descending heights for equal widths prevents the LIS
        # from incorrectly choosing two envelopes with the same width.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            # dp[i] = smallest possible ending value of an
            # increasing subsequence of length (i + 1)
            dp = [nums[0]]

            # Current LIS length
            LIS = 1

            for i in range(1, len(nums)):

                # If current number is larger than every tail,
                # we can extend the longest subsequence.
                if nums[i] > dp[-1]:
                    dp.append(nums[i])
                    LIS += 1
                    continue

                # Otherwise, replace the first tail >= nums[i]
                # with nums[i]. This keeps the same subsequence
                # length but produces a smaller ending value,
                # making future extensions easier.
                idx = bisect_left(dp, nums[i])
                dp[idx] = nums[i]

            return LIS

        # After sorting, widths are already handled.
        # Find the LIS on heights only.
        heights = [h for _, h in envelopes]
        return lis(heights)