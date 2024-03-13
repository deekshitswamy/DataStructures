import io
import math
from typing import List
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(n*(n+1)/2)
        return int(x) if int(x) == x else -1

obj = Solution()
#data = obj.pivotInteger(n = 8)
#data = obj.pivotInteger(n = 1)
data = obj.pivotInteger(n = 4)
print(data)