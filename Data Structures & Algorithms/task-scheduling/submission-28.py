class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = Counter(tasks)
        maxHeap = [] # stores remaining count of a task
        q = deque() # stores (count of task, and time of when it's available again)
        time = 0
        for task, count in taskCounts.items():
            heapq.heappush(maxHeap, -count)
        
        while q or maxHeap:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1
                if count:
                    q.append((count, time + n))
            
            while q and q[0][1] <= time:
                count, time = q.popleft()
                heapq.heappush(maxHeap, count)
        
        return time
                
