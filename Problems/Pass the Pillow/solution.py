import io
from typing import List
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        return n-abs(n-1-time%(n*2-2))

obj = Solution()
#data = obj.passThePillow(n = 4, time = 5)
data = obj.passThePillow(n = 3, time = 2)
print(data)