class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            position = q.popleft()
            l = max(farthest + 1, position + minJump)
            r = min(len(s) - 1, position + maxJump)

            for i in range(l, r + 1):
                if s[i] == "0":
                    if i == len(s) - 1:
                        return True
                    q.append(i)
            farthest = max(farthest, position + maxJump)
        
        return False