class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        heap = []
        i = 0
        curPassengers = 0
        while i < len(trips):
            numPassengers, start, end = trips[i]
            while heap and heap[0][0] <= start:
                curPassengers -= heapq.heappop(heap)[1]
            
            curPassengers += numPassengers
            if curPassengers > capacity:
                return False

            heapq.heappush(heap, (end, numPassengers))
            i += 1
        
        return True
