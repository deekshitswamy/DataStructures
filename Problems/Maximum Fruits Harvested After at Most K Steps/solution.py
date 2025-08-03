import io
from typing import List
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        pass

obj = Solution()
#data = obj.maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4)
#data = obj.maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4)
data = obj.maxTotalFruits(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2)
print(data)