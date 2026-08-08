class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def getNewLocks(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])

                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            
            return res

        if "0000" in deadends:
            return -1
        
        q = deque([["0000", 0]]) # current lock combination, number of turns
        visited = set(deadends)

        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns
            
            for newLock in getNewLocks(lock):
                if newLock not in visited:
                    q.append([newLock, turns + 1])
                    visited.add(newLock)
        return -1