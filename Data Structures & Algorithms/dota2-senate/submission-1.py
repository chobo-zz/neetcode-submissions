class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()

        for i, v in enumerate(senate):
            if v == "R":
                r.append(i)
            else:
                d.append(i)
        
        while d and r:
            dTurn = d.popleft()
            rTurn = r.popleft()

            if dTurn < rTurn:
                d.append(dTurn + len(senate))
            else:
                r.append(rTurn + len(senate))
            
        return "Radiant" if r else "Dire"