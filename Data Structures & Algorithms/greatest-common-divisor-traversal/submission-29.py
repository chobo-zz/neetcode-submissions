class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        adjList = defaultdict(list)

        for i in range(len(nums)):
            first = nums[i]
            for j in range(i + 1, len(nums)):
                second = nums[j]

                if math.gcd(first, second) > 1:
                    adjList[i].append(j)
                    adjList[j].append(i)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)
        
        dfs(0)
        return len(visited) == len(nums)