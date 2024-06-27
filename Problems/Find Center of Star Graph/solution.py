import io
from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()

obj = Solution()
#data = obj.findCenter(edges = [[1,2],[2,3],[4,2]])
data = obj.findCenter(edges = [[1,2],[5,1],[1,3],[1,4]])
print(data)