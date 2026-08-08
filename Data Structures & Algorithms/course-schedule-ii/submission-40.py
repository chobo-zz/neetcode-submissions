class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses
        ordering = []

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            indegree[crs] += 1
        
        q = deque([i for i, v in enumerate(indegree) if v == 0])

        while q:
            pre = q.popleft()

            ordering.append(pre)

            for crs in adjList[pre]:
                indegree[crs] -= 1

                if indegree[crs] == 0:
                    q.append(crs)
        
        return ordering if len(ordering) == numCourses else []        