import io
from typing import List
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        pass


obj = Solution()
#data = obj.findCriticalAndPseudoCriticalEdges(n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])
data = obj.findCriticalAndPseudoCriticalEdges(n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]])
print(data)