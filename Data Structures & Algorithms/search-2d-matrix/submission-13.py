class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        mid = -1

        while top <= bot:
            mid = (top + bot) // 2

            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[mid][m]:
                r = m - 1
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                return True
        
        return False