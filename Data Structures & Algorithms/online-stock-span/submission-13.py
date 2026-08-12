class StockSpanner:

    def __init__(self):
        self.stack = [] # price, span

    def next(self, price: int) -> int:
        # monotonically decreasing self.stack
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            lastPrice, lastSpan = self.stack.pop()
            count += lastSpan
        
        self.stack.append((price, count))
        return count

            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)