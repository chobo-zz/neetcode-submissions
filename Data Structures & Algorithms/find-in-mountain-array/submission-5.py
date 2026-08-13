class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1
        peak = -1
        while l <= r:
            m = (l + r) // 2

            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                peak = m
                break
        
        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            elif val > target:
                r = m - 1
            else:
                l = m + 1
        
        l, r = peak, mountainArr.length() - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            elif val > target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
