class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        totalVisited = set()

        preMap = { i:[] for i in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        def dfs(crs):
            if crs in visited:
                return False
            
            if crs in totalVisited:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            totalVisited.add(crs)
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

