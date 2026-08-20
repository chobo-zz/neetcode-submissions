class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                if not fives:
                    return False
                fives -= 1
            elif bill == 20:
                if tens:
                    if not fives:
                        return False
                    tens -= 1
                    fives -= 1
                elif fives < 3:
                    return False
                else:
                    fives -= 3
        return True
                
            