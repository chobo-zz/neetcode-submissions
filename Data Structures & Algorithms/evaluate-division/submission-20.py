class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i, v in enumerate(equations):
            x, y = v
            adjList[x].append((y, values[i]))
            adjList[y].append((x, 1 / values[i]))
        
        def dfs(src, target, visited):
            if src not in adjList or target not in adjList:
                return -1

            if src == target:
                return 1
            
            for nei, neiWeight in adjList[src]:
                if nei not in visited:
                    visited.add(nei)
                    result = dfs(nei, target, visited)
                    
                    if result != -1:
                        return result * neiWeight

            return -1
        
        return [dfs(x, y, set()) for x, y in queries]