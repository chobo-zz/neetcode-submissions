class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's algorithm (shortest path in non-negative graph)
        # build adjacency list for all nodes
        # keep track of visited nodes in set
        # keep a minHeap with (totalWeight, node) to efficiently get current shortest path in logV
        # keep track of result total time and set it to curTime of popped node.
            # total time will be already be updated when we push new heap values (totalTraveledTime + this node's time)
        
        adj = collections.defaultdict(list)

        # build initial adjacency list
        for u, v, t in times:
            adj[u].append((v, t))
        
        minHeap = [(0, k)] # minHeap initialized with starting k node, weight is 0 since we start there
        visit = set()
        resTime = 0

        while minHeap:
            curTime, curNode = heapq.heappop(minHeap)

            if curNode in visit:
                continue
            visit.add(curNode)
            resTime = curTime

            for v, t in adj[curNode]:
                if v not in visit:   
                    heapq.heappush(minHeap, (curTime + t, v))
        
        return resTime if len(visit) == n else -1
            
            
    
