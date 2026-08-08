class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in hand:
            start = num

            while count[start - 1]: # walk left as far as we can
                start -= 1
            
            while start <= num: # begin creating consecutive groups using the smallest number (our bottleneck)
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True
