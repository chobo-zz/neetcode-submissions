class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cardCount = Counter(hand)

        for i in range(len(hand)):
            card = hand[i]
            start = card

            while cardCount[start - 1]:
                start -= 1
            
            while start <= card:
                while cardCount[start]:
                    for j in range(groupSize):
                        if not cardCount[start + j]:
                            return False
                        cardCount[start + j] -= 1
                start += 1
        
        return True

            