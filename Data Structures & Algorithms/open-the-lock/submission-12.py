class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def getNewLocks(cur):
            res = []
            for i in range(4):
                digit = int(cur[i])
                increment = cur[:i] + str((digit + 1) % 10) + cur[i + 1:]
                res.append(increment)
                decrement = cur[:i] + str((digit + 10 - 1) % 10) + cur[i + 1:]
                res.append(decrement)
            return res

        if "0000" in deadends:
            return -1
        
        q = deque([("0000", 0)])
        visited = set(deadends)
        
        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns
            
            newLocks = getNewLocks(lock)
            for newLock in newLocks:
                if newLock not in visited:
                    q.append((newLock, turns + 1))
                    visited.add(newLock)
        return -1
            



