class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visiting = set()
        visited = set()

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True