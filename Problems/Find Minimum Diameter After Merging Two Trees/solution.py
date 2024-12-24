import io
from typing import List
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        pass

obj = Solution()
#data = obj.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]])
data = obj.minimumDiameterAfterMerge(edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]])
print(data)