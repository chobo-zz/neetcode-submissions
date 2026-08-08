class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        directPre = [set() for i in range(numCourses)]
        indirectPre = [set() for i in range(numCourses)]
        indegree = [0] * numCourses

        for pre, crs in prerequisites:
            directPre[pre].add(crs)
            indegree[crs] += 1
        
        q = deque([crs for crs in range(numCourses) if indegree[crs] == 0])

        while q:
            pre = q.popleft()

            for crs in directPre[pre]:
                indegree[crs] -= 1
                indirectPre[crs].add(pre)
                indirectPre[crs].update(indirectPre[pre])

                if indegree[crs] == 0:
                    q.append(crs)
        
        return [u in indirectPre[v] for u, v in queries]
        


