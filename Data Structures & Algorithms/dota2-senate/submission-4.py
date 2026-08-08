class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()

        for i, v in enumerate(senate):
            if v == "D":
                dire.append(i)
            else:
                radiant.append(i)
        
        while dire and radiant:
            direSenator = dire.popleft()
            radiantSenator = radiant.popleft()

            if direSenator < radiantSenator:
                dire.append(direSenator + len(senate))
            else:
                radiant.append(radiantSenator + len(senate))
        
        return "Dire" if dire else "Radiant"
