class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set()
        adjList = defaultdict(list)

        for i in range(n):
            firstNum = nums[i]
            for j in range(i + 1, n):
                secondNum = nums[j]

                if math.gcd(firstNum, secondNum) > 1:
                    adjList[i].append(j)
                    adjList[j].append(i)
        
        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)
            

        dfs(0)
        return len(visited) == n
    
            
        