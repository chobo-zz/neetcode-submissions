class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, v in enumerate(tasks):
            v.append(i)
        
        tasks.sort()
        minHeap = [] # (processing time, enqueueTime, index)
        res = []
        i = 0
        time = 0
        while minHeap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:  
                eTime, pTime, idx = tasks[i]
                heapq.heappush(minHeap, (pTime, idx))
                i += 1
            
            if minHeap:
                pTime, idx = heapq.heappop(minHeap)
                time += pTime
                res.append(idx)
            else:
                time = tasks[i][0]
        
        return res