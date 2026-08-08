class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count:
                maxHeap.append((-count, char))
        
        heapq.heapify(maxHeap)

        res = []

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            count += 1
            res.append(char)

            if len(res) >= 2 and res[-1] == res[-2]:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                count2 += 1
                res.append(char2)
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            if count:
                    heapq.heappush(maxHeap, (count, char))

        return "".join(res)

