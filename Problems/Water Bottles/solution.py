import io
from typing import List
class Solution:
    def numWaterBottles(numBottles: int, numExchange: int) -> int:
        return int(numBottles+(numBottles-1)/(numExchange-1))

obj = Solution()
#data = obj.numWaterBottles(numBottles = 9, numExchange = 3)
data = obj.numWaterBottles(numBottles = 15, numExchange = 4)
print(data)