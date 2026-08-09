class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSums = defaultdict(int) # prefixSum -> frequency count
        prefixSums[0] = 1
        curSum = 0 # our current running sum

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums[diff]
            prefixSums[curSum] += 1
        
        return res