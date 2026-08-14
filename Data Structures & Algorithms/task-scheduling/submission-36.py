class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        q = deque()
        time = 0

        taskCounts = Counter(tasks)

        for task, count in taskCounts.items():
            heapq.heappush(heap, (-count, task))
        
        while heap or q:
            time += 1

            if heap:
                count, task = heapq.heappop(heap)
                count += 1
                if count != 0:
                    q.append((count, task, time + n))
            
            while q and q[0][2] <= time:
                count, task, time = q.popleft()
                heapq.heappush(heap, (count, task))
        
        return time

