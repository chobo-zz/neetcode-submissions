class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        directPre = [set() for i in range(numCourses)]
        indirectPre = [set() for i in range(numCourses)]
        indegree = [0] * numCourses

        for pre, crs in prerequisites:
            indegree[crs] += 1
            directPre[pre].add(crs)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            crs = q.popleft()

            for nextCrs in directPre[crs]:
                indegree[nextCrs] -= 1
                indirectPre[nextCrs].add(crs)
                indirectPre[nextCrs].update(indirectPre[crs])
                if indegree[nextCrs] == 0:
                    q.append(nextCrs)
        
        return [u in indirectPre[v] for u, v in queries]