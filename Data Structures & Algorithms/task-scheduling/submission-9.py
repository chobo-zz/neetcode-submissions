class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-t for t in count.values()]

        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while q or maxHeap:
            time += 1

            if maxHeap:
                tasksRemaining = 1 + heapq.heappop(maxHeap)

                if tasksRemaining:
                    q.append((tasksRemaining, time + n))

            if q and q[0][1] == time:
                tasksRemaining = q.popleft()[0]
                heapq.heappush(maxHeap, tasksRemaining)
        
        return time

