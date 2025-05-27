import io
from typing import List
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for val in range(1, n+1):
            if val % m == 0:
                num2 += val
            else:
                num1 += val
        return num1 - num2

obj = Solution()
#data = obj.differenceOfSums(n = 10, m = 3)
#data = obj.differenceOfSums(n = 5, m = 6)
data = obj.differenceOfSums(n = 5, m = 1)
print(data)