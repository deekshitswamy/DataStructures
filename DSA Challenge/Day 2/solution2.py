# Best Time to Buy and Sell Stock
import io
from typing import List
class Solution:
    def bestBuySell(self, prices:List[int])->int:
        min_price = 0
        max_price = 0
        profit = 0
        for i in prices:
            if min_price == 0:
                min_price = i
            if max_price == 0:
                max_price = i
            if i < min_price:
                min_price = i
            if i > max_price:
                max_price = i
        profit = max_price - min_price
        if profit < 0:
            profit = 0
        return profit

obj = Solution()
data = obj.bestBuySell(prices = [1,10,2,8,2,3,2])
print(data)