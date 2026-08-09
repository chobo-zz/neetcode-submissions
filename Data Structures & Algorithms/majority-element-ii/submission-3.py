class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, cnt1, cnt2 = None, None, 0, 0

        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = num
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        res = []
        for num in [cand1, cand2]:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res