class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for i in range(len(hand)):
            start = hand[i]

            while count[start - 1]:
                start -= 1
            
            while start <= hand[i]:
                while count[start]:
                    for j in range(groupSize):
                        if not count[start + j]:
                            return False
                        count[start + j] -= 1
                start += 1
        
        return True

                

