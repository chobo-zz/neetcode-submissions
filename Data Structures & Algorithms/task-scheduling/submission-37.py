class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = Counter(tasks)
        heap = [-count for count in taskCounts.values()]
        heapq.heapify(heap)

        q = deque()

        time = 0

        while heap or q:
            time += 1

            if heap:
                remaining = heapq.heappop(heap) + 1
                if remaining != 0:
                    q.append((remaining, time + n))
            
            while q and q[0][1] <= time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time