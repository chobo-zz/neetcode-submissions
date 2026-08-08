from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # BFS queue storing every reachable position.
        q = deque([0])

        # Rightmost index we've already scanned.
        # Any index <= farthest has already been considered,
        # so we never need to scan it again.
        farthest = 0

        while q:
            # Current reachable position.
            position = q.popleft()

            # Start scanning from whichever is larger:
            #
            # 1. position + minJump
            #    -> first valid jump from this position
            #
            # 2. farthest + 1
            #    -> first index that has never been scanned before
            #
            # This prevents repeatedly scanning overlapping ranges.
            l = max(farthest + 1, position + minJump)

            # Furthest index we are allowed to jump to.
            r = min(len(s) - 1, position + maxJump)

            # Check every possible jump exactly once.
            for i in range(l, r + 1):

                # Can only land on '0'
                if s[i] == "0":

                    # If we've reached the last index,
                    # a valid path exists.
                    if i == len(s) - 1:
                        return True

                    # Otherwise continue exploring from here.
                    q.append(i)

            # Everything up to position + maxJump has now been scanned.
            # Future BFS nodes won't scan these indices again.
            farthest = max(farthest, position + maxJump)

        # Exhausted every reachable position without reaching the end.
        return False