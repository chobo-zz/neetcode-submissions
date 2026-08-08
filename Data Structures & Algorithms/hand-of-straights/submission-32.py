class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        numToFreq = Counter(hand)

        for num in hand:
            start = num

            while numToFreq[start - 1]:
                start -= 1
            
            while start <= num:
                while numToFreq[start]:
                    for i in range(start, start + groupSize):
                        if not numToFreq[i]:
                            return False
                        numToFreq[i] -= 1
                start += 1
        
        return True
            