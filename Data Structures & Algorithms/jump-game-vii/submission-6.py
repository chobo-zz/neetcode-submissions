from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        visited = {0}

        while q:
            position = q.popleft()

            l = position + minJump
            r = min(len(s) - 1, position + maxJump)

            for i in range(l, r + 1):
                if s[i] == "0" and i not in visited:
                    if i == len(s) - 1:
                        return True
                    visited.add(i)
                    q.append(i)

        return False