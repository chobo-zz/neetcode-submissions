class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqBucket = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)

        for num, count in count.items():
            freqBucket[count].append(num)

        res = []
        
        for i in range(len(freqBucket) - 1, -1, -1):
            for num in freqBucket[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        
            
