import io
from typing import List
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if (prices[0]+prices[1])<=money:
            return (money-(prices[0]+prices[1]))
        else:
            return money

obj = Solution()
#data = obj.buyChoco(prices = [1,2,2], money = 3)
data = obj.buyChoco(prices = [3,2,3], money = 3)
print(data)