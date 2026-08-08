class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # example input: [1, 2, 2, 3, 3, 3] -- k = 2
        # example output: [2, 3]

        # first create a map that stores (num -> frequency)
        # e.g.: { 1: 1, 2: 2, 3: 3}
        # also create a list that acts a bucket that uses indices as frequency, and value is list of nums
        # e.g.: [ [0], [1], [2], [3] ]

        # first, iterate through nums and store counts into map
        # second, iterate through map and populate list with freq->nums
        # now, because we have bucket with indices as frequency, 
        # we simply iterate backwards through our list and return first k nums

        count = {}
        bucket = [[] for i in range(len(nums) + 1)] # [0, 1, 2, 3, 4, 5, 6]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


