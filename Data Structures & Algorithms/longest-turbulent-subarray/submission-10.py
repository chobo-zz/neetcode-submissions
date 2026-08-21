class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res = 1
        prev = None

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                prev = "<"
                res = max(res, r - l + 1)
                r += 1
            elif arr[r - 1] > arr[r] and prev != ">":
                prev = ">"
                res = max(res, r - l + 1)
                r += 1
            else:
                r += (1 if arr[r - 1] == arr[r] else 0)
                l = r - 1
                prev = None
        
        return res