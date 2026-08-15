class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxHeap = []
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                maxHeap.append((-count, char))
        heapq.heapify(maxHeap)
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res.append(char)
            count += 1
            if len(res) >= 2 and res[-1] == res[-2]:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res.append(char2)
                count2 += 1

                if count2 != 0:
                    heapq.heappush(maxHeap, (count2, char2))
                
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        return "".join(res)