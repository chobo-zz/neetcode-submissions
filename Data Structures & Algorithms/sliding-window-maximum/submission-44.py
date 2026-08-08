class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # holds (index, value) of nums
        l, r = 0, 0
        res = []
        while r < len(nums):
            num = nums[r]
            while q and q[-1][1] < num:
                q.pop()
            q.append([r, num])

            if q[0][0] < l:
                q.popleft()
            
            if (r - l + 1) >= k:
                res.append(q[0][1])
                l += 1
            r += 1
        
        return res
