class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # holds [index, value] of num
        l = 0
        res = []
        for r in range(len(nums)):
            while q and q[-1][1] < nums[r]:
                q.pop()
            q.append([r, nums[r]])

            if q[0][0] < l:
                q.popleft()
            
            if (r - l + 1) >= k:
                res.append(q[0][1])
                l += 1
        return res