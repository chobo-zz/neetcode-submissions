class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in sorted(count):
            if count[num] > 0:
                freq = count[num]

                for i in range(num, num + groupSize):
                    if count[i] < freq:
                        return False
                    count[i] -= freq

        return True