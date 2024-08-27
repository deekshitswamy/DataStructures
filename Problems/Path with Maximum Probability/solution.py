import io
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        pass

obj = Solution()
#data = obj.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)
#data = obj.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2)
data = obj.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2)
print(data)