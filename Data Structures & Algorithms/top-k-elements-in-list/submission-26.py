class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        count = Counter(nums) # val -> count
        res = []
        bucket = [[] for i in range(len(nums) + 1)] # index represents count, value represents list of nums


        for val, count in count.items():
            bucket[count].append(val)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        
            