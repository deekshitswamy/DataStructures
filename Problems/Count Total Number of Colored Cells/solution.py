import io
from typing import List
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)

obj = Solution()
#data = obj.coloredCells(n = 1)
data = obj.coloredCells(n = 2)
print(data)