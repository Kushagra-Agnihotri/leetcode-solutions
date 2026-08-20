class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        val = price
        self.stock.append(price)

        count = 0
        for i in range(len(self.stock)-1,-1 , -1):
            if self.stock[i] <= val:
                count +=1
            else:
                break
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)