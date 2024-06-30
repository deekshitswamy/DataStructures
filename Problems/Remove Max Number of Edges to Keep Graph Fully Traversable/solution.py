import io
from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        pass

obj = Solution()
#data = obj.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])
#data = obj.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]])
data = obj.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]])
print(data)