import io
from math import comb
from typing import List
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        M = 10 ** 9 + 7
        return (m * comb(n - 1, k) * pow((m - 1), n - k - 1, M)) % M

obj = Solution()
#data = obj.countGoodArrays(n = 3, m = 2, k = 1)
#data = obj.countGoodArrays(n = 4, m = 2, k = 2)
data = obj.countGoodArrays(n = 5, m = 2, k = 0)
print(data)