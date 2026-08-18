class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v, t))
        
        visited = set()
        heap = [(0, k)]

        elapsedTime = 0
        while heap and len(visited) < n:
            elapsedTime, node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            for nei, neiTime in adjList[node]:
                if nei not in visited:
                    heapq.heappush(heap, (neiTime + elapsedTime, nei))

        return elapsedTime if len(visited) == n else -1