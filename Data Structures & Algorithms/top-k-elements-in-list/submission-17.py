class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []

        bucket = [[] for i in range(len(nums) + 1)] # index=freq, value=list of nums

        for num, freq in counter.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res