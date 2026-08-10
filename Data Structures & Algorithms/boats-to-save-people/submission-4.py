class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        res = 0

        l, r = 0, len(people) - 1

        while l <= r:
            curSum = 0
            
            curSum += people[r]
            r -= 1
            if people[l] + curSum <= limit:
                l += 1
            res += 1
        
        return res
                