import io
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        pass

obj = Solution()
#data = obj.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
data = obj.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12)
print(data)