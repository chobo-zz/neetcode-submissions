class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        q = deque()
        time = 0

        taskCount = Counter(tasks)
        for task, count in taskCount.items():
            heapq.heappush(maxHeap, -count)
        
        while q or maxHeap:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1
                if count != 0:
                    q.append((count, time + n))
            
            if q and q[0][1] <= time:
                count = q.popleft()[0]
                heapq.heappush(maxHeap, count)
        return time
                
            