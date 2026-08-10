class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        l = 0
        seen = set([nums[l]])

        for r in range(1, len(nums)):
        
            if r - l > k:
                seen.remove(nums[l])
                l += 1

            if nums[r] in seen:
                return True
            seen.add(nums[r])
        
        return False
            


        
            