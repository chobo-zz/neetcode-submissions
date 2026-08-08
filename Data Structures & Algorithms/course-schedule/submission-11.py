class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        visited = set()

        preMap = { i: [] for i in range(numCourses) }

        for crs, pre in prerequisites:
            preMap[pre].append(crs)

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
