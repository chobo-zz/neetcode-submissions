class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        visited = set()
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visiting.add(crs)
            for nei in adjList[crs]:
                if not dfs(nei):
                    return False
            
            visiting.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True