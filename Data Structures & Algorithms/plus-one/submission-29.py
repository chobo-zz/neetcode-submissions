class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        i = 0
        while carry:
            if digits[i] == 9:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(carry)
                    carry = 0
            else:
                digits[i] += carry
                carry = 0

            i += 1
        
        digits.reverse()
        return digits