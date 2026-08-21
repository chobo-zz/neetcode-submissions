class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, c in enumerate(senate):
            if c == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()

            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
            
        return "Radiant" if radiant else "Dire"

            