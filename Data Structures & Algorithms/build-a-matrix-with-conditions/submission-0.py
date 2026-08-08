class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            indegree = [0] * (k + 1)
            adj = [[] for _ in range(k + 1)]
            for u, v in edges:
                adj[u].append(v)
                indegree[v] += 1

            order = []
            q = deque()
            for i in range(1, k + 1):
                if not indegree[i]:
                    q.append(i)

            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if not indegree[nei]:
                        q.append(nei)

            return order

        row_order = topo_sort(rowConditions)
        if len(row_order) != k: return []

        col_order = topo_sort(colConditions)
        if len(col_order) != k: return []

        val_to_row = {num: i for i, num in enumerate(row_order)}
        val_to_col = {num: i for i, num in enumerate(col_order)}
        res = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            res[r][c] = num
        return res