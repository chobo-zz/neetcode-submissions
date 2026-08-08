class Solution:
    def reorganizeString(self, s: str) -> str:
        charCounts = Counter(s)
        maxHeap = [(-count, char) for char, count in charCounts.items()]
        heapq.heapify(maxHeap)
        res = []
        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            count, char = heapq.heappop(maxHeap)
            count += 1
            res.append(char)

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if count != 0:
                prev = (count, char)
        return "".join(res)
