class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            position = q.popleft()

            left = max(farthest + 1, position + minJump)
            right = min(len(s) - 1, position + maxJump)

            for jumpable in range(left, right + 1):
                if s[jumpable] == "0":
                    if jumpable == len(s) - 1:
                        return True
                    q.append(jumpable)
            
            farthest = right
        
        return False