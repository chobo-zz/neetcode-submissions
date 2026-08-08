class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array of buckets where 5th bucket means 5 counts
        # fill buckets with num vals, then iterate array in reverse order to return k vals

        count = Counter(nums) # val: freq
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        for val, freq in count.items():
            buckets[freq].append(val)
        
        for i in range(len(buckets) - 1, -1, -1):
            for val in buckets[i]:
                res.append(val)
                k -= 1
                if k == 0:
                    return res
        
        
        
        