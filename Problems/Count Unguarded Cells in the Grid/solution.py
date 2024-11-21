import io
from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        pass

obj = Solution()
#data = obj.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])
data = obj.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]])
print(data)