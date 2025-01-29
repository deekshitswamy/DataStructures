import io
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass

obj = Solution()
#data = obj.findRedundantConnection(edges = [[1,2],[1,3],[2,3]])
data = obj.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]])
print(data)