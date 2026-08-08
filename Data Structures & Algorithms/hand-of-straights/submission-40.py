class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)

        for i in range(len(hand)):
            start = hand[i]
            
            # find start of sequence
            while start - 1 in count:
                start = start - 1
            
            # begin making groups with start value
            while start <= hand[i]:
                # keep trying to make groups as long as there's still counts of start left
                while count[start]:
                    for j in range(start, start + groupSize):
                        if not count[j]:
                            return False
                        count[j] -= 1
                start += 1
        
        return True

