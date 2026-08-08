class Solution:
    def trap(self, height: List[int]) -> int:
        # algorithm to get trapped water at index i with tracked left and right boundaries:
        # min(leftMax, rightMax) - height[i] = trapped water at index i
        # using this algorithm, we need to keep track of leftMax/rightMax via two pointer approach
        # we use the min(leftMax, rightMax) because shorter boundary is the bottleneck
        # since shorter boundary is bottleneck, we also move pointer with shorter boundary


        res = 0

        if not height:
            return res
        
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res


