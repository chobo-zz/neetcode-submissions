class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("infinity")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()

            for src, dest, price in flights:
                if prices[src] == float("infinity"):
                    continue
                
                if price + prices[src] < temp[dest]:
                    temp[dest] = price + prices[src]
            prices = temp
        
        return prices[dst] if prices[dst] != float("infinity") else -1