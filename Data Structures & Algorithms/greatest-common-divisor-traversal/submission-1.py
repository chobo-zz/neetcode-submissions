class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        visit = [False] * n
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if math.gcd(nums[i], nums[j]) > 1:
                    adj[i].append(j)
                    adj[j].append(i)

        def dfs(node):
            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)

        dfs(0)
        for node in visit:
            if not node:
                return False
        return True