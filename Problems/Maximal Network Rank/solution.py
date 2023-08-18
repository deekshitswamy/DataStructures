import io
from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        pass
obj = Solution()
#data = obj.maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]])
#data = obj.maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
data = obj.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
print(data)