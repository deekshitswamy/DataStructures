import io
from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [0, 0]
        num = [0] * (n * n + 1)
        for i in range(n):
            for j in range(n):
                if num[grid[i][j]] == 1:
                    res[0] = grid[i][j]
                else:
                    num[grid[i][j]] = 1
        for i in range(1, n * n + 1):
            if num[i] == 0:
                res[1] = i
                break
        return res

obj = Solution()
#data = obj.findMissingAndRepeatedValues(grid = [[1,3],[2,2]])
data = obj.findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]])
print(data)