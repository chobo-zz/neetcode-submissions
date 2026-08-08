class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key=lambda t: t[0])

        minHeap = []
        res = []
        i = 0
        time = 0

        while minHeap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if minHeap:
                task = heapq.heappop(minHeap)
                time += task[0]
                res.append(task[1])
            else:
                time = tasks[i][0]
        
        return res