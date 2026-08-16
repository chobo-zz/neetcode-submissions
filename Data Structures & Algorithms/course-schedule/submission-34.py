class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visited = set()
        visiting = set()


        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)

            for pre in adjList[node]:
                if not dfs(pre):
                    return False
            
            visiting.remove(node)
            visited.add(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
