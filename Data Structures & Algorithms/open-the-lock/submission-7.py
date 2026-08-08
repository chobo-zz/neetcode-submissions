class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque([("0000", 0)])
        visited = set(deadends)


        def getNextLocks(lock):
            res = []

            for i in range(4):
                digit = int(lock[i])

                nextDigit = str((digit + 1) % 10)
                res.append(lock[:i] + nextDigit + lock[i + 1:])
                prevDigit = str((digit - 1 + 10) % 10)
                res.append(lock[:i] + prevDigit + lock[i + 1:])

            return res
        
        while q:
            lock, count = q.popleft()

            if lock == target:
                return count
            
            for nextLock in getNextLocks(lock):
                if nextLock not in visited:
                    visited.add(nextLock)
                    q.append((nextLock, count + 1))

        return -1