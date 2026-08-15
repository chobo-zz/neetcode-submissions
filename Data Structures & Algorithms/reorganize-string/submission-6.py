class Solution:
    def reorganizeString(self, s: str) -> str:
        charCounts = Counter(s)
        heap = [(-count, char) for char, count in charCounts.items()]
        res = []
        prev = None

        while heap or prev:
            if prev and not heap:
                return ""
            count, char = heapq.heappop(heap)
            res.append(char)
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count != 0:
                prev = (count, char)
            
        

        return "".join(res)