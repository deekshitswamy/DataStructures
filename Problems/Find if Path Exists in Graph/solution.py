import io
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        pass

obj = Solution()
#data = obj.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2)
data = obj.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5)
print(data)