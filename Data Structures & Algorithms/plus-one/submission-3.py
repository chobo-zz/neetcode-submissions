class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        carry = 1
        i = 0

        while carry:
            if i == len(digits):
                digits.append(1)
                carry = 0
            else:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            i += 1
        digits.reverse()
        return digits
            