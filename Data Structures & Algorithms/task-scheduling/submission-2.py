class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-t for t in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                

                tasksRemaining = heapq.heappop(maxHeap) + 1
                nextTimeAvailable = time + n

                if tasksRemaining:
                    q.append((tasksRemaining, nextTimeAvailable))
            
            if q and q[0][1] == time:
                tasksRemaining = q.popleft()[0]
                heapq.heappush(maxHeap, tasksRemaining)
        
        return time



