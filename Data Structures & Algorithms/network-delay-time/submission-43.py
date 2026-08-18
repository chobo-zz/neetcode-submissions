class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, t in times:
            adjList[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()

        while heap and len(visited) < n:
            time, node = heapq.heappop(heap)

            elapsed = time
            if node in visited:
                continue
            visited.add(node)

            for nei, neiTime in adjList[node]:
                if nei not in visited:
                    heapq.heappush(heap, (elapsed + neiTime, nei))

        return elapsed if len(visited) == n else -1
