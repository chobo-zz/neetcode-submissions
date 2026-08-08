class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = { crs: 0 for crs in range(numCourses) }
        q = deque()
        adjList = { crs: set() for crs in range(numCourses) }
        ordering = []

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adjList[pre].add(crs)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        while q:
            crs = q.popleft()

            finish += 1
            ordering.append(crs)

            for pre in adjList[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return ordering if finish == numCourses else []

