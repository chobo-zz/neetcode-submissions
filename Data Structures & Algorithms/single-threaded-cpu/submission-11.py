class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, v in enumerate(tasks):
            v.append(i)
        
        tasks.sort()
        heap = []
        i = 0
        res = []
        time = 0

        while i < len(tasks) or heap:
            while i < len(tasks) and tasks[i][0] <= time:
                enqueueTime, processingTime, index = tasks[i]
                heapq.heappush(heap, (processingTime, index))
                i += 1
            
            if not heap:
                time = tasks[i][0]
                continue
            
            processingTime, index = heapq.heappop(heap)
            time += processingTime
            res.append(index)
        
        return res
            
            