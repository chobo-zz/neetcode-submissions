class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = Counter(tasks)
        maxHeap = [-c for c in taskCounts.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                remaining = heapq.heappop(maxHeap) + 1
                if remaining:
                    q.append((remaining, time + n))
            
            if q and q[0][1] <= time:
                remaining = q.popleft()[0]
                heapq.heappush(maxHeap, remaining)
                
        return time
            