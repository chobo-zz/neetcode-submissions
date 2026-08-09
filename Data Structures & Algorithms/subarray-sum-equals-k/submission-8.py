class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixMap = defaultdict(int) # prefixSum -> frequency count
        prefixMap[0] = 1
        curSum = 0

        for num in nums:
            curSum += num
            res += prefixMap[curSum - k]
            prefixMap[curSum] += 1
        
        return res
