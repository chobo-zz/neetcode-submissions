class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        q = deque()
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adjList[pre].append(crs)
        
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        finished = 0
        while q:
            justFinished = q.popleft()
            finished += 1

            for crs in adjList[justFinished]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        
        return finished == numCourses
            