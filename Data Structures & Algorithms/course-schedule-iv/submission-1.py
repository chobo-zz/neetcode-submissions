class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        directPre = [set() for i in range(numCourses)]
        indegree = [0] * numCourses
        indirectPre = [set() for i in range(numCourses)]

        for pre, crs in prerequisites:
            indegree[crs] += 1
            directPre[pre].add(crs)

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            pre = q.popleft()

            for crs in directPre[pre]:
                indegree[crs] -= 1
                indirectPre[crs].add(pre)
                indirectPre[crs].update(indirectPre[pre])
                if indegree[crs] == 0:
                    q.append(crs)
                
        return [u in indirectPre[v] for u, v in queries]


