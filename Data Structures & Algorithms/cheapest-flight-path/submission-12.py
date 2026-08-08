class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford algorithm, we relax all edges k + 1 (max num flights possible) times
        # to make sure we don't use a weight of an edge we can't yet visit (not kth iteration),
        # we use a temp table from the previous iteration

        prices = [float("infinity")] * n # index is airport, value is current min price to get there
        prices[src] = 0

        for i in range(k + 1):
            # relax all edges for this iteration
            temp = prices.copy()

            for source, destination, price in flights:
                if prices[source] == float("infinity"):
                    continue

                if prices[source] + price < temp[destination]:
                    temp[destination] = prices[source] + price
            prices = temp
        return prices[dst] if prices[dst] != float("infinity") else -1
                