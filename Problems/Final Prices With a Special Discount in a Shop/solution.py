import io
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
                else:
                    pass
        return prices

obj = Solution()
#data = obj.finalPrices(n = 1)
#data = obj.finalPrices(n = 2)
data = obj.finalPrices(n = 2)
print(data)