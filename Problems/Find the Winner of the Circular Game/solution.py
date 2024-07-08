import io
from typing import List
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        vecArr = list(range(1, n + 1))
        start = 0
        while len(vecArr) > 1:
            start = (start + k - 1) % len(vecArr)
            vecArr.pop(start)
        
        return vecArr[0]

obj = Solution()
#data = obj.findTheWinner(n = 5, k = 2)
data = obj.findTheWinner(n = 6, k = 5)
print(data)