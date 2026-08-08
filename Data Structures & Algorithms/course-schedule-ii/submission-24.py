class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjList = defaultdict(list)
        res = []

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            indegree[crs] += 1
        
        q = deque([])

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            crs = q.popleft()

            res.append(crs)

            for nei in adjList[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        for num in indegree:
            if num != 0:
                return []
        
        return res