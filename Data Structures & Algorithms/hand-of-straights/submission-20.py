class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        # value -> count -- 1: 1, 2: 2
        
        for num in hand:
            start = num

            # walk left from num until we find smallest card as start of sequence
            if count[start - 1]:
                start = count[start - 1]
            
            # try to build group using this start
            
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
            
        return True
