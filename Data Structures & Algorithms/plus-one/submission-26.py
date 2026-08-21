class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        for i in range(len(digits)):
            if i == len(digits) - 1:
                if digits[i] == 9:
                    digits[i] = 0
                    digits.append(1)
                    break
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        
        digits.reverse()
        return digits

        # [0001]