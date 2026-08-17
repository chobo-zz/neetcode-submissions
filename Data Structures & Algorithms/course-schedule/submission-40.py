class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adjList[pre].append(crs)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        processed = 0
        while q:
            crs = q.popleft()
            processed += 1

            for nextCrs in adjList[crs]:
                indegree[nextCrs] -= 1
                if indegree[nextCrs] == 0:
                    q.append(nextCrs)
                    
        
        return processed == len(indegree)
                
            
        

