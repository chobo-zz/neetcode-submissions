class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i in range(len(equations)):
            x, y = equations[i]
            quotient = values[i]
            adjList[x].append((y, quotient))
            adjList[y].append((x, 1 / quotient))
        
        def dfs(src, dst, visited):
            if src not in adjList or dst not in adjList:
                return -1
            
            if src == dst:
                return 1
            
            for nei, neiWeight in adjList[src]:
                if nei not in visited:
                    visited.add(nei)
                    res = dfs(nei, dst, visited)

                    if res != -1:
                        return res * neiWeight
            return -1


        return [dfs(x, y, set()) for x, y in queries]