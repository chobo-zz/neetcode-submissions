class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        prev = ""
        l = 0
        r = 1

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            elif arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            else:
                r += 1 if arr[r - 1] == arr[r] else 0
                l = r - 1
                prev = ""
        
        return res
